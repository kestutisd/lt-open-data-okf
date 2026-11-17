# Lithuanian Open Data — OKF v0.2 Knowledge Bundle

Pure [Open Knowledge Format (`OKF v0.2`)](https://github.com/GoogleCloudPlatform/open-knowledge-format) knowledge bundle generated directly from the Lithuanian Open Data Spinta Data Structure Definition (`DSA`) catalog at [`atviriduomenys/manifest`](https://github.com/atviriduomenys/manifest) (commit `ec54998dcea52a0d26dc1c172eacec438d47e727`, `2026-11-11T14:39:20Z`).

> **Unofficial / Unverified:** Neither Lithuanian public-sector agencies nor human data stewards have reviewed or endorsed this bundle. All `3,411` concepts omit `verified:` frontmatter (`0` `human:` verifications; inferred trust tier `unverified`).

## Summary

| Metric | Value |
| --- | --- |
| OKF Specification Version | `0.2` ([bundle/index.md](bundle/index.md)) |
| Upstream Source | [`atviriduomenys/manifest`](https://github.com/atviriduomenys/manifest) (`ec54998dce`) |
| Manifest CSV Files Parsed | `1,100` (`988` in `get_data_gov_lt.in`, `112` undeployed) |
| `Dataset` Concepts | `1,104` (`992` deployed, `112` undeployed) |
| `Table` Concepts | `2,307` (`2,098` deployed, `209` undeployed) |
| Total OKF Concepts | `3,411` |
| License | `GNU AGPL-3.0` ([LICENSE](LICENSE), [NOTICE.md](NOTICE.md)) |

## Repository Structure

```text
.
├── .agents/
│   └── skills.json               # Workspace skill discovery manifest
├── .gitattributes                # LF line-ending normalization
├── .gitignore                    # OS metadata ignore rules
├── LICENSE                       # GNU AGPL-3.0 (from atviriduomenys/manifest)
├── NOTICE.md                     # Attribution & unofficial/unverified disclaimer
├── README.md                     # Repository overview
├── bundle/                       # OKF v0.2 Knowledge Bundle
│   ├── index.md                  # Root progressive-disclosure index (okf_version: "0.2")
│   ├── log.md                    # Directory update log
│   ├── viz.html                  # Self-contained offline HTML5 Canvas graph viewer
│   ├── datasets/                 # Canonical dataset & table concepts + index.md hierarchy
│   └── datasasets/               # Upstream [sic] namespace preserved verbatim from CSV
└── skills/
    └── lt-open-data/
        └── SKILL.md              # Agent skill for OKF navigation & Spinta DSA rules
```

## OKF v0.2 & Spinta DSA Conventions

- **Concept paths follow declared Spinta namespaces:** `bundle/<dataset>.md` (`type: Dataset`) and `bundle/<dataset>/<Model>.md` (`type: Table`) always reflect the CSV's declared `dataset` and `model` identifiers (`151` CSV filenames differ from their declared namespace).
- **Saugykla deployment (`get_data_gov_lt.in`):** Frontmatter `resource: "https://get.data.gov.lt/<path>"` is emitted only when the source CSV is listed in `get_data_gov_lt.in`; schema-only manifests omit `resource`.
- **Provenance (`sources`):** Every concept cites `[^manifest]` pointing to the exact upstream CSV file and 1-based line number in `atviriduomenys/manifest`.

## Quick Start

1. **Browse progressively:** Start at [bundle/index.md](bundle/index.md) or [bundle/datasets/gov/index.md](bundle/datasets/gov/index.md), open a `Dataset` concept (`bundle/<dataset>.md`), and follow `# Tables` links to `bundle/<dataset>/<Model>.md` for column-level `# Schema` definitions.
2. **Explore visually offline:** Open [bundle/viz.html](bundle/viz.html) directly in any modern browser (zero external CDN requests).
3. **Install the agent skill ([skills/lt-open-data/SKILL.md](skills/lt-open-data/SKILL.md)):**
   - **Agent Skills CLI (Claude Code, Cursor, Codex, etc.):** `npx skills add kestutisd/lt-open-data-okf` (pass `-g` for global install).
   - **Claude Code (manual copy):** Copy `skills/lt-open-data` to `$HOME/.claude/skills/lt-open-data` (global) or `.claude/skills/lt-open-data` (project).
   - **Antigravity:** Open a clone of this repository as a workspace (auto-loaded via [.agents/skills.json](.agents/skills.json)), or copy `skills/lt-open-data` to `$HOME/.gemini/config/skills/lt-open-data` (global).
   - When installed standalone without cloning this repository, the skill resolves `./bundle` or bootstraps a shallow cache at `$HOME/.cache/lt-open-data-okf` on first use.

## License

Licensed under **GNU AGPL-3.0** — see [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
