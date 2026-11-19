---
type: Table
title: "SutartisBendra — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių savivaldybes ir joms pavaldžias įstaigas, vartotojų renovacijų bendros sutartys."
description: "Viena bendrų renovacijos sutarčių lentelės eilutė atitinka vieną renovacijos sutartį daugiabučiui ar kitos paskirties pastatui."
resource: "https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/SutartisBendra"
tags: [gov, asmlis, sutartisbendra, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3880/"
    title: "data.gov.lt DCAT-AP — datasets/gov/asmlis/renovaciju_sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SutartisBendra — Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”, aptarnaujančių...

Viena bendrų renovacijos sutarčių lentelės eilutė atitinka vieną renovacijos sutartį daugiabučiui ar kitos paskirties pastatui.[^manifest]

- **Model:** `datasets/gov/asmlis/renovaciju_sutartys/SutartisBendra`[^manifest]
- **Dataset:** [Aptarnavimo ir atsiskaitymo už suteiktas paslaugas administravimo sistemų „Asmlis” ir „Mokesta”...](../renovaciju_sutartys.md) (`datasets/gov/asmlis/renovaciju_sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/asmlis/renovaciju_sutartys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/asmlis/renovaciju_sutartys/SutartisBendra` (`deployed`)[^manifest]
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
| `ren_sutarties_nr` | `string` | — | `4` | `open` | — | Renovacijos sutarties numeris | — |
| `darbo_tipo_kodas` | `string` | — | `4` | `open` | — | Renovacijos metu atlikto darbo kodas | — |
| `prelimenari_ren_sut_data` | `date` | `D` | `4` | `open` | — | Preliminari renovacijos sutarties data | — |
| `patiklsinta_ren_sut_data` | `date` | `D` | `4` | `open` | — | Patikslinta renovacijos sutarties data | — |
| `ren_sut_pabaigos_data` | `date` | `D` | `4` | `open` | — | Renovacijos sutarties pabaigos data | — |
| `kredito_grazinimo_pradz_data` | `date` | `D` | `4` | `open` | — | Kredito grąžinimo pradžios data | — |
| `kredito_grazinimo_pab_data` | `date` | `D` | `4` | `open` | — | Kredito grąžinimo pabaigos data | — |
| `kredito_teikejas` | `string` | — | `4` | `open` | — | Kredito tiekėjas | — |
| `sutarties_subjektas` | `string` | — | `4` | `open` | — | Renovacijos sutarties subjektas | — |
| `aob_kodas` | `string` | — | `4` | `open` | — | Renovuojamo objekto aob kodas | — |
| `pask_pav` | `string` | — | `4` | `open` | — | Renovuojamo objekto paskrities pavadinimas | — |
| `statyb_pab_metai` | `integer` | — | `4` | `open` | — | Renovuojamo objekto statybų metai | — |
| `bendras_plotas` | `number` | — | `4` | `open` | — | Renovuojamo objekto bendrasis plotas | — |
| `gyven_plotas` | `number` | — | `4` | `open` | — | Renovuojamo objekto gyvenamasis plotas | — |
| `aukstu_skaicius` | `number` | — | `4` | `open` | — | Renovuojamo objekto aukštų skaičius | — |
| `geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Renovuojamo objekto vietos koordinatė | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/asmlis/renovaciju_sutartys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/asmlis/renovaciju_sutartys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/asmlis/renovaciju_sutartys (https://data.gov.lt/datasets/3880/)
