---
type: Table
title: "Gimimas — Duomenys apie gimdymus Lietuvoje."
description: "Duomenų rinkinyje pateikiama informacija apie gimdymus Lietuvoje nuo 2021m."
resource: "https://get.data.gov.lt/datasets/gov/hi/gimdymai/Gimimas"
tags: [gov, hi, gimimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gimdymai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/hi/gimdymai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2732/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/gimdymai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Gimimas — Duomenys apie gimdymus Lietuvoje.

**Dataset Context:** Duomenų rinkinyje pateikiama informacija apie gimdymus Lietuvoje nuo 2021m. Rinkinio objektas - vienavaisis arba daugiavaisis gimdymas. Duomenys surinkti iš statistinių formų Nėščiosios ir negyvagimio kortelė Nr.2016-10-07_Nr_V-1149_forma+010-2-1a ir Nėščiosios ir negyvagimio kortelė Nr.2016-10-07_Nr_V-1149_forma+010-1-1a. Pateikiama informacija apie gimdymo datą, gimdyvės kilmės rajoną, gimdymo vietą, bendrą vaisių skaičių gimdymo metu bei gimdyvės RhD antigeną. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/hi/gimdymai/Gimimas`[^manifest]
- **Dataset:** [Duomenys apie gimdymus Lietuvoje.](../gimdymai.md) (`datasets/gov/hi/gimdymai`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/gimdymai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gimdymai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/gimdymai/Gimimas` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `gimdymo_data` | `datetime` | `L` | `4` | `open` | — | Gimdymo laiko žyma | — |
| `rajonas` | `string` | — | `4` | `open` | — | Nėščiosios (Motinos) gyvenamosios vietos rajonas | — |
| `gimdymo_vieta` | `string` | — | `4` | `open` | — | Gimdymo vieta | — |
| `viso_vaisiu` | `integer` | `U` | `4` | `open` | — | Vaisių skaičius gimdyme iš viso | — |
| `mot_rhd` | `string` | — | `4` | `open` | — | Nėščiosios (motinos) RhD antigenas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gimdymo_vieta` | `"Stacionare"` | — | — | — | — |
| `gimdymo_vieta` | `"Namuose"` | — | — | — | — |
| `gimdymo_vieta` | `"GMP"` | — | — | — | — |
| `gimdymo_vieta` | `"Kitur"` | — | — | — | — |
| `mot_rhd` | `"+"` | — | — | — | Teigiamas |
| `mot_rhd` | `"-"` | — | — | — | Neigiamas |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/gimdymai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/gimdymai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/gimdymai (https://data.gov.lt/datasets/2732/)
