---
type: Table
title: "VietovesAugalas — Vietovės dirvožemio augalai"
description: "Informacija apie Lietuvos teritorijos vietovėse, kuriose Gamtos Tyrimų Centro moksliniai darbuotojai tiria dirvožemio temperatūrą ir drėgmę, augalus augančius."
resource: "https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura/VietovesAugalas"
tags: [gov, gtc, vietovesaugalas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L24"
    title: "atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv#L24"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2638/"
    title: "data.gov.lt DCAT-AP — datasets/gov/gtc/dirvozemio_temperatura"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VietovesAugalas — Vietovės dirvožemio augalai

Informacija apie Lietuvos teritorijos vietovėse, kuriose Gamtos Tyrimų Centro moksliniai darbuotojai tiria dirvožemio temperatūrą ir drėgmę, augalus augančius.[^manifest]

- **Model:** `datasets/gov/gtc/dirvozemio_temperatura/VietovesAugalas`[^manifest]
- **Dataset:** [Dirvožemio temperatūra ir drėgmė bei dirvožemyje augantys augalai](../dirvozemio_temperatura.md) (`datasets/gov/gtc/dirvozemio_temperatura`)[^manifest]
- **Manifest CSV:** [datasets/gov/gtc/dirvozemio_temperatura.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L24)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura/VietovesAugalas` (`deployed`)[^manifest]
- **Provider:** `gtc` — Gamtos tyrimų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Įrašo unikalus identifikatorius | — |
| `vietoves_registratoriaus_id` | `string` | — | `4` | `open` | — | Vietovės registratoriaus identifikatorius | — |
| `augalo_pavadinimas_la` | `string` | — | `4` | `open` | — | Augalo pavadinimas lotynų kalba | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `augalo_pavadinimas_la` | `update(property: "augalo_pavadinimas@la", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv#L24 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L24)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/gtc/dirvozemio_temperatura (https://data.gov.lt/datasets/2638/)
