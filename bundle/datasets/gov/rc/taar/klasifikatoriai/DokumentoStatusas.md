---
type: Table
title: "DokumentoStatusas — Turto arešto aktų registro dokumentų statusų klasifikatorius"
description: "Spinta table datasets/gov/rc/taar/klasifikatoriai/DokumentoStatusas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai/DokumentoStatusas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L12"
    last_modified: "2026-11-11T14:39:20Z"
---

# DokumentoStatusas — Turto arešto aktų registro dokumentų statusų klasifikatorius

- **Model:** `datasets/gov/rc/taar/klasifikatoriai/DokumentoStatusas`[^manifest]
- **Dataset:** [TAAR klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/taar/klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/rc/taar/klasifikatoriai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L12)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai/DokumentoStatusas`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Turto arešto akto statuso kodas | — |
| `statusas` | `string` | — | `3` | `open` | — | Turto arešto akto statuso pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/klasifikatoriai.csv
