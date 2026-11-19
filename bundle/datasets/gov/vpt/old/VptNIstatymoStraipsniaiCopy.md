---
type: Table
title: "VptNIstatymoStraipsniaiCopy"
description: "Spinta table datasets/gov/vpt/old/VptNIstatymoStraipsniaiCopy (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/old/VptNIstatymoStraipsniaiCopy"
tags: [gov, vpt, vptnistatymostraipsniaicopy, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L111"
    title: "atviriduomenys/manifest — datasets/gov/vpt/old.csv#L111"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/390/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/old"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VptNIstatymoStraipsniaiCopy

- **Model:** `datasets/gov/vpt/old/VptNIstatymoStraipsniaiCopy`[^manifest]
- **Dataset:** [Pirkimų, vykdytų iki 2017-07-01 duomenys ir sutarčių duomenys](../old.md) (`datasets/gov/vpt/old`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/old.csv#L111](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L111)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/old/VptNIstatymoStraipsniaiCopy` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `str_id` | `integer` | — | `3` | `open` | — | — | — |
| `str_forma` | `integer` | — | `3` | `open` | — | — | — |
| `str_pirkb_id` | `integer` | — | `3` | `open` | — | — | — |
| `str_pobj_rusis` | `integer` | — | `3` | `open` | — | — | — |
| `str_kodas` | `integer` | — | `3` | `open` | — | — | — |
| `str_pav` | `string` | — | `3` | `open` | — | — | — |
| `str_galiojimo_data_iki` | `datetime` | — | `3` | `open` | — | — | — |
| `str_formos_dalis` | `integer` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/old.csv#L111 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L111)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/old (https://data.gov.lt/datasets/390/)
