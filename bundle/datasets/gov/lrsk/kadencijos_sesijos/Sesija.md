---
type: Table
title: "Sesija — Lietuvos Respublikos Seimo sesijų tvarkaraštis"
description: "Lietuvos Respublikos Seimo sesijų tvarkaraštis."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/Sesija"
tags: [gov, lrsk, sesija, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2610/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/kadencijos_sesijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sesija — Lietuvos Respublikos Seimo sesijų tvarkaraštis

Lietuvos Respublikos Seimo sesijų tvarkaraštis. Pateikiama eilinių ir neeilinių sesijų pradžia ir pabaiga bei kadencijos, kuriai priklauso sesija, id.[^manifest]

- **Model:** `datasets/gov/lrsk/kadencijos_sesijos/Sesija`[^manifest]
- **Dataset:** [Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius](../kadencijos_sesijos.md) (`datasets/gov/lrsk/kadencijos_sesijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/kadencijos_sesijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/Sesija` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Sesijos identifikacinis numeris | — |
| `sesija` | `string` | — | `4` | `open` | — | Sesijos pavadinimas | — |
| `sutrump_pav` | `string` | — | `4` | `open` | — | Sutrumpintas sesijos pavadinimas | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Sesijos pradžios data | — |
| `iki` | `date` | `D` | `4` | `open` | — | Sesijos pabaigos data | — |
| `ses_pozm` | `string` | — | `4` | `open` | — | Sesijos požymis: eilinė arba neeilinė | — |
| `kadencija` | `string` | — | `4` | `open` | — | Kadencijos numeris | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ses_pozm` | `"eilinė"` | — | — | — | — |
| `ses_pozm` | `"neeilinė"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/kadencijos_sesijos (https://data.gov.lt/datasets/2610/)
