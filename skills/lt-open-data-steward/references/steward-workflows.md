# Steward Operational Workflows, Migration, and Validator Guide

This guide details the step-by-step operational procedures for `lt-open-data-steward` alongside [frontmatter-and-provenance.md](frontmatter-and-provenance.md) and [../scripts/validate.py](../scripts/validate.py).

## 1. Upstream Refresh and `inputs.lock.json` Verification

1. **Audit locked inputs (`inputs.lock.json`):**
   - `manifest`: `repository` (`https://github.com/atviriduomenys/manifest.git`), `commit_sha`, `commit_timestamp_utc`, `license` (`AGPL-3.0-only`), and `deployment_list_sha256` (`get_data_gov_lt.in`).
   - `dcat_ap_rdf`: `url` (`https://data.gov.lt/edp/dcat-ap.rdf`), `sha256`, and `size_bytes`.
   - `standards_inputs`: SHA-256 digests and reuse terms (`Reuse Decision 2011/833/EU`, `ODC-PDDL-1.0`) for EUR-Lex CELEX HTMLs (`32006R1893`, `32008R0213`), Publications Office SPARQL exports, and ISO 639-2/4217 CSVs.
2. **Preserve Spinta namespace fidelity:**
   - Map every concept path from the CSV's declared `dataset` and `model` values — never from the CSV filename (`151` of `1,100` CSVs diverge, and `datasasets/gov/ivpk/svetainiu_atitikties_vertinimas` `[sic]` is intentionally preserved).
   - Check `get_data_gov_lt.in` before emitting `resource:`: deployed CSVs get `resource: "https://get.data.gov.lt/<path>"` and tag `deployed`; schema-only CSVs (`112` files -> `112` datasets, `209` tables) omit `resource:` and carry tag `undeployed`.
3. **Scrub PII and issue-tracker noise:**
   - Strip personal email sentences (`firstname.lastname@...`, consumer domains like `gmail.com`, `inbox.lt`), phone clauses (`+370...`, `(8 5)...`, `8 6...`), `"Įmonės vadovas – <Vardas Pavardė>"` lines, pure tracker tokens (`spinta:40`, `manifest:1290`), and `comment.source` personal names.
   - Retain official institutional contact emails (`info@...`, `atverimas@...`, `duomenys@...`, `pagalba@...`, `rastine@...`, or `<agency>@<agency>.gov.lt`).
4. **Update indexes and `log.md`:**
   - Regenerate `index.md` in each modified directory using `* [Title](path) - description`. Keep frontmatter **only** on root `bundle/index.md` (`okf_version: "0.3"`, `title`, `description`, `license: "AGPL-3.0-only"`).
   - Prepend a new `## YYYY-MM-DD` section at the top of `bundle/log.md` (newest date first, no frontmatter).

## 2. Recording Steward Sign-Offs (`verified`)

1. Verify all three preconditions before writing a `verified` event:
   - The reviewer inspected the **current** file content (`event.at >= generated.at`).
   - The reviewer explicitly instructed you to record verification.
   - The reviewer explicitly provided their actor ID (`human:<id>`, `team:<id>`, or `process:<id>`). **Never** guess `<id>` from `$USER`, `%USERNAME%`, or `git config user.name` / `user.email`.
2. Append `{ by: "<actor>", at: "<YYYY-MM-DDTHH:MM:SSZ>" }` to frontmatter `verified`.
3. Keep all older `verified` entries intact as audit history, and **do not** modify `generated` (recording a verification does not change the concept's meaning).

## 3. Retiring, Splitting, or Renaming Spinta Models

- **Retiring a removed model:** Never delete a previously published `.md` concept if downstream links or bookmarks may reference it. Keep its schema/definition and `verified` history, add `status: deprecated`, set `superseded_by: "/datasets/..."` (leading `/` required in OKF `v0.3`) if a successor model exists, and document the retirement at the top of the body.
- **Renaming or moving a model without changing meaning:** Copy the file to the new path **keeping its original `generated` and `verified` fields unchanged** (so existing `human:` or `team:` verifications remain current!), and replace the old path with a deprecated concept pointing to `superseded_by: "/<new-path>.md"`.

## 4. Authoring Statutory or Agency `Attested Computation`s

1. Only wrap formulas or queries that come verbatim from an authoritative law or steward-approved repository (e.g., `bundle/computations/ltl-to-eur-conversion.md` implementing Council Reg. (EU) No 851/2014 `1 EUR = 3.45280 LTL`).
2. Implement the executor (`bundle/references/executors/<name>.py`) as deterministic code accepting the declared `parameters` and returning a dictionary containing every field listed in `executor.receipt` (including `computation_sha256`).
3. Implement the attester (`bundle/references/attesters/<name>.py`) as deterministic, zero-LLM Python code verifying parameter types, invariants, rounding rules, and `computation_sha256`, returning `{"ok": True}` or `{"ok": False, "reason": "<explanation>"}`.
4. Ensure both `/references/executors/<name>.py` and `/references/attesters/<name>.py` exist inside `bundle/` before referencing them in frontmatter (`W116`).

## 5. Migrate OKF `v0.1` / `v0.2` Bundles to `v0.3`

1. Update root `bundle/index.md` frontmatter to include `okf_version: "0.3"`, `title`, a one-sentence routing `description`, and `license: "AGPL-3.0-only"`.
2. Prefix every bundle-root frontmatter path field (`sources[].resource`, `computation`, `executor.resource`, `attester.resource`, `superseded_by`) with `/` (`W119` -> clean `v0.3` resolution). Leave Markdown links in prose relative to each file.
3. Strip any YAML frontmatter from `bundle/log.md` (`E006`) and from every non-root `index.md` (`E004`).
4. Convert scalar `tags` strings into YAML lists (`tags: [gov, vmi, deployed]`, `W110`).
5. Add `/`-rooted `superseded_by` to `status: deprecated` concepts that have replacements.
6. Ensure every date-time carries an explicit UTC or numeric offset (`Z` or `+HH:MM`, `W101`), and use full date-times on `generated.at` and `verified[].at` (`W122`).
7. For `v0.1` files, replace `timestamp` with `generated: { by: "<actor>", at: "<timestamp>" }` (when producer is known) and convert `# Citations` body lists into `sources` entries + inline `[^id]` footnotes.
8. Run `validate.py --strict --spinta-checks` and report any `I204` findings where `generated.at` updates superseded older `verified` events.

## 6. `validate.py` Diagnostic Code Reference

| Code | Level | Meaning |
| --- | --- | --- |
| `E002` | Error | Frontmatter is unclosed or invalid YAML / non-mapping (§4). |
| `E004` | Error | Subdirectory `index.md` contains frontmatter (§8). |
| `E005` | Error | `log.md` `## ` heading is not `YYYY-MM-DD` (§9). |
| `E006` | Error | `log.md` contains frontmatter (§9). |
| `E007` | Error | Frontmatter repeats a duplicate YAML key (§4). |
| `W101` | Warning | Malformed RFC 3339 timestamp / `stale_after` / `usage_window` (§5). |
| `W102`–`W104` | Warning | Malformed `generated` (`W102`), invalid actor string (`W103`), or incomplete `verified[i]` (`W104`). |
| `W105` | Warning | `status` outside `draft`, `stable`, `deprecated` (§5.4). |
| `W106`–`W109` | Warning | Missing `sources[i].resource` (`W106`), duplicate `sources[i].id` (`W107`), uncited `[^label]` (`W108`), or `usage_count` without `usage_window` (`W109`). |
| `W110` | Warning | `tags` is a scalar string or non-list (§4.1). |
| `W111`–`W114`, `W126` | Warning | `Attested Computation` missing `runtime` (`W111`), missing/conflicting `Computation` block (`W112`, `W126`), incomplete `parameters` (`W113`), or malformed `executor`/`attester` (`W114`). |
| `W115`–`W116`, `W119` | Warning | Broken body link (`W115`), broken frontmatter path/license (`W116`), or v0.2 bare-path root fallback (`W119`). |
| `W117`–`W118`, `W120` | Warning | Unquoted non-string scalar (`W117`), `log.md` dates out of order (`W118`), or `.md` file without `type` (`W120`). |
| `W122`–`W123`, `W125` | Warning | Date-only `generated.at`/`verified[].at` (`W122`), `superseded_by` without `deprecated` (`W123`), or missing root `index.md` / `okf_version` (`W125`). |
| `W130` | Warning | (`--spinta-checks`) `deployed`/`undeployed` tag inconsistent with `get.data.gov.lt` `resource:`. |
| `W131` | Warning | (`--spinta-checks`) Unscrubbed personal email or phone number PII detected outside institutional role contacts. |
| `W132` | Warning | (`--spinta-checks`) Footnote bijection mismatch between `sources[].id`, inline `[^id]`, and `[^id]:` definitions. |
| `I201`, `I203`–`I205` | Info | Concept past `stale_after` (`I201`), unprefixed extension key (`I203`), all `verified` older than `generated.at` (`I204`), or `Attested Computation` without `attester` (`I205`). |
