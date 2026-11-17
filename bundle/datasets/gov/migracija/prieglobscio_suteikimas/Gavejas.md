---
type: Table
title: "Gavejas — Duomenys apie prieglobsčio gavėjus"
description: "Spinta table datasets/gov/migracija/prieglobscio_suteikimas/Gavejas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas/Gavejas"
tags: [gov, migracija, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/prieglobscio_suteikimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gavejas — Duomenys apie prieglobsčio gavėjus

- **Model:** `datasets/gov/migracija/prieglobscio_suteikimas/Gavejas`[^manifest]
- **Dataset:** [datasets/gov/migracija/prieglobscio_suteikimas](../prieglobscio_suteikimas.md) (`datasets/gov/migracija/prieglobscio_suteikimas`)
- **Manifest CSV:** [datasets/gov/migracija/prieglobscio_suteikimas.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas/Gavejas`
- **Primary Key (`ref`):** `id`
- **Level:** `3`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracija` | `string` | — | `2` | `open` | — | Prašymo prieglobsčiui gauti registracijos data | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis byloje | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Asmens amžiaus grupė pagal gimimo datą, nurodytą byloje | — |
| `pilietybe` | `string` | — | `3` | `open` | — | Asmens pilietybė | — |
| `sprendimas` | `date` | `D` | `4` | `open` (inherited) | — | Sprendimo suteikti prieglobstį registravimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"Šeima"` | — | — | Šeima | Kai kurie prieglobsčio prašymai tenkinami ne asmeniui, o visai šeimai. Dėl to tokie jungtiniai prašymai šeimoms žymimi atskirai. |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/prieglobscio_suteikimas.csv
