---
type: Table
title: "Pastaba — Vyriausybės atstovų pastabos savivaldybių taryboms"
description: "Lentelėje pateikiamos Vyriausybės atstovų teikiamos pastabos savivaldybių taryboms dėl sprendimų projektų atitikties centrinės valdžios teisės aktams."
resource: "https://get.data.gov.lt/datasets/gov/vai/pastabos_savivaldybiu_taryboms/Pastaba"
tags: [gov, vai, pastaba, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2816/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vai/pastabos_savivaldybiu_taryboms"
    author: "team:vda"
    last_modified: "2026-05-07T00:00:00Z"
---

# Pastaba — Vyriausybės atstovų pastabos savivaldybių taryboms

Lentelėje pateikiamos Vyriausybės atstovų teikiamos pastabos savivaldybių taryboms dėl sprendimų projektų atitikties centrinės valdžios teisės aktams. Informacija apie pastabas pateikiama nuo 2024 metų atnaujinant kas ketvirtį. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vai/pastabos_savivaldybiu_taryboms/Pastaba`[^manifest]
- **Dataset:** [Vyriausybės atstovų pastabos savivaldybių taryboms](../pastabos_savivaldybiu_taryboms.md) (`datasets/gov/vai/pastabos_savivaldybiu_taryboms`)[^manifest]
- **Manifest CSV:** [datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vai/pastabos_savivaldybiu_taryboms/Pastaba` (`deployed`)[^manifest]
- **Provider:** `vai` — Vyriausybės atstovų įstaiga *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-05-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vai/pastabos_savivaldybiu_taryboms.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vai/pastabos_savivaldybiu_taryboms (https://data.gov.lt/datasets/2816/)
