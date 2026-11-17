---
type: Table
title: "Pastaba — Vyriausybės atstovų pastabos savivaldybių taryboms"
description: "Lentelėje pateikiamos Vyriausybės atstovų teikiamos pastabos savivaldybių taryboms dėl sprendimų projektų atitikties centrinės valdžios teisės aktams."
resource: "https://get.data.gov.lt/datasets/gov/vai/pastabos_savivaldybiu_taryboms/Pastaba"
tags: [gov, vai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pastaba — Vyriausybės atstovų pastabos savivaldybių taryboms

Lentelėje pateikiamos Vyriausybės atstovų teikiamos pastabos savivaldybių taryboms dėl sprendimų projektų atitikties centrinės valdžios teisės aktams. Informacija apie pastabas pateikiama nuo 2024 metų atnaujinant kas ketvirtį.

- **Model:** `datasets/gov/vai/pastabos_savivaldybiu_taryboms/Pastaba`[^manifest]
- **Dataset:** [Vyriausybės atstovų pastabos savivaldybių taryboms](../pastabos_savivaldybiu_taryboms.md) (`datasets/gov/vai/pastabos_savivaldybiu_taryboms`)
- **Manifest CSV:** [datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vai/pastabos_savivaldybiu_taryboms/Pastaba`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `pastabos_pateikimo_data` | `datetime` | `S` | `4` | `open` | — | Pastabos pateikimo data | — |
| `vai_biuras` | `string` | — | `4` | `open` | — | Vyriausybės atstovų įstaigos biuras | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kuriai teikta pastaba | — |
| `teises_srities_tema` | `string` | — | `4` | `open` | — | Teisės srities tema | — |
| `sprendimo_projektas` | `string` | — | `4` | `open` | — | Sprendimo projektas (data, numeris, pavadinimas), dėl kurio teikiamos pastabos | — |
| `pastaba` | `string` | — | `4` | `open` | — | Teiktos pastabos turinys | — |
| `savivaldybes_tarybos_veiksmai` | `string` | — | `4` | `open` | — | Savivaldybės tarybos veiksmai | — |
| `vyriausybes_atstovo_veiksmai` | `string` | — | `4` | `open` | — | Vyriausybės atstovo planuojami veiksmai, kai į teiktas pastabas neatsižvelgta | — |
| `vyriausybes_atstovas` | `string` | — | `4` | `open` | — | Vyriausybės atstovas | — |
| `dokumento_pav` | `string` | — | `4` | `open` | — | Duomenų failo pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv
