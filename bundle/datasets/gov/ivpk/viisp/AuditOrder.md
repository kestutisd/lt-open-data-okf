---
type: Table
title: "AuditOrder — Užsakymų lenta"
description: "Kiekvieno užsakymu metu yra sukuriamas įrašas."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/viisp/AuditOrder"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# AuditOrder — Užsakymų lenta

Kiekvieno užsakymu metu yra sukuriamas įrašas. Jeigu paslauga išorinė, sukuriamas įrašas ir prie service_id lieka null. Jeigu paslauga vidinė, užsakymo metu sukuriamas įrašas ir prie service_id nurodomas vidinės paslaugos ID

- **Model:** `datasets/gov/ivpk/viisp/AuditOrder`[^manifest]
- **Dataset:** [datasets/gov/ivpk/viisp](../viisp.md) (`datasets/gov/ivpk/viisp`)
- **Manifest CSV:** [datasets/gov/ivpk/viisp.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/viisp/AuditOrder`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Unikalus užsakymo ID | — |
| `order_date` | `datetime` | `S` | `4` | `open` | — | Užsakymo data | — |
| `service_description` | `ref` | [ServiceDescription](ServiceDescription.md) | `4` | `open` | — | Paslaugos aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv
