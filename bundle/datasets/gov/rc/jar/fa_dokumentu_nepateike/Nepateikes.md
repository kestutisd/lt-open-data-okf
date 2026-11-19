---
type: Table
title: "Nepateikes — Juridinių asmenų registre įregistruoti juridiniai asmenys"
description: "Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, nevykdančius prievolės teikti registro tvarkytojui finansinės atskaitomybės dokumentus (kodas, pavadinimas, juridinio asmens forma, įregistravimo data, reikšmė,"
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/fa_dokumentu_nepateike/Nepateikes"
tags: [gov, rc, nepateikes, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1571/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/fa_dokumentu_nepateike"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Nepateikes — Juridinių asmenų registre įregistruoti juridiniai asmenys

**Dataset Context:** Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, nevykdančius prievolės teikti registro tvarkytojui finansinės atskaitomybės dokumentus (kodas, pavadinimas, juridinio asmens forma, įregistravimo data, reikšmė,[^manifest]

- **Model:** `datasets/gov/rc/jar/fa_dokumentu_nepateike/Nepateikes`[^manifest]
- **Dataset:** [Finansinės atskaitomybės dokumentų nepateikusios įmonės](../fa_dokumentu_nepateike.md) (`datasets/gov/rc/jar/fa_dokumentu_nepateike`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_dokumentu_nepateike/Nepateikes` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinis asmuo juridinių asmenų registre | — |
| `ja_reg_data` | `date` | `D` | `4` | `open` | — | Juridinio asmens įregistravimo juridinių asmenų registre data | — |
| `forma` | `ref` | [Forma](../formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | Juridinio asmens formos kodas iš jar teisinių formų klasifikatoriaus | — |
| `statusas` | `ref` | [Statusas](../formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | Juridinio asmens teisinio statuso kodas iš jar teisinių statusų klasifikatoriaus | — |
| `nepateikta_iki` | `integer` | — | `2` | `open` | — | Metai, už kuriuos juridinis asmuo nepateikė finansinės atskaitomybės dokumentų | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nepateikta_iki` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/fa_dokumentu_nepateike (https://data.gov.lt/datasets/1571/)
