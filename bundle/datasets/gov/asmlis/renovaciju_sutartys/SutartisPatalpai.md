---
type: Table
title: "SutartisPatalpai — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų sutartys patalpoms."
description: "Viena renovacijos sutarčių patalpoms lentelės eilutė atitinka vieną renovacijos sutartį butui ar kitos paskirties patalpai pastate"
resource: "https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/SutartisPatalpai"
tags: [gov, asmlis, sutartispatalpai, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L27"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv#L27"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3880/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/renovaciju_sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SutartisPatalpai — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių...

Viena renovacijos sutarčių patalpoms lentelės eilutė atitinka vieną renovacijos sutartį butui ar kitos paskirties patalpai pastate[^manifest]

- **Model:** `datasets/gov/asmlis/renovaciju_sutartys/SutartisPatalpai`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”...](../renovaciju_sutartys.md) (`datasets/gov/asmlis/renovaciju_sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/renovaciju_sutartys.csv#L27](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L27)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/SutartisPatalpai` (`deployed`)[^manifest]
- **Provider:** `asmlis` — MOKESTA ir ASMLIS sistemos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv#L27 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L27)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/renovaciju_sutartys (https://data.gov.lt/datasets/3880/)
