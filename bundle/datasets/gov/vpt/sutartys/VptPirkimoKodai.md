---
type: Table
title: "VptPirkimoKodai"
description: "Spinta table datasets/gov/vpt/sutartys/VptPirkimoKodai (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/sutartys/VptPirkimoKodai"
tags: [gov, vpt, vptpirkimokodai, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L60"
    title: "atviriduomenys/manifest — datasets/gov/vpt/sutartys.csv#L60"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# VptPirkimoKodai

- **Model:** `datasets/gov/vpt/sutartys/VptPirkimoKodai`[^manifest]
- **Dataset:** [Pirkimų sutarčių duomenys](../sutartys.md) (`datasets/gov/vpt/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/sutartys.csv#L60](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L60)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/sutartys/VptPirkimoKodai` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pk_obj_id` | `integer` | — | `4` | `open` | — | — | — |
| `pk_pirkimo_kodas` | `integer` | — | `3` | `open` | — | — | — |
| `pk_reg_data` | `datetime` | — | `3` | `open` | — | — | — |
| `pk_po_sbj_id` | `integer` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/sutartys.csv#L60 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L60)
