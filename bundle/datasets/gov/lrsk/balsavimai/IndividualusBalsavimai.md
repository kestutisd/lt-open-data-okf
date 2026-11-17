---
type: Table
title: "IndividualusBalsavimai — Individualūs balsavimai"
description: "Spinta table datasets/gov/lrsk/balsavimai/IndividualusBalsavimai (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/balsavimai/IndividualusBalsavimai"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/balsavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L23"
    last_modified: "2026-11-11T14:39:20Z"
---

# IndividualusBalsavimai — Individualūs balsavimai

- **Model:** `datasets/gov/lrsk/balsavimai/IndividualusBalsavimai`[^manifest]
- **Dataset:** [Balsavimai](../balsavimai.md) (`datasets/gov/lrsk/balsavimai`)
- **Manifest CSV:** [datasets/gov/lrsk/balsavimai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L23)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/balsavimai/IndividualusBalsavimai`
- **Primary Key (`ref`):** `rezultato_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rezultato_id` | `string` | — | `4` | `open` | — | Rezultato identifikatorius | — |
| `kadencijos_id` | `string` | — | `4` | `open` | — | Kadencijos identifikatorius | — |
| `balsavimo_id` | `string` | — | `4` | `open` | — | Balsavimo identifikatorius | — |
| `seimo_nario_id` | `string` | — | `4` | `open` | — | Seimo nario identifikatorius | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Asmens identifikatorius | — |
| `seimo_narys` | `string` | — | `4` | `open` | — | Seimo narys | — |
| `rezultatas` | `string` | — | `4` | `open` | — | Balsavimo rezultatas | — |
| `iraso_laikas` | `datetime` | `S` | `4` | `open` | — | Įrašo data ir laikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/balsavimai.csv
