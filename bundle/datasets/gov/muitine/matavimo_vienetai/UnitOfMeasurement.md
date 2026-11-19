---
type: Table
title: "UnitOfMeasurement — Matavimo vienetas"
description: "Naudojami deklaruojant prekes Lietuvos Respublikoje."
tags: [gov, muitine, unitofmeasurement, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/matavimo_vienetai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/matavimo_vienetai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# UnitOfMeasurement — Matavimo vienetas

Naudojami deklaruojant prekes Lietuvos Respublikoje.[^manifest]

- **Model:** `datasets/gov/muitine/matavimo_vienetai/UnitOfMeasurement`[^manifest]
- **Dataset:** [datasets/gov/muitine/matavimo_vienetai](../matavimo_vienetai.md) (`datasets/gov/muitine/matavimo_vienetai`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/matavimo_vienetai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/matavimo_vienetai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `code`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `4` | `open` | — | Kodas | Kodas sudarytas iš 3 simbolių. |
| `national` | `boolean` | — | `4` | `open` | — | Nacionalinis požymis | — |
| `valid_from` | `date` | — | `3` | `open` | — | Galiojimo pradžia | — |
| `valid_to` | `date` | — | `3` | `open` | — | Galiojimo pabaiga | — |
| `description_lt` | `string` | — | `2` | `open` | — | Aprašymas (LT) | — |
| `description_en` | `string` | — | `2` | `open` | — | Aprašymas (EN) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `description_lt` | `update(property: "description@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `description_en` | `update(property: "description@en", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/matavimo_vienetai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/matavimo_vienetai.csv#L6)
