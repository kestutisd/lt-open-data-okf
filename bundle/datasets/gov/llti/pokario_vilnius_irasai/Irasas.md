---
type: Table
title: "Irasas — Projekto \"Pokario Vilnius\" naujakurių pasakojimų garso ir vaizdo įrašai"
description: "Pagal projektą \"Pokario Vilnius\" atliktų interviu su pokario Vilniaus naujakuriais autobiografinių pasakojimų garso ir vaizdo įrašai."
resource: "https://get.data.gov.lt/datasets/gov/llti/pokario_vilnius_irasai/Irasas"
tags: [gov, llti, irasas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/pokario_vilnius_irasai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/llti/pokario_vilnius_irasai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Irasas — Projekto "Pokario Vilnius" naujakurių pasakojimų garso ir vaizdo įrašai

Pagal projektą "Pokario Vilnius" atliktų interviu su pokario Vilniaus naujakuriais autobiografinių pasakojimų garso ir vaizdo įrašai.[^manifest]

- **Model:** `datasets/gov/llti/pokario_vilnius_irasai/Irasas`[^manifest]
- **Dataset:** [Projekto "Pokario Vilnius" naujakurių pasakojimų garso ir vaizdo įrašai](../pokario_vilnius_irasai.md) (`datasets/gov/llti/pokario_vilnius_irasai`)[^manifest]
- **Manifest CSV:** [datasets/gov/llti/pokario_vilnius_irasai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/pokario_vilnius_irasai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/llti/pokario_vilnius_irasai/Irasas` (`deployed`)[^manifest]
- **Provider:** `llti` — Lietuvių literatūros ir tautosakos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | — | — | — | VDA sukurtas šifruotas eilutės unikalus numeris | — |
| `iraso_tipas` | `string` | — | `4` | `open` | — | Įrašo tipas | — |
| `ikelimo_data` | `date` | `D` | `4` | `open` | — | Įrašo įkėlimo arba atnaujinimo data | — |
| `nuoroda_i_irasa` | `string` | — | `4` | `open` | — | Nuoroda į įrašą | — |
| `iraso_aprasas_lt` | `string` | — | `4` | `open` | — | Trumpas įrašo aprašymas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `iraso_tipas` | — | `"Garso įrašai"` | — | — | — |
| `iraso_tipas` | — | `"Vaizdo įrašai"` | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_aprasas_lt` | `update(property: "iraso_aprasas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/llti/pokario_vilnius_irasai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/llti/pokario_vilnius_irasai.csv#L6)
