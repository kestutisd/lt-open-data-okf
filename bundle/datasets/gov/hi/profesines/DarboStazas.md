---
type: Table
title: "DarboStazas — Profesinių ligų atvejai pagal darbo stažą"
description: "Spinta table datasets/gov/hi/profesines/DarboStazas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/profesines/DarboStazas"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/profesines.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L16"
    last_modified: "2026-11-11T14:39:20Z"
---

# DarboStazas — Profesinių ligų atvejai pagal darbo stažą

- **Model:** `datasets/gov/hi/profesines/DarboStazas`[^manifest]
- **Dataset:** [Lietuvos Respublikos profesinių ligų valstybės registro duomenys](../profesines.md) (`datasets/gov/hi/profesines`)
- **Manifest CSV:** [datasets/gov/hi/profesines.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L16)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/profesines/DarboStazas`
- **Primary Key (`ref`):** `atvejis_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atvejis_id` | `string` | — | `4` | `open` | — | Profesinės ligos atvejo identifikatorius | — |
| `pagr_tlk_kodas` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Pagrindinės profesinės ligos kodas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `pagr_tlk_pav` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[name]](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Pagrindinės profesinės ligos pavadinimas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `lpk` | `string` | — | `4` | `open` | — | Paciento profesija | Pagal Lietuvos profesijų klasifikatorių |
| `evrk` | `string` | — | `4` | `open` | — | EVRK kodas | Ekonominės veiklos rūšies klasifikatoriaus kodas. Nurodo, kuriame sektoriuje pacientas dirba |
| `stazas` | `string` | — | `4` | `open` | — | Darbo stažo grupės | Metais |
| `year` | `integer` | `yr` | `2` | `open` | — | Metai | Profesinės ligos užregistravimo metai |
| `quarter` | `integer` | `3mo` | `2` | `open` | — | Ketvirtis | Profesinės ligos užregistravimo ketvirtis |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `stazas` | `'50+'` | — | — | 50+ | — |
| `stazas` | `'45-49'` | — | — | 45-49 | — |
| `stazas` | `'40-44'` | — | — | 40-44 | — |
| `stazas` | `'35-39'` | — | — | 35-39 | — |
| `stazas` | `'30-34'` | — | — | 30-34 | — |
| `stazas` | `'25-29'` | — | — | 25-29 | — |
| `stazas` | `'20-24'` | — | — | 20-24 | — |
| `stazas` | `'15-19'` | — | — | 15-19 | — |
| `stazas` | `'10-14'` | — | — | 10-14 | — |
| `stazas` | `'5-9'` | — | — | 5-9 | — |
| `stazas` | `'0-4'` | — | — | 0-4 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/profesines.csv
