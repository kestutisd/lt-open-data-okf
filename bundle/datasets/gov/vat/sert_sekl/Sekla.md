---
type: Table
title: "Sekla — Pateikiama informacija apie sertifikuotos sėklos augalo rūšį, veislę, kategoriją, kiekį, kg"
description: "Spinta table datasets/gov/vat/sert_sekl/Sekla (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/sert_sekl/Sekla"
tags: [gov, vat, sekla, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r20_sert_sekl.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r20_sert_sekl.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1876/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/sert_sekl"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sekla — Pateikiama informacija apie sertifikuotos sėklos augalo rūšį, veislę, kategoriją, kiekį, kg

- **Model:** `datasets/gov/vat/sert_sekl/Sekla`[^manifest]
- **Dataset:** [Ataskaita apie sertifikuotos sėklos kiekį (kg) ir kokybę](../sert_sekl.md) (`datasets/gov/vat/sert_sekl`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r20_sert_sekl.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r20_sert_sekl.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/sert_sekl/Sekla` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `grupe` | `string` | — | `4` | `open` | — | Augalo grupė | — |
| `rusis` | `string` | — | `3` | `open` | — | Augalo rūšies pavadinimas | — |
| `veisle` | `string` | — | `4` | `open` | — | Augalo veislės pavadinimas | — |
| `kategorija` | `string` | — | `3` | `open` | — | Kategorijos kodas | — |
| `kiekis` | `number` | `U` | `4` | `open` | — | Sėklos kiekis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `grupe` | `"Javai"` | — | — | — | — |
| `grupe` | `"Pašariniai augalai"` | — | — | — | — |
| `grupe` | `"Aliejiniai ir pluoštiniai augalai"` | — | — | — | — |
| `grupe` | `"Sėjamieji grikiai"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r20_sert_sekl.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r20_sert_sekl.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/sert_sekl (https://data.gov.lt/datasets/1876/)
