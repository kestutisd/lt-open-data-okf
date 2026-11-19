---
type: Table
title: "AmziusLytisPilietybe — Gyventojų registro duomenys apie Lietuvos gyventojų amžių, pilietybę ir lytį pagal savivaldybes"
description: "Spinta table datasets/gov/rc/gr/amzius_lytis_pilietybe/AmziusLytisPilietybe (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/amzius_lytis_pilietybe/AmziusLytisPilietybe"
tags: [gov, rc, amziuslytispilietybe, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1747/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/gr/amzius_lytis_pilietybe"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AmziusLytisPilietybe — Gyventojų registro duomenys apie Lietuvos gyventojų amžių, pilietybę ir lytį pagal savivaldybes

- **Model:** `datasets/gov/rc/gr/amzius_lytis_pilietybe/AmziusLytisPilietybe`[^manifest]
- **Dataset:** [Gyventojų registro duomenys apie Lietuvos gyventojų amžių, pilietybę ir lytį pagal savivaldybes](../amzius_lytis_pilietybe.md) (`datasets/gov/rc/gr/amzius_lytis_pilietybe`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/amzius_lytis_pilietybe/AmziusLytisPilietybe` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Gyventojo eilės numeris šiame duomenų rinkinyje | — |
| `lytis` | `string` | — | `4` | `open` | — | Gyventojo lytis | — |
| `amzius` | `string` | — | `3` | `open` | — | Gyventojo amžius / amžiaus grupė | — |
| `pilietybe` | `string` | — | `3` | `open` | — | Gyventojo turima pilietybė arba pilietybių grupė | — |
| `dek_metai` | `integer` | — | `2` | `open` | — | Gyventojo gyvenamosios vietos deklaravimo metai | — |
| `dek_ketvirtis` | `string` | — | `2` | `open` | — | Gyventojo gyvenamosios vietos deklaravimo metų ketvirtis | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybė, kurioje deklaruota gyventojo gyvenamoji vieta iš Adresų registro | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/amziu_lytis_pilietybe.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/gr/amzius_lytis_pilietybe (https://data.gov.lt/datasets/1747/)
