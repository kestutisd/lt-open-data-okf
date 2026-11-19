---
type: Table
title: "AtvejuStatistika — Atvejų statistika"
description: "Agreguota atvejų statistika pagal metus, gyvenamąją vietą ir demografinius bei socialinius pjūvius"
resource: "https://get.data.gov.lt/datasets/gov/hi/savizudybes/statistika/AtvejuStatistika"
tags: [gov, hi, atvejustatistika, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/savizudybes/statistika.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/hi/savizudybes/statistika.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/6010/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/savizudybes/statistika"
    author: "team:vda"
    last_modified: "2026-09-07T00:00:00Z"
---

# AtvejuStatistika — Atvejų statistika

Agreguota atvejų statistika pagal metus, gyvenamąją vietą ir demografinius bei socialinius pjūvius[^manifest]

- **Model:** `datasets/gov/hi/savizudybes/statistika/AtvejuStatistika`[^manifest]
- **Dataset:** [Agreguoti savižudybės atvejų ir savižudybės grėsmių skaičiai](../statistika.md) (`datasets/gov/hi/savizudybes/statistika`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/savizudybes/statistika.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/savizudybes/statistika.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/savizudybes/statistika/AtvejuStatistika` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-09-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | VDA įrašo identifikatorius | Unikalus VDA suformuotas statistinio įrašo identifikatorius |
| `metai` | `integer` | — | `4` | `open` | — | Metai | Kalendoriniai metai, kuriems priskiriama statistinė reikšmė |
| `pjuvis` | `string` | — | `4` | `open` | — | Statistinis pjūvis | Statistinis pjūvis, pagal kurį pateikiama reikšmė |
| `gyvenamoji_vieta` | `string` | — | `4` | `open` | — | Gyvenamoji vieta | Gyvenamoji vieta arba teritorija, kuriai priskiriama statistinė reikšmė |
| `atveju_skaicius` | `integer` | — | `4` | `open` | — | Atvejų skaičius | Nurodytam laikotarpiui ir pjūviui apskaičiuotas atvejų skaičius |
| `atveju_skaicius_100_tukst` | `number` | — | `4` | `open` | — | Atvejų skaičius 100 tūkst. gyventojų | Atvejų skaičius, tenkantis 100 tūkst. gyventojų |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | Lytis, pagal kurią pateikiama statistinė reikšmė |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Amžiaus grupė | Amžiaus grupė, pagal kurią pateikiama statistinė reikšmė |
| `gyvenamosios_vietos_tipas` | `string` | — | `4` | `open` | — | Gyvenamosios vietos tipas | Gyvenamosios vietos tipo kategorija, pagal kurią pateikiama statistinė reikšmė |
| `seimine_padetis` | `string` | — | `4` | `open` | — | Šeiminė padėtis | Šeiminės padėties kategorija, pagal kurią pateikiama statistinė reikšmė |
| `socialine_padetis` | `string` | — | `4` | `open` | — | Socialinė padėtis | Socialinės padėties kategorija, pagal kurią pateikiama statistinė reikšmė |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/savizudybes/statistika.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/savizudybes/statistika.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/savizudybes/statistika (https://data.gov.lt/datasets/6010/)
