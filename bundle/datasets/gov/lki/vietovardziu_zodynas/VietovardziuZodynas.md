---
type: Table
title: "VietovardziuZodynas — Vietovardžių žodynas"
description: "Rinkinyje pateikiamas Lietuvių kalbos instituto (LKI) 2007 m. paskelbtas „Vietovardžių žodynas“ (http://www.vietovardziai.lki.lt/), kurį sudaro Lietuvos ir lietuvių etninių žemių, lietuvių tremties vietų, istorinių baltų žemių vietų vardai."
resource: "https://get.data.gov.lt/datasets/gov/lki/vietovardziu_zodynas/VietovardziuZodynas"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/vietovardziu_zodynas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/vietovardziu_zodynas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# VietovardziuZodynas — Vietovardžių žodynas

Rinkinyje pateikiamas Lietuvių kalbos instituto (LKI) 2007 m. paskelbtas „Vietovardžių žodynas“ (http://www.vietovardziai.lki.lt/), kurį sudaro Lietuvos ir lietuvių etninių žemių, lietuvių tremties vietų, istorinių baltų žemių vietų vardai. „Vietovardžių žodyno“ internetinis variantas parengtas remiantis knyginiu šio žodyno leidimu (Vilnius: Mokslo ir enciklopedijų leidybos institutas, 2002). Rinkinį sudaro vietovardžiai, kirčiuotos jų linksnių formos, atitikmenys kitomis kalbomis (jei yra), kirčiuotės, rūšis, administracinis-teritorinis priklausymas, vietovardžio statusas ir kiti jo variantai.

- **Model:** `datasets/gov/lki/vietovardziu_zodynas/VietovardziuZodynas`[^manifest]
- **Dataset:** [Vietovardžių žodynas](../vietovardziu_zodynas.md) (`datasets/gov/lki/vietovardziu_zodynas`)
- **Manifest CSV:** [datasets/gov/lki/vietovardziu_zodynas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/vietovardziu_zodynas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/vietovardziu_zodynas/VietovardziuZodynas`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Unikalus vietovardžio kodas | — |
| `vietovardis_pilnas_nekirciuotas` | `string` | — | `4` | `open` | — | Nekirčiuotas pilnas vietovardžio pavadinimas | — |
| `vietovardis` | `string` | — | `4` | `open` | — | Kirčiuotas pilnas vietovardžio pavadinimas | — |
| `linksniai` | `string` | — | `4` | `open` | — | Vietovardžio linksniai | — |
| `vietovardzio_rusis` | `string` | — | `4` | `open` | — | Vietovardžio rūšis | — |
| `vietovardis_vertimas` | `string` | — | `4` | `open` | — | Vietovardžio vertimai kita kalba | — |
| `kirciuote` | `string` | — | `4` | `open` | — | Vietovardžio pagrindinė kirčiuotė | — |
| `adm_teritorinis_priklausymas` | `string` | — | `4` | `open` | — | Administracinis ir teritorinis vietovardžio priklausymas | — |
| `statusas` | `string` | — | `4` | `open` | — | Vietovardžio statusas | — |
| `kitas_statusas` | `string` | — | `4` | `open` | — | Papildomas vietovardžio statusas | — |
| `kiti_variantai` | `string` | — | `4` | `open` | — | Kiti vietovardžio variantai | — |
| `papildoma_informacija` | `string` | — | `4` | `open` | — | Papildoma informacija apie vietovardį | — |
| `susije_vietovardziai` | `string` | — | `4` | `open` | — | Nuorodos į susijusius arba panašius vietovardžius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/vietovardziu_zodynas.csv
