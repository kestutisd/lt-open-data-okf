---
type: Table
title: "ReklamosLeidimas — Rinkinyje pateikiama informacija apie Utenos rajone išduotus leidimus reklamai. Jame nurodomi leidimo numeris, išdavimo data, galiojimo laikotarpis, pareiškėjas (fizinis ar juridinis asmuo) ir susijęs kodas. Taip pat..."
description: "Utenos rajono savivaldybės reklamų leidimai"
resource: "https://get.data.gov.lt/datasets/gov/utenos_r_sav/reklamos_leidimai/ReklamosLeidimas"
tags: [gov, utenos_r_sav, reklamosleidimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3824/"
    title: "data.gov.lt DCAT-AP — datasets/gov/utenos_r_sav/reklamos_leidimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ReklamosLeidimas — Rinkinyje pateikiama informacija apie Utenos rajone išduotus leidimus reklamai. Jame nurodomi leidimo numeris...

**Dataset Context:** Utenos rajono savivaldybės reklamų leidimai[^manifest]

- **Model:** `datasets/gov/utenos_r_sav/reklamos_leidimai/ReklamosLeidimas`[^manifest]
- **Dataset:** [Reklamos leidimų duomenų rinkinys](../reklamos_leidimai.md) (`datasets/gov/utenos_r_sav/reklamos_leidimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/utenos_r_sav/reklamos_leidimai/ReklamosLeidimas` (`deployed`)[^manifest]
- **Provider:** `utenos_r_sav` — Utenos rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/reklamos_leidimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/utenos_r_sav/reklamos_leidimai (https://data.gov.lt/datasets/3824/)
