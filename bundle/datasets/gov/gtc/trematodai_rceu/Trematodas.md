---
type: Table
title: "Trematodas — Informacija apie Centrinės ir Rytų Europos trematodus"
description: "Informacija apie P.B. Šivickio Gamtos Tyrimų Centro mokslinių darbuotojų ištirtus ir aprašytus stuburinius parazitus (trematodus) išplitusius Rytų ir Centrinėje Europoje."
resource: "https://get.data.gov.lt/datasets/gov/gtc/trematodai_rceu/Trematodas"
tags: [gov, gtc, trematodas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/trematodai_rceu.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/gtc/trematodai_rceu.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2633/"
    title: "data.gov.lt DCAT-AP — datasets/gov/gtc/trematodai_rceu"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Trematodas — Informacija apie Centrinės ir Rytų Europos trematodus

Informacija apie P.B. Šivickio Gamtos Tyrimų Centro mokslinių darbuotojų ištirtus ir aprašytus stuburinius parazitus (trematodus) išplitusius Rytų ir Centrinėje Europoje.[^manifest]

- **Model:** `datasets/gov/gtc/trematodai_rceu/Trematodas`[^manifest]
- **Dataset:** [Informacija apie Centrinės ir Rytų Europos trematodus](../trematodai_rceu.md) (`datasets/gov/gtc/trematodai_rceu`)[^manifest]
- **Manifest CSV:** [datasets/gov/gtc/trematodai_rceu.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/trematodai_rceu.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/gtc/trematodai_rceu/Trematodas` (`deployed`)[^manifest]
- **Provider:** `gtc` — Gamtos tyrimų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Įrašo id | — |
| `siurbikes_pavadinimas` | `string` | — | `4` | `open` | — | Trematodo (siurbikės) pavadinimas | — |
| `klase` | `string` | — | `4` | `open` | — | Trematodo (siurbikės) klasė | — |
| `rusis_ar_tipas` | `string` | — | `4` | `open` | — | Trematodo (siurbikės) rūšis ar tipas | — |
| `turetojas` | `string` | — | `4` | `open` | — | Trematodo (siurbikės) šeimininkas | — |
| `turetojo_tipas` | `string` | — | `4` | `open` | — | Trematodo (siurbikės) šeimininko tipas | — |
| `nuotrauka` | `url` | — | `4` | `open` | — | Nuoroda į trematodo (siurbikės) nuotrauką | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/gtc/trematodai_rceu.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/trematodai_rceu.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/gtc/trematodai_rceu (https://data.gov.lt/datasets/2633/)
