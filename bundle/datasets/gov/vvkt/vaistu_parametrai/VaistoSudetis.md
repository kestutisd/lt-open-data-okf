---
type: Table
title: "VaistoSudetis — Vaistinių preparatų sudėties parametrai"
description: "Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų sudėties parametrus."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai/VaistoSudetis"
tags: [gov, vvkt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# VaistoSudetis — Vaistinių preparatų sudėties parametrai

Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų sudėties parametrus. Kiekviena eilutė nurodo vaistinio preparato komponento ingrediento stiprumo parametrą. Vieną eilutę sudaro: vaistinio preparato identifikacinis numeris, komponento eilės numeris, komponento farmacinė forma, komponento kiekis ir jo matavimo vienetai, komponento ingrediento eilės numeris, stiprumas ir stiprumo matavimo vienetai, bei pačio ingrediento pavadinimas. Paskutiniai du stulpeliai nurodo ar komponente esanti ingredientinė medžiaga yra veikliosios medžiagos ar pagalbinės medžiagos tipo.

- **Model:** `datasets/gov/vvkt/vaistu_parametrai/VaistoSudetis`[^manifest]
- **Dataset:** [Vaistinių preparatų vartojimo ir sudėties parametrai](../vaistu_parametrai.md) (`datasets/gov/vvkt/vaistu_parametrai`)
- **Manifest CSV:** [datasets/gov/vvkt/vaistu_parametrai.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai/VaistoSudetis`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | Unikalus Valstybės duomenų agentūros sugeneruotas eilutės identifikatorius. Eilutės unikalumą sudaro vid, medz_pav, komponento_eil_nr, ingrediento_eil_nr |
| `vid` | `string` | — | `4` | `open` | — | Vaistinio preparato identifikacinis numeris | — |
| `komponento_eil_nr` | `integer` | — | `4` | `open` | — | Komponento eilės numeris | Komponento eilės numeris produkto pakuotėje |
| `farmacine_forma` | `string` | — | `4` | `open` | — | Komponento farmacinė forma | — |
| `komp_kiekis` | `number` | — | `4` | `open` | — | Komponento kiekis produkto pakuotėje | — |
| `kompo_matav_vnt` | `string` | — | `4` | `open` | — | Komponento matavimo vienetai | — |
| `ingrediento_eil_nr` | `integer` | — | `4` | `open` | — | Komponente esančio ingrediento eilės numeris | — |
| `stiprumas_skaicius` | `number` | — | `4` | `open` | — | Ingrediento stiprumo skaitinė vertė | — |
| `stiprumas_matav_vnt` | `string` | — | `4` | `open` | — | Ingrediento stiprumo matavimo vienetai | — |
| `medz_pav` | `string` | — | `4` | `open` | — | Ingrediento pavadinimas | — |
| `medz_veklioji` | `boolean` | — | `4` | `open` | — | Veiklioji medžiaga | Požymis, nurodantis, ar ingrediento medžiaga yra veiklioji |
| `medz_pagalb` | `boolean` | — | `4` | `open` | — | Pagalbinė medžiaga | Požymis, nurodantis, ar ingrediento medžiaga yra pagalbinė |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv
