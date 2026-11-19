---
type: Table
title: "Klasifikacija — Lietuvoje registruotų patentų klasifikacija"
description: "Lentelė „Lietuvoje registruotų patentų klasifikacija“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/lrpr/Klasifikacija"
tags: [gov, vpb, klasifikacija, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L36"
    title: "atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv#L36"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/lrpr"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Klasifikacija — Lietuvoje registruotų patentų klasifikacija

Lentelė „Lietuvoje registruotų patentų klasifikacija“. Lentelę sudaro: patento ir paraiškos numeriai, IPCCPC klasifikacija, eilės numeris ir versija mėnesio tikslumu. Vienas įrašas atitinka vieną unikalią patento numerio, IPC klasifikacijos ir jos eilės numerio kombinaciją. Siekiant aukštesnio brandos lygio, versijos paverstos mėnesio tikslumo datomis.[^manifest]

- **Model:** `datasets/gov/vpb/lrpr/Klasifikacija`[^manifest]
- **Dataset:** [Lietuvos Respublikoje registruoti patentai](../lrpr.md) (`datasets/gov/vpb/lrpr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/lr_pr.csv#L36](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L36)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/lrpr/Klasifikacija` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `patento_nr` | `string` | — | `4` | `open` | — | Patento numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Patento paraiškos numeris | — |
| `ipccpc_kodas` | `string` | — | `4` | `open` | — | IPC kodas | — |
| `eiles_nr` | `integer` | — | `4` | `open` | — | IPC klasifikacijos eilės aprašyme numeris | — |
| `versija` | `date` | `M` | `4` | `open` | — | IPCCPC kodo versija pagal mėnesio tikslumu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv#L36 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L36)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/lrpr (https://data.gov.lt/datasets/3808/)
