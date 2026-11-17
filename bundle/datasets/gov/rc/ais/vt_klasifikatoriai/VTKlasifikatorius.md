---
type: Table
title: "VTKlasifikatorius — AIS antstolių ir jų veiklos teritorijų klasifikatorius"
description: "Spinta table datasets/gov/rc/ais/vt_klasifikatoriai/VTKlasifikatorius (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ais/vt_klasifikatoriai/VTKlasifikatorius"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ais/vt_klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# VTKlasifikatorius — AIS antstolių ir jų veiklos teritorijų klasifikatorius

- **Model:** `datasets/gov/rc/ais/vt_klasifikatoriai/VTKlasifikatorius`[^manifest]
- **Dataset:** [AIS antstolių ir jų veiklos teritorijų klasifikatorius](../vt_klasifikatoriai.md) (`datasets/gov/rc/ais/vt_klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ais/vt_klasifikatoriai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ais/vt_klasifikatoriai/VTKlasifikatorius`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `ant_indeksas` | `string` | — | `4` | `open` | — | Antstolio indeksas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje dirba antstolis, kodas iš Adresų registro | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ais/vt_klasifikatoriai.csv
