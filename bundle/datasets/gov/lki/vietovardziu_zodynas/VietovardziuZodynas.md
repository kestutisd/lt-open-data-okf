---
type: Table
title: "VietovardziuZodynas — Vietovardžių žodynas"
description: "Rinkinyje pateikiamas Lietuvių kalbos instituto (LKI) 2007 m. paskelbtas „Vietovardžių žodynas“ (http://www.vietovardziai.lki.lt/), kurį sudaro Lietuvos ir lietuvių etninių žemių, lietuvių tremties vietų, istorinių baltų žemių vietų vardai."
resource: "https://get.data.gov.lt/datasets/gov/lki/vietovardziu_zodynas/VietovardziuZodynas"
tags: [gov, lki, vietovardziuzodynas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/vietovardziu_zodynas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lki/vietovardziu_zodynas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2937/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/vietovardziu_zodynas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VietovardziuZodynas — Vietovardžių žodynas

Rinkinyje pateikiamas Lietuvių kalbos instituto (LKI) 2007 m. paskelbtas „Vietovardžių žodynas“ (http://www.vietovardziai.lki.lt/), kurį sudaro Lietuvos ir lietuvių etninių žemių, lietuvių tremties vietų, istorinių baltų žemių vietų vardai. „Vietovardžių žodyno“ internetinis variantas parengtas remiantis knyginiu šio žodyno leidimu (Vilnius: Mokslo ir enciklopedijų leidybos institutas, 2002). Rinkinį sudaro vietovardžiai, kirčiuotos jų linksnių formos, atitikmenys kitomis kalbomis (jei yra), kirčiuotės, rūšis, administracinis-teritorinis priklausymas, vietovardžio statusas ir kiti jo variantai. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lki/vietovardziu_zodynas/VietovardziuZodynas`[^manifest]
- **Dataset:** [Vietovardžių žodynas](../vietovardziu_zodynas.md) (`datasets/gov/lki/vietovardziu_zodynas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lki/vietovardziu_zodynas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/vietovardziu_zodynas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/vietovardziu_zodynas/VietovardziuZodynas` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/vietovardziu_zodynas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/vietovardziu_zodynas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/vietovardziu_zodynas (https://data.gov.lt/datasets/2937/)
