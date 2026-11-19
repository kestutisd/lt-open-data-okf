---
type: Table
title: "Rinkejas — Rinkėjai"
description: "Balso teisę turinčių rinkėjų lentelė."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Rinkejas"
tags: [gov, vrk, rinkejas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vrk/rinkeju_demografiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rinkejas — Rinkėjai

Balso teisę turinčių rinkėjų lentelė. Vienas įrašas atitinka vieną rinkėją. Lentelė sudaryta iš rinkėjo pseudonimizuoto asmens kodo, lyties ir gimimo metų. Apie 12% rinkėjų gimimo metų įrašų yra modifikuoti pridedant atsitiktines vertes – triukšmą, siekiant užtikrinti konfidencialumą.[^manifest]

- **Model:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys/Rinkejas`[^manifest]
- **Dataset:** [Rinkėjų demografiniai duomenys](../rinkeju_demografiniai_duomenys.md) (`datasets/gov/vrk/rinkeju_demografiniai_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Rinkejas` (`deployed`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `rinkejo_asm_k`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rinkejo_asm_k` | `string` | — | `4` | `open` | — | Rinkėjo pseudonimizuotas asmens kodas | — |
| `rinkejo_lytis` | `string` | — | `4` | `open` | — | Rinkėjo lytis | — |
| `rinkejo_gim_m` | `date` | `Y` | `4` | `open` | — | Rinkėjo gimimo metai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rinkejo_lytis` | `"V"` | — | — | Vyras | — |
| `rinkejo_lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vrk/rinkeju_demografiniai_duomenys (https://data.gov.lt/datasets/2808/)
