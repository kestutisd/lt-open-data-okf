#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""Scan an OKF v0.3 bundle for Lithuanian Open Data concepts, trust, and freshness.

Reads concept frontmatter (using PyYAML with timestamp-preserving SafeLoader when
installed, or a built-in zero-dependency stdlib YAML frontmatter parser when
PyYAML is absent or OKF_NO_PYYAML=1 is set). Implements OKF v0.3 SPEC.md consumer
rules: concepts (§3.2), current-only trust tiers (§5.3), status & superseded_by
(§5.4), staleness (§5.5), value normalization (§11.2), and <=0.2 fallbacks (§12.1),
plus Spinta --deployed/--undeployed filters, --limit, and Lithuanian diacritic +
inflection/palatalization stem matching on --grep.

Usage:
    scan.py BUNDLE_ROOT [--type TYPE] [--tag TAG] [--grep TEXT] [--current]
            [--stale] [--deprecated] [--unverified] [--deployed] [--undeployed]
            [--limit N] [--now DATETIME] [--json]

Filters combine with AND. Exit status is 0, or 2 for a usage problem.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
import urllib.parse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_FORCE_STDLIB = os.environ.get("OKF_NO_PYYAML", "").strip() == "1"
if not _FORCE_STDLIB:
    try:
        import yaml as _yaml  # type: ignore[import-untyped]
    except ImportError:
        _yaml = None
else:
    _yaml = None

DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(\.\d+)?([Zz]|[+-]\d{2}:\d{2})$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INT_RE = re.compile(r"^-?\d+$")
FLOAT_RE = re.compile(r"^-?\d+\.\d+$")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
TOKEN_RE = re.compile(r"[0-9a-zA-ZąčęėįšųūžĄČĘĖĮŠŲŪŽ_]{2,}")
_CAMEL_RE_1 = re.compile(r"([a-ząčęėįšųūž0-9])([A-ZĄČĘĖĮŠŲŪŽ])")
_CAMEL_RE_2 = re.compile(r"([A-ZĄČĘĖĮŠŲŪŽ]+)([A-ZĄČĘĖĮŠŲŪŽ][a-ząčęėįšųūž])")

TRUST_ORDER = ("human-reviewed", "machine-confirmed", "unverified")
CURRENT_STATUSES = ("stable", "draft")
SPINTA_ASSET_TYPES = frozenset({"dataset", "table", "open data dataset", "open data table"})
BOM = "\ufeff"

# Lithuanian irregular 5th-declension consonant stems and suffix tables for --grep
_LT_IRREGULAR_EXACT: dict[str, str] = {
    "asmuo": "asmen",
    "vanduo": "vanden",
    "akmuo": "akmen",
    "sesuo": "seser",
    "dukra": "dukter",
    "menuo": "menes",
}
_LT_IRREGULAR_PREFIXES: tuple[tuple[str, str], ...] = (
    ("asmen", "asmen"),
    ("vanden", "vanden"),
    ("akmen", "akmen"),
    ("seser", "seser"),
    ("dukter", "dukter"),
    ("menes", "menes"),
)
_LT_INFLECTION_SUFFIXES: tuple[str, ...] = (
    "iuose", "iomis", "uose", "omis", "iams", "iems", "iuju", "iais",
    "uju", "iai", "ais", "oje", "eje", "ese", "ose", "yse", "yje",
    "ims", "ems", "mis", "iui", "iu", "us", "es", "os", "ai", "is",
    "as", "io", "ys", "ui", "a", "e", "i", "o", "u",
)
_LT_DERIVATIONAL_SUFFIXES: tuple[str, ...] = (
    "toj", "jim", "avim", "inim", "ojim", "im", "ym", "ej",
)

if _yaml is not None:
    class _Loader(_yaml.SafeLoader):
        """SafeLoader that keeps timestamps as strings as written in frontmatter."""

    _Loader.yaml_implicit_resolvers = {
        ch: [(tag, rx) for tag, rx in resolvers if tag != "tag:yaml.org,2002:timestamp"]
        for ch, resolvers in _yaml.SafeLoader.yaml_implicit_resolvers.items()
    }


class _SimpleYAMLError( ValueError ):
    """Raised when the stdlib frontmatter fallback detects malformed YAML."""


def _strip_yaml_comment(line: str) -> str:
    """Remove trailing `# ...` comments outside single or double quotes."""
    in_single = False
    in_double = False
    escaped = False
    for idx, ch in enumerate(line):
        if escaped:
            escaped = False
            continue
        if ch == "\\" and in_double:
            escaped = True
            continue
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double:
            if idx == 0 or line[idx - 1].isspace():
                return line[:idx].rstrip()
    return line.rstrip()


def _split_top_level(text: str, sep: str) -> list[str]:
    """Split flow YAML (`[...]` or `{...}`) on `sep` outside quotes and nested brackets."""
    parts: list[str] = []
    buf: list[str] = []
    in_single = False
    in_double = False
    escaped = False
    depth = 0
    for ch in text:
        if escaped:
            buf.append(ch)
            escaped = False
            continue
        if ch == "\\" and in_double:
            buf.append(ch)
            escaped = True
            continue
        if ch == "'" and not in_double:
            in_single = not in_single
            buf.append(ch)
            continue
        if ch == '"' and not in_single:
            in_double = not in_double
            buf.append(ch)
            continue
        if not in_single and not in_double:
            if ch in "[{":
                depth += 1
            elif ch in "]}":
                depth -= 1
                if depth < 0:
                    raise _SimpleYAMLError("unbalanced closing bracket")
            elif ch == sep and depth == 0:
                parts.append("".join(buf).strip())
                buf = []
                continue
        buf.append(ch)
    if in_single or in_double or depth != 0:
        raise _SimpleYAMLError("unclosed quote or bracket")
    parts.append("".join(buf).strip())
    return parts


def _parse_key_value(entry: str) -> tuple[str, str]:
    """Split `key: value` at the first top-level colon followed by space or end-of-string."""
    in_single = False
    in_double = False
    escaped = False
    depth = 0
    for idx, ch in enumerate(entry):
        if escaped:
            escaped = False
            continue
        if ch == "\\" and in_double:
            escaped = True
            continue
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif not in_single and not in_double:
            if ch in "[{":
                depth += 1
            elif ch in "]}":
                depth -= 1
            elif ch == ":" and depth == 0:
                if idx + 1 == len(entry) or entry[idx + 1].isspace():
                    key_raw = entry[:idx].strip()
                    val_raw = entry[idx + 1 :].strip()
                    if not key_raw:
                        raise _SimpleYAMLError("empty mapping key")
                    key = str(_parse_inline_value(key_raw))
                    return key, val_raw
    raise _SimpleYAMLError(f"expected mapping entry, got {entry!r}")


def _parse_inline_value(raw: str) -> Any:
    """Parse an inline YAML 1.2 scalar, flow sequence `[...]`, or flow mapping `{...}`."""
    s = raw.strip()
    if not s:
        return None
    if s[0] == '"':
        if len(s) < 2 or s[-1] != '"':
            raise _SimpleYAMLError(f"unclosed double-quoted scalar: {s!r}")
        inner = s[1:-1]
        out: list[str] = []
        i = 0
        while i < len(inner):
            if inner[i] == "\\" and i + 1 < len(inner):
                nxt = inner[i + 1]
                escapes = {'"': '"', "\\": "\\", "n": "\n", "r": "\r", "t": "\t", "/": "/"}
                out.append(escapes.get(nxt, nxt))
                i += 2
            else:
                out.append(inner[i])
                i += 1
        return "".join(out)
    if s[0] == "'":
        if len(s) < 2 or s[-1] != "'":
            raise _SimpleYAMLError(f"unclosed single-quoted scalar: {s!r}")
        return s[1:-1].replace("''", "'")
    if s[0] == "[":
        if s[-1] != "]":
            raise _SimpleYAMLError(f"unclosed flow sequence: {s!r}")
        inner = s[1:-1].strip()
        if not inner:
            return []
        items = _split_top_level(inner, ",")
        return [_parse_inline_value(item) for item in items if item != ""]
    if s[0] == "{":
        if s[-1] != "}":
            raise _SimpleYAMLError(f"unclosed flow mapping: {s!r}")
        inner = s[1:-1].strip()
        if not inner:
            return {}
        result: dict[str, Any] = {}
        for item in _split_top_level(inner, ","):
            if not item:
                continue
            k, v = _parse_key_value(item)
            result[k] = _parse_inline_value(v)
        return result
    if any(ch in s for ch in ("[", "]")) and not s.startswith("[^"):
        # Catch broken flow brackets like `[unclosed`
        if s.count("[") != s.count("]"):
            raise _SimpleYAMLError(f"unbalanced brackets in {s!r}")
    if s in ("null", "Null", "NULL", "~"):
        return None
    if s in ("true", "True", "TRUE"):
        return True
    if s in ("false", "False", "FALSE"):
        return False
    if INT_RE.match(s):
        return int(s)
    if FLOAT_RE.match(s):
        return float(s)
    return s


def _parse_yaml_stdlib(block: str) -> Any:
    """Zero-dependency parser for YAML 1.2 frontmatter blocks used in OKF bundles."""
    prepared: list[tuple[int, str]] = []
    raw_lines = block.splitlines()
    idx = 0
    while idx < len(raw_lines):
        raw = raw_lines[idx]
        if not raw.strip() or raw.lstrip().startswith("#"):
            idx += 1
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if "\t" in raw[:indent]:
            raise _SimpleYAMLError("tabs are not allowed for YAML indentation")
        cleaned = _strip_yaml_comment(raw[indent:])
        if cleaned:
            # Handle block scalar indicators (`>-`, `>`, `|-`, `|`)
            if cleaned.endswith((">-", ">", "|-", "|")):
                try:
                    k, indicator = _parse_key_value(cleaned)
                except _SimpleYAMLError:
                    k, indicator = "", ""
                if k and indicator in (">-", ">", "|-", "|"):
                    folded = indicator.startswith(">")
                    idx += 1
                    chunk: list[str] = []
                    while idx < len(raw_lines):
                        sub = raw_lines[idx]
                        if not sub.strip():
                            chunk.append("")
                            idx += 1
                            continue
                        sub_indent = len(sub) - len(sub.lstrip(" "))
                        if sub_indent <= indent:
                            break
                        chunk.append(sub.strip() if folded else sub[indent + 2 :] if len(sub) >= indent + 2 else sub.lstrip())
                        idx += 1
                    joined = (" ".join(p for p in chunk if p) if folded else "\n".join(chunk)).strip()
                    prepared.append((indent, f"{json.dumps(k)}: {json.dumps(joined)}"))
                    continue
            prepared.append((indent, cleaned))
        idx += 1

    if not prepared:
        return {}

    def parse_node(pos: int, min_indent: int) -> tuple[Any, int]:
        cur_indent, cur_text = prepared[pos]
        if cur_indent < min_indent:
            return None, pos
        if cur_text == "-" or cur_text.startswith("- "):
            items: list[Any] = []
            while pos < len(prepared):
                ind, txt = prepared[pos]
                if ind < cur_indent or not (txt == "-" or txt.startswith("- ")):
                    break
                if ind != cur_indent:
                    raise _SimpleYAMLError("inconsistent list indentation")
                rest = txt[1:].strip()
                pos += 1
                if not rest:
                    if pos < len(prepared) and prepared[pos][0] > cur_indent:
                        val, pos = parse_node(pos, cur_indent + 1)
                        items.append(val)
                    else:
                        items.append(None)
                elif rest.startswith(("{", "[", '"', "'")):
                    items.append(_parse_inline_value(rest))
                else:
                    # Could be `- id: manifest` followed by indented sibling keys, or `- scalar`
                    try:
                        k, v_raw = _parse_key_value(rest)
                        is_kv = True
                    except _SimpleYAMLError:
                        is_kv = False
                        k, v_raw = "", ""
                    if is_kv:
                        entry_map: dict[str, Any] = {}
                        if v_raw == "":
                            if pos < len(prepared) and prepared[pos][0] > cur_indent:
                                sub_val, pos = parse_node(pos, cur_indent + 1)
                                entry_map[k] = sub_val
                            else:
                                entry_map[k] = None
                        else:
                            entry_map[k] = _parse_inline_value(v_raw)
                        if pos < len(prepared) and prepared[pos][0] > cur_indent:
                            extra, pos = parse_node(pos, cur_indent + 1)
                            if not isinstance(extra, dict):
                                raise _SimpleYAMLError("expected mapping continuation in list item")
                            entry_map.update(extra)
                        items.append(entry_map)
                    else:
                        items.append(_parse_inline_value(rest))
            return items, pos

        mapping: dict[str, Any] = {}
        while pos < len(prepared):
            ind, txt = prepared[pos]
            if ind < cur_indent:
                break
            if ind != cur_indent:
                raise _SimpleYAMLError("unexpected indentation in mapping")
            if txt == "-" or txt.startswith("- "):
                break
            k, v_raw = _parse_key_value(txt)
            pos += 1
            if v_raw == "":
                if pos < len(prepared) and prepared[pos][0] > cur_indent:
                    sub_val, pos = parse_node(pos, cur_indent + 1)
                    mapping[k] = sub_val
                else:
                    mapping[k] = None
            else:
                mapping[k] = _parse_inline_value(v_raw)
        return mapping, pos

    parsed, next_pos = parse_node(0, prepared[0][0])
    if next_pos != len(prepared):
        raise _SimpleYAMLError("trailing unparsed lines in frontmatter")
    return parsed


def read_frontmatter(path: Path, *, use_pyyaml: bool | None = None) -> tuple[dict, str | None]:
    """Return (frontmatter, problem). problem is None when the block is readable."""
    lines = path.read_text(encoding="utf-8").lstrip(BOM).splitlines()
    if not lines or lines[0].rstrip("\r") != "---":
        return {}, "no frontmatter"
    want_yaml = (_yaml is not None) if use_pyyaml is None else (use_pyyaml and _yaml is not None)
    for index in range(1, len(lines)):
        if lines[index].rstrip("\r") == "---":
            block = "\n".join(lines[1:index])
            if want_yaml:
                try:
                    meta = _yaml.load(block, Loader=_Loader)
                except _yaml.YAMLError:
                    return {}, "frontmatter does not parse"
            else:
                try:
                    meta = _parse_yaml_stdlib(block)
                except _SimpleYAMLError:
                    return {}, "frontmatter does not parse"
            if meta is None:
                meta = {}
            if not isinstance(meta, dict):
                return {}, "frontmatter is not a mapping"
            return meta, None
    return {}, "frontmatter is not closed"


def blank(value: Any) -> bool:
    """SPEC.md §11.2: null, an empty string, and an empty list mean an absent key."""
    return value is None or value == "" or value == []


def as_list(value: Any) -> list:
    """SPEC.md §11.2: one item stands for a list with one item."""
    if blank(value):
        return []
    return value if isinstance(value, list) else [value]


def parse_timestamp(value: Any) -> datetime | None:
    """Parse RFC 3339 date-times or dates (SPEC.md §5). A date means 00:00 UTC."""
    if not isinstance(value, str):
        return None
    try:
        if DATE_RE.match(value):
            return datetime.fromisoformat(value + "T00:00:00+00:00")
        if DATETIME_RE.match(value):
            return datetime.fromisoformat(value.upper().replace("Z", "+00:00"))
    except ValueError:
        return None
    return None


def as_tags(value: Any) -> list[str]:
    """SPEC.md §11.2: a scalar tags value is one tag. Do not split it at commas."""
    return [str(t) for t in as_list(value) if not blank(t)]


def fold_diacritics(text: str) -> str:
    """Fold Lithuanian and Latin diacritics to ASCII lowercase via Unicode NFD."""
    if not text:
        return ""
    if text.isascii():
        return text.casefold()
    nfd = unicodedata.normalize("NFD", text.casefold())
    return "".join(ch for ch in nfd if unicodedata.category(ch) != "Mn")


def _split_subtokens(raw_tok: str) -> list[str]:
    """Split `snake_case` and `CamelCase` identifiers into lowercase subtokens."""
    parts: list[str] = []
    for seg in raw_tok.split("_"):
        if not seg:
            continue
        if seg.islower() or seg.isdigit():
            if len(seg) >= 2:
                parts.append(seg)
            continue
        s = _CAMEL_RE_2.sub(r"\1 \2", seg)
        s = _CAMEL_RE_1.sub(r"\1 \2", s)
        for p in s.split():
            if len(p) >= 2:
                parts.append(p.casefold())
    return parts


def _lt_word_stems(folded: str) -> set[str]:
    """Generate ASCII-folded Lithuanian inflection, palatalization, and verbal-noun stems."""
    stems: set[str] = {folded}
    wlen = len(folded)
    if wlen < 3 or not folded.isalpha():
        return stems

    irr = _LT_IRREGULAR_EXACT.get(folded)
    if irr is not None:
        stems.add(irr)
        return stems
    for pref, canon in _LT_IRREGULAR_PREFIXES:
        if folded.startswith(pref) and wlen <= len(pref) + 5:
            rem = folded[len(pref) :]
            if rem in ("", "s", "i", "iu", "yje", "ys", "u", "ims", "is", "imis", "yse", "es", "iai", "io"):
                stems.add(canon)
                return stems

    base = folded
    for suf in _LT_INFLECTION_SUFFIXES:
        if folded.endswith(suf) and wlen - len(suf) >= 3:
            base = folded[: -len(suf)]
            stems.add(base)
            break

    # Normalize Lithuanian t -> č (`c`) and d -> dž (`dz`) palatalization across declensions
    # (e.g., `mokesčių` -> `mokesc` -> `mokest`, `apskričių` -> `apskric` -> `apskrit`, `sutarčių` -> `sutart`).
    candidates = list(stems)
    for cand in candidates:
        if len(cand) >= 4 and cand.endswith("c"):
            stems.add(cand[:-1] + "t")
        elif len(cand) >= 5 and cand.endswith("dz"):
            stems.add(cand[:-2] + "d")

    # Normalize productive deverbal agentive/abstract suffixes when root >= 4 chars
    # (e.g., `Moketojas` -> `moketoj` -> `moke` <-> `mokestis` -> `mokest` -> `moke`).
    for cand in list(stems):
        if len(cand) >= 6 and cand.endswith("est"):
            stems.add(cand[:-2])
            continue
        for dsuf in _LT_DERIVATIONAL_SUFFIXES:
            if cand.endswith(dsuf) and len(cand) - len(dsuf) >= 4:
                stems.add(cand[: -len(dsuf)])
                break
    return stems


def token_stems(raw_tok: str) -> set[str]:
    """Return all exact, folded, subtoken, and Lithuanian-stemmed forms of a token."""
    out: set[str] = set()
    low = raw_tok.casefold()
    out.add(low)
    folded = fold_diacritics(low)
    if folded:
        out.update(_lt_word_stems(folded))
    if "_" in raw_tok or not raw_tok.islower():
        for sub in _split_subtokens(raw_tok):
            out.add(sub)
            sub_fold = fold_diacritics(sub)
            if sub_fold:
                out.update(_lt_word_stems(sub_fold))
    return out


class Bundle:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.metadata: dict = {}
        index = root / "index.md"
        if index.is_file():
            meta, _ = read_frontmatter(index)
            self.metadata = meta
        version = self.metadata.get("okf_version")
        self.okf_version = str(version) if version is not None else None
        try:
            declared = tuple(int(p) for p in self.okf_version.split(".")) if self.okf_version else None
        except ValueError:
            declared = None
        # SPEC.md §12.1: older bundles may resolve bare path fields from the root.
        self.root_fallback = declared is None or declared <= (0, 2)

    def inside(self, path: Path) -> bool:
        try:
            path.relative_to(self.root)
        except ValueError:
            return False
        return True

    def concept_id(self, source: Path, target: Any) -> str | None:
        """Resolve a frontmatter path field (SPEC.md §6) to a concept ID, or None."""
        if not isinstance(target, str) or SCHEME_RE.match(target):
            return None
        clean = urllib.parse.unquote(target.split("#", 1)[0])
        base = self.root if clean.startswith("/") else source.parent
        candidates = [Path(os.path.normpath(base / clean.lstrip("/")))]
        if self.root_fallback and not clean.startswith("/"):
            candidates.append(Path(os.path.normpath(self.root / clean)))
        for candidate in candidates:
            if self.inside(candidate) and candidate.is_file() and candidate.suffix == ".md":
                return candidate.relative_to(self.root).with_suffix("").as_posix()
        return None


def describe(bundle: Bundle, path: Path, meta: dict, now: datetime) -> dict:
    concept_id = path.relative_to(bundle.root).with_suffix("").as_posix()
    generated = meta.get("generated") if isinstance(meta.get("generated"), dict) else None
    generated_at_text = (generated or {}).get("at") or meta.get("timestamp")  # v0.1 fallback
    generated_at = parse_timestamp(generated_at_text)

    # SPEC.md §5.3: an event is current when at >= generated.at, or when generated is absent.
    events = [
        e for e in as_list(meta.get("verified"))
        if isinstance(e, dict) and not blank(e.get("by")) and parse_timestamp(e.get("at"))
    ]
    current = [e for e in events if generated_at is None or parse_timestamp(e.get("at")) >= generated_at]  # type: ignore[operator]
    if not current:
        trust = "unverified"
    elif any(str(e.get("by")).startswith("human:") for e in current):
        trust = "human-reviewed"
    else:
        trust = "machine-confirmed"

    notes: list[str] = []
    stale_after_text = meta.get("stale_after")
    stale_after = parse_timestamp(stale_after_text)
    malformed_stale = not blank(stale_after_text) and stale_after is None
    if malformed_stale:
        notes.append(f"stale_after {stale_after_text!r} is malformed, so the concept counts as stale")
    if events and not current:
        notes.append("verified only before the last change")

    status = meta.get("status")
    status = "stable" if blank(status) else str(status)
    if status not in ("stable", "draft", "deprecated"):
        notes.append(f"unknown status {status!r}: not current")
    superseded_by = meta.get("superseded_by")
    replacement = bundle.concept_id(path, superseded_by) if status == "deprecated" else None

    tags = as_tags(meta.get("tags"))
    tag_set = {t.casefold() for t in tags}
    resource = meta.get("resource")
    has_spinta_res = isinstance(resource, str) and resource.startswith("https://get.data.gov.lt/")
    deployed = ("deployed" in tag_set) or (has_spinta_res and "undeployed" not in tag_set)
    undeployed = ("undeployed" in tag_set) or (
        not deployed and str(meta.get("type") or "").casefold() in SPINTA_ASSET_TYPES and blank(resource)
    )

    title = meta.get("title") or path.stem.replace("-", " ").replace("_", " ").strip()
    return {
        "id": concept_id,
        "path": path.relative_to(bundle.root).as_posix(),
        "type": meta.get("type"),
        "title": str(title),
        "description": meta.get("description"),
        "tags": tags,
        "resource": resource,
        "deployed": deployed,
        "undeployed": undeployed,
        "status": status,
        "current": status in CURRENT_STATUSES,
        "superseded_by": None if blank(superseded_by) else str(superseded_by),
        "replacement_id": replacement,
        "trust": trust,
        "verified_before_change": bool(events and not current),
        "generated_at": None if blank(generated_at_text) else str(generated_at_text),
        "stale_after": None if blank(stale_after_text) else str(stale_after_text),
        "stale": malformed_stale or bool(stale_after and now >= stale_after),
        "runtime": meta.get("runtime"),
        "notes": notes,
    }


def freshness(concept: dict) -> str:
    if concept["stale"]:
        if concept["stale_after"] and any("malformed" in n for n in concept["notes"]):
            return "stale (malformed stale_after)"
        return f"stale since {concept['stale_after']}"
    if concept["stale_after"]:
        return f"fresh until {concept['stale_after']}"
    return "no stale_after"


def _has_stem_match(q_stem_sets: list[set[str]], text: str) -> bool:
    if not text or not q_stem_sets:
        return False
    doc_stems: set[str] = set()
    for tok in TOKEN_RE.findall(text):
        doc_stems.update(token_stems(tok))
    return all(bool(qs & doc_stems) for qs in q_stem_sets)


def grep_rank(query: str, concept: dict, root: Path) -> int | None:
    """Return match tier (0=exact header, 1=folded header, 2=id stem, 3=title stem, 4=desc, 5=body) or None."""
    q_low = query.casefold()
    q_fold = fold_diacritics(query)
    q_stem_sets = [token_stems(qt) for qt in TOKEN_RE.findall(query)]

    cid = concept["id"]
    header = f"{cid} {concept['title']}"
    if q_low in header.casefold():
        return 0
    if q_fold and q_fold in fold_diacritics(header):
        return 1
    if _has_stem_match(q_stem_sets, cid):
        return 2
    if _has_stem_match(q_stem_sets, header):
        return 3
    desc = str(concept.get("description") or "")
    if desc:
        hdr_desc = f"{header} {desc}"
        if q_low in hdr_desc.casefold() or (q_fold and q_fold in fold_diacritics(hdr_desc)) or _has_stem_match(q_stem_sets, hdr_desc):
            return 4
    text = (root / concept["path"]).read_text(encoding="utf-8")
    full = f"{header} {text}"
    if q_low in full.casefold() or (q_fold and q_fold in fold_diacritics(full)) or _has_stem_match(q_stem_sets, full):
        return 5
    return None


def matches(concept: dict, args: argparse.Namespace, root: Path) -> int | None:
    """Return sort rank (0..2) when concept matches all filters, or None otherwise."""
    if args.type and str(concept["type"] or "").casefold() != args.type.casefold():
        return None
    if args.tag and args.tag.casefold() not in {t.casefold() for t in concept["tags"]}:
        return None
    if args.deployed and not concept["deployed"]:
        return None
    if args.undeployed and not concept["undeployed"]:
        return None
    if args.current and not concept["current"]:
        return None
    if args.stale and not concept["stale"]:
        return None
    if args.deprecated and concept["status"] != "deprecated":
        return None
    if args.unverified and concept["trust"] != "unverified":
        return None
    if args.grep:
        return grep_rank(args.grep, concept, root)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="List OKF v0.3 concepts with trust tier, status, deployment, and freshness."
    )
    parser.add_argument("bundle", type=Path, help="bundle root directory")
    parser.add_argument("--type", help="only concepts of this type (case-insensitive)")
    parser.add_argument("--tag", help="only concepts with this tag (case-insensitive)")
    parser.add_argument(
        "--grep",
        help="only concepts whose ID, frontmatter, or body matches TEXT (diacritic & LT-stem aware)",
    )
    parser.add_argument("--current", action="store_true", help="only current concepts (stable or draft)")
    parser.add_argument("--stale", action="store_true", help="only stale concepts")
    parser.add_argument("--deprecated", action="store_true", help="only deprecated concepts")
    parser.add_argument("--unverified", action="store_true", help="only unverified concepts")
    parser.add_argument("--deployed", action="store_true", help="only concepts deployed on get.data.gov.lt")
    parser.add_argument("--undeployed", action="store_true", help="only undeployed Spinta schema concepts")
    parser.add_argument("--limit", type=int, help="maximum number of matching concepts to return")
    parser.add_argument("--now", help="current time as an RFC 3339 date-time or date, for staleness")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args(argv)

    if args.limit is not None and args.limit < 0:
        print("scan.py: --limit must be a non-negative integer", file=sys.stderr)
        return 2

    root = args.bundle.resolve()
    if not root.is_dir():
        print(f"scan.py: {args.bundle} is not a directory", file=sys.stderr)
        return 2
    now = datetime.now(timezone.utc)
    if args.now:
        parsed = parse_timestamp(args.now)
        if parsed is None:
            print("scan.py: --now must be an RFC 3339 date-time with an offset or YYYY-MM-DD", file=sys.stderr)
            return 2
        now = parsed

    bundle = Bundle(root)
    concepts, not_concepts = [], []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if path.name in ("index.md", "log.md") or any(p.startswith(".") for p in rel.parts):
            continue
        if not bundle.inside(path.resolve()):
            continue
        meta, problem = read_frontmatter(path)
        concept_type = meta.get("type")
        if problem or not isinstance(concept_type, str) or not concept_type.strip():
            not_concepts.append({"path": rel.as_posix(), "reason": problem or "no type"})
            continue
        concepts.append(describe(bundle, path, meta, now))

    ranked: list[tuple[int, str, dict]] = []
    for c in concepts:
        rank = matches(c, args, root)
        if rank is not None:
            ranked.append((rank, c["id"], c))
    ranked.sort(key=lambda item: (item[0], item[1]))
    matched = [item[2] for item in ranked]
    selected = matched[: args.limit] if args.limit is not None else matched

    summary = {
        "concepts": len(concepts),
        "matched": len(matched),
        "selected": len(selected),
        "not_concepts": len(not_concepts),
        "types": dict(Counter(str(c["type"]) for c in concepts).most_common()),
        "trust": {tier: sum(c["trust"] == tier for c in concepts) for tier in TRUST_ORDER},
        "deployed": sum(c["deployed"] for c in concepts),
        "undeployed": sum(c["undeployed"] for c in concepts),
        "stale": sum(c["stale"] for c in concepts),
        "deprecated": sum(c["status"] == "deprecated" for c in concepts),
        "draft": sum(c["status"] == "draft" for c in concepts),
        "not_current": sum(not c["current"] for c in concepts),
        "parser": "pyyaml" if _yaml is not None else "stdlib",
    }
    meta = bundle.metadata
    bundle_info = {
        "path": str(root),
        "title": meta.get("title"),
        "description": meta.get("description"),
        "license": meta.get("license"),
    }

    if args.json:
        print(json.dumps({
            "bundle": bundle_info,
            "okf_version": bundle.okf_version,
            "now": now.isoformat(),
            "summary": summary,
            "concepts": selected,
            "not_concepts": not_concepts,
        }, indent=2))
        return 0

    name = bundle_info["title"] or root.name
    print(f"Bundle {name}: {summary['concepts']} concepts, okf_version {bundle.okf_version or 'not declared'}, now {now.isoformat()}")
    if bundle_info["description"]:
        print(f"Scope: {bundle_info['description']}")
    print("Types: " + ", ".join(f"{t} {n}" for t, n in summary["types"].items()))
    print("Trust: " + ", ".join(f"{t} {n}" for t, n in summary["trust"].items())
          + f". Deployed {summary['deployed']}, undeployed {summary['undeployed']}, "
          + f"stale {summary['stale']}, deprecated {summary['deprecated']}, "
          + f"draft {summary['draft']}, not current {summary['not_current']}.")
    if not_concepts:
        print(f"Skipped {len(not_concepts)} Markdown files that are not concepts: "
              + ", ".join(f"{n['path']} ({n['reason']})" for n in not_concepts))
    if summary["selected"] != summary["concepts"]:
        extra = f" (capped from {summary['matched']} by --limit {args.limit})" if args.limit is not None and summary["matched"] > summary["selected"] else ""
        print(f"Showing {summary['selected']} concepts that match the filters{extra}.")
    print()
    for c in selected:
        dep_label = "deployed" if c["deployed"] else ("undeployed" if c["undeployed"] else "")
        dep_part = f", {dep_label}" if dep_label else ""
        line = f"{c['id']}  [{c['type']}]  {c['trust']}, {c['status']}{dep_part}, {freshness(c)}"
        if c["status"] == "deprecated" and c["superseded_by"]:
            line += f", superseded by {c['replacement_id'] or c['superseded_by']}"
        print(line)
        text = f"    {c['title']}"
        if c["description"]:
            text += f": {c['description']}"
        print(text)
        for note in c["notes"]:
            print(f"    note: {note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
