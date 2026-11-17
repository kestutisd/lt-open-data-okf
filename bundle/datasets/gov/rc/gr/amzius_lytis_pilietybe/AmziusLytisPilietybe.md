---
type: Table
title: "AmziusLytisPilietybe — Gyventojų registro duomenys apie Lietuvos gyventojų amžių, pilietybę ir lytį pagal savivaldybes"
description: "Spinta table datasets/gov/rc/gr/amzius_lytis_pilietybe/AmziusLytisPilietybe (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/amzius_lytis_pilietybe/AmziusLytisPilietybe"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/amziu_lytis_pilietybe.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# AmziusLytisPilietybe — Gyventojų registro duomenys apie Lietuvos gyventojų amžių, pilietybę ir lytį pagal savivaldybes

- **Model:** `datasets/gov/rc/gr/amzius_lytis_pilietybe/AmziusLytisPilietybe`[^manifest]
- **Dataset:** [Gyventojų registro duomenys apie Lietuvos gyventojų amžių, pilietybę ir lytį pagal savivaldybes](../amzius_lytis_pilietybe.md) (`datasets/gov/rc/gr/amzius_lytis_pilietybe`)
- **Manifest CSV:** [datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/amzius_lytis_pilietybe/AmziusLytisPilietybe`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Gyventojo eilės numeris šiame duomenų rinkinyje | — |
| `lytis` | `string` | — | `4` | `open` | — | Gyventojo lytis | — |
| `amzius` | `string` | — | `3` | `open` | — | Gyventojo amžius / amžiaus grupė | — |
| `pilietybe` | `string` | — | `3` | `open` | — | Gyventojo turima pilietybė arba pilietybių grupė | — |
| `dek_metai` | `integer` | — | `2` | `open` | — | Gyventojo gyvenamosios vietos deklaravimo metai | — |
| `dek_ketvirtis` | `string` | — | `2` | `open` | — | Gyventojo gyvenamosios vietos deklaravimo metų ketvirtis | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybė, kurioje deklaruota gyventojo gyvenamoji vieta iš Adresų registro | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/amziu_lytis_pilietybe.csv
