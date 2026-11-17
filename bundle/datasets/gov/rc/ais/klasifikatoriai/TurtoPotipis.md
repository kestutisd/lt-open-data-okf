---
type: Table
title: "TurtoPotipis — AIS parduodamo turto potipių klasifikatorius"
description: "Spinta table datasets/gov/rc/ais/klasifikatoriai/TurtoPotipis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai/TurtoPotipis"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# TurtoPotipis — AIS parduodamo turto potipių klasifikatorius

- **Model:** `datasets/gov/rc/ais/klasifikatoriai/TurtoPotipis`[^manifest]
- **Dataset:** [AIS tipų ir potipių klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/ais/klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/rc/ais/klasifikatoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/klasifikatoriai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/klasifikatoriai/TurtoPotipis`
- **Primary Key (`ref`):** `kodas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Turto potipio kodas | — |
| `turto_tipas` | `ref` | [TurtoTipas](TurtoTipas.md) | `4` | `open` | — | Turto tipo kodas iš turto tipų klasifikatoriaus | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Turto potipio pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/klasifikatoriai.csv
