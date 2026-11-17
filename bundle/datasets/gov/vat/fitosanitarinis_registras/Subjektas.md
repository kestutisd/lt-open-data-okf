---
type: Table
title: "Subjektas — Pateikiama informacija apie ūkio subjektus, įregistruotus Fitosanitariniame registe (ūkio subjekto atpažinties kodas; pavadinimas; veiklos vykdymo adresas; veiklos ir produkcijos rūšis)"
description: "Spinta table datasets/gov/vat/fitosanitarinis_registras/Subjektas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarinis_registras/Subjektas"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/r2_fitosanitarinis_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Subjektas — Pateikiama informacija apie ūkio subjektus, įregistruotus Fitosanitariniame registe (ūkio subjekto atpažinties kodas; pavadinimas; veiklos vykdymo adresas; veiklos ir produkcijos rūšis)

- **Model:** `datasets/gov/vat/fitosanitarinis_registras/Subjektas`[^manifest]
- **Dataset:** [datasets/gov/vat/fitosanitarinis_registras](../fitosanitarinis_registras.md) (`datasets/gov/vat/fitosanitarinis_registras`)
- **Manifest CSV:** [datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarinis_registras/Subjektas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `subjektas` | `string` | — | `2` | `open` | — | Subjekto pavadinimas | — |
| `juridinis` | `boolean` | — | `4` | `open` | — | Ūkio subjekto tipas | — |
| `tel_nr` | `string` | — | `1` | `open` | — | Telefono numeris | — |
| `adresas` | `string` | — | `2` | `open` | — | Ūkio subjekto adresas | — |
| `fitosanitarinis_nr` | `string` | — | `1` | `open` | — | Fitosanitarinio registro Nr. | — |
| `specializacija` | `string` | — | `2` | `open` | — | Subjekto specializacija | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Ūkio subjekto koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `specializacija` | `"update(property: ""specializacija[]"", type: ""array"", source: ""Specializacija"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r2_fitosanitarinis_registras.csv
