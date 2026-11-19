---
type: Table
title: "Pranesimas — Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius"
description: "Informacija apie trumpąsias žinutės informuojančias gyventojus apie grėsmę keliančius įvykius ir jų zonas"
resource: "https://get.data.gov.lt/datasets/gov/pagd/pranesimai/Pranesimas"
tags: [gov, pagd, pranesimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/pranesimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/pagd/pranesimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2939/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/pranesimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pranesimas — Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius

Informacija apie trumpąsias žinutės informuojančias gyventojus apie grėsmę keliančius įvykius ir jų zonas[^manifest]

- **Model:** `datasets/gov/pagd/pranesimai/Pranesimas`[^manifest]
- **Dataset:** [Žinutės informuojančias gyventojus apie grėsmę keliančius įvykius](../pranesimai.md) (`datasets/gov/pagd/pranesimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/pranesimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/pranesimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/pranesimai/Pranesimas` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `issiustu_pranesimu_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/pranesimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/pranesimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/pranesimai (https://data.gov.lt/datasets/2939/)
