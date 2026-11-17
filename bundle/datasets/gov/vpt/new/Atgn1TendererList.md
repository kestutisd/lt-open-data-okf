---
type: Table
title: "Atgn1TendererList — AtGn-1 V.1 Dalyviai, kandidatai"
description: "Spinta table datasets/gov/vpt/new/Atgn1TendererList (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atgn1TendererList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L221"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atgn1TendererList — AtGn-1 V.1 Dalyviai, kandidatai

- **Model:** `datasets/gov/vpt/new/Atgn1TendererList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L221](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L221)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atgn1TendererList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atgn1` | `ref` | [Atgn1](Atgn1.md) | `4` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `is_tender_private_person` | `integer` | — | `3` | `open` | — | — | — |
| `code` | `string` | — | `3` | `open` | — | — | — |
| `name` | `string` | — | `3` | `open` | — | — | — |
| `selected_tenderer` | `string` | — | `3` | `open` | — | — | — |
| `name_adjustment` | `string` | — | `3` | `open` | — | — | — |
| `group_name` | `string` | — | `3` | `open` | — | — | — |
| `address` | `string` | — | `3` | `open` | — | — | — |
| `country` | `string` | — | `3` | `open` | — | — | — |
| `is_price` | `integer` | — | `3` | `open` | — | — | — |
| `price_cost_tender` | `number` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv
