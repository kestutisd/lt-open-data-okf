---
type: Table
title: "Patalpa — Adresų registro gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys"
description: "Gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinančių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys (duomenų rinkinių grupė (60 vnt.))."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/patalpa/Patalpa"
tags: [gov, rc, patalpa, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/patalpa.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/patalpa.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1343/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/patalpa"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Patalpa — Adresų registro gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys

Gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinančių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gyvenamųjų ir negyvenamųjų patalpų adresus apibūdinantys tekstiniai duomenys (duomenų rinkinių grupė (60 vnt.)). Duomenų geografinė imtis — visa šalies teritorija.[^manifest]

- **Model:** `datasets/gov/rc/ar/patalpa/Patalpa`[^manifest]
- **Dataset:** [Adresų registras](../patalpa.md) (`datasets/gov/rc/ar/patalpa`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/patalpa.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/patalpa.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/patalpa/Patalpa` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `aob_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aob_kodas` | `ref` | [Adresas](../adresai/Adresas.md) (`level=4 UUID`: `aob_kodas._id`) | `4` | `open` | — | Patalpos identifikavimo kodas | — |
| `pastatas` | `ref` | [Pastatas](../pastatas/Pastatas.md) (`level=4 UUID`: `pastatas._id`) | `4` | `open` | — | Pastato, kuriam priklauso patalpa, identifikavimo kodas | — |
| `patalpos_nr` | `string` | — | `4` | `open` | — | Patalpos numeris pastate ar korpuse (adreso komponentė) | — |
| `pat_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/patalpa.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/patalpa.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/patalpa (https://data.gov.lt/datasets/1343/)
