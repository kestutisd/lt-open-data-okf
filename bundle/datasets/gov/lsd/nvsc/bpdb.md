---
type: Dataset
title: "Biocidinių produktų duomenys"
description: "Nacionalinio visuomenės sveikatos centro naudojamoje Biocidinių produktų duomenų bazėje (toliau – BPDB) nuo 1999 m. balandžio 12 d. kaupiami duomenys apie biocidinius produktus ir jiems išduotus biocidinių produktų autorizacijos liudijimus."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Biocidinių produktų duomenys

Nacionalinio visuomenės sveikatos centro naudojamoje Biocidinių produktų duomenų bazėje (toliau – BPDB) nuo 1999 m. balandžio 12 d. kaupiami duomenys apie biocidinius produktus ir jiems išduotus biocidinių produktų autorizacijos liudijimus. Rinkinys sudarytas iš lentelių „Produktai“, „Produktų veikliosios medžiagos“ ir „Produktų liudijimai“. Svarbu atkreipti dėmesį, kad tai nėra oficialūs statistiniai duomenys, todėl gali būti netikslumų. Duomenų teikėjas – Nacionalinis visuomenės sveikatos centras.

- **Namespace:** `datasets/gov/lsd/nvsc/bpdb`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/nvsc/bpdb.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Produktas](bpdb/Produktas.md) | Produktai | `4` | `produkto_id` | — | 5 | Lentelė „Produktai“. |
| [VeikliojiMedziaga](bpdb/VeikliojiMedziaga.md) | Produktų veikliosios medžiagos | `4` | `vda_prime_key` | — | 6 | Lentelė „Produktų veikliosios medžiagos“. |
| [Liudijimas](bpdb/Liudijimas.md) | Produktų liudijimai | `4` | `vda_prime_key` | — | 6 | Lentelė „Produktų liudijimai“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv
