---
type: Dataset
title: "Šiukšliavežių maršrutai"
description: "Duomenų rinkinyje pateikiami šiukšliavežių maršrutų duomenys: šifruotas automobilio valstybinis numeris, automobilio markė, laikas ir koordinatės, nurodančios vietą, kurioje tuo metu buvo automobilis."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/marsrutai"
tags: [gov, asmlis, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/marsrutai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Šiukšliavežių maršrutai

Duomenų rinkinyje pateikiami šiukšliavežių maršrutų duomenys: šifruotas automobilio valstybinis numeris, automobilio markė, laikas ir koordinatės, nurodančios vietą, kurioje tuo metu buvo automobilis.

- **Namespace:** `datasets/gov/asmlis/marsrutai`[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/marsrutai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/marsrutai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/marsrutai`
- **Parent Namespace (`ns`):** MOKESTA ir ASMLIS sistemos (`datasets/gov/asmlis`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SalcininkuSiuksliavezioMarsrutas](marsrutai/SalcininkuSiuksliavezioMarsrutas.md) | Šalčininkų rajono šiukšliavežių maršrutai | `4` | `vda_prime_key` | — | 12 | Šalčininkų rajono savivaldybės administracijos informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. |
| [KedainiuSiuksliavezioMarsrutas](marsrutai/KedainiuSiuksliavezioMarsrutas.md) | Kėdainių rajono šiukšliavežių maršrutai | `4` | `vda_prime_key` | — | 10 | Kėdainių rajono savivaldybės administracijos informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. |
| [KaunoSvaraSiuksliavezioMarsrutas](marsrutai/KaunoSvaraSiuksliavezioMarsrutas.md) | UAB Kauno švara šiukšliavežių maršrutai | `4` | `vda_prime_key` | — | 10 | UAB Kauno švara informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. |
| [VilniausRajSiuksliavezioMarsrutas](marsrutai/VilniausRajSiuksliavezioMarsrutas.md) | Vilniaus rajono savivaldybės šiukšliavežių maršrutai | `4` | `vda_prime_key` | — | 10 | Vilniaus rajono savivaldybės informacinėje sistemoje MOKESTA kaupiami atliekų tvarkymo rinkliavų duomenys ir kitus duomenis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/marsrutai.csv
