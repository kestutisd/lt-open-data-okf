---
type: Table
title: "Istaiga — Sveikatos priežiūros įstaigos"
description: "Spinta table datasets/gov/vaspvt/licencijos/Istaiga (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Istaiga"
tags: [gov, vaspvt, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Istaiga — Sveikatos priežiūros įstaigos

- **Model:** `datasets/gov/vaspvt/licencijos/Istaiga`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Istaiga`
- **Primary Key (`ref`):** `spi_id`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `spi_id` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaigos identifikatorius | — |
| `ja_kodas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos juridinio asmens kodas | — |
| `ja_pavadinimas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos pavadinimas | — |
| `teisine_forma` | `string` | — | `4` | `open` | — | Juridinio asmens teisinė forma | — |
| `adresas` | `string` | — | `2` | `open` | — | Juridinio asmens buveinės adresas | — |
| `licencijos_nr` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `licencijos_isdavimo_data` | `datetime` | — | `3` | `open` | — | Licencijos išdavimo data | — |
| `asmuo_visuomene` | `string` | — | `2` | `open` | — | Žyma, ar tai asmens, ar visuomenės sveikatos priežiūros įstaigos licencija | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", ref: "ja_kodas")` | `base` | `4` | `open` | — | — | — |
| `ja_kodas` | `update(type: "")` | `type` | `4` | `open` | — | — | — |
| `ja_pavadinimas` | `update(property: "ja_pavadinimas@lt", type: "")` | `type` | `4` | `open` | — | — | — |
| `adresas` | `update(type: "", ref: "")` | `type` | `4` | `open` | — | — | — |
| `asmuo_visuomene` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
