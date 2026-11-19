---
type: Table
title: "Asmuo — Lietuvoje registruotiems patentams priskirti asmenys"
description: "Lentelė „Lietuvoje registruotiems patentams priskirti asmenys“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/lrpr/Asmuo"
tags: [gov, vpb, asmuo, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L21"
    title: "atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv#L21"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/lrpr"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Asmuo — Lietuvoje registruotiems patentams priskirti asmenys

Lentelė „Lietuvoje registruotiems patentams priskirti asmenys“. Lentelę sudaro: patento ir paraiškos numeriai, priskirto juridinio asmens pavadinimas arba fizinio asmens vardas ir pavardė, asmens vaidmuo, kodas, vaidmuo ir tipas patente. Vienas įrašas atitinka vieną unikalią patento numerio, asmens identifikatoriaus ir jo vaidmens patente kombinaciją.[^manifest]

- **Model:** `datasets/gov/vpb/lrpr/Asmuo`[^manifest]
- **Dataset:** [Lietuvos Respublikoje registruoti patentai](../lrpr.md) (`datasets/gov/vpb/lrpr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/lr_pr.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L21)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/lrpr/Asmuo` (`deployed`)[^manifest]
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
| `asmens_id` | `string` | — | `4` | `open` | — | Patentui priskirto asmens identifikatorius | — |
| `asmuo` | `string` | — | `4` | `open` | — | Patentui priskirto fizinio asmens vardas su pavarde arba juridinio asmens pavadinimas | — |
| `asm_kodas` | `string` | — | `4` | `open` | — | Patentui priskirto asmens kodas | — |
| `asmens_vaidmuo_patente` | `string` | — | `4` | `open` | — | Patentui priskirto asmens vaidmuo | — |
| `asmens_tipas` | `string` | — | `4` | `open` | — | Patentui priskirto asmens tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asmens_vaidmuo_patente` | `"Išradėjas"` | — | — | Išradėjas | — |
| `asmens_vaidmuo_patente` | `"Pareiškėjas"` | — | — | Pareiškėjas | — |
| `asmens_vaidmuo_patente` | `"Savininkas"` | — | — | Savininkas | — |
| `asmens_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `asmens_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv#L21 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L21)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/lrpr (https://data.gov.lt/datasets/3808/)
