---
type: Table
title: "VptNVppaStraipsniai"
description: "Spinta table datasets/gov/vpt/old/VptNVppaStraipsniai (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/old/VptNVppaStraipsniai"
tags: [gov, vpt, vptnvppastraipsniai, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L220"
    title: "atviriduomenys/manifest — datasets/gov/vpt/old.csv#L220"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/390/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/old"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VptNVppaStraipsniai

- **Model:** `datasets/gov/vpt/old/VptNVppaStraipsniai`[^manifest]
- **Dataset:** [Pirkimų, vykdytų iki 2017-07-01 duomenys ir sutarčių duomenys](../old.md) (`datasets/gov/vpt/old`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/old.csv#L220](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L220)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/old/VptNVppaStraipsniai` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `str_dok_id` | `integer` | — | `4` | `open` | — | — | — |
| `str_eil_nr` | `integer` | — | `4` | `open` | — | — | — |
| `str_id` | `integer` | — | `3` | `open` | — | — | — |
| `str_pastabos` | `string` | — | `3` | `open` | — | — | — |
| `str_reg_data` | `datetime` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/old.csv#L220 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/old.csv#L220)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/old (https://data.gov.lt/datasets/390/)
