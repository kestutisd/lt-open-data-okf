---
type: Table
title: "Vaidmuo — Vaidmenys"
description: "Lentelė „Vaidmenys“."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops/Vaidmuo"
tags: [gov, rvul, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L93"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vaidmuo — Vaidmenys

Lentelė „Vaidmenys“. Lentelę sudaro operacijos, procedūros bei mediko identifikatoriai ir vaidmuo. Vienas lentelės įrašas atitinka vieną operacijos, procedūros, mediko ir jo vaidmens kombinaciją.

- **Model:** `datasets/gov/rvul/hops/Vaidmuo`[^manifest]
- **Dataset:** [Pacientams atliktų operacijų duomenys](../hops.md) (`datasets/gov/rvul/hops`)
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L93](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L93)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops/Vaidmuo`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `operacijos_id` | `string` | — | `4` | `open` | — | Išorinis raktas į operaciją | — |
| `proceduros_id` | `string` | — | `4` | `open` | — | Išorinis raktas į procedūrą | — |
| `mediko_id` | `string` | — | `4` | `open` | — | Išorinis raktas į mediką | — |
| `vaidmuo` | `string` | — | `4` | `open` | — | Mediko vaidmuo operacijos procedūroje | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vaidmuo` | `"Instrumentatorius"` | — | — | Instrumentatorius | — |
| `vaidmuo` | `"Padėjėjas"` | — | — | Padėjėjas | — |
| `vaidmuo` | `"Asistentas"` | — | — | Asistentas | — |
| `vaidmuo` | `"Operatorius"` | — | — | Operatorius | — |
| `vaidmuo` | `"Anesteziologas"` | — | — | Anesteziologas | — |
| `vaidmuo` | `"Anestezistas"` | — | — | Anestezistas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv
