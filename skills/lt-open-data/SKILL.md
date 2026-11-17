---
name: lt-open-data
description: >-
  Use this skill when exploring or querying Lithuanian Open Data (data.gov.lt,
  get.data.gov.lt, atviriduomenys/manifest), inspecting OKF v0.2 Dataset and
  Table schemas (VMI, Registrų centras JAR & Address Register, Sodra/VSDFV,
  VKC, municipalities, state agencies), or applying Spinta DSA REST/RQL and
  foreign-key serialization rules.
---

# Lithuanian Open Data (`OKF v0.2` + Spinta DSA)

## 1. Locate the OKF Bundle (`BUNDLE_DIR`)

Resolve `BUNDLE_DIR` to the first existing directory containing `index.md`:

1. **Workspace or User Cache (offline):**
   - `./bundle` (workspace clone of `lt-open-data-okf`)
   - `${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf/bundle` (`"$HOME/.cache/lt-open-data-okf/bundle"` works natively in POSIX `sh`/`bash`/`zsh` and Windows PowerShell)
2. **One-Time Shallow Cache Bootstrap (if missing):**
   ```sh
   git clone --depth 1 https://github.com/kestutisd/lt-open-data-okf.git "$HOME/.cache/lt-open-data-okf"
   ```
   *(On POSIX with custom `XDG_CACHE_HOME`, target `"${XDG_CACHE_HOME:-$HOME/.cache}/lt-open-data-okf"` — avoid `${...:-...}` in PowerShell, where it expands to empty. Refresh when latest schemas are requested: `git -C "$HOME/.cache/lt-open-data-okf" pull --ff-only`.)*
3. **Remote Raw Fallback (only when Git and local files are unavailable):**
   Fetch `index.md` -> `<dataset>.md` -> `<dataset>/<Model>.md` from `https://raw.githubusercontent.com/kestutisd/lt-open-data-okf/main/bundle/<path>`.

## 2. Progressive Disclosure Workflow

1. Start at `$BUNDLE_DIR/index.md` (`okf_version: "0.2"`, `1,104` `Dataset` and `2,307` `Table` concepts; `# Subdirectories` -> `datasets/index.md`, `datasasets/index.md`) or `$BUNDLE_DIR/datasets/gov/index.md` (`186` provider subdirectories + `9` top-level `gov/*.md` datasets).
2. Open `$BUNDLE_DIR/<dataset>.md` (`type: Dataset`) to inspect `Saugykla` deployment (`resource:`), `# Tables`, and optional `# Enumerations`, `# Prefixes`, `# Comments`.
3. **Always open the child table file** `$BUNDLE_DIR/<dataset>/<Model>.md` (`type: Table`) before answering questions about columns, scale units, keys, or access — inspect introductory prose, `# Schema` (`Property | Type | Ref | Level | Access | URI | Title | Description`), and optional `# Enumerations`, ``# Translations (`@en`)``, `# Prefixes`, `# Comments`.
4. Every concept omits `verified:` (`unverified` trust tier; `0` human verifications); attribute schema facts to `[^manifest]` (`atviriduomenys/manifest` CSV path and `#L<line>` in `sources`).

## 3. Searching Lithuanian Schemas

Lithuanian prose inflects across grammatical cases (`mokestis`/`mokesčių`, `savivaldybė`/`savivaldybių`, `įmonė`/`įmonių`, `sutartis`/`sutarčių`), while paths and columns use ASCII `snake_case`/`PascalCase` (and *Sodra* lives under `vsdfv`, with `0` literal `"sodra"` matches). Pair short case-insensitive Lithuanian + ASCII stems and scope to `*.md` or `datasets/` to skip the 3 MB `viz.html` viewer:

```sh
git -C "$BUNDLE_DIR" grep -niE "mokes" -- "*.md"
git -C "$BUNDLE_DIR" grep -niE "juridinis|jar|įmon|imon" -- "datasets/gov/rc/"
git -C "$BUNDLE_DIR" grep -niE "savivald" -- "datasets/gov/rc/ar/"
git -C "$BUNDLE_DIR" grep -niE "vsdfv|draud|pensij|pasalp" -- "datasets/gov/vsdfv/"
```

When `ripgrep` is installed or `BUNDLE_DIR` is outside a Git working tree, run `rg -ni "mokes" "$BUNDLE_DIR/datasets/"` or `grep -rniE "mokes" "$BUNDLE_DIR/datasets/"` (also check `"$BUNDLE_DIR/datasasets/"` for the 1 `[sic]` typo namespace).

## 4. Spinta DSA & `get.data.gov.lt` Rules

- **Saugykla Deployment (`get_data_gov_lt.in`):** Frontmatter `resource: "https://get.data.gov.lt/<path>"` is present **only** when the manifest CSV is in `get_data_gov_lt.in` (`988` deployed CSVs -> `992` `Dataset` and `2,098` `Table` concepts tagged `deployed`; `112` schema-only CSVs -> `112` `Dataset` and `209` `Table` concepts tagged `undeployed` with no `resource:`, including all `vsdfv` tables).
- **CSV Path vs. Declared Namespace:** `151` of `1,100` manifest CSV filenames differ from their declared `dataset` path (e.g. `datasets/gov/vmi/ja_sumoketi_mokesciai.csv` declares `datasets/gov/vmi/ja_mokesciai`; `datasets/gov/ivpk/svetainiu_atitikties_vertinimas.csv` declares `[sic]` `datasasets/gov/ivpk/svetainiu_atitikties_vertinimas`). Concept paths and API URLs always use the declared `dataset` and `model`.
- **Spinta `access` Semantics:**
  - `open` (and `open` (inherited)): unrestricted open data with no authorization or purpose restriction.
  - `public`: requires authorized recipients under GDPR purpose limitation (not unrestricted open data).
  - `protected` / `private`: non-open restricted fields; `—` means blank in the manifest CSV.
- **Spinta REST RQL & Foreign Key (`ref`) Serialization:**
  - `https://get.data.gov.lt/<dataset>/<Model>` uses RQL (`?limit(10)`, `?select(id,pavadinimas)`); unknown `key=value` parameters like `?page=1` fail with `PropertyNotFound`.
  - **`level >= 4` `ref` columns** serialize as `{"_id": "<UUID>"}` joining on `TargetModel._id` — even when `# Schema` writes `TargetModel[field]`.
  - **`level = 3` `ref` columns** serialize natural keys (`{"<pk>": "..."}`). **`level <= 2`** columns hold unlinked scalar values without guaranteed referential integrity.
- **Hidden Scale Units & `# Comments`:** Check introductory prose and `# Comments` alongside `# Schema` — `Ref` may be `—` while prose states `tūkst. eurų` (e.g. `datasets/gov/vkc/vvi/Imone.md`) or `# Comments` records unapplied `update(type: "money", ref: "EUR")` proposals.
