---
type: Table
title: "ValstybinisNumeris — Tranporto priemonių valstybiniai numeriai pagal markę ir modelį"
description: "AB „Regitra“ Kelių transporto priemonių registre kaupiami motorinių transporto priemonių, išskyrus nurodytų Lietuvos Respublikos saugaus eismo automobilių keliais įstatymo 27 straipsnio 7 dalyje, ir jų priekabų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/regitra/ktpr/ValstybinisNumeris"
tags: [gov, regitra, valstybinisnumeris, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpr.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/regitra/ktpr.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2749/"
    title: "data.gov.lt DCAT-AP — datasets/gov/regitra/ktpr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ValstybinisNumeris — Tranporto priemonių valstybiniai numeriai pagal markę ir modelį

AB „Regitra“ Kelių transporto priemonių registre kaupiami motorinių transporto priemonių, išskyrus nurodytų Lietuvos Respublikos saugaus eismo automobilių keliais įstatymo 27 straipsnio 7 dalyje, ir jų priekabų duomenys. Rinkinio prototipo duomenys kaupiami nuo 2005 m. ir yra atnaujinami kasdien. Duomenų rinkinį sudaro automobilio markė, modelis ir valstybinių numerių žymėjimas, raides pakeitus į „X“, o skaitmenis – „0“.[^manifest]

- **Model:** `datasets/gov/regitra/ktpr/ValstybinisNumeris`[^manifest]
- **Dataset:** [Tranporto priemonių valstybiniai numeriai pagal markę ir modelį](../ktpr.md) (`datasets/gov/regitra/ktpr`)[^manifest]
- **Manifest CSV:** [datasets/gov/regitra/ktpr.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpr.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/regitra/ktpr/ValstybinisNumeris` (`deployed`)[^manifest]
- **Provider:** `regitra` — AB „Regitra“ *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `valst_nr_zym` | `string` | — | `4` | `open` | — | Valstybinio numerio žymėjimas nurodant raidžių ir skaitmenų pozicijas | — |
| `marke` | `string` | — | `4` | `open` | — | Transporto priemonės markė | — |
| `modelis` | `string` | — | `4` | `open` | — | Transporto priemonės modelis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/ktpr.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/ktpr.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/regitra/ktpr (https://data.gov.lt/datasets/2749/)
