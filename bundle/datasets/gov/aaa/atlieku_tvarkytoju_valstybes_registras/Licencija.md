---
type: Table
title: "Licencija — Informacija apie organizacijoms išduodamas licencijas"
description: "Organizacijoms išduodamos licencijos"
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Licencija"
tags: [gov, aaa, licencija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L144"
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L144"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3840/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Licencija — Informacija apie organizacijoms išduodamas licencijas

Organizacijoms išduodamos licencijos[^manifest]

- **Model:** `datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Licencija`[^manifest]
- **Dataset:** [Atliekų tvarkytojų valstybės registro duomenys](../atlieku_tvarkytoju_valstybes_registras.md) (`datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L144](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L144)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Licencija` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `licencijos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `licencijos_id` | `string` | — | `4` | `open` | — | Licencijos identifikatorius | — |
| `licencijos_numeris` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `licencijos_kodas` | `string` | — | `4` | `open` | — | Licencijos kodas | — |
| `licencijos_tipas` | `string` | — | `4` | `open` | — | Licencijos tipas | — |
| `licencijos_pavadinimas` | `string` | — | `4` | `open` | — | Licencijos pavadinimas | — |
| `licencijos_isdavimo_data` | `date` | `D` | `4` | `open` | — | Licencijos išdavimo data | — |
| `licencijos_panaikinimo_data` | `date` | `D` | `4` | `open` | — | Licencijos panaikinimo data | — |
| `licencijos_busena` | `string` | — | `4` | `open` | — | Licencijos būsena | — |
| `licencijos_turetojo_juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Licencijos turėtojo juridinio asmens kodas | — |
| `licencijos_turetojo_pavadinimas` | `string` | — | `4` | `open` | — | Licencijos turėtojo pavadinimas | — |
| `licencijos_turetojo_adresas` | `string` | — | `4` | `open` | — | Licencijos turėtojo adresas | — |
| `isdavusioji_institucija` | `string` | — | `4` | `open` | — | Išdavusioji institucija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `licencijos_busena` | `"Išduota"` | — | — | — | — |
| `licencijos_busena` | `"Įspėta"` | — | — | — | — |
| `licencijos_busena` | `"Sustabdyta"` | — | — | — | — |
| `licencijos_busena` | `"Panaikinta"` | — | — | — | — |
| `isdavusioji_institucija` | `"Lietuvos Respublikos aplinkos ministerija"` | — | — | — | — |
| `isdavusioji_institucija` | `"Aplinkos apsaugos agentūra"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L144 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L144)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras (https://data.gov.lt/datasets/3840/)
