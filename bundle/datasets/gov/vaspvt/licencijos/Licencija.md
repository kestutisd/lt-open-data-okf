---
type: Table
title: "Licencija — Licencijos"
description: "Spinta table datasets/gov/vaspvt/licencijos/Licencija (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Licencija"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L35"
    last_modified: "2026-11-11T14:39:20Z"
---

# Licencija — Licencijos

- **Model:** `datasets/gov/vaspvt/licencijos/Licencija`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L35)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Licencija`
- **Primary Key (`ref`):** `licencijos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `licencijos_id` | `string` | — | `4` | `open` | — | Licencijos identifikatorius | — |
| `istaiga` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaigos identifikatorius | — |
| `licencijos_nr` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `sudarymo_data` | `datetime` | — | `2` | `open` | — | Licencijos išdavimo data | — |
| `panaikinimo_data` | `datetime` | — | `3` | `open` | — | Licencijos panaikinimo data | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos juridinio asmens kodas | — |
| `ja_pavadinimas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos pavadinimas | — |
| `ja_buveines_adresas` | `string` | — | `1` | `open` | — | Juridinio asmens buveinės adresas | — |
| `isakymo_data` | `datetime` | — | `2` | `open` | — | Įsakymo data | — |
| `busena` | `string` | — | `4` | `open` | — | Licencijos būsena | — |
| `isakymas` | `string` | — | `4` | `open` | — | Įsakymas | — |
| `asmuo_ar_visuomene` | `string` | — | `4` | `open` | — | Žyma, ar tai asmens, ar visuomenės sveikatos priežiūros įstaigos licencija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"0"` | — | — | Sustabdyta | — |
| `busena` | `"1"` | — | — | Išduota | — |
| `busena` | `"2"` | — | — | Panaikinta | — |
| `asmuo_ar_visuomene` | `"0"` | — | — | Nepasirinkta | — |
| `asmuo_ar_visuomene` | `"1"` | — | — | Asmuo | — |
| `asmuo_ar_visuomene` | `"2"` | — | — | Visuomenė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sudarymo_data` | `update(property: "isduota")` | `property` | `4` | `open` | — | — | — |
| `panaikinimo_data` | `update(property: "panaikinta")` | `property` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(property: "istaiga.ja_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `ja_pavadinimas` | `update(property: "istaiga.ja_pavadinimas@lt", type: "")` | `property` | `4` | `open` | — | — | — |
| `ja_buveines_adresas` | `update(property: "istaiga.adresas", type: "")` | `property` | `4` | `open` | — | — | — |
| `isakymo_data` | `update(property: "isakyta")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
