# Lithuanian Open Data — OKF v0.3 Knowledge Bundle & Agent Skills

Unofficial [Open Knowledge Format (`OKF v0.3`)](https://github.com/open-knowledge-format/open-knowledge-format) knowledge bundle and multi-agent plugin for Lithuanian Open Data, generated from [`atviriduomenys/manifest`](https://github.com/atviriduomenys/manifest) (`get_data_gov_lt.in`), [`data.gov.lt`](https://data.gov.lt) DCAT-AP metadata, and statutory EU/ISO classifications.

> **Unofficial / Unverified:** Neither Lithuanian public-sector agencies (*VSSA*, *VDA*, *Registrų centras*, *VMI*, *Sodra*, *VKC*, *VPT*) nor human data stewards have reviewed or endorsed this bundle. All `3,420` shipped concepts omit `verified:` frontmatter (`0` verifications; derived OKF v0.3 trust tier `unverified`).

## Bundle Summary (`OKF v0.3`)

| Metric | Value |
| --- | --- |
| OKF Specification Version | `0.3` ([bundle/index.md](bundle/index.md)) |
| Upstream Spinta Manifest | [`atviriduomenys/manifest`](https://github.com/atviriduomenys/manifest) (`ec54998dce`, `2026-11-11T14:39:20Z`) |
| Input Provenance Lock | `inputs.lock.json` (SHA-256 digests for `manifest`, `get_data_gov_lt.in`, `dcat-ap.rdf`, EU/ISO inputs) |
| Manifest CSV Files Parsed | `1,100` (`988` listed in `get_data_gov_lt.in`, `112` undeployed) |
| `Dataset` Concepts (`type: Dataset`) | `1,104` (`992` `deployed`, `112` `undeployed`) |
| `Table` Concepts (`type: Table`) | `2,307` (`2,098` `deployed`, `209` `undeployed`) |
| `Reference` Concepts (`type: Reference`) | `8` (Spinta DSA guide, ISO 639, CPV/BVPŽ, EVRK 2/2.1, LTL/EUR history, JAR/AR/VPT join guides) |
| `Attested Computation` Concepts | `1` (`bundle/computations/ltl-to-eur-conversion.md` + deterministic Python executor & attester) |
| **Total OKF v0.3 Concepts** | **`3,420`** (`unverified` by default) |
| Interactive Graph Viewer | [bundle/viz.html](bundle/viz.html) (self-contained offline HTML5 Canvas explorer) |
| License | `AGPL-3.0-only` ([LICENSE](LICENSE), [NOTICE.md](NOTICE.md)) |

## Repository Structure

```text
.
├── .agents/
│   ├── skills.json                              # Direct workspace skill discovery
│   └── plugins/
│       └── marketplace.json                     # Codex CLI plugin marketplace (./skills root)
├── .antigravity-plugin/
│   └── plugin.json                              # Google Antigravity plugin manifest
├── .claude-plugin/
│   └── marketplace.json                         # Claude Code plugin marketplace (./skills root)
├── .gitattributes                               # Strict LF line-ending normalization
├── .gitignore                                   # Python bytecode & OS metadata ignore rules
├── LICENSE                                      # GNU AGPL-3.0-only
├── NOTICE.md                                    # Attribution, sources, & unverified disclaimer
├── README.md                                    # Repository & multi-agent installation guide
├── inputs.lock.json                             # Cryptographic SHA-256 lock of upstream inputs
├── bundle/                                      # OKF v0.3 Knowledge Bundle (3,420 concepts)
│   ├── index.md                                 # Root index (okf_version: "0.3", title, description, license)
│   ├── log.md                                   # Reverse-chronological update history (no frontmatter)
│   ├── viz.html                                 # Offline HTML5 Canvas concept graph explorer
│   ├── computations/                            # Attested Computations (ltl-to-eur-conversion.md)
│   ├── datasasets/                              # Preserved upstream [sic] Spinta namespace (1 dataset, 4 tables)
│   ├── datasets/                                # Canonical Spinta dataset & table hierarchy (1,103 datasets, 2,303 tables)
│   └── references/                              # Spinta guide, EU/ISO standards, joins/, executors/, attesters/
└── skills/                                      # Lightweight plugin root (copied without multi-MB ./bundle)
    ├── .claude-plugin/
    │   └── plugin.json                          # Claude Code plugin manifest (skills: "./")
    ├── .codex-plugin/
    │   └── plugin.json                          # Codex CLI plugin manifest (skills: "./")
    ├── lt-open-data/                            # Consumer & Spinta RQL query skill
    │   ├── SKILL.md
    │   ├── references/
    │   │   ├── cross-os-bundle.md
    │   │   ├── metadata-and-joins.md
    │   │   ├── okf-trust-and-attestation.md
    │   │   └── spinta-rql.md
    │   └── scripts/
    │       └── scan.py                          # Diacritic/stem-aware OKF v0.3 scanner (PyYAML + stdlib fallback)
    └── lt-open-data-steward/                    # Producer, verification sign-off, & OKF v0.3 validator skill
        ├── SKILL.md
        ├── references/
        │   ├── frontmatter-and-provenance.md
        │   └── steward-workflows.md
        └── scripts/
            └── validate.py                      # OKF v0.3 conformance + --spinta-checks validator
```

## Included Agent Skills

1. **[`lt-open-data`](skills/lt-open-data/SKILL.md) (Consumer & Live RQL Skill):**
   Discovers Lithuanian Open Data datasets, tables, EU/ISO standards, and canonical joins across local or sparse-cached bundles; constructs safe `get.data.gov.lt` Spinta RQL queries (`level`-aware foreign keys, `open` access checks, cursor pagination, `?count()`); executes statutory `Attested Computation`s (such as LTL-to-EUR conversion under Council Reg. 851/2014); and reports OKF v0.3 trust tiers, freshness, attestations, and `[^id]` citations.
2. **[`lt-open-data-steward`](skills/lt-open-data-steward/SKILL.md) (Producer, Steward Sign-Off & Validator Skill):**
   Refreshes or enriches concepts from `atviriduomenys/manifest` (`get_data_gov_lt.in` + `inputs.lock.json`) and `data.gov.lt` DCAT-AP metadata, scrubs personal email/phone PII, records explicit `human:<id>` / `team:<id>` / `process:<id>` verification events, retires or renames models with `status: deprecated` and `/`-rooted `superseded_by`, authors sanctioned `Attested Computation` contracts, migrates `v0.1`/`v0.2` bundles to `v0.3`, and validates bundles via `validate.py --strict --spinta-checks`.

## Multi-Agent Installation

Plugin manifests set `./skills` as the plugin source directory so plugin managers copy **only** the lightweight `skills/` tree instead of the `3,420`-concept `bundle/`. When running outside a clone of this repository, `lt-open-data` automatically bootstraps a shallow sparse-checkout cache (`'bundle/**' '!bundle/viz.html'`) at `${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf`.

### 1. Agent Skills CLI (Claude Code, Cursor, Codex, Copilot, Windsurf)

```bash
# Install both lt-open-data and lt-open-data-steward into your agent environment:
npx skills add kestutisd/lt-open-data-okf

# Or install globally (-g) or select a single skill (--skill):
npx skills add kestutisd/lt-open-data-okf -g --skill lt-open-data
npx skills add kestutisd/lt-open-data-okf -g --skill lt-open-data-steward
```

### 2. Claude Code Plugin Marketplace

```text
/plugin marketplace add kestutisd/lt-open-data-okf
/plugin install lt-open-data@lt-open-data-okf
```

### 3. OpenAI Codex CLI Plugin

Codex CLI discovers the repository marketplace at [.agents/plugins/marketplace.json](.agents/plugins/marketplace.json), which mounts [skills/.codex-plugin/plugin.json](skills/.codex-plugin/plugin.json) (`./skills` only) and exposes both `lt-open-data` and `lt-open-data-steward`.

### 4. Google Antigravity Plugin / Workspace

- **Workspace mode:** Open a clone of this repository in Antigravity — skills load automatically via [.agents/skills.json](.agents/skills.json) and [.antigravity-plugin/plugin.json](.antigravity-plugin/plugin.json).
- **Global user plugin:** Copy `.antigravity-plugin/plugin.json` and `skills/` into `$HOME/.gemini/config/plugins/lt-open-data/` (or copy individual skill folders to `$HOME/.gemini/config/skills/`).

## Quick CLI Usage

```bash
# Scan concepts with Lithuanian diacritic- and stem-insensitive matching (works with or without PyYAML):
python3 skills/lt-open-data/scripts/scan.py bundle --grep "mokesčių" --deployed

# Filter by concept type or inspect JSON summary:
python3 skills/lt-open-data/scripts/scan.py bundle --type "Attested Computation" --json

# Validate full OKF v0.3 conformance + Spinta/PII/bijection invariants:
python3 skills/lt-open-data-steward/scripts/validate.py bundle --strict --spinta-checks
```

## License

Licensed under **GNU AGPL-3.0-only** — see [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
