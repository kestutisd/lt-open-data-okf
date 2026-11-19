---
type: Table
title: "Translation"
description: "Termino atitikmenys kitomis kalbomis"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/Translation"
tags: [gov, lst, translation, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L39"
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv#L39"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/terms"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# Translation

Termino atitikmenys kitomis kalbomis[^manifest]

- **Model:** `datasets/gov/lst/terms/Translation`[^manifest]
- **Dataset:** [Standartų terminų bazė](../terms.md) (`datasets/gov/lst/terms`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L39)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/Translation` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `translation` | `string` | — | — | `open` | — | — | — |
| `language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `term` | `ref` | [Term](Term.md) | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv#L39 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L39)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/terms (https://data.gov.lt/datasets/996/)
