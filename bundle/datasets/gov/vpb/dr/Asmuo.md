---
type: Table
title: "Asmuo — Dizainams priskirti asmenys"
description: "Lentelė „Dizainams priskirti asmenys“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/dr/Asmuo"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/dr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# Asmuo — Dizainams priskirti asmenys

Lentelė „Dizainams priskirti asmenys“. Lentelę sudaro: dizaino ir paraiškos numeriai, priskirto juridinio asmens pavadinimas arba fizinio asmens vardas ir pavardė, asmens tipas, vaidmuo dizaine, pateiktas adresas ir šalis. Vienas įrašas atitinka vieną unikalią dizaino numerio, asmens ir jo vaidmens dizaine kombinaciją. Įstaigos prašymu, duomenys apie dizainerio vaidmenį turinčius asmenis buvo neįtraukti.

- **Model:** `datasets/gov/vpb/dr/Asmuo`[^manifest]
- **Dataset:** [Lietuvos Respublikos dizainų duomenys](../dr.md) (`datasets/gov/vpb/dr`)
- **Manifest CSV:** [datasets/gov/vpb/dr.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/dr/Asmuo`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus indentifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos paraiškos numeris | — |
| `asmuo` | `string` | — | `4` | `open` | — | Dizainui priskirto fizinio asmens vardas su pavarde arba juridinio asmens pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Dizainui priskirto asmens tipas | — |
| `vaidmuo` | `string` | — | `4` | `open` | — | Dizainui priskirto asmens vaidmuo | — |
| `salis` | `string` | — | `4` | `open` | — | Dizainui priskirto asmens adresas | — |
| `adresas` | `string` | — | `4` | `open` | — | Dizainui priskirto asmens šalis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Fizinis"` | — | `open` | Fizinis asmuo | — |
| `tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `vaidmuo` | `"Pareiškėjas"` | — | `open` | — | — |
| `vaidmuo` | `"Atstovas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/dr.csv
