---
type: Table
title: "AmbulatorijosPacientuApklausa — Ambulatorijos pacientų anoniminės apklausos"
description: "Anketų, pateiktų pacientams po gautų ambulatorinių paslaugų, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos/AmbulatorijosPacientuApklausa"
tags: [gov, lsd, ambulatorijospacientuapklausa, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3902/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/apklausos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AmbulatorijosPacientuApklausa — Ambulatorijos pacientų anoniminės apklausos

Anketų, pateiktų pacientams po gautų ambulatorinių paslaugų, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais.[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/apklausos/AmbulatorijosPacientuApklausa`[^manifest]
- **Dataset:** [Pacientų anoniminės apklausos](../apklausos.md) (`datasets/gov/lsd/sveikata/apklausos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos/AmbulatorijosPacientuApklausa` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kodas | — |
| `apklausos_id` | `string` | — | `4` | `open` | — | Anketos kodas | — |
| `klausimas` | `string` | — | `4` | `open` | — | Klausimo tekstas | — |
| `atsakymu_variantai` | `string` | — | `4` | `open` | — | Paciento pasirinkto atsakymo tekstas | — |
| `istaiga` | `string` | — | `4` | `open` | — | Gydymo įstaigos pavadinimas | — |
| `kvalifikacija` | `string` | — | `4` | `open` | — | Sveikatos priežiūros specialisto kvalifikacija | — |
| `paslauga` | `string` | — | `4` | `open` | — | Paslaugos pavadinimas | — |
| `vizito_data` | `datetime` | `S` | `4` | `open` | — | Paciento vizito data UTC laiku | — |
| `uzpildymo_data` | `datetime` | `S` | `4` | `open` | — | Anketos užpildymo data UTC laiku | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L17)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/apklausos (https://data.gov.lt/datasets/3902/)
