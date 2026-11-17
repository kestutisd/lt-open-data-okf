---
type: Table
title: "PrekesZenklas — Prekių ženklai"
description: "Lentelė „Prekių ženklai“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/pzr/PrekesZenklas"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/pzr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrekesZenklas — Prekių ženklai

Lentelė „Prekių ženklai“. Lentelę sudaro: prekės ženklo bylos registracijos ir paraiškos numeriai, pavadinimas, prekės ženklo tipas, dabartinė būsena su pradžios data, prekės ženklo galiojimo pabaigos, paraiškos ir registracijos bei jos paskelbimo datos bei prekės ženklo atvaizdo internetinė nuoroda. Vienas įrašas atitinka vieną prekės ženklo bylą (unikalią prekės ženklo numerio reikšmę).

- **Model:** `datasets/gov/vpb/pzr/PrekesZenklas`[^manifest]
- **Dataset:** [Lietuvos Respublikos prekių ženklai](../pzr.md) (`datasets/gov/vpb/pzr`)
- **Manifest CSV:** [datasets/gov/vpb/pzr.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/pzr/PrekesZenklas`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos paraiškos numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Prekės ženklo pavadinimas | — |
| `zenklo_tipas` | `string` | — | `4` | `open` | — | Prekės ženklo tipas | — |
| `dabartine_busena` | `string` | — | `4` | `open` | — | Prekės ženklo dabartinė būsena | — |
| `dabartines_busenos_data` | `date` | `D` | `4` | `open` | — | Data, nuo kada galioja dabartinė būsena | — |
| `paraiskos_data` | `date` | `D` | `4` | `open` | — | Prekės ženklo bylos paraiškos data | — |
| `registracijos_data` | `date` | `D` | `4` | `open` | — | Prekės ženklo registracijos data | — |
| `registracijos_paskelbimo_data` | `date` | `D` | `4` | `open` | — | Prekės ženklo registracijos paskelbimo data | — |
| `galiojimo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Prekės ženklo galiojimo pabaigos data | — |
| `zenklo_atvaizdo_url` | `string` | — | `4` | `open` | — | Vaizdinio prekės ženklo atvaizdo internetinė nuoroda | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `zenklo_tipas` | `"Grafinis"` | — | — | Grafinis | — |
| `zenklo_tipas` | `"Žodinis"` | — | — | Žodinis | — |
| `zenklo_tipas` | `"Erdvinis"` | — | — | Erdvinis | — |
| `zenklo_tipas` | `"Garsinis"` | — | — | Garsinis | — |
| `zenklo_tipas` | `"Spalva"` | — | — | Spalva | — |
| `zenklo_tipas` | `"Multimedinis"` | — | — | Multimedinis | — |
| `zenklo_tipas` | `"Judesio"` | — | — | Judesio | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/pzr.csv
