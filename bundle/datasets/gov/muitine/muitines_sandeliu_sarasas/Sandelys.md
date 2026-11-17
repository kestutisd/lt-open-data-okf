---
type: Table
title: "Sandelys — Muitinės sandėlių sąrašas"
description: "Rinkinyje pateikiamas Lietuvos teritorijoje esančių muitinės sandėlių sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_sarasas/Sandelys"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_sarasas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sandelys — Muitinės sandėlių sąrašas

Rinkinyje pateikiamas Lietuvos teritorijoje esančių muitinės sandėlių sąrašas. Pateikiami tiek šiuo metu veikiantys, tiek jau uždaryti sandėliai bei jų adresai, aprašymai, koordinatės, atidarymo, uždarymo datos ir t.t. Duomenys pateikiami nuo 1996 metų. Rinkinio vieną eilutę sudaro vienas sandėlis.

- **Model:** `datasets/gov/muitine/muitines_sandeliu_sarasas/Sandelys`[^manifest]
- **Dataset:** [Muitinės sandėlių sąrašas](../muitines_sandeliu_sarasas.md) (`datasets/gov/muitine/muitines_sandeliu_sarasas`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_sarasas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_sarasas/Sandelys`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `sand_kodas` | `string` | — | `4` | `open` | — | Sandėlio kodas | — |
| `leidimo_nr` | `string` | — | `4` | `open` | — | Sandėlio leidimo numeris | — |
| `rusies_pav` | `string` | — | `4` | `open` | — | Sandėlio rūšis | — |
| `eori_kodas` | `string` | — | `4` | `open` | — | Muitines prievolininko kodas | — |
| `imon_pavad` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `muit_kodas` | `string` | — | `4` | `open` | — | Priežiūrą atliekančio muitinės posto kodas | — |
| `muit_kodas1` | `string` | — | `4` | `open` | — | Priežiūrą atliekančio muitinės posto kodas nr.1 | — |
| `muit_kodas2` | `string` | — | `4` | `open` | — | Priežiūrą atliekančio muitinės posto kodas nr.2 | — |
| `sandelio_tipas` | `string` | — | `4` | `open` | — | Sandėlio tipas | — |
| `sandelio_adresas` | `string` | — | `4` | `open` | — | Sandėlio adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `koord_patik_proc` | `number` | — | `4` | `open` | — | Koordinatės patikimumas procentais | — |
| `adreso_tipas` | `string` | — | `4` | `open` | — | Adreso tipas | — |
| `veikla` | `string` | — | `4` | `open` | — | Sandėlio veiklos aprašymas | — |
| `privaziavimas_gelezinkeliu` | `boolean` | — | `4` | `open` | — | Ar yra privažiavimas geležinkeliu | — |
| `eeb_zem_prek` | `boolean` | — | `4` | `open` | — | Bendrijos žemės ūkio prekės | — |
| `eeb_pram_prek` | `boolean` | — | `4` | `open` | — | Bendrijos pramoninės prekės | — |
| `neeb_zem_prek` | `boolean` | — | `4` | `open` | — | Ne bendrijos pramoninės prekės | — |
| `neeb_pram_prek` | `boolean` | — | `4` | `open` | — | Ne bendrijos žemės ūkio prekės | — |
| `prek_taikoma_muit_proc` | `string` | — | `2` | `open` | — | Prekės, kurioms gali būti įforminama muitinės procedūra | — |
| `laikomos_prekes` | `string` | — | `2` | `open` | — | Sandėliuose laikomos prekės | — |
| `atidarytas` | `date` | `D` | `4` | `open` | — | Sandėlio atidarymo data | — |
| `uzdarytas` | `date` | `D` | `4` | `open` | — | Sandėlio uždarymo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rusies_pav` | `"Muitinės sandėlis"` | — | — | Muitinės sandėlis | — |
| `rusies_pav` | `"Laikinojo saugojimo sandėlis"` | — | — | Laikinojo saugojimo sandėlis | — |
| `rusies_pav` | `"Importo ir eksporto terminalas"` | — | — | Importo ir eksporto terminalas | — |
| `rusies_pav` | `"Laisvasis sandėlis"` | — | — | Laisvasis sandėlis | — |
| `rusies_pav` | `"Laisvoji zona"` | — | — | Laisvoji zona | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_sarasas.csv
