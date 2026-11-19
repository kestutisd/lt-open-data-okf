---
type: Table
title: "VptNCpvKoduTipaiMain"
description: "Spinta table datasets/gov/vpt/old/VptNCpvKoduTipaiMain (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/old/VptNCpvKoduTipaiMain"
tags: [gov, vpt, vptncpvkodutipaimain, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L83"
    title: "atviriduomenys/manifest — datasets/gov/vpt/old.csv#L83"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/390/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/old"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VptNCpvKoduTipaiMain

- **Model:** `datasets/gov/vpt/old/VptNCpvKoduTipaiMain`[^manifest]
- **Dataset:** [Pirkimų, vykdytų iki 2017-07-01 duomenys ir sutarčių duomenys](../old.md) (`datasets/gov/vpt/old`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/old.csv#L83](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L83)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/old/VptNCpvKoduTipaiMain` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/old.csv#L83 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L83)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/old (https://data.gov.lt/datasets/390/)
