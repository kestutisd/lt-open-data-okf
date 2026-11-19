---
type: Table
title: "Atgn1ContractList — AtGn-1 IX. SUTARTYS"
description: "Spinta table datasets/gov/vpt/new/Atgn1ContractList (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atgn1ContractList"
tags: [gov, vpt, atgn1contractlist, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L84"
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv#L84"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/389/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/new"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Atgn1ContractList — AtGn-1 IX. SUTARTYS

- **Model:** `datasets/gov/vpt/new/Atgn1ContractList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L84](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L84)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atgn1ContractList` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atgn1` | `ref` | [Atgn1](Atgn1.md) (`level=4 UUID`: `atgn1._id`) | `4` | `open` | — | — | — |
| `part_number` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_code` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_name` | `string` | — | `3` | `open` | — | — | — |
| `conclusion_date` | `datetime` | — | `3` | `open` | — | — | — |
| `expiry_date` | `datetime` | — | `3` | `open` | — | — | — |
| `total_value_of_part` | `number` | — | `3` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `will_subcontract_be_concluded` | `string` | — | `3` | `open` | — | — | — |
| `value_in_eur` | `number` | — | `3` | `open` | — | — | — |
| `percentage` | `number` | — | `3` | `open` | — | — | — |
| `is_un_known` | `integer` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv#L84 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L84)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/new (https://data.gov.lt/datasets/389/)
