---
type: Table
title: "TermDomain"
description: "Taikymo sritis (standartizacija ir metrologija)"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/TermDomain"
tags: [gov, lst, termdomain, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L35"
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv#L35"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/terms"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# TermDomain

Taikymo sritis (standartizacija ir metrologija)[^manifest]

- **Model:** `datasets/gov/lst/terms/TermDomain`[^manifest]
- **Dataset:** [Standartų terminų bazė](../terms.md) (`datasets/gov/lst/terms`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L35](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L35)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/TermDomain` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `term, domain`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `term` | `ref` | [Term](Term.md) | — | `open` | — | — | — |
| `domain` | `ref` | [Domain](Domain.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv#L35 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L35)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/terms (https://data.gov.lt/datasets/996/)
