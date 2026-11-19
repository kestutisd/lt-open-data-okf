---
type: Table
title: "Licencija — Lošimo bendrovių licencijos"
description: "Lošimų bendrovėms išduotų licencijų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/lpt/bendroviu_licencijos/Licencija"
tags: [gov, lpt, licencija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/bendroviu_licencijos.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lpt/bendroviu_licencijos.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1261/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lpt/bendroviu_licencijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Licencija — Lošimo bendrovių licencijos

Lošimų bendrovėms išduotų licencijų sąrašas. Licencijų, priskirtų šiems tipams, informacija yra teisinga: Lažybas, Stalo lošimus ir A kategorijos automatais, Lošimus B kategorijos automatais.[^manifest]

- **Model:** `datasets/gov/lpt/bendroviu_licencijos/Licencija`[^manifest]
- **Dataset:** [Lošimo bendrovių licencijos](../bendroviu_licencijos.md) (`datasets/gov/lpt/bendroviu_licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lpt/bendroviu_licencijos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/bendroviu_licencijos.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lpt/bendroviu_licencijos/Licencija` (`deployed`)[^manifest]
- **Provider:** `lpt` — Lošimų priežiūros tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus įrašo identifikatorius | — |
| `licencijos_id` | `string` | — | `4` | `open` | — | Licencijos identifikatorius | — |
| `licencijos_numeris` | `string` | — | `4` | `open` | — | Licencijos numeris | — |
| `licencijos_tipas` | `string` | — | `4` | `open` | — | Licencijos tipas | Licencijų, priskirtų šiems tipams, informacija yra teisinga: Lažybas, Stalo lošimus ir A kategorijos automatais, Lošimus B kategorijos automatais |
| `organizacijos_pavadinimas` | `string` | — | `4` | `open` | — | Lošimų bendrovės pavadinimas | — |
| `organizacijos_kodas` | `string` | — | `2` | `open` | — | Lošimų bendrovės juridinio asmens kodas | — |
| `organizacijos_adresas` | `string` | — | `2` | `open` | — | Lošimų bendrovės registracijos adresas | — |
| `licencijos_isdavimo_data` | `date` | `D` | `4` | `open` | — | Licencijos išdavimo data | — |
| `licencijos_isdavimo_pagrindas` | `string` | — | `4` | `open` | — | Licencijos išdavimo pagrindas | — |
| `licencijos_panaikinimo_data` | `date` | `D` | `4` | `open` | — | Licencijos panaikinimo data | — |
| `licencijos_panaikinimo_pagrindas` | `string` | — | `4` | `open` | — | Licencijos panaikinimo pagrindas | — |
| `komentaras_lt` | `string` | — | `4` | `open` | — | Komentaras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `komentaras_lt` | `update(property: "komentaras_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lpt/bendroviu_licencijos.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lpt/bendroviu_licencijos.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lpt/bendroviu_licencijos (https://data.gov.lt/datasets/1261/)
