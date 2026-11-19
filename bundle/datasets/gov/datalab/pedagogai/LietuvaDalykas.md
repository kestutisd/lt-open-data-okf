---
type: Table
title: "LietuvaDalykas — LietuvaDalykas"
description: "Spinta table datasets/gov/datalab/pedagogai/LietuvaDalykas (21 columns)."
resource: "https://get.data.gov.lt/datasets/gov/datalab/pedagogai/LietuvaDalykas"
tags: [gov, datalab, lietuvadalykas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/pedagogai.csv#L15"
    title: "atviriduomenys/manifest — datasets/gov/datalab/pedagogai.csv#L15"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# LietuvaDalykas — LietuvaDalykas

- **Model:** `datasets/gov/datalab/pedagogai/LietuvaDalykas`[^manifest]
- **Dataset:** [Pedagogų statistika](../pedagogai.md) (`datasets/gov/datalab/pedagogai`)[^manifest]
- **Manifest CSV:** [datasets/gov/datalab/pedagogai.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/pedagogai.csv#L15)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/datalab/pedagogai/LietuvaDalykas` (`deployed`)[^manifest]
- **Provider:** `datalab` — Valstybės duomenų agentūra (DataLab) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | ID | — |
| `statistikos_tipas` | `string` | — | `4` | `open` | — | Statistikos tipas | — |
| `asmens_numeris` | `string` | — | `4` | `open` | — | Asmens numeris | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Amžiaus grupė | — |
| `institucijos_id` | `string` | — | `4` | `open` | — | Institucijos ID | — |
| `institucijos_savivaldybes_kodas` | `string` | — | `4` | `open` | — | Institucijos savivaldybės kodas | — |
| `institucijos_sav_pav` | `string` | — | `4` | `open` | — | Institucijos savivaldybės pavadinimas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | JAR kodas | — |
| `priklausomybe` | `string` | — | `4` | `open` | — | Priklausomybė | — |
| `tipas` | `string` | — | `4` | `open` | — | Tipas | — |
| `mokslo_metai` | `string` | — | `4` | `open` | — | Mokslo metai | — |
| `dalyko_pavadinimas_vda` | `string` | — | `4` | `open` | — | Dalyko pavadinimas (VDA) | — |
| `istaigos_primary_key` | `string` | — | `4` | `open` | — | Įstaigos primary key | — |
| `grupe` | `string` | — | `4` | `open` | — | Grupė | — |
| `paskirties_grupe` | `string` | — | `4` | `open` | — | Paskirties grupė | — |
| `savivaldybes_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `mokyklos_amziaus_mediana` | `integer` | — | `4` | `open` | — | Mokyklos amžiaus mediana | — |
| `duomenu_atnaujinimo_laikas` | `datetime` | — | `4` | `open` | — | Duomenų atnaujinimo laikas | — |
| `statistikos_busena` | `string` | — | `4` | `open` | — | Statistikos būsena | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/datalab/pedagogai.csv#L15 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/datalab/pedagogai.csv#L15)
