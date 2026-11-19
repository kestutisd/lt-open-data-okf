---
type: Table
title: "Sumos — Sumokėtos sumos už medicinos priemonių (prietaisų) nuomą"
description: "Spinta table datasets/gov/vlk/nmp_sumos/Sumos (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/nmp_sumos/Sumos"
tags: [gov, vlk, sumos, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/nmp_sumos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/nmp_sumos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2280/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/nmp_sumos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sumos — Sumokėtos sumos už medicinos priemonių (prietaisų) nuomą

- **Model:** `datasets/gov/vlk/nmp_sumos/Sumos`[^manifest]
- **Dataset:** [Mokamos sumos už medicinos priemonių (prietaisų) nuomą](../nmp_sumos.md) (`datasets/gov/vlk/nmp_sumos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/nmp_sumos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/nmp_sumos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/nmp_sumos/Sumos` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `straipsnis` | `string` | — | `3` | `open` | — | PSDF biudžeto straipsnis | — |
| `kreditorius` | `string` | — | `3` | `open` | — | Įstaigos pavadinimas | — |
| `data_ad` | `date` | — | `4` | `open` | — | Data | Ataskaitinio laikotarpio data mėnesio tikslumu |
| `suma` | `number` | — | `2` | `open` | — | Suma eurais | Kompensuojama suma eurais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money, ref: "EUR")"` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/nmp_sumos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/nmp_sumos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/nmp_sumos (https://data.gov.lt/datasets/2280/)
