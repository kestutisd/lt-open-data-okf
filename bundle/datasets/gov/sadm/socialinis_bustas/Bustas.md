---
type: Table
title: "Bustas — Socialinio būsto fondas"
description: "Lentelėje pateikiama informacija apie būstus Lietuvoje, kurie tam tikru laikotarpiu praeityje atliko ar iki šiol atlieka socialinio būsto funkciją."
resource: "https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Bustas"
tags: [gov, sadm, bustas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L41"
    title: "atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L41"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Bustas — Socialinio būsto fondas

Lentelėje pateikiama informacija apie būstus Lietuvoje, kurie tam tikru laikotarpiu praeityje atliko ar iki šiol atlieka socialinio būsto funkciją. Lentelės objektas – vienas būstas. Nurodomos būsto charakteristikos (plotas, kambarių skaičius, būsena duomenų atnaujinimo metu, pirmo ir paskutinio apgyvendinimo datos) bei vietovės duomenys (gyvenvietė, savivaldybė, koordinatės pagal LKS ir WGS koordinačių sistemas). Duomenys jungiami su lentele „Socialinio ir savivaldybės būsto nuomos duomenys“ pagal lauką „busto_id“.[^manifest]

- **Model:** `datasets/gov/sadm/socialinis_bustas/Bustas`[^manifest]
- **Dataset:** [Socialinio būsto duomenys](../socialinis_bustas.md) (`datasets/gov/sadm/socialinis_bustas`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/soc_bustas.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L41)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/socialinis_bustas/Bustas` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `busto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `busto_id` | `string` | — | `4` | `open` | — | Būsto identifikacinis numeris | — |
| `busto_tipas` | `string` | — | `4` | `open` | — | Būsto tipas | — |
| `plotas_kv_m` | `number` | `m²` | `4` | `open` | — | Būsto plotas, išreikštas kvadratiniais metais | — |
| `kambariu_sk` | `integer` | — | `4` | `open` | — | Kambarių skaičius būste | — |
| `busena` | `string` | — | `4` | `open` | — | Būsto būsena | — |
| `apgyvendinimo_pradzia` | `date` | `D` | `4` | `open` | — | Pirmo apgyvendinimo būste data | — |
| `apgyvendinimo_pabaiga` | `date` | `D` | `4` | `open` | — | Paskutinio apgyvendinimo būste data | — |
| `pastato_tipas` | `string` | — | `4` | `open` | — | Būsto pastato tipas | — |
| `gyvenviete` | `string` | — | `4` | `open` | — | Būsto gyvenvietė | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Būsto savivaldybė | — |
| `geometrija_lks_adp` | `geometry(3346)` | — | `4` | `open` | — | Būsto adreso koordinatės, išreikštos LKS koordinačių sistemoje | — |
| `geometrija_wgs_adp` | `geometry(4326)` | — | `4` | `open` | — | Būsto adreso koordinatės, išreikštos WGS koordinačių sistemoje | — |
| `geometrijos_ivertis` | `integer` | — | `4` | `open` | — | Būsto koordinačių tikslumo įvertis | — |
| `duomenu_atnaujinimas` | `datetime` | `S` | `4` | `open` | — | Būsto būsenos atnaujinimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busto_tipas` | `"savivaldybė"` | — | — | — | — |
| `busto_tipas` | `"rinka"` | — | — | — | — |
| `pastato_tipas` | `"daugiabutis"` | — | — | — | — |
| `pastato_tipas` | `"1 arba 2 butų"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/soc_bustas.csv#L41 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/soc_bustas.csv#L41)
