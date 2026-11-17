---
type: Table
title: "Patalpa — Adresų registro gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys"
description: "Gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinančių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys (duomenų rinkinių grupė (60 vnt.))."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/patalpa/Patalpa"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/patalpa.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/patalpa.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patalpa — Adresų registro gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys

Gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinančių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys (duomenų rinkinių grupė (60 vnt.)). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/patalpa/Patalpa`[^manifest]
- **Dataset:** [Adresų registras](../patalpa.md) (`datasets/gov/rc/ar/patalpa`)
- **Manifest CSV:** [datasets/gov/rc/ar/patalpa.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/patalpa.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/patalpa/Patalpa`
- **Primary Key (`ref`):** `aob_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aob_kodas` | `ref` | [/datasets/gov/rc/ar/adresai/Adresas](../adresai/Adresas.md) | `4` | `open` | — | Patalpos identifikavimo kodas | — |
| `pastatas` | `ref` | [/datasets/gov/rc/ar/pastatas/Pastatas](../pastatas/Pastatas.md) | `4` | `open` | — | Pastato, kuriam priklauso patalpa, identifikavimo kodas | — |
| `patalpos_nr` | `string` | — | `4` | `open` | — | Patalpos numeris pastate ar korpuse (adreso komponentė) | — |
| `pat_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/patalpa.csv
