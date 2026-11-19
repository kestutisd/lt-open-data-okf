---
type: Dataset
title: "Patentai"
description: "Lithuanian open data dataset datasets/gov/pb/patentai (16 lentelių)."
tags: [gov, pb, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patentai

- **Namespace:** `datasets/gov/pb/patentai`[^manifest]
- **Manifest CSV:** [datasets/gov/pb/patentai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (`undeployed` — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `16` (16 lentelių)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Time](patentai/Time.md) | — | — | — | — | `2` | — |
| [BibliographicData](patentai/BibliographicData.md) | — | `3` | — | `open` | `2` | — |
| [PublicationReference](patentai/PublicationReference.md) | — | `4` | `doc_number` | `open` | `4` | — |
| [ClassificationICPR](patentai/ClassificationICPR.md) | — | `4` | `date` | `open` | `7` | — |
| [ApplicationReference](patentai/ApplicationReference.md) | — | `3` | `doc_number` | — | `3` | — |
| [Applicant](patentai/Applicant.md) | — | `3` | `sequence` | — | `3` | — |
| [AddressBook](patentai/AddressBook.md) | — | `3` | `orgname` | — | `2` | — |
| [ApplicantAddress](patentai/ApplicantAddress.md) | — | `3` | `country` | — | `2` | — |
| [ApplicantNationality](patentai/ApplicantNationality.md) | — | `3` | `country` | — | `2` | — |
| [ApplicantResidence](patentai/ApplicantResidence.md) | — | `3` | `country` | — | `2` | — |
| [Inventor](patentai/Inventor.md) | — | `3` | `sequence` | — | `1` | — |
| [InventorAddress](patentai/InventorAddress.md) | — | `3` | `country` | — | `2` | — |
| [InventorNationality](patentai/InventorNationality.md) | — | `3` | `country` | — | `2` | — |
| [InventorResidence](patentai/InventorResidence.md) | — | `3` | `country` | — | `2` | — |
| [Agent](patentai/Agent.md) | — | `3` | `sequence` | — | `2` | — |
| [AgentAddress](patentai/AgentAddress.md) | — | `3` | `country` | — | `2` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `ns` | `http://vpb.lt/open-data/schemas/trademark/v1` |
| `ns2` | `http://vpb.lt/open-data/schemas/address/v1` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L2)
