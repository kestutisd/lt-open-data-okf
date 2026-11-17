---
type: Table
title: "Dizainas — Dizainai"
description: "Lentelė „Dizainai“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/dr/Dizainas"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/dr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dizainas — Dizainai

Lentelė „Dizainai“. Lentelę sudaro: dizaino bylos registracijos ir paraiškos numeriai, pavadinimas, dabartinė būsena su pradžios data, dizaino galiojimo pabaigos, paraiškos ir registracijos bei jos paskelbimo datos. Vienas įrašas atitinka vieną dizaino bylą (unikalią dizaino numerio reikšmę).

- **Model:** `datasets/gov/vpb/dr/Dizainas`[^manifest]
- **Dataset:** [Lietuvos Respublikos dizainų duomenys](../dr.md) (`datasets/gov/vpb/dr`)
- **Manifest CSV:** [datasets/gov/vpb/dr.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/dr/Dizainas`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus indentifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos paraiškos numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Dizaino pavadinimas | — |
| `dabartine_busena` | `string` | — | `4` | `open` | — | Dizaino dabartinė būsena | — |
| `dabartines_busenos_data` | `date` | `D` | `4` | `open` | — | Data, nuo kada galioja dizaino dabartinė būsena | — |
| `paraiskos_data` | `date` | `D` | `4` | `open` | — | Dizaino paraiškos data | — |
| `registracijos_data` | `date` | `D` | `4` | `open` | — | Dizaino registracijos data | — |
| `registracijos_paskelbimo_data` | `date` | `D` | `4` | `open` | — | Dizaino registracijos paskelbimo data | — |
| `galiojimo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Dizaino galiojimo pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/dr.csv
