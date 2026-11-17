---
type: Table
title: "ReklamosLeidimas — Rinkinyje pateikiama informacija apie Utenos rajone išduotus leidimus reklamai. Jame nurodomi leidimo numeris, išdavimo data, galiojimo laikotarpis, pareiškėjas (fizinis ar juridinis..."
description: "Spinta table datasets/gov/utenos_r_sav/reklamos_leidimai/ReklamosLeidimas (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/utenos_r_sav/reklamos_leidimai/ReklamosLeidimas"
tags: [gov, utenos_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/utenos_r_sav/reklamos_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ReklamosLeidimas — Rinkinyje pateikiama informacija apie Utenos rajone išduotus leidimus reklamai. Jame nurodomi leidimo numeris, išdavimo data, galiojimo laikotarpis, pareiškėjas (fizinis ar juridinis...

- **Model:** `datasets/gov/utenos_r_sav/reklamos_leidimai/ReklamosLeidimas`[^manifest]
- **Dataset:** [Reklamos leidimų duomenų rinkinys](../reklamos_leidimai.md) (`datasets/gov/utenos_r_sav/reklamos_leidimai`)
- **Manifest CSV:** [datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/utenos_r_sav/reklamos_leidimai/ReklamosLeidimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `leidimo_nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `isdavimo_data` | `datetime` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `galioja_nuo` | `datetime` | `D` | `4` | `open` | — | Leidimas galioja nuo | — |
| `galioja_iki` | `datetime` | `D` | `4` | `open` | — | Leidimas galioja iki | — |
| `imone` | `string` | — | `4` | `open` | — | Fizinio ar juridinio asmens pavadinimas | — |
| `imones_k` | `string` | — | `4` | `open` | — | Fizinio ar juridinio asmens kodas | — |
| `irenginio_id` | `string` | — | `4` | `open` | — | Įrenginio unikalus identifikatorius | — |
| `reklamos_tipas` | `string` | — | `4` | `open` | — | Reklamos įrenginio tipas | — |
| `reklamos_zona` | `string` | — | `4` | `open` | — | Reklamos zona | — |
| `reklamos_plotas` | `number` | — | `4` | `open` | — | Reklamos plotas | — |
| `reklamos_adresas` | `string` | — | `4` | `open` | — | Reklamos įrenginio adresas | — |
| `geometrija` | `geometry(point,3346)` | — | `4` | `open` | — | Geometrija LKS sistemoje | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/utenos_r_sav/reklamos_leidimai.csv
