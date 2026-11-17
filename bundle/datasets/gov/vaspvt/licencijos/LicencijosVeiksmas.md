---
type: Table
title: "LicencijosVeiksmas — Atlikti veiksmai su licencija"
description: "Spinta table datasets/gov/vaspvt/licencijos/LicencijosVeiksmas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/LicencijosVeiksmas"
tags: [gov, vaspvt, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# LicencijosVeiksmas — Atlikti veiksmai su licencija

- **Model:** `datasets/gov/vaspvt/licencijos/LicencijosVeiksmas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/LicencijosVeiksmas`
- **Primary Key (`ref`):** `id`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Atlikto veiksmo identifikatorius | — |
| `veiksmas` | `string` | — | `2` | `open` | — | Atlikto veiksmo pavadiniams | — |
| `isakymas` | `string` | — | `4` | `open` | — | Įsakymo identifikatorius | — |
| `licencijos_id` | `string` | — | `2` | `open` | — | Licencijos identifikatorius | — |
| `data` | `datetime` | — | `2` | `open` | — | Atlikto veiksmo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "id")` | `ref` | `4` | `open` | — | — | — |
| `veiksmas` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |
| `licencijos_id` | `update(property: "licencija", type: "ref", ref: "Licencija")` | `type` | `4` | `open` | — | — | — |
| `data` | `update(property: "atlikta")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
