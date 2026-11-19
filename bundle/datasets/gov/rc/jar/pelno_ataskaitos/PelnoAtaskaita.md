---
type: Table
title: "PelnoAtaskaita — Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – pelno (nuostolių) ataskaitos"
description: "Lietuvos Respublikos juridinių asmenų registrui įregistruotų juridinių asmenų pateikti finansinės atskaitomybės dokumentai – pelno (nuostolių) ataskaitos (RAW data)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/pelno_ataskaitos/PelnoAtaskaita"
tags: [gov, rc, pelnoataskaita, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/pelno_ataskaitos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/pelno_ataskaitos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1666/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/pelno_ataskaitos"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# PelnoAtaskaita — Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – pelno (nuostolių) ataskaitos

**Dataset Context:** Lietuvos Respublikos juridinių asmenų registrui įregistruotų juridinių asmenų pateikti finansinės atskaitomybės dokumentai – pelno (nuostolių) ataskaitos (RAW data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nu[^manifest]

- **Model:** `datasets/gov/rc/jar/pelno_ataskaitos/PelnoAtaskaita`[^manifest]
- **Dataset:** [Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – pelno (nuostolių) ataskaitos](../pelno_ataskaitos.md) (`datasets/gov/rc/jar/pelno_ataskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/pelno_ataskaitos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/pelno_ataskaitos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/pelno_ataskaitos/PelnoAtaskaita` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `forma` | `ref` | [Forma](../formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | Juridinio asmens formos kodas iš jar teisinių formų klasifikatoriaus | — |
| `statusas` | `ref` | [Statusas](../formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | Juridinio asmens teisinio statuso kodas iš jar teisinių statusų klasifikatoriaus | — |
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

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/pelno_ataskaitos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/pelno_ataskaitos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/pelno_ataskaitos (https://data.gov.lt/datasets/1666/)
