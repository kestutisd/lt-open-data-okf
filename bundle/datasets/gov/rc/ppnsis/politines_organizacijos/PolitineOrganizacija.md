---
type: Table
title: "PolitineOrganizacija — PPNSIS duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas"
description: "Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas"
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/politines_organizacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# PolitineOrganizacija — PPNSIS duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas

Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas

- **Model:** `datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos politinių organizacijų duomenys](../politines_organizacijos.md) (`datasets/gov/rc/ppnsis/politines_organizacijos`)
- **Manifest CSV:** [datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/politines_organizacijos.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../../jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Politinės organizacijos, kaip juridinio asmens, kodas iš Juridinių asmenų registro | — |
| `reg_data` | `date` | `D` | `4` | `open` | — | Įregistravimo data iš Juridinių asmenų registro | — |
| `statusas` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Statusas](../../jar/formos_statusai/Statusas.md) | `4` | `open` | — | Teisinis statusas iš Juridinių asmenų registro | — |
| `stat_data_nuo` | `date` | `D` | `4` | `open` | — | Teisinio statuso data iš Juridinių asmenų registro | — |
| `par_busena` | `string` | — | `4` | `open` | — | Būsena (veikianti / neveikianti) iš Politinių partijų narių sąrašų informacinės sistemos | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `par_busena` | `"VEI"` | — | — | Veikianti | — |
| `par_busena` | `"NEV"` | — | — | Neveikianti | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/politines_organizacijos.csv
