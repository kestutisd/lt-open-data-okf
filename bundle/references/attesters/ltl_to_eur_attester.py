#!/usr/bin/env python3
# Copyright 2026 Lithuanian Open Data OKF Bundle Contributors
# SPDX-License-Identifier: Apache-2.0

"""Deterministic consumer-side attester for Statutory LTL to EUR Currency Conversion.

Verifies OKF v0.3 receipts produced by `/references/executors/ltl_to_eur.py`:
  1. Required receipt fields (`ltl_amount`, `rate_used`, `unrounded_eur`,
     `eur_amount`, `computation_sha256`) are present and non-empty.
  2. Exact statutory rate `rate_used == "3.45280"` (all 6 significant figures
     per Council Regulation (EC) No 1103/97 Art. 4 & Reg. (EU) No 851/2014;
     inverted/truncated multipliers like `0.28962` or `3.45` are rejected).
  3. Provenance digest `computation_sha256` matches the canonicalized
     `# Computation` code block when `sanctioned_code` is provided (or the
     canonical statutory computation digest otherwise).
  4. Exact `ROUND_HALF_UP` `0.01` EUR equality of
     `Decimal(str(receipt["ltl_amount"])) / Decimal("3.45280")` against both
     `receipt["eur_amount"]` and `claimed_value`.

Never uses an LLM or network access. Pure Python 3.9+ standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from typing import Any

REQUIRED_RECEIPT_FIELDS = (
    "ltl_amount",
    "rate_used",
    "unrounded_eur",
    "eur_amount",
    "computation_sha256",
)
STATUTORY_RATE_STR = "3.45280"
STATUTORY_RATE_DEC = Decimal(STATUTORY_RATE_STR)
EUR_CENT = Decimal("0.01")
DEFAULT_SANCTIONED_SHA256 = "8148194b64fdc4db1509edf19ae2bfd2d912f72cd518848476f9f5abd919cb87"
HEX_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


def canonicalize_code(code: str) -> str:
    """Strip blank lines and comment lines for deterministic SHA-256 comparison."""
    lines = []
    for raw_line in code.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lines.append(stripped)
    return "\n".join(lines)


def _extract_computation_block_if_markdown(text: str) -> str:
    """Extract the `# Computation` fenced code block if a full concept `.md` was passed."""
    level = None
    in_fence = False
    fence_marker = ""
    collected: list[str] = []
    for line in text.replace("\r\n", "\n").split("\n"):
        stripped = line.lstrip()
        if in_fence:
            if stripped.startswith(fence_marker):
                return "\n".join(collected)
            collected.append(line)
            continue
        if level is not None and stripped.startswith(("```", "~~~")):
            in_fence = True
            fence_marker = stripped[:3]
            continue
        m = HEADING_RE.match(line)
        if m:
            depth = len(m.group(1))
            if level is not None and depth <= level:
                break
            if level is None and m.group(2).strip().lower() == "computation":
                level = depth
    return text


def _parse_decimal(value: Any) -> Decimal | None:
    """Parse `int | float | str | Decimal` into a finite `Decimal`, rejecting booleans."""
    if isinstance(value, bool) or value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    try:
        d = Decimal(s)
    except InvalidOperation:
        return None
    return d if d.is_finite() else None


def attest(
    receipt: dict[str, Any],
    claimed_value: float | str | Decimal,
    sanctioned_code: str | None = None,
) -> dict[str, Any]:
    """Verify an LTL-to-EUR execution receipt and claimed EUR figure."""
    if not isinstance(receipt, dict):
        return {
            "ok": False,
            "reason": "receipt must be a mapping",
            "details": {"receipt_type": type(receipt).__name__},
        }

    missing = [
        k for k in REQUIRED_RECEIPT_FIELDS
        if k not in receipt or receipt[k] is None or receipt[k] == "" or isinstance(receipt[k], bool)
    ]
    if missing:
        return {
            "ok": False,
            "reason": f"receipt is missing required fields: {', '.join(missing)}",
            "details": {"missing_fields": missing, "receipt_keys": sorted(receipt.keys())},
        }

    rate_raw = receipt.get("rate_used")
    if not isinstance(rate_raw, str) or rate_raw != STATUTORY_RATE_STR:
        return {
            "ok": False,
            "reason": f"rate_used must equal exact statutory rate {STATUTORY_RATE_STR!r}, got {rate_raw!r}",
            "details": {"expected_rate": STATUTORY_RATE_STR, "actual_rate": rate_raw},
        }

    rec_sha = str(receipt.get("computation_sha256", "")).strip().lower()
    if not HEX_SHA256_RE.match(rec_sha):
        return {
            "ok": False,
            "reason": "receipt computation_sha256 is not a valid 64-character hex SHA-256 digest",
            "details": {"computation_sha256": receipt.get("computation_sha256")},
        }

    if sanctioned_code is not None:
        extracted = _extract_computation_block_if_markdown(sanctioned_code)
        expected_sha = hashlib.sha256(canonicalize_code(extracted).encode("utf-8")).hexdigest()
        if rec_sha != expected_sha:
            return {
                "ok": False,
                "reason": "receipt computation_sha256 does not match sanctioned # Computation code",
                "details": {"expected_sha256": expected_sha, "receipt_sha256": rec_sha},
            }
    elif rec_sha != DEFAULT_SANCTIONED_SHA256:
        return {
            "ok": False,
            "reason": "receipt computation_sha256 does not match statutory LTL-to-EUR computation",
            "details": {"expected_sha256": DEFAULT_SANCTIONED_SHA256, "receipt_sha256": rec_sha},
        }

    ltl_dec = _parse_decimal(receipt.get("ltl_amount"))
    if ltl_dec is None:
        return {
            "ok": False,
            "reason": f"receipt ltl_amount {receipt.get('ltl_amount')!r} is not a valid finite decimal",
            "details": {},
        }

    with localcontext() as ctx:
        ctx.prec = 28
        expected_unrounded = ltl_dec / STATUTORY_RATE_DEC
        expected_eur = expected_unrounded.quantize(EUR_CENT, rounding=ROUND_HALF_UP)

    rec_unrounded = _parse_decimal(receipt.get("unrounded_eur"))
    if rec_unrounded is None or abs(rec_unrounded - expected_unrounded) > Decimal("1e-12"):
        return {
            "ok": False,
            "reason": "receipt unrounded_eur does not match ltl_amount / 3.45280",
            "details": {
                "expected_unrounded_eur": format(expected_unrounded, "f"),
                "receipt_unrounded_eur": receipt.get("unrounded_eur"),
            },
        }

    rec_eur = _parse_decimal(receipt.get("eur_amount"))
    if rec_eur is None or rec_eur != expected_eur or rec_eur.as_tuple().exponent < -2:
        return {
            "ok": False,
            "reason": "receipt eur_amount does not match ROUND_HALF_UP 0.01 EUR conversion",
            "details": {
                "expected_eur": format(expected_eur, ".2f"),
                "receipt_eur_amount": receipt.get("eur_amount"),
            },
        }

    if "eur_decimal" in receipt and receipt["eur_decimal"] is not None:
        if str(receipt["eur_decimal"]) != format(expected_eur, ".2f"):
            return {
                "ok": False,
                "reason": "receipt eur_decimal does not match 2-decimal statutory EUR representation",
                "details": {
                    "expected_eur_decimal": format(expected_eur, ".2f"),
                    "receipt_eur_decimal": receipt.get("eur_decimal"),
                },
            }

    claimed_dec = _parse_decimal(claimed_value)
    if claimed_dec is None or claimed_dec != expected_eur or claimed_dec.as_tuple().exponent < -2:
        return {
            "ok": False,
            "reason": "claimed_value does not match attested EUR conversion result",
            "details": {
                "expected_eur": format(expected_eur, ".2f"),
                "claimed_value": str(claimed_value),
            },
        }

    return {
        "ok": True,
        "reason": None,
        "details": {
            "ltl_amount": format(ltl_dec, "f"),
            "rate_used": STATUTORY_RATE_STR,
            "expected_eur": format(expected_eur, ".2f"),
            "claimed_eur": format(claimed_dec, ".2f"),
            "computation_sha256": rec_sha,
        },
    }


def _load_text_or_arg(val: str) -> str:
    p = pathlib.Path(val)
    if p.is_file():
        return p.read_text(encoding="utf-8")
    return val


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify an LTL-to-EUR execution receipt and claimed EUR value."
    )
    parser.add_argument(
        "--receipt",
        required=True,
        help="JSON receipt string or path to a JSON receipt file.",
    )
    parser.add_argument(
        "--claimed",
        required=True,
        help="Claimed EUR value to verify (e.g. 100.00 or 289.62).",
    )
    parser.add_argument(
        "--sanctioned-code",
        default=None,
        help="Optional Python code string or path to computations/ltl-to-eur-conversion.md.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON verdict (default output format).")
    args = parser.parse_args(argv)

    try:
        receipt_obj = json.loads(_load_text_or_arg(args.receipt))
    except Exception as exc:
        verdict = {"ok": False, "reason": f"failed to parse receipt JSON: {exc}", "details": {}}
        print(json.dumps(verdict, indent=2))
        return 1

    code_str = _load_text_or_arg(args.sanctioned_code) if args.sanctioned_code is not None else None
    verdict = attest(sanctioned_code=code_str, receipt=receipt_obj, claimed_value=args.claimed)
    print(json.dumps(verdict, indent=2))
    return 0 if verdict["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
