---
type: Table
title: "Vaidmuo — Vaidmenys"
description: "Lentelė „Vaidmenys“. Lentelę sudaro operacijos, procedūros bei mediko identifikatoriai ir vaidmuo."
resource: "https://get.data.gov.lt/datasets/gov/rvul/hops/Vaidmuo"
tags: [gov, rvul, vaidmuo, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L93"
    title: "atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L93"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3865/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rvul/hops"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vaidmuo — Vaidmenys

Lentelė „Vaidmenys“. Lentelę sudaro operacijos, procedūros bei mediko identifikatoriai ir vaidmuo. Vienas lentelės įrašas atitinka vieną operacijos, procedūros, mediko ir jo vaidmens kombinaciją.[^manifest]

- **Model:** `datasets/gov/rvul/hops/Vaidmuo`[^manifest]
- **Dataset:** [Pacientams atliktų operacijų duomenys](../hops.md) (`datasets/gov/rvul/hops`)[^manifest]
- **Manifest CSV:** [datasets/gov/rvul/hops.csv#L93](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L93)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rvul/hops/Vaidmuo` (`deployed`)[^manifest]
- **Provider:** `rvul` — VšĮ Respublikinė Vilniaus universitetinė ligoninė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `operacijos_id` | `string` | — | `4` | `open` | — | Išorinis raktas į operaciją | — |
| `proceduros_id` | `string` | — | `4` | `open` | — | Išorinis raktas į procedūrą | — |
| `mediko_id` | `string` | — | `4` | `open` | — | Išorinis raktas į mediką | — |
| `vaidmuo` | `string` | — | `4` | `open` | — | Mediko vaidmuo operacijos procedūroje | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vaidmuo` | `"Instrumentatorius"` | — | — | Instrumentatorius | — |
| `vaidmuo` | `"Padėjėjas"` | — | — | Padėjėjas | — |
| `vaidmuo` | `"Asistentas"` | — | — | Asistentas | — |
| `vaidmuo` | `"Operatorius"` | — | — | Operatorius | — |
| `vaidmuo` | `"Anesteziologas"` | — | — | Anesteziologas | — |
| `vaidmuo` | `"Anestezistas"` | — | — | Anestezistas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rvul/hops.csv#L93 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rvul/hops.csv#L93)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rvul/hops (https://data.gov.lt/datasets/3865/)
