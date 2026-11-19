---
type: Table
title: "Atn2EndOfDesignContestProcedureList"
description: "Spinta table datasets/gov/vpt/new/Atn2EndOfDesignContestProcedureList (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atn2EndOfDesignContestProcedureList"
tags: [gov, vpt, atn2endofdesigncontestprocedurelist, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L1012"
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv#L1012"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/389/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpt/new"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Atn2EndOfDesignContestProcedureList

- **Model:** `datasets/gov/vpt/new/Atn2EndOfDesignContestProcedureList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L1012](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L1012)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atn2EndOfDesignContestProcedureList` (`deployed`)[^manifest]
- **Provider:** `vpt` — Viešųjų pirkimų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atn2` | `ref` | [Atn2](Atn2.md) (`level=4 UUID`: `atn2._id`) | `4` | `open` | — | — | — |
| `part_number_of_object` | `string` | — | `3` | `open` | — | — | — |
| `compliance_obligation_imposed_by_public_procurement` | `string` | — | `3` | `open` | — | — | — |
| `compliance_court_decision` | `string` | — | `3` | `open` | — | — | — |
| `other_reasons` | `string` | — | `3` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

# Related References

- [VPT Public Procurement Notices Join Reference](../../../../references/joins/vpt-procurement-notices.md) — Notice parent-child UUID joins, CPV normalization, and buyer/supplier JAR links.

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv#L1012 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L1012)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpt/new (https://data.gov.lt/datasets/389/)
