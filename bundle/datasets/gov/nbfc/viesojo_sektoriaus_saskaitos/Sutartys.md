---
type: Table
title: "Sutartys — Sutartys"
description: "Viešųjų pirkimų sutarčių informacija"
resource: "https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Sutartys"
tags: [gov, nbfc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L43"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartys — Sutartys

Viešųjų pirkimų sutarčių informacija

- **Model:** `datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Sutartys`[^manifest]
- **Dataset:** [Viešojo sektoriaus sąskaitų administravimo bendroji informacinė sistema](../viesojo_sektoriaus_saskaitos.md) (`datasets/gov/nbfc/viesojo_sektoriaus_saskaitos`)
- **Manifest CSV:** [datasets/gov/nbfc/sabis.csv#L43](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nbfc/sabis.csv#L43)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nbfc/viesojo_sektoriaus_saskaitos/Sutartys`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikatorius | — |
| `sutarties_uid` | `string` | — | `4` | `open` | — | Unikalus sutarties identifikatorius | — |
| `vp_id` | `string` | — | `4` | `open` | — | Viešųjų pirkimų sutarties identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `sutarties_numeris` | `string` | — | `4` | `open` | — | Viešųjų pirkimų sutarties numeris | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Sutarties pavadinimas | — |
| `cpv_kodas` | `string` | — | `4` | `open` | — | Sutarties Bendrąjį Viešųjų Pirkimų Žodyno kodas | — |
| `cpv_pav` | `string` | — | `4` | `open` | — | Sutarties Bendrąjį Viešųjų Pirkimų Žodyno kodo pavadinimas | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Sutarties įsigaliojimo data | — |
| `sutarties_galiojimo_data` | `date` | `D` | `4` | `open` | — | Sutarties galiojima data | — |
| `suma` | `number` | — | `4` | `open` | — | Sutarties suma eurais | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nbfc/sabis.csv
