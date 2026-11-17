---
type: Dataset
title: "datasets/gov/vlk/otp_sumos"
description: "Spinta dataset datasets/gov/vlk/otp_sumos (5 tables)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/otp_sumos"
tags: [gov, vlk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vlk/otp_sumos

- **Namespace:** `datasets/gov/vlk/otp_sumos`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/otp_sumos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/otp_sumos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Uzsakymas](otp_sumos/Uzsakymas.md) | Mokamos sumos už ortopedijos technines ir medicinos priemones | `4` | `ad_id` | — | 5 | Informacija apie PSDF biudžeto išlaidas ortopedijos techninėms priemonėms |
| [Tipas](otp_sumos/Tipas.md) | Ortopedijos techninių ir medicinos priemonių tipai | `4` | `ad_id` | — | 2 | Informacija apie ortopedijos techninių ir medicinos priemonių tipus |
| [Grupe](otp_sumos/Grupe.md) | Ortopedijos techninių ir medicinos priemonių tipai | `4` | `ad_id` | — | 4 | Informacija apie ortopedijos techninių ir medicinos priemonių tipus |
| [Klase](otp_sumos/Klase.md) | Ortopedijos techninių ir medicinos priemonių klasė | `4` | `ad_id` | — | 3 | Informacija apie ortopedijos techninių ir medicinos priemonių klases |
| [Istaiga](otp_sumos/Istaiga.md) | Įstaigų sąrašas | `4` | `istg_id` | — | 1 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv
