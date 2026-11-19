---
type: Table
title: "Project"
description: "Nacionalinių, tarptautinių ir Europos standartų projektų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/Project"
tags: [gov, lst, project, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L117"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L117"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# Project

Nacionalinių, tarptautinių ir Europos standartų projektų duomenys[^manifest]

- **Model:** `datasets/gov/lst/standards/Project`[^manifest]
- **Dataset:** [Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė](../standards.md) (`datasets/gov/lst/standards`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L117](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L117)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/Project` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `status` | `ref` | [ProjectStatus](ProjectStatus.md) | — | `open` | — | — | — |
| `type` | `ref` | [ProjectType](ProjectType.md) | — | `open` | — | — | — |
| `responsible_organisation_unit` | `ref` | [OrganisationUnit](OrganisationUnit.md) | — | `open` | — | — | — |
| `work_group` | `ref` | [OrganisationUnit](OrganisationUnit.md) | — | `open` | — | — | — |
| `current_stage` | `integer` | — | — | `open` | — | — | — |
| `european_stage` | `integer` | — | — | `open` | — | — | — |
| `track` | `string` | — | — | `open` | — | — | — |
| `notes` | `string` | — | — | `open` | — | — | — |
| `dop` | `datetime` | — | — | `open` | — | — | — |
| `doa` | `datetime` | — | — | `open` | — | — | — |
| `dow` | `datetime` | — | — | `open` | — | — | — |
| `modification_date` | `datetime` | — | — | `open` | — | — | — |
| `creation_date` | `datetime` | — | — | `open` | — | — | — |
| `work_item` | `string` | — | — | `open` | — | — | — |
| `notification_date` | `datetime` | — | — | `open` | — | — | — |
| `notification_status` | `ref` | [ProjectNotificationStatus](ProjectNotificationStatus.md) | — | `open` | — | — | — |
| `notification_number` | `integer` | — | — | `open` | — | — | — |
| `approval_date` | `datetime` | — | — | `open` | — | — | — |
| `archive_date` | `datetime` | — | — | `open` | — | — | — |
| `docs_delete_date` | `datetime` | — | — | `open` | — | — | — |
| `approval_protocol_nr` | `string` | — | — | `open` | — | — | — |
| `priority` | `boolean` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L117 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L117)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
