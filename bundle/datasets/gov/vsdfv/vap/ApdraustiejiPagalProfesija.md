---
type: Table
title: "ApdraustiejiPagalProfesija"
description: "Spinta table datasets/gov/vsdfv/vap/ApdraustiejiPagalProfesija (4 columns)."
tags: [gov, vsdfv, apdraustiejipagalprofesija, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L39"
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv#L39"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ApdraustiejiPagalProfesija

- **Model:** `datasets/gov/vsdfv/vap/ApdraustiejiPagalProfesija`[^manifest]
- **Dataset:** [datasets/gov/vsdfv/vap](../vap.md) (`datasets/gov/vsdfv/vap`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/vap.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L39)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `vsdfv` — Valstybinio socialinio draudimo fondo valdyba („Sodra“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `metai, menuo, profesija`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `string` | — | `2` | `open` | — | Mėnuo | — |
| `profesija` | `string` | — | `3` | `open` | — | Profesija | Darbdavio suteiktas keturženklis profesijos kodas iš LPK |
| `vid_apdraustuju_pajamos` | `number` | — | `3` | `open` | — | Vidutinės apdraustųjų pajamos, Eur | Vidutinės apdraustųjų pajamos vidutinės asmens pajamos, nuo kurių buvo priskaičiuotos valstybinio socialinio draudimo įmokos per ataskaitinį laikotarpį |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `vid_apdraustuju_pajamos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/vap.csv#L39 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/vap.csv#L39)
