---
type: Table
title: "BalansoAtaskaita — Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos"
description: "Spinta table datasets/gov/rc/jar/balanso_ataskaitos/BalansoAtaskaita (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/balanso_ataskaitos/BalansoAtaskaita"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/balanso_ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/balanso_ataskaitos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# BalansoAtaskaita — Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos

- **Model:** `datasets/gov/rc/jar/balanso_ataskaitos/BalansoAtaskaita`[^manifest]
- **Dataset:** [Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos](../balanso_ataskaitos.md) (`datasets/gov/rc/jar/balanso_ataskaitos`)
- **Manifest CSV:** [datasets/gov/rc/jar/balanso_ataskaitos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/balanso_ataskaitos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/balanso_ataskaitos/BalansoAtaskaita`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | juridinio asmens formos kodas iš JAR teisinių formų klasifikatoriaus | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../formos_statusai/Statusas.md) | `4` | `open` | — | juridinio asmens teisinio statuso kodas iš JAR teisinių statusų klasifikatoriaus | — |
| `template_id` | `string` | — | `2` | `open` | — | finansinės ataskaitos rūšies kodas | — |
| `template_name` | `string` | — | `2` | `open` | — | finansinės ataskaitos rūšies pavadinimas | — |
| `standard_id` | `string` | — | `2` | `open` | — | finansinės ataskaitos dokumentų rinkinio kodas | — |
| `standard_name` | `string` | — | `2` | `open` | — | finansinės ataskaitos dokumentų rinkinio tipas | — |
| `line_type_id` | `string` | — | `2` | `open` | — | rodiklio kodas | — |
| `line_name` | `string` | — | `2` | `open` | — | rodiklio pavadinimas | — |
| `reiksme` | `integer` | — | `2` | `open` | — | rodiklio reikšmė eurais | — |
| `laikotarpis_nuo` | `date` | `D` | `4` | `open` | — | finansinių metų pradžios data | — |
| `laikotarpis_iki` | `date` | `D` | `4` | `open` | — | finansinių metų pabaigos data | — |
| `reg_date` | `date` | `D` | `4` | `open` | — | finansinės atskaitomybės dokumentų įregistravimo JAR data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/balanso_ataskaitos.csv
