---
type: Table
title: "Liga — Augalų ligų katalogas"
description: "Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos ligų katalogas"
resource: "https://get.data.gov.lt/datasets/gov/lzukt/Liga"
tags: [gov, lzukt, liga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L19"
    title: "atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv#L19"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3922/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lzukt"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Liga — Augalų ligų katalogas

Integruotos augalų apsaugos informavimo, konsultavimo ir mokymų informacinė sistemos ligų katalogas[^manifest]

- **Model:** `datasets/gov/lzukt/Liga`[^manifest]
- **Dataset:** [Lietuvos žemės ūkio konsultavimo tarnyba](../lzukt.md) (`datasets/gov/lzukt`)[^manifest]
- **Manifest CSV:** [datasets/gov/lzukt/ikmis.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L19)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lzukt/Liga` (`deployed`)[^manifest]
- **Provider:** `lzukt` — Lietuvos žemės ūkio konsultavimo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus kenkėjo identifikatorius | — |
| `liga` | `string` | — | `4` | `open` | — | Kenkėjo pavadinimas | — |
| `liga_lot` | `string` | — | `4` | `open` | — | Kenkėjo pavadinimas lotyniškai | — |
| `sritis` | `string` | — | `4` | `open` | — | Kenkėjo priklausomybė sričiai | — |
| `grupe` | `string` | — | `4` | `open` | — | Kenkėjo grupė | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Kenkėjo aprašymas | — |
| `palankios_plisti_salygos` | `string` | — | `4` | `open` | — | Kenkėjui plisti palankios salygos | — |
| `zalingumo_riba` | `string` | — | `4` | `open` | — | Žalingumo riba | — |
| `kontroles_priemones` | `string` | — | `4` | `open` | — | Kontrolinės priemonės | — |
| `kokius_augalus_pazeidzia` | `string` | — | `4` | `open` | — | Aprašymas, kokius augalus pažeidžia | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lzukt/ikmis.csv#L19 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lzukt/ikmis.csv#L19)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lzukt (https://data.gov.lt/datasets/3922/)
