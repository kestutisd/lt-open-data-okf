---
type: Table
title: "Parodymas — Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai"
description: "Rinkinyje pateikiami UAB „Vilkaviškio vandenys“ nuo 2004 m. kaupiami ir saugomi Vilkaviškio vandenų geriamojo vandens skaitiklių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliai/Parodymas"
tags: [gov, vilkavi_vand, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Parodymas — Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai

Rinkinyje pateikiami UAB „Vilkaviškio vandenys“ nuo 2004 m. kaupiami ir saugomi Vilkaviškio vandenų geriamojo vandens skaitiklių duomenys. Duomenų viena eilutė, tai vieno skaitiklio vienas rodmenų deklaravimas. Be skaitiklio rodmenų, čia galiam rasti ir deklaravimo datą, tipą bei apytikslę skaitiklio koordinatę. Pačios koordinatės suskirstytos į 200 m. x 200 m. gardeles, bei juose visi esantys taškai sudėti į apatinį dešinį gardelės kampą.

- **Model:** `datasets/gov/vilkavi_vand/skaitikliai/Parodymas`[^manifest]
- **Dataset:** [Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai](../skaitikliai.md) (`datasets/gov/vilkavi_vand/skaitikliai`)
- **Manifest CSV:** [datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliai/Parodymas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | `Identifikatorius` | — | — |
| `skaitiklioid` | `string` | — | `4` | `open` | `Skaitiklio indentifikatorius` | — | — |
| `abonentas` | `string` | — | `4` | `open` | `Abonentas` | — | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | `X koordinatė LKS94 koordinačių sistemoje (apatiniame dešiniame 200 m x 200 m gardelės kampe` | — | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | `Y koordinatė LKS94 koordinačių sistemoje (apatiniame dešiniame 200 m x 200 m gardelės kampe` | — | — |
| `koord_patik_proc` | `number` | — | `4` | `open` | `Koordinatės patikimumas procentais (prieš patalpinant koordinatę į gardelę)` | — | — |
| `abonento_tipas` | `string` | — | `4` | `open` | `Abonento tipas` | — | — |
| `nuo_data` | `date` | `D` | `4` | `open` | `Skaitiklio deklaravimo periodo data nuo` | — | — |
| `iki_data` | `date` | `D` | `4` | `open` | `Skaitiklio deklaravimo periodo data iki` | — | — |
| `nuo_m3` | `number` | `m^3` | `4` | `open` | `Skaitiklio deklaruojami rodmenys nuo m^3` | — | — |
| `iki_m3` | `number` | `m^3` | `4` | `open` | `Skaitiklio deklaruojami rodmenys iki m^3` | — | — |
| `kiekis_m3` | `number` | `m^3` | `4` | `open` | `Sunaudoto vandens kiekis m^3` | — | — |
| `deklaravimo_data` | `date` | `D` | `4` | `open` | `Skaitiklio deklaravimo data` | — | — |
| `deklaravimo_tipas` | `string` | — | `4` | `open` | `Deklaravimo tipas` | — | — |
| `tarifo_pav` | `string` | — | `4` | `open` | `Tarifo pavadinimas` | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv
