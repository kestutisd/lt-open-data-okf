---
type: Table
title: "Buveine"
description: "Spinta table datasets/gov/rc/jar/buveines/Buveine (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/buveines/Buveine"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/buveines.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/buveines.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Buveine

- **Model:** `datasets/gov/rc/jar/buveines/Buveine`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruotų juridinių asmenų buveinių (adresų) duomenys (raw data)](../buveines.md) (`datasets/gov/rc/jar/buveines`)
- **Manifest CSV:** [datasets/gov/rc/jar/buveines.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/buveines.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/buveines/Buveine`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmens kodas iš juridinių asmenų registro | — |
| `adresas` | `ref` | [/datasets/gov/rc/ar/adresai/Adresas](../../ar/adresai/Adresas.md) | `4` | `open` | — | Adreso kodas (išorinis LR AR) | — |
| `adresas_nuo` | `date` | `D` | `4` | `open` | — | Juridinio asmens adreso įrašymo į juridinių asmenų registro įrašą data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/buveines.csv
