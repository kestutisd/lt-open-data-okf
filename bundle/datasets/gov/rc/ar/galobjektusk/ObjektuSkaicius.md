---
type: Table
title: "ObjektuSkaicius — Adresų registro galiojančių objektų kiekiai mėnesio pradžiai"
description: "Spinta table datasets/gov/rc/ar/galobjektusk/ObjektuSkaicius (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/galobjektusk/ObjektuSkaicius"
tags: [gov, rc, objektuskaicius, deployed, level-3, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1553/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/galobjektusk"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# ObjektuSkaicius — Adresų registro galiojančių objektų kiekiai mėnesio pradžiai

- **Model:** `datasets/gov/rc/ar/galobjektusk/ObjektuSkaicius`[^manifest]
- **Dataset:** [Adresų registro galiojančių objektų kiekiai mėnesio pradžiai](../galobjektusk.md) (`datasets/gov/rc/ar/galobjektusk`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/galobjektusk/ObjektuSkaicius` (`deployed`)[^manifest]
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
| `sen_kiekis` | `integer` | `U` | `4` | `open` | — | Seniūnijų sk. | — |
| `gyv_vietoves_viso` | `integer` | `U` | `4` | `open` | — | Gyvenamųjų vietovių sk. iš viso | — |
| `gyv_vietoves_m` | `integer` | `U` | `4` | `open` | — | Miesto tipo gyvenamųjų vietovių sk. | — |
| `gyv_vietoves_mstl` | `integer` | `U` | `4` | `open` | — | Miestelio tipo gyvenamųjų vietovių sk. | — |
| `gyv_vietoves_k` | `integer` | `U` | `4` | `open` | — | Kaimo tipo gyvenamųjų vietovių sk. | — |
| `gyv_vietoves_vs` | `integer` | `U` | `4` | `open` | — | Viensėdžio tipo gyvenamųjų vietovių sk. | — |
| `gyv_vietoves_su_gat` | `integer` | `U` | `4` | `open` | — | Gyvenamųjų vietovių su gatvėmis sk. | — |
| `gyv_vietoves_be_gat_su_adr` | `integer` | `U` | `4` | `open` | — | Gyvenamųjų vietovių su adresais, be gatvių, sk. | — |
| `gat_kiekis` | `integer` | `U` | `4` | `open` | — | Gatvių sk. | — |
| `adresu_kiekis` | `integer` | `U` | `4` | `open` | — | Adresų taškų sk. | — |
| `pat_kiekis` | `integer` | `U` | `4` | `open` | — | Patalpų adresų sk. | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/galobjektusk (https://data.gov.lt/datasets/1553/)
