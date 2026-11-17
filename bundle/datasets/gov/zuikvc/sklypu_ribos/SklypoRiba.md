---
type: Table
title: "SklypoRiba — KŽS ribų pasikeitimų duomeys"
description: "Išankstinių kontrolinių žemės sklypų (KŽS) ribų pasikeitimų duomeys"
tags: [gov, zuikvc, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/sklypu_ribos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/sklypu_ribos.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# SklypoRiba — KŽS ribų pasikeitimų duomeys

Išankstinių kontrolinių žemės sklypų (KŽS) ribų pasikeitimų duomeys

- **Model:** `datasets/gov/zuikvc/sklypu_ribos/SklypoRiba`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/sklypu_ribos](../sklypu_ribos.md) (`datasets/gov/zuikvc/sklypu_ribos`)
- **Manifest CSV:** [datasets/gov/zuikvc/sklypu_ribos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/sklypu_ribos.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas` | `string` | — | `3` | `open` | — | KŽS ribų pasikeitimų aprašymas | — |
| `ivestas` | `datetime` | `S` | `4` | `open` | — | KŽS ribų pasikeitimų aprašymo data ir laikas | — |
| `koordinates` | `geometry(point,3346)` | — | `3` | `open` | — | KŽS ribų pasikeitimų orientacinė vieta WKT formatu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/sklypu_ribos.csv
