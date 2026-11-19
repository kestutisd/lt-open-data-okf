---
type: Table
title: "Ivertis — Augalų kenksmingų organizmų plitimo žalingumo įverčiai"
description: "Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos augalų kenksmingų organizmų plitimo žalingumo įverčiai"
resource: "https://get.data.gov.lt/datasets/gov/lzukt/Ivertis"
tags: [gov, lzukt, ivertis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L31"
    title: "atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv#L31"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3922/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lzukt"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Ivertis — Augalų kenksmingų organizmų plitimo žalingumo įverčiai

Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos augalų kenksmingų organizmų plitimo žalingumo įverčiai[^manifest]

- **Model:** `datasets/gov/lzukt/Ivertis`[^manifest]
- **Dataset:** [Lietuvos žemės ūkio konsultavimo tarnyba](../lzukt.md) (`datasets/gov/lzukt`)[^manifest]
- **Manifest CSV:** [datasets/gov/lzukt/ikmis.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L31)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lzukt/Ivertis` (`deployed`)[^manifest]
- **Provider:** `lzukt` — Lietuvos žemės ūkio konsultavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus stebėjimo identifikatorius | — |
| `stebejimo_data` | `date` | `D` | `4` | `open` | — | Stebėjimo data | — |
| `augalo_pavadinimas` | `string` | — | `4` | `open` | — | Stebėto augalo pavadinimas | — |
| `ligos_kenkejo_pavadinimas` | `string` | — | `4` | `open` | — | Aptiktos ligos ar kenkėjo pavadinimas | — |
| `ligos_kenkejo_pavadinimas_lot` | `string` | — | `4` | `open` | — | Aptiktos ligos ar kenkėjo pavadinimas lotyniškai | — |
| `zalingumo_ivertis` | `integer` | — | `4` | `open` | — | Žalingumo įvertis | — |
| `pazeidimo_lygis` | `string` | — | `4` | `open` | — | Augalų pažeidimo lygis | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kuriuoje atlikti stebėjimai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv#L31 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L31)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lzukt (https://data.gov.lt/datasets/3922/)
