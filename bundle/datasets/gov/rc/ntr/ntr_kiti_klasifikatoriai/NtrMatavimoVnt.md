---
type: Table
title: "NtrMatavimoVnt — NTR matavimo vienetai"
description: "Spinta table datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrMatavimoVnt (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrMatavimoVnt"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrMatavimoVnt — NTR matavimo vienetai

- **Model:** `datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrMatavimoVnt`[^manifest]
- **Dataset:** [Kiti NTR klasifikatoriai](../ntr_kiti_klasifikatoriai.md) (`datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrMatavimoVnt`
- **Primary Key (`ref`):** `vien_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vien_kodas` | `integer` | — | `4` | `open` | — | Matavimo vieneto kodas | — |
| `vien_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `vien_zyme` | `string` | — | `4` | `open` | — | Matavimo vieneto žymė aplikacijose | — |
| `vien_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `vien_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `vien_zyme_en` | `string` | — | `4` | `open` | — | Matavimo vieneto žymė aplikacijose angliškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv
