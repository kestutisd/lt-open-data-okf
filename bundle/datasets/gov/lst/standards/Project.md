---
type: Table
title: "Project"
description: "Nacionalinių, tarptautinių ir Europos standartų projektų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/Project"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L117"
    last_modified: "2026-11-11T14:39:20Z"
---

# Project

Nacionalinių, tarptautinių ir Europos standartų projektų duomenys

- **Model:** `datasets/gov/lst/standards/Project`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L117](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L117)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/Project`
- **Primary Key (`ref`):** `id`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv
