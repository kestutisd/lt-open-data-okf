---
type: Dataset
title: "Pacientams atliktų laboratorinių tyrimų rezultatai"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami LSMULKK laboratorijoje atliktų tyrimų, jų užsakymų ir atsakymų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsmu/lab_tyrimai"
tags: [gov, lsmu, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsmu/lab_tyrimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/lab_tyrimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pacientams atliktų laboratorinių tyrimų rezultatai

Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami LSMULKK laboratorijoje atliktų tyrimų, jų užsakymų ir atsakymų duomenys. Rinkinyje pateikiama pacientų informacija: pseudonimizuotas asmens kodas, gimimo metai, lytis, tyrimų duomenys – tyrimo grupė, užsakymo laikas, pavadinimas, trumpinys; taip pat tyrimų atsakymai – rezultato reikšmė, tipas, matavimo vienetai, normos ir jų ribos. Duomenyse asmenų gimimo metai „triukšminti“ (gimimo metai nurodomi su +-1 metų paklaida). Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos.

- **Namespace:** `datasets/gov/lsmu/lab_tyrimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/lab_tyrimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/lab_tyrimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsmu/lab_tyrimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LaboratorinisTyrimas](lab_tyrimai/LaboratorinisTyrimas.md) | LSMU Kauno Klinikų laboratorijoje pacientams atliktų laboratorinių tyrimų rezultatai | — | `vda_prime_key` | — | 20 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/lab_tyrimai.csv
