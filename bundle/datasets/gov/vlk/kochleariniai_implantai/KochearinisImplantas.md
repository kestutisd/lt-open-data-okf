---
type: Table
title: "KochearinisImplantas — KI panaudojimas"
description: "Informacija apie panaudotų kochlearinių implantų kiekį"
resource: "https://get.data.gov.lt/datasets/gov/vlk/kochleariniai_implantai/KochearinisImplantas"
tags: [gov, vlk, kochearinisimplantas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/kochleariniai_implantai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/kochleariniai_implantai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1590/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/kochleariniai_implantai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# KochearinisImplantas — KI panaudojimas

Informacija apie panaudotų kochlearinių implantų kiekį[^manifest]

- **Model:** `datasets/gov/vlk/kochleariniai_implantai/KochearinisImplantas`[^manifest]
- **Dataset:** [Kochlearinių implantų panaudojimas](../kochleariniai_implantai.md) (`datasets/gov/vlk/kochleariniai_implantai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/kochleariniai_implantai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/kochleariniai_implantai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/kochleariniai_implantai/KochearinisImplantas` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/kochleariniai_implantai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/kochleariniai_implantai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/kochleariniai_implantai (https://data.gov.lt/datasets/1590/)
