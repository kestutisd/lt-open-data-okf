---
type: Table
title: "Kvota — Verslinės žvejybos kvotos"
description: "Informacija apie išduotas verslinės žvejybos kvotas Baltijos jūroje ir Atlanto vandenyne."
resource: "https://get.data.gov.lt/datasets/gov/ztzum/verslines_zvejybos_kvotos/Kvota"
tags: [gov, ztzum, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ztzum/verslines_zvejybos_kvotos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ztzum/verslines_zvejybos_kvotos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kvota — Verslinės žvejybos kvotos

Informacija apie išduotas verslinės žvejybos kvotas Baltijos jūroje ir Atlanto vandenyne.

- **Model:** `datasets/gov/ztzum/verslines_zvejybos_kvotos/Kvota`[^manifest]
- **Dataset:** [Verslinės žvejybos kvotos](../verslines_zvejybos_kvotos.md) (`datasets/gov/ztzum/verslines_zvejybos_kvotos`)
- **Manifest CSV:** [datasets/gov/ztzum/verslines_zvejybos_kvotos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ztzum/verslines_zvejybos_kvotos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ztzum/verslines_zvejybos_kvotos/Kvota`
- **Primary Key (`ref`):** `kvotos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kvotos_id` | `string` | — | `4` | `open` | — | Skirtos kvotos id | — |
| `rusis` | `string` | — | `4` | `open` | — | Žuvies rūšis kuriai skirta kvota | — |
| `einamosios_kvotos_dydis` | `number` | — | `4` | `open` | — | Ukio subjektui skirtos kvotos dydis | — |
| `kvotos_dydis_lietuvai` | `number` | — | `4` | `open` | — | Pradinis Lietuvai skirtos kvotos dydis | — |
| `mato_vienetai` | `string` | — | `4` | `open` | — | Dydžių mato vienetai | — |
| `kvotos_lietuvai_id` | `string` | — | `4` | `open` | — | Kvotos skirtos Lietuvai identifikatorius | — |
| `kvotos_metai` | `integer` | — | `4` | `open` | — | Metai, kuriems skirta kvota | — |
| `kvotos_regiono_pavadinimas` | `string` | — | `4` | `open` | — | Kvotos regiono pavadinimas | — |
| `kvotos_pavadinimas` | `string` | — | `4` | `open` | — | Kvotos pavadinimas | — |
| `juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Juridinio asmens kodas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mato_vienetai` | `"Tona"` | — | — | — | — |
| `mato_vienetai` | `"Vienetas"` | — | — | — | — |
| `mato_vienetai` | `"Kilogramas"` | — | — | — | — |
| `kvotos_regiono_pavadinimas` | `"Baltijos"` | — | — | — | — |
| `kvotos_regiono_pavadinimas` | `"Tolimųjų jūrų"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ztzum/verslines_zvejybos_kvotos.csv
