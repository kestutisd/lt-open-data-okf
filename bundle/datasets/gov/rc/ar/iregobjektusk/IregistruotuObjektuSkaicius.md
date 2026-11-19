---
type: Table
title: "IregistruotuObjektuSkaicius — Naujai įregistruotų Adresų registro objektų skaičius per mėnesį"
description: "Spinta table datasets/gov/rc/ar/iregobjektusk/IregistruotuObjektuSkaicius (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/iregobjektusk/IregistruotuObjektuSkaicius"
tags: [gov, rc, iregistruotuobjektuskaicius, deployed, level-3, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1554/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/iregobjektusk"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# IregistruotuObjektuSkaicius — Naujai įregistruotų Adresų registro objektų skaičius per mėnesį

- **Model:** `datasets/gov/rc/ar/iregobjektusk/IregistruotuObjektuSkaicius`[^manifest]
- **Dataset:** [Naujai įregistruotų Adresų registro objektų skaičius per mėnesį](../iregobjektusk.md) (`datasets/gov/rc/ar/iregobjektusk`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/iregobjektusk/IregistruotuObjektuSkaicius` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe, metai, menuo`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `ref` | [Apskritis](../apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Apskrities kodas | — |
| `savivaldybe` | `ref` | [Savivaldybe](../savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės kodas | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `patalpos_n` | `integer` | — | `4` | `open` | — | Naujai įregistruotų patalpų sk. | — |
| `adresai_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų adresų taškų sk. | — |
| `gatves_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų gatvių sk. | — |
| `gyv_vietoves_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų gyvenamųjų vietovių sk. | — |
| `seniunijos_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų seniūnijų sk. | — |
| `pavadinimai_n` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų pavadinimų sk. | — |
| `viso` | `integer` | `U` | `4` | `open` | — | Naujai įregistruotų objektų sk., iš viso | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/iregistruotu_objektu_skaicius.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/iregobjektusk (https://data.gov.lt/datasets/1554/)
