---
type: Table
title: "SveikatosSpecialistas — Sveikatos priežiūros specialistai"
description: "Asmens duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/SveikatosSpecialistas"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16"
    last_modified: "2026-11-11T14:39:20Z"
---

# SveikatosSpecialistas — Sveikatos priežiūros specialistai

Asmens duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos. Viena lentelės eilutė atitinka vieną unikalų sveikatos priežiūros specialistą. Eilutėje nurodoma informacija apie specialisto lytį, gimimo ir mirties metus.

- **Model:** `datasets/gov/vaspvt/specialistu_kompetencijos/SveikatosSpecialistas`[^manifest]
- **Dataset:** [Sveikatos priežiūros specialistų kompetencijų duomenys](../specialistu_kompetencijos.md) (`datasets/gov/vaspvt/specialistu_kompetencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/SveikatosSpecialistas`
- **Primary Key (`ref`):** `specialist_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `specialist_id` | `string` | — | `4` | `open` | — | Specialisto ID | Sveikatos priežiūros specialisto vidinis identifikacinis numeris |
| `lytis_ak` | `string` | — | `4` | `open` | — | Lytis | Valstybės duomenų agentūros sugeneruotas specialisto lyties stulpelis, kuris gautas iš asmens kodo |
| `gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Gimimo metai | Valstybės duomenų agentūros sugeneruotas specialisto gimimo metų stulpelis, kuris gautas iš asmens kodo |
| `mirties_metai` | `date` | `Y` | `4` | `open` | — | Mirties metai | Sveikatos priežiūros specialisto mirties metai |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_ak` | `"M"` | — | — | Moteris | — |
| `lytis_ak` | `"V"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv
