---
type: Table
title: "PolitineOrganizacija — PPNSIS duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas"
description: "Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas"
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija"
tags: [gov, rc, politineorganizacija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1735/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/politines_organizacijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PolitineOrganizacija — PPNSIS duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas

Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas[^manifest]

- **Model:** `datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos politinių organizacijų duomenys](../politines_organizacijos.md) (`datasets/gov/rc/ppnsis/politines_organizacijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `juridinis_asmuo`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID`: `juridinis_asmuo._id`) | `4` | `open` | — | Politinės organizacijos, kaip juridinio asmens, kodas iš Juridinių asmenų registro | — |
| `reg_data` | `date` | `D` | `4` | `open` | — | Įregistravimo data iš Juridinių asmenų registro | — |
| `statusas` | `ref` | [Statusas](../../jar/formos_statusai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | Teisinis statusas iš Juridinių asmenų registro | — |
| `stat_data_nuo` | `date` | `D` | `4` | `open` | — | Teisinio statuso data iš Juridinių asmenų registro | — |
| `par_busena` | `string` | — | `4` | `open` | — | Būsena (veikianti / neveikianti) iš Politinių partijų narių sąrašų informacinės sistemos | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `par_busena` | `"VEI"` | — | — | Veikianti | — |
| `par_busena` | `"NEV"` | — | — | Neveikianti | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/politines_organizacijos (https://data.gov.lt/datasets/1735/)
