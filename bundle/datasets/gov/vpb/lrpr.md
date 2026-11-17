---
type: Dataset
title: "Lietuvos Respublikoje registruoti patentai"
description: "Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vpb/lrpr"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos Respublikoje registruoti patentai

Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys. Duomenų rinkinį sudaro nuo 1992 m. kaupiami ir iki šiol atnaujinami nacionalinių patentų duomenys. Bendras rinkinys sudarytas iš trijų lentelių: „Lietuvoje registruoti patentai“, „Lietuvoje registruotiems patentams priskirti asmenys“ ir „Lietuvoje registruotų patentų klasifikacija“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras.

- **Namespace:** `datasets/gov/vpb/lrpr`[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/lr_pr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/lrpr`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Byla](lrpr/Byla.md) | Lietuvoje registruoti patentai | `4` | `patento_nr` | — | 12 | Lentelė „Lietuvoje registruoti patentai“. |
| [Asmuo](lrpr/Asmuo.md) | Lietuvoje registruotiems patentams priskirti asmenys | — | `vda_prime_key` | — | 8 | Lentelė „Lietuvoje registruotiems patentams priskirti asmenys“. |
| [Klasifikacija](lrpr/Klasifikacija.md) | Lietuvoje registruotų patentų klasifikacija | — | `vda_prime_key` | — | 6 | Lentelė „Lietuvoje registruotų patentų klasifikacija“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv
