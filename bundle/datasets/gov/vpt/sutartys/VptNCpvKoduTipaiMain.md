---
type: Table
title: "VptNCpvKoduTipaiMain"
description: "Spinta table datasets/gov/vpt/sutartys/VptNCpvKoduTipaiMain (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/sutartys/VptNCpvKoduTipaiMain"
tags: [gov, vpt, vptncpvkodutipaimain, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L48"
    title: "atviriduomenys/manifest — datasets/gov/vpt/sutartys.csv#L48"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# VptNCpvKoduTipaiMain

- **Model:** `datasets/gov/vpt/sutartys/VptNCpvKoduTipaiMain`[^manifest]
- **Dataset:** [Pirkimų sutarčių duomenys](../sutartys.md) (`datasets/gov/vpt/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/sutartys.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L48)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/sutartys/VptNCpvKoduTipaiMain` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mcpv_kodas` | `string` | — | `3` | `open` | — | — | — |
| `mcpv_pav` | `string` | — | `3` | `open` | — | — | — |
| `pirk_obj_objt_id` | `integer` | — | `3` | `open` | — | — | — |
| `kategorija` | `integer` | — | `3` | `open` | — | — | — |
| `mcpv_versija` | `integer` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.
- [BVPŽ / CPV Procurement Vocabulary (Reg. (EC) No 213/2008)](../../../../references/cpv-bvpz-kodai.md) — 45 2-digit CPV divisions (`03`–`98`) and 272 3-digit groups.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/sutartys.csv#L48 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/sutartys.csv#L48)
