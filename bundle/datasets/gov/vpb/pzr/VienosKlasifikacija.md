---
type: Table
title: "VienosKlasifikacija — Prekių ženklų Vienos klasifikacijos"
description: "Lentelė „Prekių ženklų Vienos klasifikacijos“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/pzr/VienosKlasifikacija"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/pzr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L41"
    last_modified: "2026-11-11T14:39:20Z"
---

# VienosKlasifikacija — Prekių ženklų Vienos klasifikacijos

Lentelė „Prekių ženklų Vienos klasifikacijos“. Lentelę sudaro: prekės ženklo registracijos ir paraiškos numeriai, Vienos klasifikacijos sekcija ir jos semantinis apibūdinimas. Vienas įrašas atitinka vieną unikalią prekės ženklo registracijos, paraiškos numerių ir Vienos klasifikacijos sekcijos kombinaciją.

- **Model:** `datasets/gov/vpb/pzr/VienosKlasifikacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos prekių ženklai](../pzr.md) (`datasets/gov/vpb/pzr`)
- **Manifest CSV:** [datasets/gov/vpb/pzr.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L41)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/pzr/VienosKlasifikacija`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos paraiškos numeris | — |
| `sekcija` | `string` | — | `4` | `open` | — | Vienos klasifikacijos sekcija | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Vienos klasifikacijos sekcijos aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/pzr.csv
