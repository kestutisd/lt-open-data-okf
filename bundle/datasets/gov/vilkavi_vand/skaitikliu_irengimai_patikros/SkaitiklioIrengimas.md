---
type: Table
title: "SkaitiklioIrengimas — UAB „Vilkaviškio vandenys“ aktyvių geriamojo vandens skaitiklių įrengimo ir patikros duomenys"
description: "Lentelėje pateikiami UAB „Vilkaviškio vandenys“ aktyvių (šiuo metu veikiančių, galiojančių) geriamojo vandens skaitiklių įrengimo ir patikros duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros/SkaitiklioIrengimas"
tags: [gov, vilkavi_vand, skaitiklioirengimas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# SkaitiklioIrengimas — UAB „Vilkaviškio vandenys“ aktyvių geriamojo vandens skaitiklių įrengimo ir patikros duomenys

Lentelėje pateikiami UAB „Vilkaviškio vandenys“ aktyvių (šiuo metu veikiančių, galiojančių) geriamojo vandens skaitiklių įrengimo ir patikros duomenys. Lentelėje galima rasti skaitiklio prijungimo, patikros (ir jos galiojimo) datas bei apytikslę skaitiklio koordinatę. Svarbu paminėti, kad koordinatės suskirstytos į 1500m. x 1500m. gardeles, o visi juose esantys taškai sudėti į apatinį dešinį gardelės kampą. Duomenys atnaujinami kas mėnesį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros/SkaitiklioIrengimas`[^manifest]
- **Dataset:** [UAB „Vilkaviškio vandenys“ aktyvių geriamojo vandens skaitiklių įrengimo ir patikros duomenys](../skaitikliu_irengimai_patikros.md) (`datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros/SkaitiklioIrengimas` (`deployed`)[^manifest]
- **Provider:** `vilkavi_vand` — UAB „Vilkaviškio vandenys“ *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius (skaitiklio įrengimo identifikatorius) | — |
| `abonento_kodas` | `string` | — | `4` | `open` | — | Abonento kodas | — |
| `abonento_ivadas` | `string` | — | `4` | `open` | — | Įvado kodas | — |
| `skaitiklio_kodas` | `string` | — | `4` | `open` | — | Skaitiklio kodas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje (apatiniame dešiniame 1500 m x 1500 m gardelės kampe | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje (apatiniame dešiniame 1500 m x 1500 m gardelės kampe | — |
| `koord_patik_proc` | `number` | — | `4` | `open` | — | Koordinatės patikimumas procentais (prieš patalpinat koordinatę į gardelę) | — |
| `prijungimo_data` | `date` | `D` | `4` | `open` | — | Skaitikio prijungimo data | — |
| `ar_galiojantis_irengimas` | `boolean` | — | `4` | `open` | — | Požymis, ar skaitiklis yra galiojantis (true - galiojantis, false - negaliojantis) | — |
| `ar_ivadinis_skaitiklis` | `boolean` | — | `4` | `open` | — | Požymis, ar skaitiklis įvadinis (true - įvadinis, false - ne įvadinis) | — |
| `patikros_data` | `date` | `D` | `4` | `open` | — | Skaitiklio patikros data | — |
| `patikros_galiojimo_data` | `date` | `D` | `4` | `open` | — | Skaitiklio patikros galiojimo data (iki) | — |
| `iraso_sukurimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `iraso_atnaujinimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilkavi_vand/skaitikliu_irengimai_patikros.csv#L6)
