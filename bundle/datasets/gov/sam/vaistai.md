---
type: Dataset
title: "Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys"
description: "Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos pagalbos priemonių (MPP) įtraukimo į kompensuojamųjų sąrašus."
resource: "https://get.data.gov.lt/datasets/gov/sam/vaistai"
tags: [gov, sam, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sam/vaistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/vaistai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys

Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos pagalbos priemonių (MPP) įtraukimo į kompensuojamųjų sąrašus. Šie duomenys suteikia galimybę stebėti sveikatos technologijų vertinimo (STV) procesą ir priimamus sprendimus dėl kompensavimo.

STV paraiškų duomenis teikia Valstybinė vaistų kontrolės tarnyba (VVKT). MPP duomenys gaunami iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos (VASPVT) duomenų bazių.

Šio rinkinio duomenis galima praturtinti jungiant su VVKT atvertu rinkiniu (duomenys jungiami per stulpelį „paraiskos_numeris“): https://data.gov.lt/datasets/2897/.

- **Namespace:** `datasets/gov/sam/vaistai`[^manifest]
- **Manifest CSV:** [datasets/gov/sam/vaistai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sam/vaistai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sam/vaistai`
- **Parent Namespace (`ns`):** Lietuvos Respublikos sveikatos apsaugos ministerija (`datasets/gov/sam`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paraiska](vaistai/Paraiska.md) | Paraiškų dėl vaistinių preparatų ar medicinos pagalbos priemonių įrašymo į kompensavimo sąrašus svarstymo duomenys | `4` | `vda_prime_key` | — | 13 | Lietuvos Respublikos sveikatos apsaugos ministerija (LR SAM) renka ir skelbia duomenis apie svarstomas paraiškas dėl vaistinių preparatų ir medicinos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/sam/vaistai.csv
