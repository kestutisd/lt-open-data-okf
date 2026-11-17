---
type: Table
title: "MdarboVertinimas — Mokslo ir meno darbų vertinimo duomenys"
description: "Lentelėje - mokslo ir meno darbų vertinimo duomenys iš Lietuvos mokslo tarybos Mokslo (meno) veiklos rezultatų vertinimo sistemos „Vieversys“."
resource: "https://get.data.gov.lt/datasets/gov/lmt/darbu_vertinimas/MdarboVertinimas"
tags: [gov, lmt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lmt/darbu_vertinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmt/darbu_vertinimas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MdarboVertinimas — Mokslo ir meno darbų vertinimo duomenys

Lentelėje - mokslo ir meno darbų vertinimo duomenys iš Lietuvos mokslo tarybos Mokslo (meno) veiklos rezultatų vertinimo sistemos „Vieversys“. Duomenys lentelėje pateikiami nuo 2018 metų ir atnaujinami, papildomi kas metus.

- **Model:** `datasets/gov/lmt/darbu_vertinimas/MdarboVertinimas`[^manifest]
- **Dataset:** [Mokslo ir meno darbų vertinimo duomenys](../darbu_vertinimas.md) (`datasets/gov/lmt/darbu_vertinimas`)
- **Manifest CSV:** [datasets/gov/lmt/darbu_vertinimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmt/darbu_vertinimas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmt/darbu_vertinimas/MdarboVertinimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `darbo_id` | `string` | — | `4` | `open` | — | Darbo identifikatorius | — |
| `darbo_pav_pilnas` | `string` | — | `4` | `open` | — | Pilnas darbo pavadinimas | — |
| `darbo_pav` | `string` | — | `4` | `open` | — | Darbo pavadinimas | — |
| `autoriu_institucijos` | `string` | — | `4` | `open` | — | Institucijos, kuriose dirba darbo autoriai | — |
| `autoriu_instituciju_tipai` | `string` | — | `4` | `open` | — | Institucijų, kuriose dirba darbo autoriai, tipai | — |
| `autoriniu_lanku_skaic` | `number` | — | `4` | `open` | — | Darbo autorinių lankų skaičius | — |
| `darbo_puslapiu_skaic` | `number` | — | `4` | `open` | — | Darbo puslapių skaičius | — |
| `darbo_leidejas` | `string` | — | `4` | `open` | — | Darbo leidėjas | — |
| `darbo_metai` | `date` | `Y` | `4` | `open` | — | Darbo publikavimo metai | — |
| `darbo_issn_kodas` | `string` | — | `4` | `open` | — | Darbo ISSN kodas | — |
| `darbo_nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į darbą | — |
| `darbo_tipas` | `string` | — | `4` | `open` | — | Darbo tipas | — |
| `darbo_mokslo_kryptis` | `string` | — | `4` | `open` | — | Darbo mokslo kryptis | — |
| `ar_top_darbas` | `boolean` | — | `4` | `open` | — | Požymis, ar darbas randamas geriausių darbų sąraše ("true" - taip, "false" - ne) | — |
| `versijos_nr` | `string` | — | `4` | `open` | — | Darbo versijos numeris | — |
| `komisijos_pav` | `string` | — | `4` | `open` | — | Ekspertų komisijos pavadinimas | — |
| `ivertinimo_statusas` | `string` | — | `4` | `open` | — | Darbo įvertinimo statusas | — |
| `ivertinimo_publikavimo_data` | `date` | `D` | `4` | `open` | — | Darbo įvertinimo publikavimo data | — |
| `apeliacijos_ivertinimo_statusas` | `string` | — | `4` | `open` | — | Apeliacijos dėl darbo įvertinimo statusas | — |
| `komentaras_lt` | `string` | — | `4` | `open` | — | Apeliacijos įvertinimo komentaras | — |
| `ai_publikavimo_data` | `date` | `D` | `4` | `open` | — | Apeliacijos įvertinimo publikavimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `komentaras_lt` | `update(property: "komentaras_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lmt/darbu_vertinimas.csv
