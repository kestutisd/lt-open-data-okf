---
type: Table
title: "JuridinisAsmuo — Juridinis asmuo"
description: "Spinta table datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo"
tags: [gov, rc, juridinisasmuo, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/iregistruoti.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1484/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/iregistruoti"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# JuridinisAsmuo — Juridinis asmuo

- **Model:** `datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruoti juridiniai asmenys](../iregistruoti.md) (`datasets/gov/rc/jar/iregistruoti`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/iregistruoti.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ja_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ja_kodas` | `integer` | — | `4` | `open` | — | Juridinio asmens kodas | — |
| `ja_pavadinimas` | `string` | — | `4` | `open` | — | Juridinio asmens pavadinimas | — |
| `pilnas_adresas` | `string` | — | `1` | `open` | — | Registracijos adresas | — |
| `adresas` | `ref` | [Adresas](../../ar/adresai/Adresas.md) (`level=4 UUID`: `adresas._id`) | `4` | `open` | — | Adresas | — |
| `reg_data` | `date` | `D` | `4` | `open` | — | Įregistravimo data | — |
| `isreg_data` | `date` | `D` | `4` | `open` | — | Išregistravimo data | — |
| `forma` | `ref` | [Forma](../formos_statusai/Forma.md) (`level=4 UUID`: `forma._id`) | `4` | `open` | — | Formos pavadinimas | — |
| `statusas` | `ref` | [Statusas](../formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | Statuso pavadinimas | — |
| `stat_data` | `date` | `D` | `4` | `open` | — | Statuso įgijimo data | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/iregistruoti.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruoti.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/iregistruoti (https://data.gov.lt/datasets/1484/)
