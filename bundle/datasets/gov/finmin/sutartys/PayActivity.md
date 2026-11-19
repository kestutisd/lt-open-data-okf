---
type: Table
title: "PayActivity — Projekto mokėjimo prašymo dalies Nr. 1 veiklos"
description: "Spinta table datasets/gov/finmin/sutartys/PayActivity (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayActivity"
tags: [gov, finmin, payactivity, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L238"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L238"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PayActivity — Projekto mokėjimo prašymo dalies Nr. 1 veiklos

- **Model:** `datasets/gov/finmin/sutartys/PayActivity`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L238](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L238)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayActivity` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `pay_activity_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_activity_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies veiklos identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) (`level=4 UUID`: `payment._id`) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | MPD1 veiklos numeris | — |
| `from` | `date` | `M` | `4` | `open` | — | Faktinio veiklos vykdymo laikotarpio pradžia (metai ir mėnuo) | — |
| `till` | `date` | `M` | `4` | `open` | — | Faktinio veiklos vykdymo laikotarpio pabaiga (metai ir mėnuo) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L238 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L238)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
