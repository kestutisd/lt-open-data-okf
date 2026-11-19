---
type: Table
title: "SveikatosSpecialistas — Sveikatos priežiūros specialistai"
description: "\"Asmens duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/SveikatosSpecialistas"
tags: [gov, vaspvt, sveikatosspecialistas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3887/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/specialistu_kompetencijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SveikatosSpecialistas — Sveikatos priežiūros specialistai

"Asmens duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos. Viena lentelės eilutė atitinka vieną unikalų sveikatos priežiūros specialistą. Eilutėje nurodoma informacija apie specialisto lytį, gimimo ir mirties metus."[^manifest]

- **Model:** `datasets/gov/vaspvt/specialistu_kompetencijos/SveikatosSpecialistas`[^manifest]
- **Dataset:** [Sveikatos priežiūros specialistų kompetencijų duomenys](../specialistu_kompetencijos.md) (`datasets/gov/vaspvt/specialistu_kompetencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/SveikatosSpecialistas` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `specialist_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `specialist_id` | `string` | — | `4` | `open` | — | Specialisto ID | Sveikatos priežiūros specialisto vidinis identifikacinis numeris |
| `lytis_ak` | `string` | — | `4` | `open` | — | Lytis | "Valstybės duomenų agentūros sugeneruotas specialisto lyties stulpelis, kuris gautas iš asmens kodo" |
| `gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Gimimo metai | "Valstybės duomenų agentūros sugeneruotas specialisto gimimo metų stulpelis, kuris gautas iš asmens kodo" |
| `mirties_metai` | `date` | `Y` | `4` | `open` | — | Mirties metai | Sveikatos priežiūros specialisto mirties metai |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_ak` | `"M"` | — | — | Moteris | — |
| `lytis_ak` | `"V"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L16)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/specialistu_kompetencijos (https://data.gov.lt/datasets/3887/)
