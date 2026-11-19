---
type: Table
title: "PastatoElementoRizika"
description: "Informacija apie pastatų charakteristikas, pastatų ir jų elementų būklę."
resource: "https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoRizika"
tags: [gov, ssva, pastatoelementorizika, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4143/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/pastatu_duomenu_bankas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PastatoElementoRizika

**Dataset Context:** Informacija apie pastatų charakteristikas, pastatų ir jų elementų būklę.[^manifest]

- **Model:** `datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoRizika`[^manifest]
- **Dataset:** [Pastatų ir jo elementų nusidėvėjimas ir rizikos](../pastatu_duomenu_bankas.md) (`datasets/gov/ssva/pastatu_duomenu_bankas`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/pastatu_duomenu_bankas/PastatoElementoRizika` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `rizikos_vertinimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rizikos_vertinimo_id` | `string` | — | `4` | `open` | — | Rizikos vertinimo įrašo unikalus identifikatorius | — |
| `objekto_id` | `string` | — | `4` | `open` | — | Pastato identifikatorius | — |
| `statybos_metai` | `integer` | — | `4` | `open` | — | Pastato statybos metai | — |
| `elemento_pavadinimas` | `string` | — | `4` | `open` | — | Pastato elemento pavadinimas | — |
| `rizikos_balas` | `string` | — | `4` | `open` | — | Pastato elemento rizikos vertinimo balas | — |
| `ivertinimo_balas` | `string` | — | `4` | `open` | — | Apžiūros ar vertinimo metu suteiktas balas | — |
| `didziausias_galimas_balas` | `string` | — | `4` | `open` | — | Didžiausias galimas vertinimo balas | — |
| `ar_kritinis` | `string` | — | `4` | `open` | — | Požymis, ar rizikos vertinimas yra kritinis | — |
| `kategorijos_pavadinimas` | `string` | — | `4` | `open` | — | Vertinimo kategorijos pavadinimas | — |
| `dokumento_numeris` | `string` | — | `4` | `open` | — | Dokumento numeris | — |
| `apziuros_tipas` | `string` | — | `4` | `open` | — | Pastato elemento apžiūros tipas | — |
| `adresas` | `string` | — | `4` | `open` | — | Pastato adresas | — |
| `geometrija_adp` | `geometry(point, 3346)` | — | `4` | `open` | — | Pastato vietos koordinatės LKS-94 (EPSG:3346) sistemoje | — |
| `sukurimo_data` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/pastatu_duomenu_bankas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/pastatu_duomenu_bankas (https://data.gov.lt/datasets/4143/)
