---
type: Dataset
title: "Nesuformuoti žemės plotai"
description: "Duomenis apie sklypais nesuformuotus žemės plotus bei su jais susijusius prašymus, pateiktus žemės informacinėje sistemoje."
resource: "https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme"
tags: [gov, ssva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nesuformuoti žemės plotai

Duomenis apie sklypais nesuformuotus žemės plotus bei su jais susijusius prašymus, pateiktus žemės informacinėje sistemoje.

- **Namespace:** `datasets/gov/ssva/nesuformuota_zeme`[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/nesuformuota_zeme.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NesuformuotasPlotas](nesuformuota_zeme/NesuformuotasPlotas.md) | Nesuformuoti žemės plotai | `4` | `vda_prime_key` | — | 13 | Duomenų rinkinys apima informaciją apie valstybės valdomus, bet dar nesuformuotus žemės plotus. |
| [Prasymas](nesuformuota_zeme/Prasymas.md) | Nekilnojamojo turto (nesuformuotų plotų) prašymų duomenys | `4` | `vda_prime_key` | — | 13 | Duomenų rinkinys apima informaciją apie fizinių ar juridinių asmenų prašymus, susijusius su nesuformuotais žemės plotais. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv
