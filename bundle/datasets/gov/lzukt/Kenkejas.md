---
type: Table
title: "Kenkejas — Augalų kenkėjų katalogas"
description: "Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos kenkėjų katalogas"
resource: "https://get.data.gov.lt/datasets/gov/lzukt/Kenkejas"
tags: [gov, lzukt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kenkejas — Augalų kenkėjų katalogas

Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos kenkėjų katalogas

- **Model:** `datasets/gov/lzukt/Kenkejas`[^manifest]
- **Dataset:** [Lietuvos žemės ūkio konsultavimo tarnyba](../lzukt.md) (`datasets/gov/lzukt`)
- **Manifest CSV:** [datasets/gov/lzukt/ikmis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lzukt/Kenkejas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kenkėjo identifikatorius | — |
| `kenkejas` | `string` | — | `4` | `open` | — | Kenkėjo pavadinimas | — |
| `kenkejas_lot` | `string` | — | `4` | `open` | — | Kenkėjo pavadinimas lotyniškai | — |
| `sritis` | `string` | — | `4` | `open` | — | Kenkėjo priklausomybė sričiai | — |
| `grupe` | `string` | — | `4` | `open` | — | Kenkėjo grupė | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Kenkėjo aprašymas | — |
| `palankios_plisti_salygos` | `string` | — | `4` | `open` | — | Kenkėjui plisti palankios salygos | — |
| `zalingumo_riba` | `string` | — | `4` | `open` | — | Žalingumo riba | — |
| `kontroles_priemones` | `string` | — | `4` | `open` | — | Kontrolinės priemonės | — |
| `kokius_augalus_pazeidzia` | `string` | — | `4` | `open` | — | Aprašymas, kokius augalus pažeidžia | — |
| `atsparumo_valdymas` | `string` | — | `4` | `open` | — | Aprašymas, kaip valdyti atsparumą kenkėjui | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv
