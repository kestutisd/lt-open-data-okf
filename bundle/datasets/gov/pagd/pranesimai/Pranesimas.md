---
type: Table
title: "Pranesimas — Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius"
description: "Informacija apie trumpąsias žinutės informuojančias gyventojus apie grėsmę keliančius įvykius ir jų zonas"
resource: "https://get.data.gov.lt/datasets/gov/pagd/pranesimai/Pranesimas"
tags: [gov, pagd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pagd/pranesimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/pranesimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pranesimas — Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius

Informacija apie trumpąsias žinutės informuojančias gyventojus apie grėsmę keliančius įvykius ir jų zonas

- **Model:** `datasets/gov/pagd/pranesimai/Pranesimas`[^manifest]
- **Dataset:** [Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius](../pranesimai.md) (`datasets/gov/pagd/pranesimai`)
- **Manifest CSV:** [datasets/gov/pagd/pranesimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/pranesimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/pranesimai/Pranesimas`
- **Primary Key (`ref`):** `issiustu_pranesimu_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `issiustu_pranesimu_id` | `string` | — | `4` | `open` | — | Išsisųstų pranešimų identifikatorius | — |
| `ivykio_data` | `datetime` | `1S` | `4` | `open` | — | Įvykio data | — |
| `siunciamu_pranesimu_pradzia` | `datetime` | `1S` | `4` | `open` | — | Siunčiamų pranešimų pradžios laikas | — |
| `siunciamu_pranesimu_pabaiga` | `datetime` | `1S` | `4` | `open` | — | Siunčiamų pranešimų pabaigos laikas | — |
| `pranesimo_tekstas_lt` | `string` | — | `4` | `open` | — | Siunčiamo pranešimo tekstas lietuvių kalba | — |
| `ivykio_vietoves_aprasymas_lt` | `string` | — | `4` | `open` | — | Įvykio vietovės aprašymas | — |
| `informacijos_saltinis` | `string` | — | `4` | `open` | — | Informacijos šaltinis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pranesimo_tekstas_lt` | `update(property: "pranesimo_tekstas_lt@lt", type: "text")` | `type` | — | — | — | — | — |
| `ivykio_vietoves_aprasymas_lt` | `update(property: "ivykio_vietoves_aprasymas_lt@lt", type: "text")` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/pranesimai.csv
