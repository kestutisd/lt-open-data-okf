---
type: Table
title: "Tiekejas — Pateikiama informacija apie pluoštinių kanapių produktus tiekiančius ūkio subjektus (vardas, pavardė/ pavadinimas, juridinio asmens kodas, el. p., tel., tiekiamos produkcijos rūšys)"
description: "Spinta table datasets/gov/vat/pluostines_kanapes/Tiekejas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/pluostines_kanapes/Tiekejas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r22_pluost_kanap.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r22_pluost_kanap.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tiekejas — Pateikiama informacija apie pluoštinių kanapių produktus tiekiančius ūkio subjektus (vardas, pavardė/ pavadinimas, juridinio asmens kodas, el. p., tel., tiekiamos produkcijos rūšys)

- **Model:** `datasets/gov/vat/pluostines_kanapes/Tiekejas`[^manifest]
- **Dataset:** [datasets/gov/vat/pluostines_kanapes](../pluostines_kanapes.md) (`datasets/gov/vat/pluostines_kanapes`)
- **Manifest CSV:** [datasets/gov/vat/r22_pluost_kanap.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r22_pluost_kanap.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/pluostines_kanapes/Tiekejas`
- **Primary Key (`ref`):** `eiles_nr`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r22_pluost_kanap.csv
