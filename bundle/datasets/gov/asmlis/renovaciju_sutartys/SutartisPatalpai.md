---
type: Table
title: "SutartisPatalpai — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų sutartys..."
description: "Viena renovacijos sutarčių patalpoms lentelės eilutė atitinka vieną renovacijos sutartį butui ar kitos paskirties patalpai pastate"
resource: "https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/SutartisPatalpai"
tags: [gov, asmlis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L27"
    last_modified: "2026-11-11T14:39:20Z"
---

# SutartisPatalpai — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų sutartys...

Viena renovacijos sutarčių patalpoms lentelės eilutė atitinka vieną renovacijos sutartį butui ar kitos paskirties patalpai pastate

- **Model:** `datasets/gov/asmlis/renovaciju_sutartys/SutartisPatalpai`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų sutartys.](../renovaciju_sutartys.md) (`datasets/gov/asmlis/renovaciju_sutartys`)
- **Manifest CSV:** [datasets/gov/asmlis/renovaciju_sutartys.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L27)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/SutartisPatalpai`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus pirminis raktas | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Renovacijos sutarties identifikatorius | — |
| `ren_sutart_tipas` | `string` | — | `4` | `open` | — | Renovacijos sutarties tipas | — |
| `ren_sutart_data` | `date` | — | `4` | `open` | — | Renovacijos sutarties data | — |
| `sutarties_subjektas` | `string` | — | `4` | `open` | — | Renovacijos sutarties subjektas | — |
| `aob_kodas` | `string` | — | `4` | `open` | — | Renovuojamos patalpos aob kodas | — |
| `pask_pav` | `string` | — | `4` | `open` | — | Renovuojamos patalpos paskrities pavadinimas | — |
| `bendras_plotas` | `number` | — | `4` | `open` | — | Renovuojamos patalpos bendrasis plotas | — |
| `gyven_plotas` | `number` | — | `4` | `open` | — | Renovuojamo patalpos gyvenamasis plotas | — |
| `akto_suma` | `number` | — | `4` | `open` | — | Akto suma | — |
| `kredito_suma` | `number` | — | `4` | `open` | — | Kredito suma | — |
| `atidetos_palukanos` | `number` | — | `4` | `open` | — | Atidėtos palūkanos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv
