---
type: Table
title: "Vehicle — Transporto priemonė"
description: "Spinta table datasets/gov/sumin/vintra/Vehicle (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sumin/vintra/Vehicle"
tags: [gov, sumin, vehicle, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sumin/vintra.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/sumin/vintra.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vehicle — Transporto priemonė

- **Model:** `datasets/gov/sumin/vintra/Vehicle`[^manifest]
- **Dataset:** [datasets/gov/sumin/vintra](../vintra.md) (`datasets/gov/sumin/vintra`)[^manifest]
- **Manifest CSV:** [datasets/gov/sumin/vintra.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sumin/vintra.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sumin/vintra/Vehicle` (`deployed`)[^manifest]
- **Provider:** `sumin` — Lietuvos Respublikos susisiekimo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agency` | `ref` | [Agency](Agency.md) (`level=4 UUID`: `agency._id`) | `4` | `open` | — | Paslaugų teikėjas | — |
| `vehicle_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `plate_number` | `string` | — | `4` | `open` | — | Registracijos numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sumin/vintra.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sumin/vintra.csv#L8)
