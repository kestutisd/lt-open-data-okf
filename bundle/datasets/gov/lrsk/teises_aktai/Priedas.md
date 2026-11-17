---
type: Table
title: "Priedas — Teisės aktų priedų tekstai"
description: "Spinta table datasets/gov/lrsk/teises_aktai/Priedas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai/Priedas"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L78"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priedas — Teisės aktų priedų tekstai

- **Model:** `datasets/gov/lrsk/teises_aktai/Priedas`[^manifest]
- **Dataset:** [Teisės aktų registro duomenys](../teises_aktai.md) (`datasets/gov/lrsk/teises_aktai`)
- **Manifest CSV:** [datasets/gov/lrsk/teises_aktai.csv#L78](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/teises_aktai.csv#L78)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/teises_aktai/Priedas`
- **Primary Key (`ref`):** `priedo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priedo_id` | `string` | — | `4` | `open` | — | Priedo identifikacinis numeris | — |
| `dokumento_id` | `string` | — | `4` | `open` | — | Teisės akto, kuriam priklauso nurodytasis priedas, identifikacinis numeris. | Laukas dokumento_id jungia duomenų modelį su kitais dviem rinkinio modeliais. |
| `priedo_pav` | `string` | — | `4` | `open` | — | Priedo failo pavadinimas | — |
| `failo_pletinys` | `string` | — | `4` | `open` | — | Priedo failo plėtinys | — |
| `priedo_tekstas` | `string` | — | `4` | `open` | — | Tekstas, ištrauktas iš priedo failo, kai jo dydis neviršija 50MB. Atkreipiamas dėmesys, jog apdoroti tik nesudėtingo formatavimo .pdf, .xlsx ir .docx formato failai. Jeigu tekstas negalėjo būti ištrauktas, laužtiniuose skliausteliuose pateikiama priežastis. | — |
| `priedo_url` | `string` | — | `4` | `open` | — | URL nuoroda į priedo failą teisės aktų registre. | — |
| `atnaujinimo_data` | `datetime` | `S` | `4` | `open` | — | Priedo failo atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/teises_aktai.csv
