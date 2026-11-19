---
type: Table
title: "Prasymas — Duomenys apie trečiųjų šalių piliečių prašymus išduoti ar pakeisti leidimą laikinai gyventi Lietuvos Respublikoje"
description: "Duomenys apie trečiųjų šalių piliečius"
resource: "https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr/Prasymas"
tags: [gov, migracija, prasymas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/migracija/teise_gyventi_lr.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1942/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/teise_gyventi_lr"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Prasymas — Duomenys apie trečiųjų šalių piliečių prašymus išduoti ar pakeisti leidimą laikinai gyventi Lietuvos Respublikoje

**Dataset Context:** Duomenys apie trečiųjų šalių piliečius[^manifest]

- **Model:** `datasets/gov/migracija/teise_gyventi_lr/Prasymas`[^manifest]
- **Dataset:** [Duomenys apie teisės gyventi Lietuvos Respublikoje suteikimą](../teise_gyventi_lr.md) (`datasets/gov/migracija/teise_gyventi_lr`)[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/teise_gyventi_lr.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr/Prasymas` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pateikimas` | `date` | `D` | `4` | `open` | — | Prašymo pateikimo data | — |
| `prasymo_registracija` | `date` | `D` | `4` | `open` | — | Prašymo registracijos data | — |
| `pagrindas` | `string` | — | `3` | `open` | — | Prašymo pagrindas | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Asmens pilietybė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Asmens amžiaus grupė pagal gimimo datą | — |
| `lytis` | `string` | — | `4` | `open` (inherited) | — | Lytis byloje | — |
| `skubus_prasymas` | `boolean` | — | `4` | `open` | — | Prašymo nagrinėjimo tvarka | — |
| `skyrius` | `string` | — | `4` | `open` | — | Prašymo būsenos sukūrimo vieta | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | `open` | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/teise_gyventi_lr.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/teise_gyventi_lr (https://data.gov.lt/datasets/1942/)
