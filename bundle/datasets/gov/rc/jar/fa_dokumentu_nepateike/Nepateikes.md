---
type: Table
title: "Nepateikes — Juridinių asmenų registre įregistruoti juridiniai asmenys"
description: "Spinta table datasets/gov/rc/jar/fa_dokumentu_nepateike/Nepateikes (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/fa_dokumentu_nepateike/Nepateikes"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/fa_dokumentu_nepateike.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nepateikes — Juridinių asmenų registre įregistruoti juridiniai asmenys

- **Model:** `datasets/gov/rc/jar/fa_dokumentu_nepateike/Nepateikes`[^manifest]
- **Dataset:** [Finansinės atskaitomybės dokumentų nepateikusios įmonės](../fa_dokumentu_nepateike.md) (`datasets/gov/rc/jar/fa_dokumentu_nepateike`)
- **Manifest CSV:** [datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_dokumentu_nepateike/Nepateikes`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens įregistravimo juridinių asmenų registre data | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens formos kodas iš jar teisinių formų klasifikatoriaus | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../formos_statusai/Statusas.md) | `4` | `open` | — | Juridinio asmens teisinio statuso kodas iš jar teisinių statusų klasifikatoriaus | — |
| `nepateikta_iki` | `integer` | — | `2` | `open` | — | Metai, už kuriuos juridinis asmuo nepateikė finansinės atskaitomybės dokumentų | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nepateikta_iki` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/fa_dokumentu_nepateike.csv
