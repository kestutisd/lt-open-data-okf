---
type: Table
title: "InkstoTransplantacija — Inkstų transplantacijų duomenys"
description: "Pacientams atliktų inkstų transplantacijų (intervencijos ACHI kodas 36503-00) datos (mėnesio tikslumu)"
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoTransplantacija"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58"
    last_modified: "2026-11-11T14:39:20Z"
---

# InkstoTransplantacija — Inkstų transplantacijų duomenys

Pacientams atliktų inkstų transplantacijų (intervencijos ACHI kodas 36503-00) datos (mėnesio tikslumu)

- **Model:** `datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoTransplantacija`[^manifest]
- **Dataset:** [Pacientų, kuriems atlikta inkstų biopsija, duomenys](../inkstu_biopsijos.md) (`datasets/gov/lsd/sveikata/inkstu_biopsijos`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L58)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoTransplantacija`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius, kuri sudaro stulpeliai - asmens_kodas, transpl_data |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `transpl_eiles_nr` | `integer` | — | `4` | `open` | — | Transplantacijos eilės numeris | Rodiklis, nurodantis, kelintą kartą atlikta transplantacija |
| `transpl_data` | `date` | `M` | `4` | `open` | — | Transplantacijos atlikimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv
