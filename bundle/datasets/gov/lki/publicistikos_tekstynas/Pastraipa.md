---
type: Table
title: "Pastraipa — Moderniosios tapatybės ideologinio naratyvo publicistinių tekstų pastraipos"
description: "Lentelėje pateiktos tekstų pastraipos iš Lietuvių kalbos instituto Moderniosios tapatybės ideologinio naratyvo tekstyno."
resource: "https://get.data.gov.lt/datasets/gov/lki/publicistikos_tekstynas/Pastraipa"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/publicistikos_tekstynas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/publicistikos_tekstynas.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pastraipa — Moderniosios tapatybės ideologinio naratyvo publicistinių tekstų pastraipos

Lentelėje pateiktos tekstų pastraipos iš Lietuvių kalbos instituto Moderniosios tapatybės ideologinio naratyvo tekstyno. Šis tekstynas - tekstų duomenų bazė, naudojama lingvistinei, statistinei, sociologinei rašytinės kalbos analizei. Duomenys rinkti nuo 2018 metų iki 2021 metų. Kiti šių duomenų atnaujinimai galimi ateityje, Lietuvių kalbos institutui vykdant papildomus duomenų rinkimo projektus.

- **Model:** `datasets/gov/lki/publicistikos_tekstynas/Pastraipa`[^manifest]
- **Dataset:** [Moderniosios tapatybės ideologinio naratyvo publicistikos tekstynas](../publicistikos_tekstynas.md) (`datasets/gov/lki/publicistikos_tekstynas`)
- **Manifest CSV:** [datasets/gov/lki/publicistikos_tekstynas.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/publicistikos_tekstynas.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/publicistikos_tekstynas/Pastraipa`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `teksto_id` | `string` | — | `4` | `open` | — | Teksto identifikacinis numeris (-iai) | — |
| `teksto_id_tipas` | `string` | — | `4` | `open` | — | Teksto identifikacinio numerio tipas (-ai) | — |
| `pastraipos_nr` | `string` | — | `4` | `open` | — | Pastraipos eilės numeris tekste | — |
| `pastraipa` | `string` | — | `4` | `open` | — | Pastraipos sakiniai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/publicistikos_tekstynas.csv
