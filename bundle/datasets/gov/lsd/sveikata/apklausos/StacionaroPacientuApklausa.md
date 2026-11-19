---
type: Table
title: "StacionaroPacientuApklausa — Stacionaro pacientų anoniminės apklausos"
description: "Anketų, pateiktų pacientams po gydymo stacionare, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos/StacionaroPacientuApklausa"
tags: [gov, lsd, stacionaropacientuapklausa, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3902/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/apklausos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# StacionaroPacientuApklausa — Stacionaro pacientų anoniminės apklausos

Anketų, pateiktų pacientams po gydymo stacionare, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais.[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/apklausos/StacionaroPacientuApklausa`[^manifest]
- **Dataset:** [Pacientų anoniminės apklausos](../apklausos.md) (`datasets/gov/lsd/sveikata/apklausos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos/StacionaroPacientuApklausa` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/apklausos (https://data.gov.lt/datasets/3902/)
