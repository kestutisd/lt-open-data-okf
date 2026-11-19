---
type: Table
title: "BalansoAtaskaita — Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos"
description: "Juridinių asmenų registre tvarkomų juridinių asmenų finansinės atskaitomybės dokumentų duomenys iš balanso ataskaitų (apie juridinių asmenų nuosavą kapitalą; apie juridinių asmenų mokėtinas sumas ir kitus įsipareigojimus; apie juridinių asmenų trumpalaikį turtą; apie..."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/balanso_ataskaitos/BalansoAtaskaita"
tags: [gov, rc, balansoataskaita, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/balanso_ataskaitos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/balanso_ataskaitos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1806/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/balanso_ataskaitos"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# BalansoAtaskaita — Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos

**Dataset Context:** Juridinių asmenų registre tvarkomų juridinių asmenų finansinės atskaitomybės dokumentų duomenys iš balanso ataskaitų (apie juridinių asmenų nuosavą kapitalą; apie juridinių asmenų mokėtinas sumas ir kitus įsipareigojimus; apie juridinių asmenų trumpalaikį turtą; apie juridinių asmenų ilgalaikį turtą) (RAW data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Model:** `datasets/gov/rc/jar/balanso_ataskaitos/BalansoAtaskaita`[^manifest]
- **Dataset:** [Juridinių asmenų pateikti finansinės atskaitomybės dokumentai – balanso ataskaitos](../balanso_ataskaitos.md) (`datasets/gov/rc/jar/balanso_ataskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/balanso_ataskaitos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/balanso_ataskaitos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/balanso_ataskaitos/BalansoAtaskaita` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `forma` | `ref` | [Forma](../formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | juridinio asmens formos kodas iš JAR teisinių formų klasifikatoriaus | — |
| `statusas` | `ref` | [Statusas](../formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | juridinio asmens teisinio statuso kodas iš JAR teisinių statusų klasifikatoriaus | — |
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

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/balanso_ataskaitos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/balanso_ataskaitos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/balanso_ataskaitos (https://data.gov.lt/datasets/1806/)
