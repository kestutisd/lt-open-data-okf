---
type: Table
title: "Korekcija — Atestavimo veiksmų istoriniai įrašai"
description: "Spinta table datasets/gov/ssva/pense_atestatai/Korekcija (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pense_atestatai/Korekcija"
tags: [gov, ssva, korekcija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/ssva/atestatai.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2287/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/pense_atestatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Korekcija — Atestavimo veiksmų istoriniai įrašai

- **Model:** `datasets/gov/ssva/pense_atestatai/Korekcija`[^manifest]
- **Dataset:** [Duomenys apie pastatų energinio naudingumo sertifikavimo ekspertų kvalifikacijos atestatus...](../pense_atestatai.md) (`datasets/gov/ssva/pense_atestatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/atestatai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pense_atestatai/Korekcija` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc-nd/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `ref` | [Atestatas](Atestatas.md) (`level=4 UUID`: `nr._id`) | `4` | `open` | — | Kvalifikacijos atestato numeris | — |
| `veiksmas` | `integer` | — | `4` | `open` | — | Atestavimo etapas ar poveikio priemonė | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Atestavimo etapo ar poveikio priemonės pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Atestavimo etapo ar poveikio priemonės pabaiga | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `veiksmas` | `1` | — | — | Išduotas neriboto galiojimo atestatas | — |
| `veiksmas` | `2` | — | — | Išduotas riboto galiojimo atestatas | — |
| `veiksmas` | `3` | — | — | Atestato galiojimas patvirtintas | — |
| `veiksmas` | `4` | — | — | Nepatvirtintas atestato galiojimas | — |
| `veiksmas` | `5` | — | — | Pratęstas riboto galiojimo atestatas | — |
| `veiksmas` | `6` | — | — | Ekspertui pareikštas įspėjimas | — |
| `veiksmas` | `7` | — | — | Atestato galiojimas laikinai sustabdytas | — |
| `veiksmas` | `8` | — | — | Atestato galiojimas panaikintas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/atestatai.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/pense_atestatai (https://data.gov.lt/datasets/2287/)
