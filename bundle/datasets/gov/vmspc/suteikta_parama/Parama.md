---
type: Table
title: "Parama"
description: "Vilniaus miesto socialinių paslaugų centro suteikta parama asmenims be gyvenamosios vietos"
resource: "https://get.data.gov.lt/datasets/gov/vmspc/suteikta_parama/Parama"
tags: [gov, vmspc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmspc/suteikta_parama.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmspc/suteikta_parama.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Parama

Vilniaus miesto socialinių paslaugų centro suteikta parama asmenims be gyvenamosios vietos

- **Model:** `datasets/gov/vmspc/suteikta_parama/Parama`[^manifest]
- **Dataset:** [Vilniaus miesto socialinių paslaugų centro suteikta parama asmenims be gyvenamosios vietos](../suteikta_parama.md) (`datasets/gov/vmspc/suteikta_parama`)
- **Manifest CSV:** [datasets/gov/vmspc/suteikta_parama.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmspc/suteikta_parama.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmspc/suteikta_parama/Parama`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Asmens be pastovios gyvenamosios vietos unikalus identifikatorius | — |
| `tinkamas_ak` | `string` | — | `4` | `open` | — | Požymis, ar asmens kodas validus | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `gim_desimtm_ak` | `date` | `10Y` | `4` | `open` | — | Asmens gimimo metų dešimtmetis iš asmens kodo | — |
| `gim_desimtm` | `date` | `10Y` | `4` | `open` | — | Asmens gimimo metu dešimtmetis | — |
| `lytis` | `string` | — | `4` | `open` | — | Asmens lytis | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Parama suteikta nuo | — |
| `iki` | `date` | `D` | `4` | `open` | — | Parama suteikta iki | — |
| `parama` | `string` | — | `4` | `open` | — | Socialinės paramos tipo pavadinimas | — |
| `istaiga` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_ak` | `"Moteris"` | — | — | Moteris | — |
| `lytis_ak` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmspc/suteikta_parama.csv
