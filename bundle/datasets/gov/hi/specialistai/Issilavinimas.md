---
type: Table
title: "Issilavinimas — Visuomenės sveikatos specialistų duomenys pagal išsilavinimą"
description: "Specialistai, atliekantys visuomenės sveikatos priežiūros funkcijas Lietuvos nacionalinės sveikatos sistemos visuomenės sveikatos priežiūros įstaigose (amžiaus grupė, išsilavinimas, lytis, įstaigų grupė)."
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai/Issilavinimas"
tags: [gov, hi, issilavinimas, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1106/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/specialistai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Issilavinimas — Visuomenės sveikatos specialistų duomenys pagal išsilavinimą

**Dataset Context:** Specialistai, atliekantys visuomenės sveikatos priežiūros funkcijas Lietuvos nacionalinės sveikatos sistemos visuomenės sveikatos priežiūros įstaigose (amžiaus grupė, išsilavinimas, lytis, įstaigų grupė).[^manifest]

- **Model:** `datasets/gov/hi/specialistai/Issilavinimas`[^manifest]
- **Dataset:** [Visuomenės sveikatos priežiūros specialistų duomenys](../specialistai.md) (`datasets/gov/hi/specialistai`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai/Issilavinimas` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar` | `ref` | [JuridinisAsmuo](../../rc/jar/iregistruoti/JuridinisAsmuo.md) (`level=4 UUID` via `JuridinisAsmuo[ja_kodas]`: `jar._id`) | `4` | `open` | — | Įstaiga | Įstaigos, kurioje dirba visuomenės sveikatos priežiūros specialistas, kodas |
| `lytis` | `string` | — | `4` | `open` | — | Specialisto lytis | — |
| `amzius` | `string` | — | `4` | `open` | — | Specialisto amžiaus grupė | — |
| `studiju_sritis` | `string` | — | `4` | `open` | — | Specialistui priskirta studijų krypčių grupė | — |
| `kvalifikacija` | `string` | — | `4` | `open` | — | Specialisto kvalifikacinis laipsnis | — |
| `mokslo_laipsnis` | `string` | — | `4` | `open` | — | Specialisto mokslo laipsnis | — |
| `issilavinimas` | `string` | — | `4` | `open` | — | Specialisto išsilavinimas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/specialistai (https://data.gov.lt/datasets/1106/)
