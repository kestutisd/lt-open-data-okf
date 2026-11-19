---
type: Table
title: "ForeignTC"
description: "Tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų technikos komitetai ir jų darbo grupės"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/ForeignTC"
tags: [gov, lst, foreigntc, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L187"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L187"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# ForeignTC

Tarptautinių standartizacijos institucijų ir Europos standartizacijos organizacijų technikos komitetai ir jų darbo grupės[^manifest]

- **Model:** `datasets/gov/lst/standards/ForeignTC`[^manifest]
- **Dataset:** [Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė](../standards.md) (`datasets/gov/lst/standards`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L187](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L187)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/ForeignTC` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `organisation` | `ref` | [Organisation](Organisation.md) | — | `open` | — | — | — |
| `status` | `ref` | [OrganisationUnitStatus](OrganisationUnitStatus.md) | — | `open` | — | — | — |
| `name` | `string` | — | — | `open` | — | — | — |
| `description` | `string` | — | — | `open` | — | — | — |
| `secretary_name` | `string` | — | — | `open` | — | — | — |
| `description_lt` | `string` | — | — | `open` | — | — | — |
| `membership_status` | `ref` | [ForeignTcMembershipStatus](ForeignTcMembershipStatus.md) | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L187 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L187)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
