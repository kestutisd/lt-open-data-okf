---
type: Table
title: "Tiekejas — Pateikiama informacija apie pluoštinių kanapių produktus tiekiančius ūkio subjektus (vardas, pavardė/ pavadinimas, juridinio asmens kodas, el. p., tel., tiekiamos produkcijos rūšys)"
description: "Spinta table datasets/gov/vat/pluostines_kanapes/Tiekejas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/pluostines_kanapes/Tiekejas"
tags: [gov, vat, tiekejas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r22_pluost_kanap.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r22_pluost_kanap.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1878/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/pluostines_kanapes"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Tiekejas — Pateikiama informacija apie pluoštinių kanapių produktus tiekiančius ūkio subjektus (vardas, pavardė/ pavadinimas, juridinio...

- **Model:** `datasets/gov/vat/pluostines_kanapes/Tiekejas`[^manifest]
- **Dataset:** [Pluoštinių kanapių produktų tiekėjų sąrašas](../pluostines_kanapes.md) (`datasets/gov/vat/pluostines_kanapes`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r22_pluost_kanap.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r22_pluost_kanap.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/pluostines_kanapes/Tiekejas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `tiekejas` | `string` | — | `2` | `open` | — | Tiekėjo vardas, pavardė / pavadinimas | — |
| `tiekejo_nr` | `string` | — | `3` | `open` | — | Tiekėjui suteiktas Nr. | — |
| `kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `kontaktai` | `string` | — | `1` | `open` | — | Kontaktinė informacija | — |
| `paskelbimas_is` | `string` | — | `1` | `open` | — | Įsakymo data, numeris/ paskelbimo Licencijų informacinėje sistemoje data | — |
| `produktai` | `string` | — | `2` | `open` | — | Pluoštinių kanapių produktai | — |
| `paskirtis` | `string` | — | `2` | `open` | — | Produktų paskirtis | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Ūkio subjekto vietos koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tiekejas` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `kodas` | `create(property: "imone", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r22_pluost_kanap.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r22_pluost_kanap.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/pluostines_kanapes (https://data.gov.lt/datasets/1878/)
