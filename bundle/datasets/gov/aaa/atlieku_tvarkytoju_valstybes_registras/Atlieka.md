---
type: Table
title: "Atlieka — Atliekų klasifikatorius"
description: "Atliekų klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Atlieka"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atlieka — Atliekų klasifikatorius

Atliekų klasifikatorius

- **Model:** `datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Atlieka`[^manifest]
- **Dataset:** [Atliekų tvarkytojų valstybės registro duomenys](../atlieku_tvarkytoju_valstybes_registras.md) (`datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`)
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Atlieka`
- **Primary Key (`ref`):** `atliekos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atliekos_id` | `string` | — | `4` | `open` | — | Atliekos identifikatorius | — |
| `atliekos_kodas` | `string` | — | `4` | `open` | — | Atliekos kodas | — |
| `atliekos_pavadinimas` | `string` | — | `4` | `open` | — | Atliekos pavadinimas | — |
| `ar_atlieka_pavojinga` | `boolean` | — | `4` | `open` | — | Požymis, ar atlieka pavojinga | — |
| `tevines_atliekos_id` | `string` | — | `4` | `open` | — | Tėvinės atliekos identifikatorius | — |
| `tevines_atliekos_pavadinimas` | `string` | — | `4` | `open` | — | Tėvinės atliekos pavadinimas | — |
| `atliekos_techninio_srauto_kodas` | `string` | — | `4` | `open` | — | Atliekos technologinio srauto kodas | — |
| `atliekos_techninio_srauto_pavadinimas` | `string` | — | `4` | `open` | — | Atliekos technologinio srauto pavadinimas | — |
| `atliekos_statistinio_srauto_kodas` | `string` | — | `4` | `open` | — | Atliekos statistinio srauto kodas | — |
| `atliekos_statistinio_srauto_pavadinimas` | `string` | — | `4` | `open` | — | Atliekos statistinio srauto pavadinimas | — |
| `tevines_atliekos_statistinio_srauto_id` | `string` | — | `4` | `open` | — | Tėvinės atliekos statistinio srauto pavadinimas | — |
| `iraso_galiojimo_pradzia` | `date` | `D` | `4` | `open` | — | Įrašo galiojimo pradžia | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv
