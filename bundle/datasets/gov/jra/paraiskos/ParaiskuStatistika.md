---
type: Table
title: "ParaiskuStatistika — Savanorių paraiškų statistika pagal priimančias organizacijas"
description: "Jaunimo reikalų agentūros Jaunimo savanoriškos tarnybos sistema kaupia duomenis apie jaunimo savanorystę priimančiose organizacijose."
resource: "https://get.data.gov.lt/datasets/gov/jra/paraiskos/ParaiskuStatistika"
tags: [gov, jra, paraiskustatistika, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/paraiskos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/jra/paraiskos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2630/"
    title: "data.gov.lt DCAT-AP — datasets/gov/jra/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ParaiskuStatistika — Savanorių paraiškų statistika pagal priimančias organizacijas

Jaunimo reikalų agentūros Jaunimo savanoriškos tarnybos sistema kaupia duomenis apie jaunimo savanorystę priimančiose organizacijose. Institucija teikia duomenis, kaupiamus nuo 2018 m., juos atnaujinti numatyta kasdien. Duomenyse kaupiama priimančios organizacijos pavadinimas ir adresas, savanorystės paraiškos teikimo metai, priimtų, atmestų įprastų paraiškų skaičiai bei jų suma, paraiškų tapti kuratoriumi bei mentoriumi skaičiai.[^manifest]

- **Model:** `datasets/gov/jra/paraiskos/ParaiskuStatistika`[^manifest]
- **Dataset:** [Savanorių paraiškų statistika pagal priimančias organizacijas](../paraiskos.md) (`datasets/gov/jra/paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/jra/paraiskos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/paraiskos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/jra/paraiskos/ParaiskuStatistika` (`deployed`)[^manifest]
- **Provider:** `jra` — Jaunimo reikalų agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/jra/paraiskos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/paraiskos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/jra/paraiskos (https://data.gov.lt/datasets/2630/)
