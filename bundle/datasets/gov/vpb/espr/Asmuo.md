---
type: Table
title: "Asmuo — Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys"
description: "Lentelė „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/espr/Asmuo"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# Asmuo — Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys

Lentelė „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“. Lentelę sudaro: juridinio asmens pavadinimas arba fizinio asmens vardas ir pavardė, patento ir paraiškos numeris, asmens vaidmuo ir eilės numeris patente. Svarbu atkreipti dėmesį, kad patentas, turintis asmenų, atliekančių skirtingus vaidmenis, juose turi po vieną pirmą asmenį, pvz., pirmą pareiškėją bei pirmą išradėją. Vienas įrašas atitinka vieną unikalią patento numerio, asmens vaidmens ir asmens eilės numerio patente kombinaciją.

- **Model:** `datasets/gov/vpb/espr/Asmuo`[^manifest]
- **Dataset:** [Lietuvoje įsigalioję Europos patentai](../espr.md) (`datasets/gov/vpb/espr`)
- **Manifest CSV:** [datasets/gov/vpb/es_pr.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/espr/Asmuo`
- **Primary Key (`ref`):** `vda_prime_key`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asm_tipas` | `"Išradėjas"` | — | — | Išradėjas | — |
| `asm_tipas` | `"Savininkas"` | — | — | Savininkas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv
