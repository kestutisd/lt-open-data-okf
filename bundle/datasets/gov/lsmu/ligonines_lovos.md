---
type: Dataset
title: "Lietuvos sveikatos universiteto Kauno klinikų Lovų duomenys"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami lovų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos"
tags: [gov, lsmu, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos sveikatos universiteto Kauno klinikų Lovų duomenys

Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami lovų duomenys. Rinkinyje pateikiama lovų vietos informacija – vietos kodas, lygmuo, tipas, aprašymas; taip pat Įstaigos duomenys – juridinio asmens kodas ir pavadinimas. Atkreipiame dėmesį, kad šis rinkinys negali būti naudojamas oficialiai statistikai rengti, kadangi dalis lovų duomenų tikslinami rankiniu būdu. Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/lsmu/ligonines_lovos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/ligonines_lovos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsmu/ligonines_lovos` (`deployed`)[^manifest]
- **Provider:** `lsmu` — Lietuvos sveikatos mokslų universitetas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LovosVieta](ligonines_lovos/LovosVieta.md) | Lovų vietų duomenys | — | `vietos_id` | — | `9` | — |
| [LovosStatusas](ligonines_lovos/LovosStatusas.md) | Lovų užimtumo duomenys | — | `vda_prime_key` | — | `6` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/ligonines_lovos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/ligonines_lovos.csv#L2)
