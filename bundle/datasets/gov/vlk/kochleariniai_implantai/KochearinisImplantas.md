---
type: Table
title: "KochearinisImplantas — KI panaudojimas"
description: "Informacija apie panaudotų kochlearinių implantų kiekį"
resource: "https://get.data.gov.lt/datasets/gov/vlk/kochleariniai_implantai/KochearinisImplantas"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/kochleariniai_implantai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/kochleariniai_implantai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# KochearinisImplantas — KI panaudojimas

Informacija apie panaudotų kochlearinių implantų kiekį

- **Model:** `datasets/gov/vlk/kochleariniai_implantai/KochearinisImplantas`[^manifest]
- **Dataset:** [datasets/gov/vlk/kochleariniai_implantai](../kochleariniai_implantai.md) (`datasets/gov/vlk/kochleariniai_implantai`)
- **Manifest CSV:** [datasets/gov/vlk/kochleariniai_implantai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/kochleariniai_implantai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/kochleariniai_implantai/KochearinisImplantas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis | — |
| `isakymas` | `string` | — | `4` | `open` | — | Įsakymo eilės numeris | Lietuvos Respublikos sveikatos apsaugos ministro 2014 m. rugpjūčio 28 d. įsakymu V-910 „Dėl centralizuotai apmokaų vaistinių preparatų ir medicinos pagalbos priemonių sąrašo patvirtinimo“ patvirtinto Centralizuotai apmokamų vaistinių preparatų ir medicinos pagalbos priemonių sąrašo eilės numeris |
| `grupe` | `string` | — | `4` | `open` | — | Preparato/MPP grupė | Vaistinio preparato/MPP grupės pavadinimas |
| `bendrinis_pavadinimas` | `string` | — | `4` | `open` | — | Bendrinis pavadinimas | Bendrinis vaistinio preparato / MPP pavadinimas |
| `prekinis_pavadinimas` | `string` | — | `4` | `open` | — | Prekinis pavadinimas | Prekinis vaistinio preparato / MPP pavadinimas |
| `kodas` | `string` | — | `4` | `open` | — | Diagnozių kodai | Diagnozių kodai pagal TLK-10-AM |
| `matas` | `string` | — | `4` | `open` | — | Nedalomas vienetas (matas) | — |
| `kiekis` | `integer` | `U` | `4` | `open` | — | Kiekis | Panaudotų kochlearinių implantų kiekis |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/kochleariniai_implantai.csv
