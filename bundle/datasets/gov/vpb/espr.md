---
type: Dataset
title: "Lietuvoje įsigalioję Europos patentai"
description: "Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vpb/espr"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvoje įsigalioję Europos patentai

Lietuvos Respublikos patentų registre nuo 2002 m. kaupiami ir iki šiol atnaujinami nacionalinių bei Lietuvoje įsigaliojusių Europos patentų duomenys. Duomenų rinkinyje nuo 1994 m. kaupiami ir iki šiol atnaujinami Lietuvoje įsigaliojusių Europos patentų duomenys. Bendras rinkinys sudarytas iš trijų lentelių: „Lietuvoje įsigaliojusių Europos patentų bylos“, „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“ ir „Lietuvoje įsigaliojusių Europos patentų klasifikacija“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras.

- **Namespace:** `datasets/gov/vpb/espr`[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/es_pr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/espr`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Byla](espr/Byla.md) | Lietuvoje įsigaliojusių Europos patentų bylos | `4` | `patento_numeris` | — | 8 | Lentelė „Lietuvoje įsigaliojusių Europos patentų bylos“. |
| [Asmuo](espr/Asmuo.md) | Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys | — | `vda_prime_key` | — | 6 | Lentelė „Lietuvoje įsigaliojusiems Europos patentams priskirti asmenys“. |
| [Klasifikacija](espr/Klasifikacija.md) | Lietuvoje įsigaliojusių Europos patentų klasifikacija | — | `vda_prime_key` | — | 5 | Lentelė „Lietuvoje įsigaliojusių Europos patentų klasifikacija“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv
