---
type: Table
title: "Position — Transporto priemonės pozicija"
description: "Spinta table datasets/gov/sumin/vintra/Position (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/sumin/vintra/Position"
tags: [gov, sumin, position, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sumin/vintra.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/sumin/vintra.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Position — Transporto priemonės pozicija

- **Model:** `datasets/gov/sumin/vintra/Position`[^manifest]
- **Dataset:** [datasets/gov/sumin/vintra](../vintra.md) (`datasets/gov/sumin/vintra`)[^manifest]
- **Manifest CSV:** [datasets/gov/sumin/vintra.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sumin/vintra.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sumin/vintra/Position` (`deployed`)[^manifest]
- **Provider:** `sumin` — Lietuvos Respublikos susisiekimo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vehicle` | `ref` | [Vehicle](Vehicle.md) (`level=4 UUID`: `vehicle._id`) | `4` | `open` | — | Transporto priemonė | — |
| `trip` | `ref` | [Trip](Trip.md) (`level=4 UUID`: `trip._id`) | `4` | `open` | — | Reisas | — |
| `position` | `geometry(point, 4326)` | — | `3` | `open` | — | Taškas žemėlapyje | — |
| `bearing` | `number` | `°` | `4` | `open` | — | Azimutas | — |
| `speed` | `number` | `m/s` | `4` | `open` | — | Judėjimo greitis | — |
| `delay` | `integer` | `s` | `4` | `open` | — | Transporto priemonės vėlavimas | — |
| `timestamp` | `datetime` | `S` | `4` | `open` | — | Pozicijos gavimo data ir laikas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/sumin/vintra.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sumin/vintra.csv#L19)
