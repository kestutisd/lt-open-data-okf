---
type: Table
title: "GyventojuSkaiciusGyvenvietese"
description: "\"Gyventojų skaičius gyvenvietėse ir gyvenviečių koordinates."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sgr/gyventojai_gyvenvietese/GyventojuSkaiciusGyvenvietese"
tags: [gov, lsd, gyventojuskaiciusgyvenvietese, deployed, level-4, cadence-other]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2938/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sgr/gyventojai_gyvenvietese"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GyventojuSkaiciusGyvenvietese

"Gyventojų skaičius gyvenvietėse ir gyvenviečių koordinates. Dėl techninių klausimų ar klaidų kreiptis į atverimas@stat.gov.lt"[^manifest]

- **Model:** `datasets/gov/lsd/sgr/gyventojai_gyvenvietese/GyventojuSkaiciusGyvenvietese`[^manifest]
- **Dataset:** [gyventojų skaičius gyvenvietėse](../gyventojai_gyvenvietese.md) (`datasets/gov/lsd/sgr/gyventojai_gyvenvietese`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sgr/gyventojai_gyvenvietese/GyventojuSkaiciusGyvenvietese` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `gr_gyv_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `OTHER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gr_gyv_id` | `string` | — | `4` | `open` | — | "Gyvenvietės identifikacinis kodas" | — |
| `gyv_pav` | `string` | — | `4` | `open` | — | "Gyvenvietės pavadinimas" | — |
| `gyventoju_sk` | `number` | — | `4` | `open` | — | "Gyventojų skaičius" | — |
| `taskas_wgs` | `geometry(4326)` | — | `4` | `open` | — | "Koordinate wgs 84 formatu" | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sgr/gyventojai_gyvenvietese.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sgr/gyventojai_gyvenvietese (https://data.gov.lt/datasets/2938/)
