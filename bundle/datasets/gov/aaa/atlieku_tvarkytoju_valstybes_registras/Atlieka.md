---
type: Table
title: "Atlieka — Atliekų klasifikatorius"
description: "Atliekų klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Atlieka"
tags: [gov, aaa, atlieka, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130"
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3840/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Atlieka — Atliekų klasifikatorius

Atliekų klasifikatorius[^manifest]

- **Model:** `datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Atlieka`[^manifest]
- **Dataset:** [Atliekų tvarkytojų valstybės registro duomenys](../atlieku_tvarkytoju_valstybes_registras.md) (`datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/Atlieka` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `atliekos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L130)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras (https://data.gov.lt/datasets/3840/)
