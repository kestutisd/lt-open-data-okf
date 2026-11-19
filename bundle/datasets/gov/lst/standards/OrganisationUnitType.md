---
type: Table
title: "OrganisationUnitType"
description: "Lietuvos standartizacijos departamento struktūriniai subjektai (vidinis skyrius, darbo grupė, technikos komitetas, laikinoji darbo grupė, terminologijos komisija)"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/OrganisationUnitType"
tags: [gov, lst, organisationunittype, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L43"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L43"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# OrganisationUnitType

Lietuvos standartizacijos departamento struktūriniai subjektai (vidinis skyrius, darbo grupė, technikos komitetas, laikinoji darbo grupė, terminologijos komisija)[^manifest]

- **Model:** `datasets/gov/lst/standards/OrganisationUnitType`[^manifest]
- **Dataset:** [Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė](../standards.md) (`datasets/gov/lst/standards`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L43](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L43)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/OrganisationUnitType` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | — | — | `open` | — | — | — |
| `level` | `integer` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L43 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L43)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
