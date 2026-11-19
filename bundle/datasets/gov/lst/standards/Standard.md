---
type: Table
title: "Standard"
description: "Duomenys apie Lietuvos standartus (standarto žymuo, išleidimo data, panaikinimo data, atitikties laipsnis ir kt."
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/Standard"
tags: [gov, lst, standard, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L242"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L242"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# Standard

Duomenys apie Lietuvos standartus (standarto žymuo, išleidimo data, panaikinimo data, atitikties laipsnis ir kt. duomenys)[^manifest]

- **Model:** `datasets/gov/lst/standards/Standard`[^manifest]
- **Dataset:** [Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė](../standards.md) (`datasets/gov/lst/standards`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L242](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L242)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/Standard` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `status` | `ref` | [StandardStatus](StandardStatus.md) | — | `open` | — | — | — |
| `project` | `ref` | [Project](Project.md) | — | `open` | — | — | — |
| `type_of_publication` | `ref` | [TypeOfPublication](TypeOfPublication.md) | — | `open` | — | — | — |
| `organisation` | `ref` | [Organisation](Organisation.md) | — | `open` | — | — | — |
| `organisation_unit` | `ref` | [OrganisationUnit](OrganisationUnit.md) | — | `open` | — | — | — |
| `modification_date` | `datetime` | — | — | `open` | — | — | — |
| `creation_date` | `datetime` | — | — | `open` | — | — | — |
| `standard_reference` | `string` | — | — | `open` | — | — | — |
| `edition` | `string` | — | — | `open` | — | — | — |
| `edition_notes` | `string` | — | — | `open` | — | — | — |
| `publication_date` | `datetime` | — | — | `open` | — | — | — |
| `withdrawal_document_number` | `string` | — | — | `open` | — | — | — |
| `withdrawal_date` | `datetime` | — | — | `open` | — | — | — |
| `is_valid_until` | `datetime` | — | — | `open` | — | — | — |
| `general_notes` | `string` | — | — | `open` | — | — | — |
| `sector` | `string` | — | — | `open` | — | — | — |
| `contract_number` | `string` | — | — | `open` | — | — | — |
| `registration_date` | `datetime` | — | — | `open` | — | — | — |
| `title_aproved` | `boolean` | — | — | `open` | — | — | — |
| `foreign_reference` | `string` | — | — | `open` | — | — | — |
| `implementation_type` | `ref` | [ImplementationType](ImplementationType.md) | — | `open` | — | — | — |
| `degree_of_equivalence` | `ref` | [DegreeOfEquivalence](DegreeOfEquivalence.md) | — | `open` | — | — | — |
| `international_reference` | `string` | — | — | `open` | — | — | — |
| `translation_start_date` | `datetime` | — | — | `open` | — | — | — |
| `implementation_date` | `datetime` | — | — | `open` | — | — | — |
| `translation_date` | `datetime` | — | — | `open` | — | — | — |
| `language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `original_language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `harmonized` | `integer` | — | — | `open` | — | — | — |
| `cancel_date` | `datetime` | — | — | `open` | — | — | — |
| `link` | `string` | — | — | `open` | — | — | — |
| `remarks` | `string` | — | — | `open` | — | — | — |
| `notification_state` | `ref` | [StandardNotificationState](StandardNotificationState.md) | — | `open` | — | — | — |
| `term_count` | `integer` | — | — | `open` | — | — | — |
| `term_approved_by` | `ref` | [TermApprovedBy](TermApprovedBy.md) | — | `open` | — | — | — |
| `term_source` | `ref` | [TermSource](TermSource.md) | — | `open` | — | — | — |
| `archive_date` | `datetime` | — | — | `open` | — | — | — |
| `terms_note` | `string` | — | — | `open` | — | — | — |
| `applicability_date` | `datetime` | — | — | `open` | — | — | — |
| `oj_publication_date` | `datetime` | — | — | `open` | — | — | — |
| `coexistence_end_date` | `datetime` | — | — | `open` | — | — | — |
| `have_deviation` | `boolean` | — | — | `open` | — | — | — |
| `have_exceptional_reference` | `boolean` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L242 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L242)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
