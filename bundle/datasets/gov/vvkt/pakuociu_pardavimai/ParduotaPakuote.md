---
type: Table
title: "ParduotaPakuote — Vaistinių preparatų pakuočių pardavimai"
description: "Spinta table datasets/gov/vvkt/pakuociu_pardavimai/ParduotaPakuote (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai/ParduotaPakuote"
tags: [gov, vvkt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkt/pakuociu_pardavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# ParduotaPakuote — Vaistinių preparatų pakuočių pardavimai

- **Model:** `datasets/gov/vvkt/pakuociu_pardavimai/ParduotaPakuote`[^manifest]
- **Dataset:** [Vaistinių preparatų pakuočių pardavimai](../pakuociu_pardavimai.md) (`datasets/gov/vvkt/pakuociu_pardavimai`)
- **Manifest CSV:** [datasets/gov/vvkt/pakuociu_pardavimai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/pakuociu_pardavimai.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/pakuociu_pardavimai/ParduotaPakuote`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | VDA identifikatorius | Unikalus Valstybės duomenų agentūros sugeneruotas eilutės identifikatorius. Eilutės unikalumą sudaro pakid, data, pardavimai |
| `pakid` | `string` | — | `4` | `open` | — | Pakuotės identifikacinis numeris | — |
| `npakid` | `string` | — | `4` | `open` | — | Nacionalinis vaistinio preparato pakuotės identifikatorius | — |
| `vid` | `string` | — | `4` | `open` | — | Vaistinio preparato identifikacinis numeris | — |
| `data` | `date` | `M` | `4` | `open` | — | Pardavimų data | Data, nurodanti pardavimų ataskaitą už konkretų mėnesį |
| `bendrinis_pavadinimas` | `string` | — | `4` | `open` | — | Vaistinio preparato bendrinis pavadinimas | — |
| `farmacine_forma` | `string` | — | `4` | `open` | — | Vaisto fizinė forma | — |
| `pakuote` | `string` | — | `4` | `open` | — | Pakuotės aprašymas | — |
| `pakuotes_pirminis_dydis` | `string` | — | `3` | `open` | — | Pakuotės pirminis dydis | Pirminis pakuotės dydis, nurodantis vaistinio preparato dozės skaitinę talpą |
| `pakuotes_matav_vnt` | `string` | — | `4` | `open` | — | Pakuotės pirminio dydžio matavimo vienetai | — |
| `pakuotes_antrinis_dydis` | `string` | — | `3` | `open` | — | Pakuotės antrinis dydis | Antrinis pakuotės dydis, nurodantis dozių skaičių pakuotėje |
| `stiprumas` | `string` | — | `4` | `open` | — | Vaistinio preparato stiprumas | — |
| `pardavimai` | `string` | — | `4` | `open` | — | Vaistų pardavimo tipai | — |
| `parduota_vnt` | `integer` | — | `4` | `open` | — | Parduotas vaistinių preparatų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pardavimai` | — | `"Mažmenai"` | — | — | — |
| `pardavimai` | — | `"Vaistinėms"` | — | — | — |
| `pardavimai` | — | `"Pavieniams pacientams"` | — | — | — |
| `pardavimai` | — | `"ASPĮ"` | — | Asmens sveikatos priežiūros įstaigoms | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/pakuociu_pardavimai.csv
