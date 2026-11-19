---
type: Table
title: "Asmuo — Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys"
description: "Lentelė „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/espr/Asmuo"
tags: [gov, vpb, asmuo, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2905/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/espr"
    author: "team:vda"
    last_modified: "2026-10-27T00:00:00Z"
---

# Asmuo — Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys

Lentelė „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“. Lentelę sudaro: juridinio asmens pavadinimas arba fizinio asmens vardas ir pavardė, patento ir paraiškos numeris, asmens vaidmuo ir eilės numeris patente. Svarbu atkreipti dėmesį, kad patentas, turintis asmenų, atliekančių skirtingus vaidmenis, juose turi po vieną pirmą asmenį, pvz., pirmą pareiškėją bei pirmą išradėją. Vienas įrašas atitinka vieną unikalią patento numerio, asmens vaidmens ir asmens eilės numerio patente kombinaciją.[^manifest]

- **Model:** `datasets/gov/vpb/espr/Asmuo`[^manifest]
- **Dataset:** [Lietuvoje įsigalioję Europos patentai](../espr.md) (`datasets/gov/vpb/espr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/es_pr.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/espr/Asmuo` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-27`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `asmuo` | `string` | — | `4` | `open` | — | Patentui priskirtas asmuo | — |
| `patento_numeris` | `string` | — | `4` | `open` | — | Patento numeris | — |
| `paraiskos_numeris` | `string` | — | `4` | `open` | — | Patento paraiškos numeris | — |
| `asm_tipas` | `string` | — | `4` | `open` | — | Asmens vaidmens tipas patente | — |
| `asm_eiles_pat_nr` | `integer` | — | `4` | `open` | — | Asmens eilės numeris patente pagal vaidmenį | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asm_tipas` | `"Išradėjas"` | — | — | Išradėjas | — |
| `asm_tipas` | `"Savininkas"` | — | — | Savininkas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L17)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/espr (https://data.gov.lt/datasets/2905/)
