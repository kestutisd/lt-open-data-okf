---
type: Table
title: "Klasifikacija — Lietuvoje įsigaliojusių Europos patentų klasifikacija"
description: "Lentelė „Lietuvoje įsigaliojusių Europos patentų klasifikacija“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/espr/Klasifikacija"
tags: [gov, vpb, klasifikacija, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2905/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/espr"
    author: "team:vda"
    last_modified: "2026-10-27T00:00:00Z"
---

# Klasifikacija — Lietuvoje įsigaliojusių Europos patentų klasifikacija

Lentelė „Lietuvoje įsigaliojusių Europos patentų klasifikacija“. Lentelę sudaro: patento ir paraiškos numeris, IPC klasifikacija ir jos versija mėnesio tikslumu. Vienas įrašas atitinka vieną unikalią patento numerio, IPC klasifikacijos ir jos versijos kombinaciją.[^manifest]

- **Model:** `datasets/gov/vpb/espr/Klasifikacija`[^manifest]
- **Dataset:** [Lietuvoje įsigalioję Europos patentai](../espr.md) (`datasets/gov/vpb/espr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/es_pr.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/espr/Klasifikacija` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-27`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `patento_numeris` | `string` | — | `4` | `open` | — | Patento numeris | — |
| `paraiskos_numeris` | `string` | — | `4` | `open` | — | Patento paraiškos numeris | — |
| `ipc_klase` | `string` | — | `4` | `open` | — | Patento IPC klasė | — |
| `ipc_versija` | `date` | `M` | `4` | `open` | — | Patento IPC klasės versija mėnesio tikslumu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/espr (https://data.gov.lt/datasets/2905/)
