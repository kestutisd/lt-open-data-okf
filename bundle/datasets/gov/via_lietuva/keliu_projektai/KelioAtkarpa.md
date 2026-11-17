---
type: Table
title: "KelioAtkarpa — „Kelio darbų atkarpos“"
description: "Duomenys apie kelių atkarpas, kuriose vykdomi kelių darbų projektai."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai/KelioAtkarpa"
tags: [gov, via_lietuva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/keliu_projektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L36"
    last_modified: "2026-11-11T14:39:20Z"
---

# KelioAtkarpa — „Kelio darbų atkarpos“

Duomenys apie kelių atkarpas, kuriose vykdomi kelių darbų projektai. Viena eilutė atitinka vieną unikalią kelio atkarpą, kurioje atliekami arba buvo atliekami kelio darbai. Eilutėje pateikiamą informaciją sudaro: kelio atkarpos unikalus identifikacinis numeris, kelio pavadinimas, visas kelio ilgis, atkarpos pradžios kilometro taškas, ties kuriuo darbai prasideda, ir atkarpos kilometro pabaigos taškas, ties kuriuo darbai baigiasi. Kelio atkarpos koordinačių duomenys bus pridėti ateityje.

- **Model:** `datasets/gov/via_lietuva/keliu_projektai/KelioAtkarpa`[^manifest]
- **Dataset:** [Duomenys apie valstybinės reikšmės kelių projektus](../keliu_projektai.md) (`datasets/gov/via_lietuva/keliu_projektai`)
- **Manifest CSV:** [datasets/gov/via_lietuva/keliu_projektai.csv#L36](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L36)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai/KelioAtkarpa`
- **Primary Key (`ref`):** `atkarpos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atkarpos_id` | `string` | — | `4` | `open` | — | Kelio atkarpos identifikacinis numeris | — |
| `kelio_pavadinimas` | `string` | — | `4` | `open` | — | Kelio pavadinimas | — |
| `kelio_ilgis_km` | `number` | `km` | `4` | `open` | — | Viso kelio ilgis kilometrais | — |
| `atkarpa_nuo_km` | `number` | `km` | `4` | `open` | — | Kelio atkarpos pradžios kilometras | — |
| `atkarpa_iki_km` | `number` | `km` | `4` | `open` | — | Kelio atkarpos pabaigos kilometras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/keliu_projektai.csv
