---
type: Table
title: "StacionaroPacientuApklausa — Stacionaro pacientų anoniminės apklausos"
description: "Anketų, pateiktų pacientams po gydymo stacionare, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos/StacionaroPacientuApklausa"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# StacionaroPacientuApklausa — Stacionaro pacientų anoniminės apklausos

Anketų, pateiktų pacientams po gydymo stacionare, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais.

- **Model:** `datasets/gov/lsd/sveikata/apklausos/StacionaroPacientuApklausa`[^manifest]
- **Dataset:** [Pacientų anoniminės apklausos](../apklausos.md) (`datasets/gov/lsd/sveikata/apklausos`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos/StacionaroPacientuApklausa`
- **Primary Key (`ref`):** `vda_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `pa_id` | `string` | — | `4` | `open` | — | Anketos kodas | — |
| `kk_pavadinimas` | `string` | — | `4` | `open` | — | Klausimo tekstas | — |
| `ka_atsakymas` | `string` | — | `4` | `open` | — | Paciento pasirinkto atsakymo tekstas | — |
| `pa_fo_pavadinimas` | `string` | — | `4` | `open` | — | Gydymo įstaigos pavadinimas | — |
| `pav_lpk_2012` | `string` | — | `4` | `open` | — | Sveikatos priežiūros specialisto kvalifikacija | — |
| `pa_vizito_data` | `datetime` | `S` | `4` | `open` | — | Paciento išrašymo data UTC laiku | — |
| `pa_uzpildymo_data` | `datetime` | `S` | `4` | `open` | — | Anketos užpildymo data UTC laiku | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv
