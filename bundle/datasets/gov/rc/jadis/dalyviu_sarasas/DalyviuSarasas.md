---
type: Table
title: "DalyviuSarasas — Juridinių asmenų dalyvių sąrašų duomenys"
description: "Spinta table datasets/gov/rc/jadis/dalyviu_sarasas/DalyviuSarasas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviu_sarasas/DalyviuSarasas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviu_sarasas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# DalyviuSarasas — Juridinių asmenų dalyvių sąrašų duomenys

- **Model:** `datasets/gov/rc/jadis/dalyviu_sarasas/DalyviuSarasas`[^manifest]
- **Dataset:** [Juridinių asmenų dalyvių sąrašų duomenys](../dalyviu_sarasas.md) (`datasets/gov/rc/jadis/dalyviu_sarasas`)
- **Manifest CSV:** [datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jadis/dalyviu_sarasas.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jadis/dalyviu_sarasas/DalyviuSarasas`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmuo iš Juridinių asmenų registro | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../../jar/formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens teisinė forma iš Juridinių asmenų registro | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../../jar/formos_statusai/Statusas.md) | `4` | `open` | — | Juridinio asmens teisinio statusas iš Juridinių asmenų registro | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens įregistravimo į Juridinių asmenų registrą data | — |
| `pateikimo_poz` | `integer` | — | `4` | `open` | — | Juridinio asmens JAD sąrašo pateikimo požymis | — |
| `saraso_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens JAD sąrašo pateikimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pateikimo_poz` | `0` | — | — | Nepateikė | — |
| `pateikimo_poz` | `1` | — | — | Pateikė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jadis/dalyviu_sarasas.csv
