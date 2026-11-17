---
type: Table
title: "Klasifikacija — Lietuvoje registruotų patentų klasifikacija"
description: "Lentelė „Lietuvoje registruotų patentų klasifikacija“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/lrpr/Klasifikacija"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L36"
    last_modified: "2026-11-11T14:39:20Z"
---

# Klasifikacija — Lietuvoje registruotų patentų klasifikacija

Lentelė „Lietuvoje registruotų patentų klasifikacija“. Lentelę sudaro: patento ir paraiškos numeriai, IPCCPC klasifikacija, eilės numeris ir versija mėnesio tikslumu. Vienas įrašas atitinka vieną unikalią patento numerio, IPC klasifikacijos ir jos eilės numerio kombinaciją. Siekiant aukštesnio brandos lygio, versijos paverstos mėnesio tikslumo datomis.

- **Model:** `datasets/gov/vpb/lrpr/Klasifikacija`[^manifest]
- **Dataset:** [Lietuvos Respublikoje registruoti patentai](../lrpr.md) (`datasets/gov/vpb/lrpr`)
- **Manifest CSV:** [datasets/gov/vpb/lr_pr.csv#L36](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L36)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/lrpr/Klasifikacija`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `patento_nr` | `string` | — | `4` | `open` | — | Patento numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Patento paraiškos numeris | — |
| `ipccpc_kodas` | `string` | — | `4` | `open` | — | IPC kodas | — |
| `eiles_nr` | `integer` | — | `4` | `open` | — | IPC klasifikacijos eilės aprašyme numeris | — |
| `versija` | `date` | `M` | `4` | `open` | — | IPCCPC kodo versija pagal mėnesio tikslumu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv
