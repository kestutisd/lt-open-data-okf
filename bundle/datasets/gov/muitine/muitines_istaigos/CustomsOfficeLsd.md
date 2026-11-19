---
type: Table
title: "CustomsOfficeLsd"
description: "Spinta table datasets/gov/muitine/muitines_istaigos/CustomsOfficeLsd (8 columns)."
tags: [gov, muitine, customsofficelsd, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L44"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv#L44"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# CustomsOfficeLsd

- **Model:** `datasets/gov/muitine/muitines_istaigos/CustomsOfficeLsd`[^manifest]
- **Dataset:** [datasets/gov/muitine/muitines_istaigos](../muitines_istaigos.md) (`datasets/gov/muitine/muitines_istaigos`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_istaigos.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L44)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | — | — |
| `customs_office` | `ref` | [CustomsOffice](CustomsOffice.md) (`level=4 UUID`: `customs_office._id`) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `language_code` | `string` | — | `3` | `open` | — | Kalbos kodas | — |
| `usual_name` | `string` | — | `3` | `open` | `foaf:name` | Muitinės įstaigos pavadinimas | — |
| `city` | `string` | — | `3` | `open` | — | Įstaigos miestas | — |
| `street_and_number` | `string` | — | `3` | `open` | — | Įstaigos adresas | — |
| `prefix_suffix_flag` | `boolean` | — | `3` | `open` | — | Šalies kodo sufikso taikymo požymis | — |
| `space_to_add` | `boolean` | — | `3` | `open` | — | Tarpų įstaigos kode naudojimo požymis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `prefix_suffix_flag` | `true` | `1` | — | — | — |
| `prefix_suffix_flag` | `false` | `0` | — | — | — |
| `space_to_add` | `true` | `1` | — | — | — |
| `space_to_add` | `false` | `0` | — | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `foaf` | `http://xmlns.com/foaf/0.1/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_istaigos.csv#L44 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_istaigos.csv#L44)
