---
type: Dataset
title: "Prekių ženklai"
description: "Lithuanian open data dataset datasets/gov/pb/prekiuzenklai (9 lentelės)."
tags: [gov, pb, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prekių ženklai

- **Namespace:** `datasets/gov/pb/prekiuzenklai`[^manifest]
- **Manifest CSV:** [datasets/gov/pb/prekiuzenklai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (`undeployed` — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `9` (9 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Time](prekiuzenklai/Time.md) | — | — | — | — | `2` | — |
| [TradeMark](prekiuzenklai/TradeMark.md) | Trademark | `4` | `application_number` | `open` | `12` | — |
| [MarkImage](prekiuzenklai/MarkImage.md) | Mark image | `3` | `trade_mark, mark_image_uri` | `open` | `3` | — |
| [MarkImageCategory](prekiuzenklai/MarkImageCategory.md) | Mark image category | `4` | `category_code` | `open` | `2` | — |
| [ClassDescription](prekiuzenklai/ClassDescription.md) | Class description | `3` | `class_number` | `open` | `2` | — |
| [Priority](prekiuzenklai/Priority.md) | Priority | `4` | `priority_number` | `open` | `3` | — |
| [Publication](prekiuzenklai/Publication.md) | Publication | `3` | `publication_identifier` | `open` | `3` | — |
| [Applicant](prekiuzenklai/Applicant.md) | Applicant | `3` | `person_type` | `open` | `1` | — |
| [FormattedNameAddress](prekiuzenklai/FormattedNameAddress.md) | Name address | `3` | `organization_name` | `open` | `1` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `ns` | `http://vpb.lt/open-data/schemas/trademark/v1` |
| `ns2` | `http://vpb.lt/open-data/schemas/address/v1` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/prekiuzenklai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/prekiuzenklai.csv#L2)
