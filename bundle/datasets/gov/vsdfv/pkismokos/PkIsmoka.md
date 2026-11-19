---
type: Table
title: "PkIsmoka"
description: "Spinta table datasets/gov/vsdfv/pkismokos/PkIsmoka (7 columns)."
tags: [gov, vsdfv, pkismoka, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkismokos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/pkismokos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# PkIsmoka

- **Model:** `datasets/gov/vsdfv/pkismokos/PkIsmoka`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/pkismokos](../pkismokos.md) (`datasets/gov/vsdfv/pkismokos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/pkismokos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkismokos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `metai`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `ismoku_sutarciu_sk` | `integer` | — | `4` | `open` | — | Išmokų sutarčių skaičius (kiek sudaryta iš viso) | — |
| `vienkartine_ismoka_sk` | `integer` | — | `4` | `open` | — | Vienkartinė išmoka | — |
| `periodine_ismoka_sk` | `integer` | — | `4` | `open` | — | Periodinė išmoka | — |
| `standartinis_anuitetas_sk` | `integer` | — | `4` | `open` | — | Standartinis anuitetas | — |
| `atidetas_anuitetas_sk` | `integer` | — | `4` | `open` | — | Atidėtas anuitetas | — |
| `anuitetas_su_gar_mok_sk` | `integer` | — | `4` | `open` | — | Anuitetas su garantuotu mokejimu | Anuitetas su garantuojamu mokėjimo laikotarpiu |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/pkismokos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkismokos.csv#L6)
