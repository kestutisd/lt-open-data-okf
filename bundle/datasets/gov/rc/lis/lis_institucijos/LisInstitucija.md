---
type: Table
title: "LisInstitucija — Licencijas išduodančių institucijų klasifikatorius"
description: "Spinta table datasets/gov/rc/lis/lis_institucijos/LisInstitucija (1 column)."
resource: "https://get.data.gov.lt/datasets/gov/rc/lis/lis_institucijos/LisInstitucija"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/lis/lis_institucijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_institucijos.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# LisInstitucija — Licencijas išduodančių institucijų klasifikatorius

- **Model:** `datasets/gov/rc/lis/lis_institucijos/LisInstitucija`[^manifest]
- **Dataset:** [Licencijų informacinės sistemos licencijas išduodančių institucijų klasifikatorius](../lis_institucijos.md) (`datasets/gov/rc/lis/lis_institucijos`)
- **Manifest CSV:** [datasets/gov/rc/lis/lis_institucijos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/lis/lis_institucijos.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/lis/lis_institucijos/LisInstitucija`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Licencijas išduodančios institucijos kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/lis/lis_institucijos.csv
