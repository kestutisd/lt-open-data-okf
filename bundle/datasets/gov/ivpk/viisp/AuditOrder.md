---
type: Table
title: "AuditOrder — Užsakymų lenta"
description: "Kiekvieno užsakymu metu yra sukuriamas įrašas."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/viisp/AuditOrder"
tags: [gov, ivpk, auditorder, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L22"
    title: "atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv#L22"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# AuditOrder — Užsakymų lenta

Kiekvieno užsakymu metu yra sukuriamas įrašas. Jeigu paslauga išorinė, sukuriamas įrašas ir prie service_id lieka null. Jeigu paslauga vidinė, užsakymo metu sukuriamas įrašas ir prie service_id nurodomas vidinės paslaugos ID[^manifest]

- **Model:** `datasets/gov/ivpk/viisp/AuditOrder`[^manifest]
- **Dataset:** [datasets/gov/ivpk/viisp](../viisp.md) (`datasets/gov/ivpk/viisp`)[^manifest]
- **Manifest CSV:** [datasets/gov/ivpk/viisp.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L22)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/viisp/AuditOrder` (`deployed`)[^manifest]
- **Provider:** `ivpk` — Valstybės skaitmeninių sprendimų agentūra (VSSA, buv. IVPK) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Unikalus užsakymo ID | — |
| `order_date` | `datetime` | `S` | `4` | `open` | — | Užsakymo data | — |
| `service_description` | `ref` | [ServiceDescription](ServiceDescription.md) (`level=4 UUID`: `service_description._id`) | `4` | `open` | — | Paslaugos aprašymas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv#L22 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L22)
