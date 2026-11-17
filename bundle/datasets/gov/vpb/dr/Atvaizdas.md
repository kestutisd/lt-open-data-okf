---
type: Table
title: "Atvaizdas — Dizainų atvaizdai"
description: "Lentelė „Dizainų atvaizdai“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/dr/Atvaizdas"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/dr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L39"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atvaizdas — Dizainų atvaizdai

Lentelė „Dizainų atvaizdai“. Lentelę sudaro: dizaino ir paraiškos numeriai ir dizaino atvaizdo pavyzdžio internetinė nuoroda. Kiekvienas dizainas gali turėti po keletą atvaizdų, o kiekvienas atvaizdas – po keletą pavyzdžių (paveikslėlių). Vienas įrašas atitinka vieną internetinę nuorodą.

- **Model:** `datasets/gov/vpb/dr/Atvaizdas`[^manifest]
- **Dataset:** [Lietuvos Respublikos dizainų duomenys](../dr.md) (`datasets/gov/vpb/dr`)
- **Manifest CSV:** [datasets/gov/vpb/dr.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L39)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/dr/Atvaizdas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus indentifikatorius | — |
| `registracijos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos registracijos numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Dizaino bylos paraiškos numeris | — |
| `atvaizdo_nuoroda` | `string` | — | `4` | `open` | — | Dizaino pavyzdžių vaizdų internetinė nuoroda | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/dr.csv
