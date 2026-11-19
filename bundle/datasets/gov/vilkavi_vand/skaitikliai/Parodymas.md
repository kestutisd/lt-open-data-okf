---
type: Table
title: "Parodymas — Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai"
description: "Rinkinyje pateikiami UAB „Vilkaviškio vandenys“ nuo 2004 m. kaupiami ir saugomi Vilkaviškio vandenų geriamojo vandens skaitiklių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliai/Parodymas"
tags: [gov, vilkavi_vand, parodymas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2841/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilkavi_vand/skaitikliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Parodymas — Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai

Rinkinyje pateikiami UAB „Vilkaviškio vandenys“ nuo 2004 m. kaupiami ir saugomi Vilkaviškio vandenų geriamojo vandens skaitiklių duomenys. Duomenų viena eilutė, tai vieno skaitiklio vienas rodmenų deklaravimas. Be skaitiklio rodmenų, čia galiam rasti ir deklaravimo datą, tipą bei apytikslę skaitiklio koordinatę. Pačios koordinatės suskirstytos į 200 m. x 200 m. gardeles, bei juose visi esantys taškai sudėti į apatinį dešinį gardelės kampą. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilkavi_vand/skaitikliai/Parodymas`[^manifest]
- **Dataset:** [Vilkaviškio vandenų geriamojo vandens skaitiklių parodymai](../skaitikliai.md) (`datasets/gov/vilkavi_vand/skaitikliai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliai/Parodymas` (`deployed`)[^manifest]
- **Provider:** `vilkavi_vand` — UAB „Vilkaviškio vandenys“ *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitliuku_parodymai.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilkavi_vand/skaitikliai (https://data.gov.lt/datasets/2841/)
