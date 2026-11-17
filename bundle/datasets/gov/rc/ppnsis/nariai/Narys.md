---
type: Table
title: "Narys — PPNSIS duomenys apie politinių organizacijų narius"
description: "Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizcijų narius - jų lytį, amžių, pilietybę, geografinę padėtį ir narystę partijoje"
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariai/Narys"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Narys — PPNSIS duomenys apie politinių organizacijų narius

Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizcijų narius - jų lytį, amžių, pilietybę, geografinę padėtį ir narystę partijoje

- **Model:** `datasets/gov/rc/ppnsis/nariai/Narys`[^manifest]
- **Dataset:** [Politinių organizacijų narių duomenys apie lytį, amžių, pilietybę, geografinę padėtį ir narystę](../nariai.md) (`datasets/gov/rc/ppnsis/nariai`)
- **Manifest CSV:** [datasets/gov/rc/ppnsis/nariai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariai/Narys`
- **Primary Key (`ref`):** `nr, politine_organizacija`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `3` | `open` | — | Politinės organizacijos nario eil. numeris šiame duomenų rinkinyje | — |
| `nar_lytis` | `string` | — | `4` | `open` | — | Politinės organizacijos nario lytis | — |
| `nar_amzius` | `string` | — | `3` | `open` | — | Politinės organizacijos nario amžiaus grupė | — |
| `nario_pilietybe` | `string` | — | `3` | `open` | — | Politinės organizacijos nario pilietybė | — |
| `adreso_salis` | `string` | — | `3` | `open` | — | Šalies, kurioje deklaruota partijos nario gyvenamoji vieta, kodas iš Gyventojų registro | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje deklaruota partijos nario gyvenamoji vieta, iš Gyventojų registro | — |
| `saraso_data` | `date` | `D` | `4` | `open` | — | Politinės organizacijos sąrašo pateikimo data | — |
| `politine_organizacija` | `ref` | [/datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija](../politines_organizacijos/PolitineOrganizacija.md) | `4` | `open` | — | Politinės organizacijos, kaip juridinio asmens, pavadinimas iš Juridinių asmenų registro | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `nar_lytis` | `"V"` | — | — | Vyras | — |
| `nar_lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariai.csv
