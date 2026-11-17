---
type: Dataset
title: "Lietuvos sveikatos universiteto Kauno klinikų medicininio personalo etatai"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami dirbančio medicininio personalo tarnybiniai duomenys: darbuotojo pseudonimizuotas asmens kodas, lytis, gimimo..."
resource: "https://get.data.gov.lt/datasets/gov/med_personalas"
tags: [gov, med_personalas, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsmu/med_personalas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos sveikatos universiteto Kauno klinikų medicininio personalo etatai

Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami dirbančio medicininio personalo tarnybiniai duomenys: darbuotojo pseudonimizuotas asmens kodas, lytis, gimimo metai, darbuotojui priskirtas skyrius, pareigos, darbo pradžios ir pabaigos datos. Atkreipiame dėmesį, kad Kauno klinikose darbuotojų duomenys tvarkomi rankiniu būdų, todėl duomenyse gali atsirasti neatitikimų. Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos.

- **Namespace:** `datasets/gov/med_personalas`[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/med_personalas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/med_personalas`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MedPersonalas](med_personalas/MedPersonalas.md) | Medicininio personalo etatai | — | `vda_prime_key` | — | 12 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/med_personalas.csv
