---
type: Table
title: "NariuSkaicius — PPNSIS duomenys apie politinių organizacijų narių skaičių"
description: "Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizacijų narių skaičių"
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariu_skaicius/NariuSkaicius"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariu_skaicius.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# NariuSkaicius — PPNSIS duomenys apie politinių organizacijų narių skaičių

Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizacijų narių skaičių

- **Model:** `datasets/gov/rc/ppnsis/nariu_skaicius/NariuSkaicius`[^manifest]
- **Dataset:** [Duomenys apie politinių organizacijų narių skaičių](../nariu_skaicius.md) (`datasets/gov/rc/ppnsis/nariu_skaicius`)
- **Manifest CSV:** [datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariu_skaicius/NariuSkaicius`
- **Primary Key (`ref`):** `politine_organizacija`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `politine_organizacija` | `ref` | [/datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija](../politines_organizacijos/PolitineOrganizacija.md) | `4` | `open` | — | Politinės organizacijos, kaip juridinio asmens, kodas iš Juridinių asmenų registro | — |
| `saraso_data` | `date` | `D` | `4` | `open` | — | Politinės organizacijos sąrašo pateikimo data | — |
| `nariu_skaicius` | `integer` | `U` | `4` | `open` | — | Politinės organizacijos narių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariu_skaicius.csv
