---
type: Table
title: "Aprupinimas — Duomenys apie paramą mokiniams"
description: "Socialinės Apsaugos ir Darbo Ministerijos duomenys apie mokiniams suteiktą socialinę paramą savivaldybėse (nemokamas maitinimas ir parama mokinio reikmenims įsigyti)."
resource: "https://get.data.gov.lt/datasets/gov/sadm/parama_mokiniams/Aprupinimas"
tags: [gov, sadm, aprupinimas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/parama_mokiniams.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/sadm/parama_mokiniams.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1997/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sadm/parama_mokiniams"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Aprupinimas — Duomenys apie paramą mokiniams

**Dataset Context:** Socialinės Apsaugos ir Darbo Ministerijos duomenys apie mokiniams suteiktą socialinę paramą savivaldybėse (nemokamas maitinimas ir parama mokinio reikmenims įsigyti). Duomenys atnaujinami kas ketvirtį.[^manifest]

- **Model:** `datasets/gov/sadm/parama_mokiniams/Aprupinimas`[^manifest]
- **Dataset:** [Mokiniams suteiktos socialinės paramos duomenys](../parama_mokiniams.md) (`datasets/gov/sadm/parama_mokiniams`)[^manifest]
- **Manifest CSV:** [datasets/gov/sadm/parama_mokiniams.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/parama_mokiniams.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sadm/parama_mokiniams/Aprupinimas` (`deployed`)[^manifest]
- **Provider:** `sadm` — Lietuvos Respublikos socialinės apsaugos ir darbo ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė, kurioje suteikta parama | — |
| `paslauga` | `string` | — | `3` | `open` | — | Suteiktos socialinės paslaugos tipas | — |
| `parama` | `string` | — | `3` | `open` | — | Suteiktos paramos kategorija | — |
| `menuo` | `date` | `D` | `4` | `open` | — | Suteiktos paslaugos menuo | — |
| `suma` | `number` | — | `2` | `open` | — | Suteiktos paramos suma | Eurais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sadm/parama_mokiniams.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sadm/parama_mokiniams.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sadm/parama_mokiniams (https://data.gov.lt/datasets/1997/)
