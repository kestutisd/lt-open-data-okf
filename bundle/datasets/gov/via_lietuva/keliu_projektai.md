---
type: Dataset
title: "Duomenys apie valstybinės reikšmės kelių projektus"
description: "Duomenų rinkinyje pateikiami AB „Via Lietuva“ duomenys apie užsakomus valstybinės reikšmės kelių projektavimo, tiesimo, statybos, rekonstravimo, taisymo (remonto) ir priežiūros darbų projektus, finansuojamus iš Lietuvos Respublikos..."
resource: "https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai"
tags: [gov, via_lietuva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/via_lietuva/keliu_projektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Duomenys apie valstybinės reikšmės kelių projektus

Duomenų rinkinyje pateikiami AB „Via Lietuva“ duomenys apie užsakomus valstybinės reikšmės kelių projektavimo, tiesimo, statybos, rekonstravimo, taisymo (remonto) ir priežiūros darbų projektus, finansuojamus iš Lietuvos Respublikos kelių priežiūros ir plėtros programos bei Europos Sąjungos paramos lėšų. Duomenų rinkinį sudaro dvi lentelės:

1. „Kelių projektų darbai“ – informacija apie kelių atkarpose vykdomus darbus,

2. „Kelio darbų atkarpos“ – informacija apie kelio atkarpas.

Duomenų teikėjas – AB „Via Lietuva“.

Duomenys kaupiami nuo 2004 m.

- **Namespace:** `datasets/gov/via_lietuva/keliu_projektai`[^manifest]
- **Manifest CSV:** [datasets/gov/via_lietuva/keliu_projektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/via_lietuva/keliu_projektai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/via_lietuva/keliu_projektai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KelioDarbuProjektas](keliu_projektai/KelioDarbuProjektas.md) | „Kelių projektų darbai“ | `4` | `vda_prime_key` | — | 19 | Duomenys apie valstybinės reikšmės keliuose vykstančius kelio darbų projektus. |
| [KelioAtkarpa](keliu_projektai/KelioAtkarpa.md) | „Kelio darbų atkarpos“ | `4` | `atkarpos_id` | — | 5 | Duomenys apie kelių atkarpas, kuriose vykdomi kelių darbų projektai. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/via_lietuva/keliu_projektai.csv
