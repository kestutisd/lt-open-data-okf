---
type: Table
title: "Punktas — Pasienio kontrolės punktų fitosanitarijos postų (skyrių) duomenys"
description: "Spinta table datasets/gov/vat/fitosanitarijos_postai/Punktas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_postai/Punktas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/fitosanitarijos_postai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_postai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Punktas — Pasienio kontrolės punktų fitosanitarijos postų (skyrių) duomenys

- **Model:** `datasets/gov/vat/fitosanitarijos_postai/Punktas`[^manifest]
- **Dataset:** [datasets/gov/vat/fitosanitarijos_postai](../fitosanitarijos_postai.md) (`datasets/gov/vat/fitosanitarijos_postai`)
- **Manifest CSV:** [datasets/gov/vat/fitosanitarijos_postai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_postai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_postai/Punktas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `padalinys` | `string` | — | `4` | `open` | — | Padalinio pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Padalinio adresas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Padalinio vietos koordinatės (LKS - 3346) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `padalinys` | `"Klaipėdos jūrų uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Medininkų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Šalčininkų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Kybartų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Kauno oro uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/fitosanitarijos_postai.csv
