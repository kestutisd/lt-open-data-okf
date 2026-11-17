---
type: Table
title: "Pastatas — Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys"
description: "Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/pastatas/Pastatas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/pastatas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/pastatas.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pastatas — Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys

Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/pastatas/Pastatas`[^manifest]
- **Dataset:** [Adresų registras](../pastatas.md) (`datasets/gov/rc/ar/pastatas`)
- **Manifest CSV:** [datasets/gov/rc/ar/pastatas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/pastatas.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/pastatas/Pastatas`
- **Primary Key (`ref`):** `aob_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurios teritorijoje yra statinys arba žemės sklypas, identifikavimo kodas | — |
| `aob_kodas` | `ref` | [/datasets/gov/rc/ar/adresai/Adresas](../adresai/Adresas.md) | `4` | `open` | — | Statinio arba žemės sklypo identifikavimo kodas | — |
| `gyvenamoji_vietove` | `ref` | [/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove](../gyvenamojivietove/GyvenamojiVietove.md) | `4` | `open` | — | Gyvenamosios vietovės, kuriai priklauso adresas, identifikavimo kodas | — |
| `gatve` | `ref` | [/datasets/gov/rc/ar/gatve/Gatve](../gatve/Gatve.md) | `4` | `open` | — | Gatvės, kuriai priklauso adresas, identifikavimo kodas | — |
| `nr` | `string` | — | `4` | `open` | — | Žemės sklypo ir (ar) pastato numeris gatvėje arba gyvenamojoje vietovėje | — |
| `korpuso_nr` | `string` | — | `4` | `open` | — | Korpuso numeris | — |
| `pasto_kodas` | `string` | — | `4` | `open` | — | Pašto kodas | — |
| `aob_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/pastatas.csv
