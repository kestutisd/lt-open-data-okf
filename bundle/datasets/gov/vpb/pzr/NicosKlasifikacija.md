---
type: Table
title: "NicosKlasifikacija — Prekių ženklų Nicos klasifikacijos"
description: "Lentelė „Prekių ženklų Nicos klasifikacijos“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/pzr/NicosKlasifikacija"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/pzr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L48"
    last_modified: "2026-11-11T14:39:20Z"
---

# NicosKlasifikacija — Prekių ženklų Nicos klasifikacijos

Lentelė „Prekių ženklų Nicos klasifikacijos“. Lentelę sudaro: prekės ženklo registracijos ir paraiškos numeriai, Nicos klasifikacinis kodas ir jam priskirti terminai. Vienas įrašas atitinka vieną unikalią prekės ženklo registracijos, paraiškos numerių ir Nicos klasifikacinio kodo kombinaciją.

- **Model:** `datasets/gov/vpb/pzr/NicosKlasifikacija`[^manifest]
- **Dataset:** [Lietuvos Respublikos prekių ženklai](../pzr.md) (`datasets/gov/vpb/pzr`)
- **Manifest CSV:** [datasets/gov/vpb/pzr.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L48)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/pzr/NicosKlasifikacija`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Prekės ženklo bylos paraiškos numeris | — |
| `klases_kodas` | `string` | — | `4` | `open` | — | Nicos klasifikacijos klasės kodas | — |
| `klases_terminai` | `string` | — | `4` | `open` | — | Nicos klasifikacijos klasės terminai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/pzr.csv
