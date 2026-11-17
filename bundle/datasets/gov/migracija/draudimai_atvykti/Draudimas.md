---
type: Table
title: "Draudimas — Duomenys apie užsieniečius, kuriems buvo uždrausta atvykti į Lietuvos Respubliką, kuriems buvo atsisakyta išduoti vizą ar ji buvo panaikinta, ar atšaukta Šengeno viza arba kuriems buvo..."
description: "Spinta table datasets/gov/migracija/draudimai_atvykti/Draudimas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/draudimai_atvykti/Draudimas"
tags: [gov, migracija, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/draudimai_atvykti.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/draudimai_atvykti.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Draudimas — Duomenys apie užsieniečius, kuriems buvo uždrausta atvykti į Lietuvos Respubliką, kuriems buvo atsisakyta išduoti vizą ar ji buvo panaikinta, ar atšaukta Šengeno viza arba kuriems buvo...

- **Model:** `datasets/gov/migracija/draudimai_atvykti/Draudimas`[^manifest]
- **Dataset:** [datasets/gov/migracija/draudimai_atvykti](../draudimai_atvykti.md) (`datasets/gov/migracija/draudimai_atvykti`)
- **Manifest CSV:** [datasets/gov/migracija/draudimai_atvykti.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/draudimai_atvykti.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/draudimai_atvykti/Draudimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `sprendimo_registracija` | `date` | `D` | `4` | `open` | — | Sprendimo registracijos data | — |
| `sprendimas` | `string` | — | `3` | `open` | — | Migracijos departamento sprendimas | — |
| `sprendimo_pagrindas` | `string` | — | `2` | `open` | — | Migracijos departamento pagrindas uždrausti atvykti į Lietuvos Respubliką | — |
| `poreiksme` | `string` | — | `2` | `open` | — | Sprendimo poreikšmė | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Sprendimą gavusio asmens pilietybė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis byloje | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Sprendimą gavusio asmens amžiaus grupė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sprendimo_pagrindas` | `"update(property: ""sprendimo_pagrindas[]"", type: ""array"", source: ""Sprendimo_pagrindas"")"` | `property` | `4` | — | — | — | — |
| `poreiksme` | `"update(property: ""poreiksme[]"", type: ""array"", source: ""Poreiksme"")"` | `property` | `4` | — | — | — | — |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/draudimai_atvykti.csv
