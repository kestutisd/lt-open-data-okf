---
type: Table
title: "SutartiesSalysTbl"
description: "Spinta table datasets/gov/vpt/sutartys/SutartiesSalysTbl (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/sutartys/SutartiesSalysTbl"
tags: [gov, vpt, sutartiessalystbl, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/vpt/sutartys.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# SutartiesSalysTbl

- **Model:** `datasets/gov/vpt/sutartys/SutartiesSalysTbl`[^manifest]
- **Dataset:** [Pirkimų sutarčių duomenys](../sutartys.md) (`datasets/gov/vpt/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/sutartys.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/sutartys/SutartiesSalysTbl` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suts_sut_id` | `integer` | — | `4` | `open` | — | — | — |
| `suts_eil_nr` | `integer` | — | `4` | `open` | — | — | — |
| `suts_pasirase_data` | `datetime` | — | `3` | `open` | — | — | — |
| `suts_pastabos` | `string` | — | `3` | `open` | — | — | — |
| `suts_patikslinimas` | `string` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/sutartys.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L33)
