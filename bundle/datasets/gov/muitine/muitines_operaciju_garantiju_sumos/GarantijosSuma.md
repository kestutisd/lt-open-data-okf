---
type: Table
title: "GarantijosSuma — Muitinės operacijų garantijų sumos"
description: "Lentelėje pateikiamos muitinės operacijų garantijų sumos iš LR Muitinės garantijų valdymo sistemos (Muitinės GVS)."
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_operaciju_garantiju_sumos/GarantijosSuma"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_operaciju_garantiju_sumos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_operaciju_garantiju_sumos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# GarantijosSuma — Muitinės operacijų garantijų sumos

Lentelėje pateikiamos muitinės operacijų garantijų sumos iš LR Muitinės garantijų valdymo sistemos (Muitinės GVS). Duomenys renkami nuo 2016 metų.

- **Model:** `datasets/gov/muitine/muitines_operaciju_garantiju_sumos/GarantijosSuma`[^manifest]
- **Dataset:** [Muitinės operacijų garantijų sumos](../muitines_operaciju_garantiju_sumos.md) (`datasets/gov/muitine/muitines_operaciju_garantiju_sumos`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_operaciju_garantiju_sumos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_operaciju_garantiju_sumos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_operaciju_garantiju_sumos/GarantijosSuma`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `garantijos_dydis` | `number` | — | `4` | `open` | — | Garantijos dydis | — |
| `referencinis_dydis` | `number` | — | `4` | `open` | — | Garantijos referencinis dydis | — |
| `sumazinimo_lygis_proc` | `integer` | `%` | `4` | `open` | — | Sumažinimo lygis (procentais) | — |
| `muitines_operacija` | `string` | — | `4` | `open` | — | Muitinės operacija | — |
| `garantijos_grn` | `string` | — | `4` | `open` | — | Garantijos GRN | — |
| `garantijos_tipo_kodas` | `string` | — | `4` | `open` | — | Garantijos tipo kodas | — |
| `garantijos_tipas` | `string` | — | `4` | `open` | — | Garantijos tipas | — |
| `garantijos_busena` | `string` | — | `4` | `open` | — | Garantijos būsena | — |
| `garantijos_busenos_data` | `datetime` | `S` | `4` | `open` | — | Garantijos būsenos data | — |
| `garantijos_galiojimo_pradzia` | `date` | `D` | `4` | `open` | — | Garantijos galiojimo pradžia | — |
| `registruojancios_institucijos_pavadinimas` | `string` | — | `4` | `open` | — | Garantijos muitinės įstaiga | — |
| `garanto_id` | `string` | — | `4` | `open` | — | Garanto identifikatorius | — |
| `proceduros_vykdytojo_id` | `string` | — | `4` | `open` | — | Procedūros vykdytojo identifikatorius | — |
| `ar_visos_es_salys` | `boolean` | — | `4` | `open` | — | Požymis, ar garantija galioja visose Europos Sąjungos ir asociacijos susitarimą turinčiose (Andora, San Marinas) šalyse | — |
| `eu_salys` | `string` | — | `4` | `open` | — | Galiojimo teritorija Europos Sąjungos šalyse | — |
| `tranzito_salys` | `string` | — | `4` | `open` | — | Galiojimo teritorija bendrojo tranzito šalyse | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_operaciju_garantiju_sumos.csv
