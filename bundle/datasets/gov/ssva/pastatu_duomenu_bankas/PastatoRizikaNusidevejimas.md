---
type: Table
title: "PastatoRizikaNusidevejimas"
description: "Informacija apie pastatų charakteristikas, pastatų ir jų elementų būklę."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoRizikaNusidevejimas"
tags: [gov, ssva, pastatorizikanusidevejimas, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4143/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/pastatu_duomenu_bankas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PastatoRizikaNusidevejimas

**Dataset Context:** Informacija apie pastatų charakteristikas, pastatų ir jų elementų būklę.[^manifest]

- **Model:** `datasets/gov/ssva/pastatu_duomenu_bankas/PastatoRizikaNusidevejimas`[^manifest]
- **Dataset:** [Pastatų ir jo elementų nusidėvėjimas ir rizikos](../pastatu_duomenu_bankas.md) (`datasets/gov/ssva/pastatu_duomenu_bankas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoRizikaNusidevejimas` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `objekto_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objekto_id` | `string` | — | `4` | `open` | — | Pastato identifikatorius | — |
| `nusidevejimo_balas` | `number` | — | `4` | `open` | — | Pastato nusidėvvėjimo balas | — |
| `rizikos_balas` | `number` | — | `4` | `open` | — | Pastato rizikos balas | — |
| `statybos_metai` | `integer` | — | `4` | `open` | — | Pastato statybos metai | — |
| `adresas` | `string` | — | `4` | `open` | — | Pastato adresas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Pastato vietos koordinatės LKS-94 (EPSG:3346) sistemoje | — |
| `iraso_sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L33)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/pastatu_duomenu_bankas (https://data.gov.lt/datasets/4143/)
