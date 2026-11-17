---
type: Table
title: "Dalyvis — Juridinių asmenų dalyvių duomenys iš JADIS"
description: "Spinta table datasets/gov/rc/jadis/dalyviai/Dalyvis (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviai/Dalyvis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dalyvis — Juridinių asmenų dalyvių duomenys iš JADIS

- **Model:** `datasets/gov/rc/jadis/dalyviai/Dalyvis`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių duomenys iš JADIS](../dalyviai.md) (`datasets/gov/rc/jadis/dalyviai`)
- **Manifest CSV:** [datasets/gov/rc/jadis/dalyviai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviai/Dalyvis`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmuo iš Juridinių asmenų registro | — |
| `form_kodas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../../jar/formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `stat_statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../../jar/formos_statusai/Statusas.md) | `4` | `open` | — | Juridinio asmens teisinis statusas iš Juridinių asmenų registro | — |
| `lr_fiziniai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių Lietuvos Respublikos piliečių skaičius | — |
| `lr_juridiniai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių Lietuvos Respublikoje įregistruotų juridinių asmenų skaičius | — |
| `uzsienio_fiziniai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio fizinių asmenų skaičius | — |
| `uzsienio_juridiniai` | `integer` | `U` | `4` | `open` | — | Juridiniame asmenyje dalyvaujančių užsienio juridinių asmenų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviai.csv
