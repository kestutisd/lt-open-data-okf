---
type: Dataset
title: "Lietuvos Respublikos dizainų duomenys"
description: "Lietuvos Respublikos dizainų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių dizainų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vpb/dr"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/dr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos Respublikos dizainų duomenys

Lietuvos Respublikos dizainų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių dizainų duomenys. Duomenų rinkinį sudaro nuo 1993 m. kaupiami ir iki šiol atnaujinami duomenys. Bendras rinkinys sudarytas iš keturių lentelių: „Dizainai“, „Dizainams priskirti asmenys“, „Dizainų Lokarno klasifikacijos“ ir „Dizainų atvaizdai“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras.

- **Namespace:** `datasets/gov/vpb/dr`[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/dr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/dr.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/dr`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dizainas](dr/Dizainas.md) | Dizainai | — | `vda_prime_key` | — | 10 | Lentelė „Dizainai“. |
| [Asmuo](dr/Asmuo.md) | Dizainams priskirti asmenys | — | — | — | 8 | Lentelė „Dizainams priskirti asmenys“. |
| [LokarnoKlasifikacija](dr/LokarnoKlasifikacija.md) | Dizainų Lokarno klasifikacijos | — | — | — | 5 | Lentelė „Dizainų Lokarno klasifikacijos“. |
| [Atvaizdas](dr/Atvaizdas.md) | Dizainų atvaizdai | — | — | — | 4 | Lentelė „Dizainų atvaizdai“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/dr.csv
