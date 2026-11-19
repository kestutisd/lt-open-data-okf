---
type: Table
title: "EdukacijosDalyvis"
description: "Spinta table datasets/gov/lnb/kulturos_pasas/EdukacijosDalyvis (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas/EdukacijosDalyvis"
tags: [gov, lnb, edukacijosdalyvis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2659/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/kulturos_pasas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# EdukacijosDalyvis

- **Model:** `datasets/gov/lnb/kulturos_pasas/EdukacijosDalyvis`[^manifest]
- **Dataset:** [KEIS Kultūros paso edukacijos](../kulturos_pasas.md) (`datasets/gov/lnb/kulturos_pasas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/kulturos_pasas.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/kulturos_pasas/EdukacijosDalyvis` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `uzsakymo_id` | `string` | — | `4` | `open` | — | Užsakymo unikalus identitfikatorius | — |
| `dalyvio_id` | `string` | — | `4` | `open` | — | Užsakymo unikalus identitfikatorius | — |
| `dalyvio_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Dalyvio gimimo metai | — |
| `dalyvio_tipas` | `string` | — | `4` | `open` | — | Tipas | — |
| `dalyvio_institucijos_kodas` | `string` | — | `4` | `open` | — | Institucijos unikalus identifikatorius | — |
| `dalyvio_institucija` | `string` | — | `4` | `open` | — | Institucija | — |
| `dalyvio_savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/kulturos_pasas.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/kulturos_pasas.csv#L33)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/kulturos_pasas (https://data.gov.lt/datasets/2659/)
