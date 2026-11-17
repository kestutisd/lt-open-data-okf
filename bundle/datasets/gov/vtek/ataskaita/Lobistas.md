---
type: Table
title: "Lobistas — Lobistų skaičius pagal asmens tipą"
description: "Pateikiamos aktyviai veikiančių fizinių ir juridinių asmenų suvestinės."
resource: "https://get.data.gov.lt/datasets/gov/vtek/ataskaita/Lobistas"
tags: [gov, vtek, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lobistas — Lobistų skaičius pagal asmens tipą

Pateikiamos aktyviai veikiančių fizinių ir juridinių asmenų suvestinės.

- **Model:** `datasets/gov/vtek/ataskaita/Lobistas`[^manifest]
- **Dataset:** [Lobistinės veiklos statistiniai duomenys](../ataskaita.md) (`datasets/gov/vtek/ataskaita`)
- **Manifest CSV:** [datasets/gov/vtek/ataskaitos.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/ataskaita/Lobistas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `viso_fiziniu` | `integer` | — | `4` | `open` | — | Bendras aktyvių fizinių lobistų skaičius įskaičiuojant ir ankstesnių mėnesių duomenis | — |
| `viso_juridiniu` | `integer` | — | `4` | `open` | — | Bendras aktyvių juridinių asmenų lobistų skaičius įskaičiuojant ir ankstesnių mėnesių duomenis | — |
| `viso_lobistu` | `integer` | — | `4` | `open` | — | Bendras aktyvių fizinių ir juridinių lobistų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv
