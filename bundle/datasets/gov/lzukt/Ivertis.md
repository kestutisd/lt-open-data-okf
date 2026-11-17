---
type: Table
title: "Ivertis — Augalų kenksmingų organizmų plitimo žalingumo įverčiai"
description: "Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos augalų kenksmingų organizmų plitimo žalingumo įverčiai"
resource: "https://get.data.gov.lt/datasets/gov/lzukt/Ivertis"
tags: [gov, lzukt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# Ivertis — Augalų kenksmingų organizmų plitimo žalingumo įverčiai

Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos augalų kenksmingų organizmų plitimo žalingumo įverčiai

- **Model:** `datasets/gov/lzukt/Ivertis`[^manifest]
- **Dataset:** [Lietuvos žemės ūkio konsultavimo tarnyba](../lzukt.md) (`datasets/gov/lzukt`)
- **Manifest CSV:** [datasets/gov/lzukt/ikmis.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lzukt/Ivertis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv
