---
type: Table
title: "Apygarda — Rinkimų apygardos"
description: "Rinkimų apygardų lentelė."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Apygarda"
tags: [gov, vrk, apygarda, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20"
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vrk/rinkeju_demografiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Apygarda — Rinkimų apygardos

Rinkimų apygardų lentelė. Vienas įrašas atitinka vieną apygardą tam tikrų rinkimų metu. Lentelė sudaryta iš apygardos identifikatoriaus ir pavadinimo.[^manifest]

- **Model:** `datasets/gov/vrk/rinkeju_demografiniai_duomenys/Apygarda`[^manifest]
- **Dataset:** [Rinkėjų demografiniai duomenys](../rinkeju_demografiniai_duomenys.md) (`datasets/gov/vrk/rinkeju_demografiniai_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkeju_demografiniai_duomenys/Apygarda` (`deployed`)[^manifest]
- **Provider:** `vrk` — Vyriausioji rinkimų komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `apygardos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apygardos_id` | `string` | — | `4` | `open` | — | Apygardos identifikatorius | — |
| `apygardos_pav` | `string` | — | `4` | `open` | — | Apygardos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkeju_demografiniai_duomenys.csv#L20)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vrk/rinkeju_demografiniai_duomenys (https://data.gov.lt/datasets/2808/)
