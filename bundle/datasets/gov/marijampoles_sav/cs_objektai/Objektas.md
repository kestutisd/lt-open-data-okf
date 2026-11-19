---
type: Table
title: "Objektas — Marijampolės savivaldybėje šiuo metu veikiantys civilinės saugos objektai"
description: "Marijampolės mieste bei rajone šiuo metu veikiančios priedangos ir kolektyvinės apsaugos statiniai"
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/cs_objektai/Objektas"
tags: [gov, marijampoles_sav, objektas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/cs_objektai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/cs_objektai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2850/"
    title: "data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/cs_objektai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Objektas — Marijampolės savivaldybėje šiuo metu veikiantys civilinės saugos objektai

Marijampolės mieste bei rajone šiuo metu veikiančios priedangos ir kolektyvinės apsaugos statiniai[^manifest]

- **Model:** `datasets/gov/marijampoles_sav/cs_objektai/Objektas`[^manifest]
- **Dataset:** [Marijampolės savivaldybėje šiuo metu veikiantys civilinės saugos objektai](../cs_objektai.md) (`datasets/gov/marijampoles_sav/cs_objektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/cs_objektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/cs_objektai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/cs_objektai/Objektas` (`deployed`)[^manifest]
- **Provider:** `marijampoles_sav` — Marijampolės savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_eil_nr` | `string` | — | `4` | `open` | — | Objekto identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Objekto tipas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Objekto seniūnija | — |
| `adresas` | `string` | — | `4` | `open` | — | Objekto adresas | — |
| `objekto_pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `su_negalia` | `string` | — | `4` | `open` | — | Ar žmonės su negalia gali naudotis | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS koordinačių sistemoje | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS koordinačių sistemoje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Priedanga"` | — | — | — | — |
| `tipas` | `"Kolektyvinės apsaugos statinys"` | — | — | — | — |
| `su_negalia` | `"Taip"` | — | — | — | — |
| `su_negalia` | `"Ne"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/cs_objektai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/cs_objektai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/cs_objektai (https://data.gov.lt/datasets/2850/)
