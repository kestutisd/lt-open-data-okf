---
type: Dataset
title: "Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys"
description: "Vilniaus miesto viešojo transporto keleivių skaičiavimo sistemos DILAX duomenys"
resource: "https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai"
tags: [gov, sp, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys

Vilniaus miesto viešojo transporto keleivių skaičiavimo sistemos DILAX duomenys

- **Namespace:** `datasets/gov/sp/keleiviu_srautai`[^manifest]
- **Manifest CSV:** [datasets/gov/sp/keleiviu_srautai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai`
- **Parent Namespace (`ns`):** Vilniaus miesto SĮ „Susisiekimo paslaugos“ (`datasets/gov/sp`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kelione](keleiviu_srautai/Kelione.md) | — | `4` | `reiso_id` | — | 10 | Lentelėje pateikiama bendra informacija apie reisą – maršruto grafiko pavadinimas bei pradžia ir pabaiga |
| [Stotele](keleiviu_srautai/Stotele.md) | — | `4` | `keliones_stoteles_id` | — | 20 | Lentelėje pateikiamas detalus keleivių skaičius kiekvienoje reiso stotelėje |
| [TransportoPriemone](keleiviu_srautai/TransportoPriemone.md) | — | `4` | `tp_id` | — | 6 | Lentelėje pateikiamos, reiso metu naudotos, keleivių vežimo priemonės |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv
