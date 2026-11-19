---
type: Table
title: "HemosporidinisParazitas — Informacija apie paukščių hemosporidinius parazitus"
description: "Informacija apie P.B. Šivickio Gamtos Tyrimų Centro mokslinių darbuotojų ištirtus ir aprašytus paukščių hemosporidinius parazitus išplitusius po visą pasaulį."
resource: "https://get.data.gov.lt/datasets/gov/gtc/hemosporidiniai_parazitai/HemosporidinisParazitas"
tags: [gov, gtc, hemosporidinisparazitas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/hemosporidiniai_parazitai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/gtc/hemosporidiniai_parazitai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2634/"
    title: "data.gov.lt DCAT-AP — datasets/gov/gtc/hemosporidiniai_parazitai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# HemosporidinisParazitas — Informacija apie paukščių hemosporidinius parazitus

Informacija apie P.B. Šivickio Gamtos Tyrimų Centro mokslinių darbuotojų ištirtus ir aprašytus paukščių hemosporidinius parazitus išplitusius po visą pasaulį.[^manifest]

- **Model:** `datasets/gov/gtc/hemosporidiniai_parazitai/HemosporidinisParazitas`[^manifest]
- **Dataset:** [Informacija apie paukščių hemosporidinius parazitus](../hemosporidiniai_parazitai.md) (`datasets/gov/gtc/hemosporidiniai_parazitai`)[^manifest]
- **Manifest CSV:** [datasets/gov/gtc/hemosporidiniai_parazitai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/hemosporidiniai_parazitai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/gtc/hemosporidiniai_parazitai/HemosporidinisParazitas` (`deployed`)[^manifest]
- **Provider:** `gtc` — Gamtos tyrimų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Įrašo id | — |
| `parazito_rusis` | `string` | — | `4` | `open` | — | Hemosporidinio paukščio parazito rūšis | — |
| `malavi_kodas` | `string` | — | `4` | `open` | — | Parazito genetinės linijos aprašymas MalAvi duomenų bazėj | — |
| `nuoroda_i_aprasyma` | `url` | — | `4` | `open` | — | Nuoroda į parazito aprašymą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/gtc/hemosporidiniai_parazitai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/hemosporidiniai_parazitai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/gtc/hemosporidiniai_parazitai (https://data.gov.lt/datasets/2634/)
