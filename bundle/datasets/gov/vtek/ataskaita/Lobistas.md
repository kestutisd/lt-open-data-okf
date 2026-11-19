---
type: Table
title: "Lobistas — Lobistų skaičius pagal asmens tipą"
description: "Pateikiamos aktyviai veikiančių fizinių ir juridinių asmenų suvestinės."
resource: "https://get.data.gov.lt/datasets/gov/vtek/ataskaita/Lobistas"
tags: [gov, vtek, lobistas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2935/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vtek/ataskaita"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lobistas — Lobistų skaičius pagal asmens tipą

Pateikiamos aktyviai veikiančių fizinių ir juridinių asmenų suvestinės.[^manifest]

- **Model:** `datasets/gov/vtek/ataskaita/Lobistas`[^manifest]
- **Dataset:** [Lobistinės veiklos statistiniai duomenys](../ataskaita.md) (`datasets/gov/vtek/ataskaita`)[^manifest]
- **Manifest CSV:** [datasets/gov/vtek/ataskaitos.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/ataskaita/Lobistas` (`deployed`)[^manifest]
- **Provider:** `vtek` — Vyriausioji tarnybinės etikos komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `viso_fiziniu` | `integer` | — | `4` | `open` | — | Bendras aktyvių fizinių lobistų skaičius įskaičiuojant ir ankstesnių mėnesių duomenis | — |
| `viso_juridiniu` | `integer` | — | `4` | `open` | — | Bendras aktyvių juridinių asmenų lobistų skaičius įskaičiuojant ir ankstesnių mėnesių duomenis | — |
| `viso_lobistu` | `integer` | — | `4` | `open` | — | Bendras aktyvių fizinių ir juridinių lobistų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/ataskaitos.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/ataskaitos.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vtek/ataskaita (https://data.gov.lt/datasets/2935/)
