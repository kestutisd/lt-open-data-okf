---
type: Table
title: "NariuSkaicius — PPNSIS duomenys apie politinių organizacijų narių skaičių"
description: "Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizacijų narių skaičių"
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariu_skaicius/NariuSkaicius"
tags: [gov, rc, nariuskaicius, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1737/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/nariu_skaicius"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NariuSkaicius — PPNSIS duomenys apie politinių organizacijų narių skaičių

Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizacijų narių skaičių[^manifest]

- **Model:** `datasets/gov/rc/ppnsis/nariu_skaicius/NariuSkaicius`[^manifest]
- **Dataset:** [Duomenys apie politinių organizacijų narių skaičių](../nariu_skaicius.md) (`datasets/gov/rc/ppnsis/nariu_skaicius`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariu_skaicius/NariuSkaicius` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `politine_organizacija`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `politine_organizacija` | `ref` | [PolitineOrganizacija](../politines_organizacijos/PolitineOrganizacija.md) (`level=4 UUID`: `politine_organizacija._id`) | `4` | `open` | — | Politinės organizacijos, kaip juridinio asmens, kodas iš Juridinių asmenų registro | — |
| `saraso_data` | `date` | `D` | `4` | `open` | — | Politinės organizacijos sąrašo pateikimo data | — |
| `nariu_skaicius` | `integer` | `U` | `4` | `open` | — | Politinės organizacijos narių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariu_skaicius.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/nariu_skaicius (https://data.gov.lt/datasets/1737/)
