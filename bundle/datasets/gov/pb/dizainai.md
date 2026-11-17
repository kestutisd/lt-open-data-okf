---
type: Dataset
title: "Dizainai"
description: "Spinta dataset datasets/gov/pb/dizainai (15 tables)."
tags: [gov, pb, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dizainai

- **Namespace:** `datasets/gov/pb/dizainai`[^manifest]
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Time](dizainai/Time.md) | — | — | — | — | 2 | — |
| [Design](dizainai/Design.md) | — | `4` | `application_number` | `open` | 13 | — |
| [DesignRepresentation](dizainai/DesignRepresentation.md) | — | `3` | `view_uri` | — | 2 | — |
| [DesignRepresentationSheet](dizainai/DesignRepresentationSheet.md) | — | `3` | `view_uri` | — | 2 | — |
| [IndicationProductDetails](dizainai/IndicationProductDetails.md) | — | `3` | `indication_product_lt` | — | 1 | — |
| [ClassDescription](dizainai/ClassDescription.md) | — | `4` | `class_number` | — | 1 | — |
| [Priority](dizainai/Priority.md) | — | `4` | `priority_number` | — | 3 | — |
| [Publication](dizainai/Publication.md) | — | `4` | `publication_identifier` | — | 3 | — |
| [ExhibitionPriority](dizainai/ExhibitionPriority.md) | — | `4` | `exhibition_date` | — | 2 | — |
| [Applicant](dizainai/Applicant.md) | — | `3` | `person_type` | — | 1 | — |
| [FormattedNameAddress](dizainai/FormattedNameAddress.md) | — | `3` | `organization_name` | — | 1 | — |
| [FormattedAddress](dizainai/FormattedAddress.md) | — | `3` | `address_post_code` | — | 3 | — |
| [ApplicantAddress](dizainai/ApplicantAddress.md) | — | `3` | `address_country_code` | — | 1 | — |
| [Representative](dizainai/Representative.md) | — | `3` | `person_type` | — | 1 | — |
| [RepresentativeAddress](dizainai/RepresentativeAddress.md) | — | `3` | `address_country_code` | — | 1 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv
