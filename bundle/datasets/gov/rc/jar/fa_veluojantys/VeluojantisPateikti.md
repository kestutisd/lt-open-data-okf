---
type: Table
title: "VeluojantisPateikti — Juridinių asmenų registre įregistruoto juridinio asmens kodas"
description: "Spinta table datasets/gov/rc/jar/fa_veluojantys/VeluojantisPateikti (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/fa_veluojantys/VeluojantisPateikti"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/fa_veluojantys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_veluojantys.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# VeluojantisPateikti — Juridinių asmenų registre įregistruoto juridinio asmens kodas

- **Model:** `datasets/gov/rc/jar/fa_veluojantys/VeluojantisPateikti`[^manifest]
- **Dataset:** [Jurdiniai asmenys vėluojantys pateikti finansinės atskaitomybės dokumentus už praėjusius finansinius metus](../fa_veluojantys.md) (`datasets/gov/rc/jar/fa_veluojantys`)
- **Manifest CSV:** [datasets/gov/rc/jar/fa_veluojantys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_veluojantys.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_veluojantys/VeluojantisPateikti`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens įregistravimo juridinių asmenų registre data | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens formos kodas | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../formos_statusai/Statusas.md) | `4` | `open` | — | Juridinio asmens teisinio statuso kodas | — |
| `veluojantis_iki` | `date` | `D` | `4` | `open` | — | Metai, už kuriuos juridinio asmens pateikta paskutinė finansinė ataskaita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/fa_veluojantys.csv
