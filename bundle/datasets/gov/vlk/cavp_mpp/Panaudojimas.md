---
type: Table
title: "Panaudojimas — Centralizuotai apmokamų vaistinių preparatų ir MPP panaudojimas"
description: "Informacija apie panaudotus centralizuotai apmokamus vaistus ir MPP"
resource: "https://get.data.gov.lt/datasets/gov/vlk/cavp_mpp/Panaudojimas"
tags: [gov, vlk, panaudojimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cavp_mpp.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/cavp_mpp.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1797/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/cavp_mpp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Panaudojimas — Centralizuotai apmokamų vaistinių preparatų ir MPP panaudojimas

Informacija apie panaudotus centralizuotai apmokamus vaistus ir MPP[^manifest]

- **Model:** `datasets/gov/vlk/cavp_mpp/Panaudojimas`[^manifest]
- **Dataset:** [Centralizuotai apmokamų vaistinių preparatų ir MPP panaudojimas](../cavp_mpp.md) (`datasets/gov/vlk/cavp_mpp`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/cavp_mpp.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cavp_mpp.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/cavp_mpp/Panaudojimas` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `ketvirtis` | `integer` | — | `4` | `open` | — | Ketvirtis | — |
| `isakymas` | `string` | — | `4` | `open` | — | Įsakymo eilės numeris | Lietuvos Respublikos sveikatos apsaugos ministro 2014 m. rugpjūčio 28 d. įsakymu V-910 „Dėl centralizuotai apmokaų vaistinių preparatų ir medicinos pagalbos priemonių sąrašo patvirtinimo“ patvirtinto Centralizuotai apmokamų vaistinių preparatų ir medicinos pagalbos priemonių sąrašo eilės numeris |
| `grupe` | `string` | — | `4` | `open` | — | Preparato/MPP grupė | Vaistinio preparato/MPP grupės pavadinimas |
| `bendrinis_pavadinimas` | `string` | — | `4` | `open` | — | Bendrinis pavadinimas | Bendrinis vaistinio preparato / MPP pavadinimas |
| `atc` | `string` | — | `4` | `open` | — | Vaisto kodas | Vaisto kodas pagal ATC klasifikaciją |
| `prekinis_pavadinimas` | `string` | — | `4` | `open` | — | Prekinis pavadinimas | Prekinis vaistinio preparato / MPP pavadinimas |
| `stiprumas` | `string` | — | `4` | `open` | — | Nedalomo vieneto stiprumas | Vaistinių preparatų ar MPP nedalomo vieneto stiprumas (mg, TV ir kt.) |
| `kodas` | `string` | — | `4` | `open` | — | Diagnozės kodas | Diagnozės kodas pagal TLK-10-AM |
| `matas` | `string` | — | `4` | `open` | — | Nedalomas vienetas (matas) | — |
| `npakid7` | `integer` | — | `4` | `open` | — | NPAKID7 | Vaistinio preparato identifikavimo kodas |
| `kiekis` | `number` | `U` | `4` | `open` | — | Kiekis | Per ataskaitinį laikotarpį sunaudotas vaistinio preparato / MPP kiekis nedalomais vienetais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date, ref: "Y")"` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/cavp_mpp.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cavp_mpp.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/cavp_mpp (https://data.gov.lt/datasets/1797/)
