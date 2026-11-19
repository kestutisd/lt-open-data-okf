---
type: Table
title: "Buveine"
description: "Įregistruotų juridinių asmenų buveinių (adresų) duomenų rinkinys iš Lietuvos Respublikos juridinių asmenų registro (juridinius asmenis apibūdinantys duomenys (kodas, pavadinimas, adreso identifikatorius iš Adresų registro, adresas)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/buveines/Buveine"
tags: [gov, rc, buveine, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/buveines.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/buveines.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1562/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/buveines"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Buveine

**Dataset Context:** Įregistruotų juridinių asmenų buveinių (adresų) duomenų rinkinys iš Lietuvos Respublikos juridinių asmenų registro (juridinius asmenis apibūdinantys duomenys (kodas, pavadinimas, adreso identifikatorius iš Adresų registro, adresas). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Model:** `datasets/gov/rc/jar/buveines/Buveine`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruotų juridinių asmenų buveinių (adresų) duomenys (raw data)](../buveines.md) (`datasets/gov/rc/jar/buveines`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/buveines.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/buveines.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/buveines/Buveine` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Juridinio asmens kodas iš juridinių asmenų registro | — |
| `adresas` | `ref` | [Adresas](../../ar/adresai/Adresas.md) (`level=4 UUID`: `adresas._id`) | `4` | `open` | — | Adreso kodas (išorinis LR AR) | — |
| `adresas_nuo` | `date` | `D` | `4` | `open` | — | Juridinio asmens adreso įrašymo į juridinių asmenų registro įrašą data | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.
- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/buveines.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/buveines.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/buveines (https://data.gov.lt/datasets/1562/)
