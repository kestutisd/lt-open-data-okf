---
type: Table
title: "Daviklis — Klaipėdos valstybinio jūrų uosto vandens srovių daviklių duomenys"
description: "AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai/Daviklis"
tags: [gov, kvjud, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# Daviklis — Klaipėdos valstybinio jūrų uosto vandens srovių daviklių duomenys

AB Klaipėdos valstybinio jūrų uosto direkcijos geografinėje informacinėje sistemoje PortGIS kaupiami geografiniai jūrų uosto duomenys. Rinkinyje pateikiami nuo 2016 m. gegužės veikaintys vertikalaus ir horizontaliojo daviklių duomenys. Vienas įrašas atitinka vieną daviklį.

Duomenų teikėjas – AB Klaipėdos valstybinio jūrų uosto direkcija.

- **Model:** `datasets/gov/kvjud/sroviu_matavimai/Daviklis`[^manifest]
- **Dataset:** [Klaipėdos valstybinio jūrų uosto vandens srovių matavimo duomenys](../sroviu_matavimai.md) (`datasets/gov/kvjud/sroviu_matavimai`)
- **Manifest CSV:** [datasets/gov/kvjud/sroviu_matavimai.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/sroviu_matavimai.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/sroviu_matavimai/Daviklis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `daviklio_id` | `string` | — | `4` | `open` | — | Daviklio identifikacinis numeris | — |
| `dav_pavadinimas` | `string` | — | `4` | `open` | — | Daviklio pavadinimas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `geometrija` | `geometry(point, 3346)` | — | `3` | `open` | — | Geometrija (lokacija) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `dav_pavadinimas` | `"Horizontalus daviklis"` | — | — | Horizontalus daviklis | — |
| `dav_pavadinimas` | `"Vertikalus daviklis"` | — | — | Vertikalus daviklis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/sroviu_matavimai.csv
