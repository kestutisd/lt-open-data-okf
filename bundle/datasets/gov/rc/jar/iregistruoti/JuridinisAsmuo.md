---
type: Table
title: "JuridinisAsmuo — Juridinis asmuo"
description: "Spinta table datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/iregistruoti.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# JuridinisAsmuo — Juridinis asmuo

- **Model:** `datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruoti juridiniai asmenys](../iregistruoti.md) (`datasets/gov/rc/jar/iregistruoti`)
- **Manifest CSV:** [datasets/gov/rc/jar/iregistruoti.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo`
- **Primary Key (`ref`):** `ja_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `integer` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `ja_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens pavadinimas | — |
| `pilnas_adresas` | `string` | — | `1` | `open` | — | Registracijos adresas | — |
| `adresas` | `ref` | [/datasets/gov/rc/ar/adresai/Adresas](../../ar/adresai/Adresas.md) | `4` | `open` | — | Adresas | — |
| `reg_data` | `date` | `D` | `4` | `open` | — | Įregistravimo data | — |
| `isreg_data` | `date` | `D` | `4` | `open` | — | Išregistravimo data | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | Formos pavadinimas | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../formos_statusai/Statusas.md) | `4` | `open` | — | Statuso pavadinimas | — |
| `stat_data` | `date` | `D` | `4` | `open` | — | Statuso įgijimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/iregistruoti.csv
