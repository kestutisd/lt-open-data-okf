---
type: Table
title: "AddressBook"
description: "Spinta table datasets/gov/pb/patentai/AddressBook (2 columns)."
tags: [gov, pb, addressbook, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L36"
    title: "atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L36"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# AddressBook

- **Model:** `datasets/gov/pb/patentai/AddressBook`[^manifest]
- **Dataset:** [Patentai](../patentai.md) (`datasets/gov/pb/patentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/patentai.csv#L36](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L36)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `orgname`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `applicant` | `ref` | [Applicant](Applicant.md) (`level=4 UUID`: `applicant._id`) | `4` | `open` | — | — | — |
| `orgname` | `string` | — | `3` | `open` | — | Pareiškėjo vardas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L36 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L36)
