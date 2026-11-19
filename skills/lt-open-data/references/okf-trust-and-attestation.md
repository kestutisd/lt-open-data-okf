# OKF v0.3 Trust, Lifecycle, Freshness, Conflict, Path, and Attestation Rules

This reference specifies the deterministic consumer rules from [`SPEC.md`](https://github.com/open-knowledge-format/open-knowledge-format/blob/main/SPEC.md) (`OKF v0.3`) applied by `lt-open-data`.

## 1. Trust Tier Derivation (`SPEC.md` §5.3)

Derive a concept's trust tier strictly from **current** verification events in frontmatter `verified`:

1. Read `verified`. If it is a single mapping `{ by, at }`, normalize it to a one-element list `[{ by, at }]`.
2. Ignore any event that lacks a non-empty `by` or a valid RFC 3339 `at`.
3. Compare instants in UTC (a date without a time `YYYY-MM-DD` means `YYYY-MM-DDT00:00:00Z`). An event is **current** when `event.at >= generated.at`, or when `generated` (and v0.1 `timestamp`) is absent.
4. Derive the exact OKF trust tier string:
   - **`unverified`**: no current verification event exists (default across all `3,420` shipped concepts).
   - **`machine-confirmed`**: at least one current event exists, and all current `by` actors are non-`human:` (`team:<id>`, `process:<id>`, other schemes, or `<producer>/<version>`).
   - **`human-reviewed`**: at least one current event has a `by` actor starting with `human:`.
5. Keep events older than `generated.at` as historical provenance and report `"verified only before the last change"` when every event predates `generated.at`.
6. Treat trust tiers as reader guidance, never as access control — never refuse to read or answer from an `unverified` concept.

## 2. Lifecycle Status and `superseded_by` (`SPEC.md` §5.4)

| `status` | Meaning | Required Consumer Action |
| --- | --- | --- |
| Absent or `stable` | Current | Use normally. |
| `draft` | Current, provisional (`model.level == "0"` or `/provisional/`) | Use, and explicitly tell the user the concept is `draft`. |
| `deprecated` | Retired; retained for historical links | Do **not** present as current. Follow `superseded_by` to the replacement (or inspect body links if `superseded_by` is absent) and report the replacement. |
| Any other value | Not current | Do **not** present as current; report the raw `status` string verbatim. |

`superseded_by` is a frontmatter path field and carries meaning only when `status: deprecated`.

## 3. Freshness (`stale_after`, `SPEC.md` §5.5)

1. Read `stale_after`. Treat `null`, `""`, or `[]` as absent (no `stale_after`).
2. Parse RFC 3339 date-time (`2026-12-31T00:00:00Z`) or date (`2026-12-31` -> `2026-12-31T00:00:00Z`).
3. When `now >= stale_after`, the concept is **stale** — report the date/time since which it became stale.
4. When `stale_after` is non-empty and fails to parse, **always** treat the concept as **stale** and note that `stale_after` is malformed.
5. Stale means "re-check against live or upstream sources", not "false". Freshness is orthogonal to trust (`human-reviewed` concepts can be stale).

## 4. Source Credibility Signals and Citations (`SPEC.md` §5.1)

Weigh source facts without collapsing them into synthetic scores:

| Field | Signal | How to Interpret |
| --- | --- | --- |
| `sources[].author` | Authority | Actor that published the source (e.g., `team:vssa` for `atviriduomenys/manifest`, `team:vda` for `data.gov.lt` DCAT-AP). |
| `sources[].usage_count` + `usage_window` | Liveness | Compare only as used-vs-unused or by order of magnitude across comparable sources. |
| `sources[].last_modified` | Recency | Upstream modification timestamp of the source (distinct from `generated.at`). |

- Resolve every inline footnote `[^label]` by matching `sources[].id == label` (e.g., `[^manifest]`, `[^dcat]`, `[^std-eur]`, `[^std-evrk]`, `[^std-cpv]`, `[^std-iso639]`).
- If `sources[].resource` points to another concept inside the bundle, follow that concept's `sources` when tracing lineage.

## 5. Deterministic Conflict Resolution (`SPEC.md` §5)

When two concepts in the bundle make conflicting claims, prefer them in strict lexicographic order (first difference wins):

1. **Current status:** `stable` or `draft` beats `deprecated` or unknown `status`.
2. **Trust tier:** `human-reviewed` > `machine-confirmed` > `unverified`.
3. **Freshness:** non-stale beats stale.
4. **Generation recency:** later `generated.at` beats earlier `generated.at`.

Always disclose the conflict and explain which rule decided. If all four steps tie, present both claims with their concept IDs.

## 6. Path Resolution and Older-Bundle Fallbacks (`SPEC.md` §§6, 11.2, 12.1)

### Paths (§6)

1. A string with a URI scheme (`https:`, `http:`, `urn:`) is an external URI.
2. A path starting with `/` resolves from `BUNDLE_DIR` (e.g., `/references/executors/ltl_to_eur.py` -> `<BUNDLE_DIR>/references/executors/ltl_to_eur.py`).
3. Any other relative path resolves from the directory of the file containing it (e.g., `../ja_mokesciai.md`).
4. Any path resolving outside `BUNDLE_DIR` is external — **never** read it from the local filesystem.
5. Paths are case-sensitive; percent-decode (`%20` -> space) before filesystem lookup.
6. A `sources[].resource` containing raw spaces is a human scope descriptor, not a filesystem path.

### Value Normalization (§11.2)

- `null`, `""`, and `[]` are equivalent to an omitted key.
- List-valued fields (`tags`, `sources`, `verified`, `parameters`) promote a single item to a 1-item list.
- A scalar `tags` string is **one single tag** — never split it on commas.
- Ignore list entries missing their required key (e.g., `sources` entry without `resource`, `verified` entry without `by` or `at`).

### Fallbacks for `okf_version <= 0.2` or Unversioned Bundles (§12.1)

- If a bare frontmatter path field (no leading `/`) does not resolve relative to its file, resolve it from `BUNDLE_DIR` (applies to frontmatter path fields only, never body links).
- If `generated` is absent, use frontmatter `timestamp` as the last-change instant.
- If `sources` is absent, read `# Citations` in the Markdown body.

## 7. Attested Computations and Attestation Gate {#attestation-gate}

When answering a numerical question governed by an `Attested Computation` (such as `bundle/computations/ltl-to-eur-conversion.md` for statutory LTL -> EUR conversion under Council Reg. (EU) No 851/2014):

1. **Load:** Read `runtime`, `parameters`, `executor`, `attester`, and either frontmatter `computation` or the first fenced code block under `# Computation` (at any heading depth).
2. **Parameterize:** Bind only declared `parameters` (ask the user if a required value is ambiguous; never edit the code or write an ad-hoc calculation).
3. **Execute:** Run `executor.resource` verbatim and capture all fields listed in `executor.receipt`.
4. **Attest:** Run `attester.resource` on `(receipt, candidate_value)` to obtain `{"ok": bool, "reason"?: str}` — never simulate the attester in prose.

### Mandatory 6-Case Attestation Gate (`SPEC.md` §§10.2, 10.5)

| Runtime Outcome | Mandatory Consumer Output |
| --- | --- |
| Attestation `ok: true` and concept is **not stale** | Show the computed value, `attested`, and a receipt reference (e.g., `computation_sha256` / `rate_used`). |
| Attestation `ok: true` and concept **is stale** | Warn that the computation passed `stale_after`, then show the value, `attested`, and receipt reference. |
| Attestation `ok: false` (failed) | **Show NO value in any form** (not even inside prose explanation). Show only the failure `reason`. |
| Execution did not run (no Python/runtime/credentials) | **Show NO computed value.** Show the computation code with parameter values bound, marked `not attested` (did not run). |
| Concept lacks `runtime` or lacks `attester` | Show the value only if executed, explicitly labeled `not attested` — **never** call it `attested`. |
| Concept has neither `computation` path nor `# Computation` code fence | **Show NO value.** Report that the concept is not attestable. |

### Worked Walkthrough: `computations/ltl-to-eur-conversion.md`

```bash
python3 -X utf8 -c '
import importlib.util, json, pathlib, sys
bundle = pathlib.Path(sys.argv[1])
ltl = float(sys.argv[2])

def load_mod(name, rel):
    spec = importlib.util.spec_from_file_location(name, bundle / rel.lstrip("/"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

ex = load_mod("ltl_exec", "/references/executors/ltl_to_eur.py")
at = load_mod("ltl_att", "/references/attesters/ltl_to_eur_attester.py")
doc_md = (bundle / "computations/ltl-to-eur-conversion.md").read_text(encoding="utf-8")
receipt = ex.execute(ltl_amount=ltl)
verdict = at.attest(receipt=receipt, claimed_value=receipt["eur_amount"], sanctioned_code=doc_md)
print(json.dumps({"receipt": receipt, "verdict": verdict}, indent=2))
' "$BUNDLE_DIR" "1000"
```

Remember: `verified` (stored in frontmatter) records whether a steward or process confirmed the **definition**, whereas `attested` (evaluated at runtime, never written back to the bundle) confirms whether **this single run** executed the sanctioned computation. Always report both in **Concepts used**.
