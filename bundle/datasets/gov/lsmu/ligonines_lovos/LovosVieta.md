---
type: Table
title: "LovosVieta — Lovų vietų duomenys"
description: "Spinta table datasets/gov/lsmu/ligonines_lovos/LovosVieta (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos/LovosVieta"
tags: [gov, lsmu, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# LovosVieta — Lovų vietų duomenys

- **Model:** `datasets/gov/lsmu/ligonines_lovos/LovosVieta`[^manifest]
- **Dataset:** [Lietuvos sveikatos universiteto Kauno klinikų Lovų duomenys](../ligonines_lovos.md) (`datasets/gov/lsmu/ligonines_lovos`)
- **Manifest CSV:** [datasets/gov/lsmu/ligonines_lovos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos/LovosVieta`
- **Primary Key (`ref`):** `vietos_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vietos_id` | `string` | — | `4` | `open` | — | Unikalus vietos eilutės identifikatorius | — |
| `vietos_tevinis_id` | `string` | — | `4` | `open` | — | Vietos tėvinis id (referuoja į vietos_id) | — |
| `vietos_kodas` | `string` | — | `4` | `open` | — | Vietai suteiktas kodas (trumpinys) | — |
| `vietos_lygmuo` | `string` | — | `4` | `open` | — | Lygmuo apibūdinantis vietą (kambarys, palata, aukštas ...) | — |
| `vietos_tipas` | `string` | — | `4` | `open` | — | Vietos tipas (papildoma informacija vietai apibūdinti) | — |
| `vietos_aprasymas` | `string` | — | `4` | `open` | — | Pilnas vietos aprašymas | — |
| `jar_validacija` | `string` | — | `4` | `open` | — | Juridinio asmens kodo validacijos stulpelis | — |
| `aspi_jar_kodas` | `string` | — | `4` | `open` | — | Ambulatorines asmens sveikatos priežiūros įstaigos juridinio asmens kodas | — |
| `aspi_pavadinimas` | `string` | — | `4` | `open` | — | Ambulatorines asmens sveikatos priežiūros pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `jar_validacija` | `"9 sktm. JAR"` | — | — | 9 skaitmenų validus juridinio asmens kodas | — |
| `jar_validacija` | `"7 sktm. JAR"` | — | — | 7 skaitmenų validus juridinio asmens kodas | — |
| `jar_validacija` | `"Ne JAR"` | — | — | Nevalidus juridinio asmens kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv
