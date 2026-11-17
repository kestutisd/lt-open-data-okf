---
type: Dataset
title: "Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų sutartys."
description: "Savivaldybių MOKESTA ir ASMLIS sistemų duomenys"
resource: "https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys"
tags: [gov, asmlis, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų sutartys.

- **Namespace:** `datasets/gov/asmlis/renovaciju_sutartys`[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/renovaciju_sutartys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys`
- **Parent Namespace (`ns`):** MOKESTA ir ASMLIS sistemos (`datasets/gov/asmlis`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SutartisBendra](renovaciju_sutartys/SutartisBendra.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų bendros sutartys. | `4` | `vda_prime_key` | — | 18 | Viena bendrų renovacijos sutarčių lentelės eilutė atitinka vieną renovacijos sutartį daugiabučiui ar kitos paskirties pastatui. |
| [SutartisPatalpai](renovaciju_sutartys/SutartisPatalpai.md) | Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų sutartys patalpoms. | `4` | `vda_prime_key` | — | 12 | Viena renovacijos sutarčių patalpoms lentelės eilutė atitinka vieną renovacijos sutartį butui ar kitos paskirties patalpai pastate |
| [Darbas](renovaciju_sutartys/Darbas.md) | Renovacijos darbų klasifikatorius | `4` | `darbo_tipo_kodas` | — | 3 | Viena renovacijos darbų klasifikatoriaus eilutė atitinka vieno renovacijos darbo pavadinimą |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv
