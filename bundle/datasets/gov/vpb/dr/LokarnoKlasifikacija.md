---
type: Table
title: "LokarnoKlasifikacija — Dizainų Lokarno klasifikacijos"
description: "Lentelė „Dizainų Lokarno klasifikacijos“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/dr/LokarnoKlasifikacija"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/dr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L32"
    last_modified: "2026-11-11T14:39:20Z"
---

# LokarnoKlasifikacija — Dizainų Lokarno klasifikacijos

Lentelė „Dizainų Lokarno klasifikacijos“. Lentelę sudaro: dizaino ir paraiškos numeriai, Lokarno klasifikacijos kodas ir jo semantinis apibūdinimas. Vienas įrašas atitinka vieną unikalią dizaino numerio ir Lokarno klasifikacijos kodo kombinaciją.

- **Model:** `datasets/gov/vpb/dr/LokarnoKlasifikacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos dizainų duomenys](../dr.md) (`datasets/gov/vpb/dr`)
- **Manifest CSV:** [datasets/gov/vpb/dr.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L32)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/dr/LokarnoKlasifikacija`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus indentifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos paraiškos numeris | — |
| `lokarno_klasifikacija` | `string` | — | `4` | `open` | — | Lokarno klasifikacijos kodas | — |
| `klasifikacijos_apibudinimas` | `string` | — | `4` | `open` | — | Lokarno klasifikacijos kodo apibūdinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/dr.csv
