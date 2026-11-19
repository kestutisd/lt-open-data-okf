---
type: Table
title: "Sudetis — Valstybės valdomų įmonių sąrašas"
description: "Valstybės valdomų įmonių sąraše yra pateikiamas - įmonės pavadinimas,įmonės kodas, nario vardas ir pavardė, pareigos, pozicija."
resource: "https://get.data.gov.lt/datasets/gov/vkc/sudetis/Sudetis"
tags: [gov, vkc, sudetis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/sudetis.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vkc/sudetis.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2840/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vkc/sudetis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sudetis — Valstybės valdomų įmonių sąrašas

Valstybės valdomų įmonių sąraše yra pateikiamas - įmonės pavadinimas,įmonės kodas, nario vardas ir pavardė, pareigos, pozicija. Duomenys vienkartiniai.[^manifest]

- **Model:** `datasets/gov/vkc/sudetis/Sudetis`[^manifest]
- **Dataset:** [Valstybės valdomų įmonių sąrašas](../sudetis.md) (`datasets/gov/vkc/sudetis`)[^manifest]
- **Manifest CSV:** [datasets/gov/vkc/sudetis.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/sudetis.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkc/sudetis/Sudetis` (`deployed`)[^manifest]
- **Provider:** `vkc` — Valdymo koordinavimo centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"valdyba"` | — | — | Asmuo, priklausantis valdybai | — |
| `tipas` | `"vadovybė"` | — | — | Asmuo, priklausantis vadovybei | — |
| `tipas` | `"stebėtojų taryba"` | — | — | Asmuo, priklausantis stabėtojų tarybai | — |
| `pozicija` | `"Įmonės vadovas"` | — | — | Įmonės vadovas | — |
| `pozicija` | `"Narys"` | — | — | Narys | — |
| `pozicija` | `"Pirmininkas"` | — | — | Pirmininkas | — |

# Related References

- [JAR Legal Entities Join Reference](../../../../references/joins/jar-legal-entities.md) — Two-step `level>=4` UUID joins, `ja_kodas` keys, and GDPR masking rules.

[^manifest]: atviriduomenys/manifest — datasets/gov/vkc/sudetis.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkc/sudetis.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vkc/sudetis (https://data.gov.lt/datasets/2840/)
