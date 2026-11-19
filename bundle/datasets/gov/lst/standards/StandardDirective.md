---
type: Table
title: "StandardDirective"
description: "Standarto ryšys su Europos Sąjungos direktyvomis"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/StandardDirective"
tags: [gov, lst, standarddirective, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L302"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L302"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# StandardDirective

Standarto ryšys su Europos Sąjungos direktyvomis[^manifest]

- **Model:** `datasets/gov/lst/standards/StandardDirective`[^manifest]
- **Dataset:** [Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė](../standards.md) (`datasets/gov/lst/standards`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L302](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L302)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/StandardDirective` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `directive, standard`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `directive` | `ref` | [Directive](Directive.md) | — | `open` | — | — | — |
| `standard` | `ref` | [Standard](Standard.md) | — | `open` | — | — | — |
| `oficial_journal` | `string` | — | — | `open` | — | — | — |
| `lithuanian_oficial_journal` | `string` | — | — | `open` | — | — | — |
| `lithuanian_oficial_journal_date` | `datetime` | — | — | `open` | — | — | — |
| `harmonised` | `boolean` | — | — | `open` | — | — | — |
| `report_generation_date` | `datetime` | — | — | `open` | — | — | — |
| `applicability_date` | `datetime` | — | — | `open` | — | — | — |
| `oj_publication_date` | `datetime` | — | — | `open` | — | — | — |
| `coexistence_end_date` | `datetime` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L302 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L302)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
