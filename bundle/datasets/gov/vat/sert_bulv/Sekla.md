---
type: Table
title: "Sekla — Pateikiama informacija apie sertifikuotos bulvių sėklos veislę, kategoriją / klasę, kiekį, kg"
description: "Spinta table datasets/gov/vat/sert_bulv/Sekla (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/sert_bulv/Sekla"
tags: [gov, vat, sekla, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r19_sertif_bulv.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r19_sertif_bulv.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1875/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/sert_bulv"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Sekla — Pateikiama informacija apie sertifikuotos bulvių sėklos veislę, kategoriją / klasę, kiekį, kg

- **Model:** `datasets/gov/vat/sert_bulv/Sekla`[^manifest]
- **Dataset:** [Ataskaita apie sertifikuotos bulvių sėklos kiekį (kg) ir kokybę](../sert_bulv.md) (`datasets/gov/vat/sert_bulv`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r19_sertif_bulv.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r19_sertif_bulv.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/sert_bulv/Sekla` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `veisle` | `string` | — | `4` | `open` | — | Augalo veislės pavadinimas | — |
| `kategorija` | `string` | — | `3` | `open` | — | Kategorijos kodas | — |
| `kiekis` | `number` | `U` | `4` | `open` | — | Sėklos kiekis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r19_sertif_bulv.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r19_sertif_bulv.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/sert_bulv (https://data.gov.lt/datasets/1875/)
