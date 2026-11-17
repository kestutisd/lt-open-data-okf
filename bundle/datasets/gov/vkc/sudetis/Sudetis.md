---
type: Table
title: "Sudetis — Valstybės valdomų įmonių sąrašas"
description: "Valstybės valdomų įmonių sąraše yra pateikiamas - įmonės pavadinimas,įmonės kodas, nario vardas ir pavardė, pareigos, pozicija."
resource: "https://get.data.gov.lt/datasets/gov/vkc/sudetis/Sudetis"
tags: [gov, vkc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vkc/sudetis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/sudetis.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sudetis — Valstybės valdomų įmonių sąrašas

Valstybės valdomų įmonių sąraše yra pateikiamas - įmonės pavadinimas,įmonės kodas, nario vardas ir pavardė, pareigos, pozicija. Duomenys vienkartiniai.

- **Model:** `datasets/gov/vkc/sudetis/Sudetis`[^manifest]
- **Dataset:** [Valstybės valdomų įmonių sąrašas](../sudetis.md) (`datasets/gov/vkc/sudetis`)
- **Manifest CSV:** [datasets/gov/vkc/sudetis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/sudetis.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkc/sudetis/Sudetis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Vienas iš: vadovybė, valdyba, stebėtojų taryba | — |
| `eile` | `integer` | — | `4` | `open` | — | Nario eilės numeris | — |
| `pozicija` | `string` | — | `4` | `open` | — | Duomenys apie poziciją | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Nario vardas ir pavardė | — |
| `pareigos` | `string` | — | `4` | `open` | — | Duomenys apie vadovybės nario pareigas lietuvių kalba | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Duomenys apie įmonės kodą | — |
| `imones_pavadinimas` | `string` | — | `4` | `open` | — | Duomenys apie įmonės pavadinimą | — |
| `informacija_aktuali_datai` | `date` | `D` | `4` | `open` | — | Duomenys apie informacijos aktualumo datą | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"valdyba"` | — | — | Asmuo, priklausantis valdybai | — |
| `tipas` | `"vadovybė"` | — | — | Asmuo, priklausantis vadovybei | — |
| `tipas` | `"stebėtojų taryba"` | — | — | Asmuo, priklausantis stabėtojų tarybai | — |
| `pozicija` | `"Įmonės vadovas"` | — | — | Įmonės vadovas | — |
| `pozicija` | `"Narys"` | — | — | Narys | — |
| `pozicija` | `"Pirmininkas"` | — | — | Pirmininkas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vkc/sudetis.csv
