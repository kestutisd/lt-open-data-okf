---
type: Table
title: "Document"
description: "Duomenys apie išleistą standartą"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/Document"
tags: [gov, lst, document, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L215"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L215"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# Document

Duomenys apie išleistą standartą[^manifest]

- **Model:** `datasets/gov/lst/standards/Document`[^manifest]
- **Dataset:** [Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė](../standards.md) (`datasets/gov/lst/standards`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L215](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L215)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/Document` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `stage` | `ref` | [Stage](Stage.md) | — | `open` | — | — | — |
| `original_language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `name` | `string` | — | — | `open` | — | — | — |
| `isbn` | `string` | — | — | `open` | — | — | — |
| `version` | `string` | — | — | `open` | — | — | — |
| `finished_date` | `datetime` | — | — | `open` | — | — | — |
| `number_of_pages` | `integer` | — | — | `open` | — | — | — |
| `free_number_of_pages` | `integer` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L215 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L215)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
