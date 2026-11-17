---
type: Table
title: "GresmiuStatistika — Grėsmių statistika"
description: "Agreguota atvejų statistika pagal metus, gyvenamąją vietą ir demografinius bei socialinius pjūvius"
resource: "https://get.data.gov.lt/datasets/gov/hi/savizudybes/statistika/GresmiuStatistika"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/savizudybes/statistika.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/savizudybes/statistika.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# GresmiuStatistika — Grėsmių statistika

Agreguota atvejų statistika pagal metus, gyvenamąją vietą ir demografinius bei socialinius pjūvius

- **Model:** `datasets/gov/hi/savizudybes/statistika/GresmiuStatistika`[^manifest]
- **Dataset:** [datasets/gov/hi/savizudybes/statistika](../statistika.md) (`datasets/gov/hi/savizudybes/statistika`)
- **Manifest CSV:** [datasets/gov/hi/savizudybes/statistika.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/savizudybes/statistika.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/savizudybes/statistika/GresmiuStatistika`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | VDA įrašo identifikatorius | Unikalus VDA suformuotas statistinio įrašo identifikatorius |
| `metai` | `integer` | — | `4` | `open` | — | Metai | Kalendoriniai metai, kuriems priskiriama statistinė reikšmė |
| `pjuvis` | `string` | — | `4` | `open` | — | Statistinis pjūvis | Statistinis pjūvis, pagal kurį pateikiama reikšmė |
| `gyvenamoji_vieta` | `string` | — | `4` | `open` | — | Gyvenamoji vieta | Gyvenamoji vieta arba teritorija, kuriai priskiriama statistinė reikšmė |
| `atveju_skaicius` | `integer` | — | `4` | `open` | — | Grėsmių skaičius | Nurodytam laikotarpiui ir pjūviui apskaičiuotas atvejų skaičius |
| `atveju_skaicius_100_tukst` | `number` | — | `4` | `open` | — | Grėsmių skaičius 100 tūkst. gyventojų | Atvejų skaičius, tenkantis 100 tūkst. gyventojų |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | Lytis, pagal kurią pateikiama statistinė reikšmė |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Amžiaus grupė | Amžiaus grupė, pagal kurią pateikiama statistinė reikšmė |
| `gyvenamosios_vietos_tipas` | `string` | — | `4` | `open` | — | Gyvenamosios vietos tipas | Gyvenamosios vietos tipo kategorija, pagal kurią pateikiama statistinė reikšmė |
| `seimine_padetis` | `string` | — | `4` | `open` | — | Šeiminė padėtis | Šeiminės padėties kategorija, pagal kurią pateikiama statistinė reikšmė |
| `socialine_padetis` | `string` | — | `4` | `open` | — | Socialinė padėtis | Socialinės padėties kategorija, pagal kurią pateikiama statistinė reikšmė |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/savizudybes/statistika.csv
