---
type: Table
title: "ParaiskuStatistika — Savanorių paraiškų statistika pagal priimančias organizacijas"
description: "Jaunimo reikalų agentūros Jaunimo savanoriškos tarnybos sistema kaupia duomenis apie jaunimo savanorystę priimančiose organizacijose."
resource: "https://get.data.gov.lt/datasets/gov/jra/paraiskos/ParaiskuStatistika"
tags: [gov, jra, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/jra/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/paraiskos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ParaiskuStatistika — Savanorių paraiškų statistika pagal priimančias organizacijas

Jaunimo reikalų agentūros Jaunimo savanoriškos tarnybos sistema kaupia duomenis apie jaunimo savanorystę priimančiose organizacijose. Institucija teikia duomenis, kaupiamus nuo 2018 m., juos atnaujinti numatyta kasdien. Duomenyse kaupiama priimančios organizacijos pavadinimas ir adresas, savanorystės paraiškos teikimo metai, priimtų, atmestų įprastų paraiškų skaičiai bei jų suma, paraiškų tapti kuratoriumi bei mentoriumi skaičiai.

- **Model:** `datasets/gov/jra/paraiskos/ParaiskuStatistika`[^manifest]
- **Dataset:** [Savanorių paraiškų statistika pagal priimančias organizacijas](../paraiskos.md) (`datasets/gov/jra/paraiskos`)
- **Manifest CSV:** [datasets/gov/jra/paraiskos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/paraiskos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/jra/paraiskos/ParaiskuStatistika`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `organizacijos_pavadinimas` | `string` | — | `3` | `open` | — | Organizacijos pavadinimas, kuriai teikta paraiška | — |
| `organizacijos_addresas` | `string` | — | `2` | `open` | — | Organizacijos adresas, kuriai teikta paraiška | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Metai, kada teikta paraiška | — |
| `iprastu_paraisku_sk` | `integer` | `U` | `4` | `open` | — | Įprastų paraiškų savanoriauti organizacijoje skaičius | — |
| `priimta_iprastu_paraisku_sk` | `integer` | `U` | `4` | `open` | — | Priimtų įprastų paraiškų savanoriauti organizacijoje skaičius | — |
| `atmesta_iprastu_paraisku_sk` | `integer` | `U` | `4` | `open` | — | Atmestų įprastų paraiškų savanoriauti organizacijoje skaičius | — |
| `kuratoriu_paraisku_sk` | `integer` | `U` | `4` | `open` | — | Paraiškų savanoriauti kuratoriais organizacijoje skaičius | — |
| `mentoriu_paraisku_sk` | `integer` | `U` | `4` | `open` | — | Paraiškų savanoriauti mentoriais organizacijoje skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/jra/paraiskos.csv
