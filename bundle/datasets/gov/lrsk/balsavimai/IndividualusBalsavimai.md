---
type: Table
title: "IndividualusBalsavimai — Individualūs balsavimai"
description: "Spinta table datasets/gov/lrsk/balsavimai/IndividualusBalsavimai (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/balsavimai/IndividualusBalsavimai"
tags: [gov, lrsk, individualusbalsavimai, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L23"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/balsavimai.csv#L23"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/6101/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/balsavimai"
    author: "team:vda"
    last_modified: "2026-10-27T00:00:00Z"
---

# IndividualusBalsavimai — Individualūs balsavimai

- **Model:** `datasets/gov/lrsk/balsavimai/IndividualusBalsavimai`[^manifest]
- **Dataset:** [Balsavimai](../balsavimai.md) (`datasets/gov/lrsk/balsavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/balsavimai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L23)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/balsavimai/IndividualusBalsavimai` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `rezultato_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-27`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/balsavimai.csv#L23 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/balsavimai.csv#L23)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/balsavimai (https://data.gov.lt/datasets/6101/)
