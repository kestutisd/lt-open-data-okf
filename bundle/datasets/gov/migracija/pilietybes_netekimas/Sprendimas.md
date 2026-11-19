---
type: Table
title: "Sprendimas — Duomenys apie Migracijos departamento sprendimus panaikinti Lietuvos Respublikos pilietybę."
description: "Duomenys apie asmenis, kurie neteko Lietuvos Respublikos pilietybės jos atsisakius ar įgijus kitos valstybės pilietybę."
resource: "https://get.data.gov.lt/datasets/gov/migracija/pilietybes_netekimas/Sprendimas"
tags: [gov, migracija, sprendimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/pilietybes_netekimas.csv#L12"
    title: "atviriduomenys/manifest — datasets/gov/migracija/pilietybes_netekimas.csv#L12"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1946/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/pilietybes_netekimas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sprendimas — Duomenys apie Migracijos departamento sprendimus panaikinti Lietuvos Respublikos pilietybę.

**Dataset Context:** Duomenys apie asmenis, kurie neteko Lietuvos Respublikos pilietybės jos atsisakius ar įgijus kitos valstybės pilietybę.[^manifest]

- **Model:** `datasets/gov/migracija/pilietybes_netekimas/Sprendimas`[^manifest]
- **Dataset:** [Duomenys apie pilietybės netekimą](../pilietybes_netekimas.md) (`datasets/gov/migracija/pilietybes_netekimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/pilietybes_netekimas.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/pilietybes_netekimas.csv#L12)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/pilietybes_netekimas/Sprendimas` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `sprendimo_registracija` | `date` | `D` | `4` | `open` | — | Sprendimo registracijos data | — |
| `sprendimas` | `string` | — | `3` | `open` | — | Migracijos departamento sprendimas | — |
| `sprendimo_pagrindas` | `string` | — | `2` | `open` | — | Sprendimo pagrindas | — |
| `poreiksme` | `string` | — | `2` | `open` | — | Sprendimo poreikšmė | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Sprendimą gavusio asmens pilietybė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis byloje | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Sprendimą gavusio asmens amžiaus grupė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimo_pagrindas` | `"update(property: ""sprendimo_pagrindas[]"", type: ""array"", source: ""Sprendimo_pagrindas"")"` | `property` | `4` | — | — | — | — |
| `poreiksme` | `"update(property: ""poreiksme[]"", type: ""array"", source: ""Poreiksme"")"` | `property` | `4` | — | — | — | — |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/pilietybes_netekimas.csv#L12 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/pilietybes_netekimas.csv#L12)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/pilietybes_netekimas (https://data.gov.lt/datasets/1946/)
