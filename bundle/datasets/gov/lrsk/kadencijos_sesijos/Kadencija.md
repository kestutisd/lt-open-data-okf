---
type: Table
title: "Kadencija — Lietuvos Respublikos Seimo kadencijų tvarkaraštis"
description: "Lietuvos Respublikos Seimo kadencijų tvarkaraštis su kadencijų pradžios ir pabaigos datomis."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/Kadencija"
tags: [gov, lrsk, kadencija, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2610/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/kadencijos_sesijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kadencija — Lietuvos Respublikos Seimo kadencijų tvarkaraštis

Lietuvos Respublikos Seimo kadencijų tvarkaraštis su kadencijų pradžios ir pabaigos datomis.[^manifest]

- **Model:** `datasets/gov/lrsk/kadencijos_sesijos/Kadencija`[^manifest]
- **Dataset:** [Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius](../kadencijos_sesijos.md) (`datasets/gov/lrsk/kadencijos_sesijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/kadencijos_sesijos.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/Kadencija` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Kadencijos id numeris | — |
| `nuo` | `date` | `D` | `4` | `open` | — | kadencijos pradžios data | — |
| `iki` | `date` | `D` | `4` | `open` | — | kadencijos pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L17)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/kadencijos_sesijos (https://data.gov.lt/datasets/2610/)
