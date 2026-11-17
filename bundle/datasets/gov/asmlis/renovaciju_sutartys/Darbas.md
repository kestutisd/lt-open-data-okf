---
type: Table
title: "Darbas — Renovacijos darbų klasifikatorius"
description: "Viena renovacijos darbų klasifikatoriaus eilutė atitinka vieno renovacijos darbo pavadinimą"
resource: "https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/Darbas"
tags: [gov, asmlis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L41"
    last_modified: "2026-11-11T14:39:20Z"
---

# Darbas — Renovacijos darbų klasifikatorius

Viena renovacijos darbų klasifikatoriaus eilutė atitinka vieno renovacijos darbo pavadinimą

- **Model:** `datasets/gov/asmlis/renovaciju_sutartys/Darbas`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų sutartys.](../renovaciju_sutartys.md) (`datasets/gov/asmlis/renovaciju_sutartys`)
- **Manifest CSV:** [datasets/gov/asmlis/renovaciju_sutartys.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L41)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/Darbas`
- **Primary Key (`ref`):** `darbo_tipo_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `darbo_tipo_kodas` | `string` | — | `4` | `open` | — | Renovacijos darbo tipo kodas | — |
| `darbo_pavadinimas` | `string` | — | `4` | `open` | — | Renovacijos darbo pavadinimas | — |
| `paskut_redagav_data` | `datetime` | `L` | `4` | `open` | — | Renovacijos darbų paskutinio redagavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv
