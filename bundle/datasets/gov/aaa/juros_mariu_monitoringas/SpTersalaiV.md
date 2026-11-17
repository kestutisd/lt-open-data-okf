---
type: Table
title: "SpTersalaiV — Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros vandenyje"
description: "Spinta table datasets/gov/aaa/juros_mariu_monitoringas/SpTersalaiV (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/SpTersalaiV"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L127"
    last_modified: "2026-11-11T14:39:20Z"
---

# SpTersalaiV — Specifinių teršalų tyrimai Kuršių marių ir Baltijos jūros vandenyje

- **Model:** `datasets/gov/aaa/juros_mariu_monitoringas/SpTersalaiV`[^manifest]
- **Dataset:** [datasets/gov/aaa/juros_mariu_monitoringas](../juros_mariu_monitoringas.md) (`datasets/gov/aaa/juros_mariu_monitoringas`)
- **Manifest CSV:** [datasets/gov/aaa/juros_mariu_monitoringas.csv#L127](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/juros_mariu_monitoringas.csv#L127)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/juros_mariu_monitoringas/SpTersalaiV`
- **Primary Key (`ref`):** `reg_nr`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_nr` | `string` | — | `2` | `open` | — | Tyrimo registracijos numeris | Registracijos nr. nėra unikalus |
| `data` | `datetime` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |
| `telkinio_pav` | `string` | — | `3` | `open` | — | Vandens telkinio pavadinimas | — |
| `m_vietos_kodas` | `string` | — | `3` | `open` | — | Monitoringo vietos kodas | — |
| `m_vietos_pav` | `string` | — | `3` | `open` | — | Monitoringo vietos pavadinimas | — |
| `m_koordinate` | `geometry(point, 3346)` | — | `3` | `open` | — | Monitoringo vietos koordinatės (LKS-94) | — |
| `tyrim_objektas` | `string` | — | `3` | `open` | — | Tyrimų objektas | — |
| `horizontas` | `string` | — | `3` | `open` | — | Vandens sluoksnis, iš kurio paimtas mėginys | — |
| `gylis` | `number` | `m` | `4` | `open` | — | Gylis, iš kurio paimtas mėginys, metrais | — |
| `parametro_pav` | `string` | — | `3` | `open` | — | Tiriamo parametro pavadinimas | — |
| `maziau_ribos` | `boolean` | — | `4` | `open` | — | Simbolis "<", žymintis, kad rezultatas yra žemiau kiekybinio įvertinimo ribos | — |
| `rezultatas` | `number` | — | `4` | `open` | — | Parametro tyrimo rezultatas | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Matavimo vienetai | — |
| `tyr_metodas` | `string` | — | `2` | `open` | — | Tyrimų metodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/juros_mariu_monitoringas.csv
