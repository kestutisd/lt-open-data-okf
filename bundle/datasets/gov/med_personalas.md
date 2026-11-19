---
type: Dataset
title: "Lietuvos sveikatos universiteto Kauno klinikų medicininio personalo etatai"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami dirbančio medicininio personalo tarnybiniai duomenys: darbuotojo pseudonimizuotas asmens kodas, lytis, gimimo metai, darbuotojui priskirtas skyrius..."
resource: "https://get.data.gov.lt/datasets/gov/med_personalas"
tags: [gov, med_personalas, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsmu/med_personalas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos sveikatos universiteto Kauno klinikų medicininio personalo etatai

Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami dirbančio medicininio personalo tarnybiniai duomenys: darbuotojo pseudonimizuotas asmens kodas, lytis, gimimo metai, darbuotojui priskirtas skyrius, pareigos, darbo pradžios ir pabaigos datos. Atkreipiame dėmesį, kad Kauno klinikose darbuotojų duomenys tvarkomi rankiniu būdų, todėl duomenyse gali atsirasti neatitikimų. Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/med_personalas`[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/med_personalas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/med_personalas` (`deployed`)[^manifest]
- **Provider:** `med_personalas`[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MedPersonalas](med_personalas/MedPersonalas.md) | Medicininio personalo etatai | — | `vda_prime_key` | — | `12` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/med_personalas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/med_personalas.csv#L2)
