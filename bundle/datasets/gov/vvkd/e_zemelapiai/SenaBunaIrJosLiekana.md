---
type: Table
title: "SenaBunaIrJosLiekana — Senų būnu ir jų liekanų geoerdviniai duomenys"
description: "Šiame sluoksnyje pateikiami senų būnu ir jų liekanų geoerdviniai duomenys Nemune atkarpoje nuo Jurbarko iki Nemuno žiočių."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/SenaBunaIrJosLiekana"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L114"
    last_modified: "2026-11-11T14:39:20Z"
---

# SenaBunaIrJosLiekana — Senų būnu ir jų liekanų geoerdviniai duomenys

Šiame sluoksnyje pateikiami senų būnu ir jų liekanų geoerdviniai duomenys Nemune atkarpoje nuo Jurbarko iki Nemuno žiočių.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/SenaBunaIrJosLiekana`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L114](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L114)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/SenaBunaIrJosLiekana`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `konstr` | `string` | — | `4` | `open` | — | Bunos konstrukcijos tipas | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto ilgis | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `konstr` | `"Akmeninė"` | — | — | Akmeninė | — |
| `konstr` | `"Smelinė-Žvyrinė"` | — | — | Akmeninė Smelinė-Žvyrinė | — |
| `konstr` | `"Gruntinė"` | — | — | Gruntinė | — |
| `konstr` | `"Smėlio-žvyro"` | — | — | Smėlio-žvyro | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
