---
type: Table
title: "Tekstynas — Moderniosios tapatybės ideologinio naratyvo publicistikos tekstai"
description: "Lentelėje pateikti pilni tekstai iš Lietuvių kalbos instituto Moderniosios tapatybės ideologinio naratyvo publicistikos tekstyno."
resource: "https://get.data.gov.lt/datasets/gov/lki/publicistikos_tekstynas/Tekstynas"
tags: [gov, lki, tekstynas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/publicistikos_tekstynas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lki/publicistikos_tekstynas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2713/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/publicistikos_tekstynas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Tekstynas — Moderniosios tapatybės ideologinio naratyvo publicistikos tekstai

Lentelėje pateikti pilni tekstai iš Lietuvių kalbos instituto Moderniosios tapatybės ideologinio naratyvo publicistikos tekstyno. Šis tekstynas - tekstų duomenų bazė, naudojama lingvistinei, statistinei, sociologinei rašytinės kalbos analizei. Duomenys rinkti nuo 2018 metų iki 2021 metų. Kiti šių duomenų atnaujinimai galimi ateityje, Lietuvių kalbos institutui vykdant papildomus duomenų rinkimo projektus.[^manifest]

- **Model:** `datasets/gov/lki/publicistikos_tekstynas/Tekstynas`[^manifest]
- **Dataset:** [Moderniosios tapatybės ideologinio naratyvo publicistikos tekstynas](../publicistikos_tekstynas.md) (`datasets/gov/lki/publicistikos_tekstynas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lki/publicistikos_tekstynas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/publicistikos_tekstynas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/publicistikos_tekstynas/Tekstynas` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `teksto_id` | `string` | — | `4` | `open` | — | Teksto identifikacinis numeris (-iai) | — |
| `teksto_id_tipas` | `string` | — | `4` | `open` | — | Teksto identifikacinio numerio tipas (-ai) | — |
| `teksto_autorius` | `string` | — | `4` | `open` | — | Teksto autorius (-iai) | — |
| `teksto_antraste` | `string` | — | `4` | `open` | — | Teksto antraštė (-s) | — |
| `teksto_paantraste` | `string` | — | `4` | `open` | — | Teksto paantraštė (-s) | — |
| `teksto_pavadinimas` | `string` | — | `4` | `open` | — | Teksto pavadinimas (-ai) | — |
| `tekstas` | `string` | — | `4` | `open` | — | Pilnas tekstas | — |
| `teksto_data` | `string` | — | `4` | `open` | — | Teksto rašymo data (-os) | — |
| `teksto_vieta` | `string` | — | `4` | `open` | — | Teksto rašymo vieta (-os) | — |
| `laikrastis` | `string` | — | `4` | `open` | — | Laikraštis, kuriame tekstas buvo publikuotas | — |
| `laikrascio_data` | `date` | `D` | `4` | `open` | — | Laikraščio data (-os) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/publicistikos_tekstynas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/publicistikos_tekstynas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/publicistikos_tekstynas (https://data.gov.lt/datasets/2713/)
