---
type: Table
title: "PelnoAtaskaita — Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – pelno (nuostolių) ataskaitos"
description: "Spinta table datasets/gov/rc/jar/pelno_ataskaitos/PelnoAtaskaita (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/pelno_ataskaitos/PelnoAtaskaita"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/pelno_ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/pelno_ataskaitos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# PelnoAtaskaita — Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – pelno (nuostolių) ataskaitos

- **Model:** `datasets/gov/rc/jar/pelno_ataskaitos/PelnoAtaskaita`[^manifest]
- **Dataset:** [Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – pelno (nuostolių) ataskaitos](../pelno_ataskaitos.md) (`datasets/gov/rc/jar/pelno_ataskaitos`)
- **Manifest CSV:** [datasets/gov/rc/jar/pelno_ataskaitos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/pelno_ataskaitos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/pelno_ataskaitos/PelnoAtaskaita`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens formos kodas iš jar teisinių formų klasifikatoriaus | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../formos_statusai/Statusas.md) | `4` | `open` | — | Juridinio asmens teisinio statuso kodas iš jar teisinių statusų klasifikatoriaus | — |
| `template_id` | `string` | — | `2` | `open` | — | Finansinės ataskaitos rūšies kodas | — |
| `template_name` | `string` | — | `2` | `open` | — | Finansinės ataskaitos rūšies pavadinimas | — |
| `standard_id` | `string` | — | `2` | `open` | — | Finansinės ataskaitos dokumentų rinkinio kodas | — |
| `standard_name` | `string` | — | `2` | `open` | — | Finansinės ataskaitos dokumentų rinkinio tipas | — |
| `line_type_id` | `string` | — | `2` | `open` | — | rodiklio kodas | — |
| `line_name` | `string` | — | `2` | `open` | — | rodiklio pavadinimas | — |
| `reiksme` | `integer` | — | `2` | `open` | — | rodiklio reikšmė eurais | — |
| `laikotarpis_nuo` | `date` | `D` | `4` | `open` | — | Finansinių metų pradžios data | — |
| `laikotarpis_iki` | `date` | `D` | `4` | `open` | — | Finansinių metų pabaigos data | — |
| `reg_date` | `date` | `D` | `4` | `open` | — | Finansinės atskaitomybės dokumentų įregistravimo jar data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/pelno_ataskaitos.csv
