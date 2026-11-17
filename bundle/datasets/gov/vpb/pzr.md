---
type: Dataset
title: "Lietuvos Respublikos prekių ženklai"
description: "Lietuvos Respublikos prekių ženklų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių prekių ženklų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vpb/pzr"
tags: [gov, vpb, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/pzr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos Respublikos prekių ženklai

Lietuvos Respublikos prekių ženklų registre nuo 2014 m. kaupiami ir iki šiol atnaujinami Lietuvoje galiojančių prekių ženklų duomenys. Duomenų rinkinį sudaro nuo 1991 m. kaupiami ir iki šiol atnaujinami prekių ženklų duomenys. Bendras rinkinys sudarytas iš keturių lentelių: „Prekių ženklai“, „Prekių ženklams priskirti asmenys“, „Prekių ženklų Vienos klasifikacijos“ ir „Prekių ženklų Nicos klasifikacijos“. Duomenų teikėjas – Lietuvos Respublikos valstybinis patentų biuras.

- **Namespace:** `datasets/gov/vpb/pzr`[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/pzr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/pzr.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/pzr`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PrekesZenklas](pzr/PrekesZenklas.md) | Prekių ženklai | — | `vda_prime_key` | — | 12 | Lentelė „Prekių ženklai“. |
| [Asmuo](pzr/Asmuo.md) | Prekių ženklams priskirti asmenys | — | `vda_prime_key` | — | 8 | Lentelė „Prekių ženklams priskirti asmenys“. |
| [VienosKlasifikacija](pzr/VienosKlasifikacija.md) | Prekių ženklų Vienos klasifikacijos | — | `vda_prime_key` | — | 5 | Lentelė „Prekių ženklų Vienos klasifikacijos“. |
| [NicosKlasifikacija](pzr/NicosKlasifikacija.md) | Prekių ženklų Nicos klasifikacijos | — | `vda_prime_key` | — | 5 | Lentelė „Prekių ženklų Nicos klasifikacijos“. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/pzr.csv
