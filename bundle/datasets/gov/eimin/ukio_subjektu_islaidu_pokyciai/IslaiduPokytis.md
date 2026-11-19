---
type: Table
title: "IslaiduPokytis — Ūkio subjektų administracinės naštos ir prisitaikymo prie reguliavimo išlaidų stebėsenos pokyčiai"
description: "Lentelėje pateikti Lietuvos Respublikos ekonomikos ir inovacijų ministerijos Ūkio subjektų prisitaikymo prie reguliavimo išlaidų vertinimo stebėsenos duomenys nuo 2014 metų."
resource: "https://get.data.gov.lt/datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai/IslaiduPokytis"
tags: [gov, eimin, islaidupokytis, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1727/"
    title: "data.gov.lt DCAT-AP — datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# IslaiduPokytis — Ūkio subjektų administracinės naštos ir prisitaikymo prie reguliavimo išlaidų stebėsenos pokyčiai

Lentelėje pateikti Lietuvos Respublikos ekonomikos ir inovacijų ministerijos Ūkio subjektų prisitaikymo prie reguliavimo išlaidų vertinimo stebėsenos duomenys nuo 2014 metų. Duomenų atnaujinimas vykdomas 2 kartus per metus (kas pusę metų). Daugiau informacijos apie prisitaikymo prie reguliavimo išlaidų vertinimą galite rasti https://eimin.lrv.lt/lt/veiklos-sritys/verslo-aplinka/geresnis-reglamentavimas/administracines-nastos-ir-prisitaikymo-prie-reguliavimo-islaidu-vertinimo-praktine-informacija/. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai/IslaiduPokytis`[^manifest]
- **Dataset:** [Ūkio subjektų administracinės naštos ir prisitaikymo prie reguliavimo išlaidų stebėsenos pokyčiai](../ukio_subjektu_islaidu_pokyciai.md) (`datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai`)[^manifest]
- **Manifest CSV:** [datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai/IslaiduPokytis` (`deployed`)[^manifest]
- **Provider:** `eimin` — Lietuvos Respublikos ekonomikos ir inovacijų ministerija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Data, kuriai apskaičiuotas bendras prisitaikymo prie reguliavimo išlaidų pokytis ūkio subjektams | — |
| `inst_ja_kodas` | `string` | — | `4` | `open` | — | Institucijos, parengusios teisės akto projektą, juridinio asmens kodas | — |
| `ar_ja_kodas_validus` | `boolean` | — | `4` | `open` | — | Požymis, ar juridinio asmens kodas yra validus ( "true" - validus, "false" - nevalidus) | — |
| `inst_pavadinimas` | `string` | — | `4` | `open` | — | Institucijos, parengusios teisės akto projektą, pavadinimas | — |
| `teises_aktu_projektas` | `string` | — | `4` | `open` | — | Teisės akto projekto pavadinimas | — |
| `bendras_islaidu_pokytis` | `number` | — | `4` | `open` | — | Bendras teisės aktų projektais sukeliamo prisitaikymo prie reguliavimo išlaidų pokytis (Eurais) ūkio subjektams | — |
| `an_islaidu_pokytis` | `number` | — | `4` | `open` | — | Teisės aktų projektais, tik informacinių įpareigojimų (pvz., pateikti ataskaitą, ženklinti pakuotes), sukeliamos administracinės naštos pokytis (Eurais) ūkio subjektams | — |
| `pri_islaidu_pokytis` | `number` | — | `4` | `open` | — | Teisės aktų projektais, ne informacinių įpareigojimų (pvz., pritaikyti patalpas pagal reikalavimus), sukeliamos naštos pokytis (Eurais) ūkio subjektams | — |
| `es_islaidu_pokytis` | `number` | — | `4` | `open` | — | Europos Sąjungos kilmės teisės akto sukeliamo prisitaikymo prie reguliavimo išlaidų pokytis (Eurais) ūkio subjektams | — |
| `nac_islaidu_pokytis` | `number` | — | `4` | `open` | — | Nacionalinės kilmės teisės akto sukeliamo prisitaikymo prie reguliavimo išlaidų pokytis (Eurais) ūkio subjektams | — |
| `v_islaidu_pokyits` | `number` | — | `4` | `open` | — | Vienkartinių išlaidų (pavyzdžiui, įsirengti patalpas, įdiegti kokybės sistemą, įdiegti naujus funkcionalumus sistemoje) pokytis (Eurais) ūkio subjektams | — |
| `p_islaidu_pokytis` | `number` | — | `4` | `open` | — | Periodinių išlaidų (pavyzdžiui, kas mėnesį teikiama ataskaita arba kas metus pildoma deklaracijos forma) pokytis (Eurais) ūkio subjektams | — |
| `nastos_mazinimo_sektorius` | `string` | — | `4` | `open` | — | Prioritetinis reguliavimo naštos ūkio subjektams mažinimo sektorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bendras_islaidu_pokytis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `an_islaidu_pokytis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `pri_islaidu_pokytis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `es_islaidu_pokytis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `nac_islaidu_pokytis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `v_islaidu_pokyits` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `p_islaidu_pokytis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/eimin/ukio_subjektu_islaidu_pokyciai (https://data.gov.lt/datasets/1727/)
