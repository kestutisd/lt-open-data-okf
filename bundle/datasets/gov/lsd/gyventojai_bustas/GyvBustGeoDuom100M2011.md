---
type: Table
title: "GyvBustGeoDuom100M2011 — Gyventojų ir būstų surašymo geoerdviniai duomenys 100x100 gardelėse 2011 m."
description: "Spinta table datasets/gov/lsd/gyventojai_bustas/GyvBustGeoDuom100M2011 (39 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas/GyvBustGeoDuom100M2011"
tags: [gov, lsd, gyvbustgeoduom100m2011, deployed, cadence-decennial]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/lsd/gyventojai_bustas.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1911/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/gyventojai_bustas"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# GyvBustGeoDuom100M2011 — Gyventojų ir būstų surašymo geoerdviniai duomenys 100x100 gardelėse 2011 m.

- **Model:** `datasets/gov/lsd/gyventojai_bustas/GyvBustGeoDuom100M2011`[^manifest]
- **Dataset:** [Lietuvos Respublikos visuotinio gyventojų ir būstų surašymo rezultatų duomenys](../gyventojai_bustas.md) (`datasets/gov/lsd/gyventojai_bustas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/gyventojai_bustas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/gyventojai_bustas/GyvBustGeoDuom100M2011` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DECENNIAL`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gyv_bustas` | `string` | — | `4` | `open` | — | Vidutinis gyventojų skaičius gardelės būstuose | — |
| `issituoke` | `string` | — | `4` | `open` | — | Išsituokusių gyventojų skaičius | — |
| `lt_k` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurių gimtoji kalba yra lietuvių | — |
| `vidurinis` | `string` | — | `4` | `open` | — | Gyventojų skaičius su viduriniu išsilavinimu | — |
| `amzius0_14` | `string` | — | `4` | `open` | — | 0-14 metų amžiaus gyventojų skaičius | — |
| `islaikomas` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurie yra šeimos ir (ar) kitų asmenų išlaikomas, arba turi kitą pragyvenimo šaltinį | — |
| `wc` | `string` | — | `4` | `open` | — | Butų, turinčių tualetą su nutekamuoju vandeniu, skaičius | — |
| `moteru_sk` | `string` | — | `4` | `open` | — | Moterų skaičius | — |
| `gyv_sk` | `string` | — | `4` | `open` | — | Gyventojų skaičius | — |
| `amzius15_64` | `string` | — | `4` | `open` | — | 15-64 metų amžiaus gyventojų skaičius | — |
| `grid_id` | `string` | — | `4` | `open` | — | Gardelės identifikavimo kodas | — |
| `aukstasis` | `string` | — | `4` | `open` | — | Gyventojų skaičius su aukštuoju išsilavinimu | — |
| `bustu_sk` | `string` | — | `4` | `open` | — | Gyvenamųjų būstų skaičius | — |
| `pagrindinis` | `string` | — | `4` | `open` | — | Gyventojų skaičius su pagrindiniu ir pradiniu išsilavinimu | — |
| `ru_k` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurių gimtoji kalba yra rusų | — |
| `verslas` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurių pragyvenimo šaltinis yra pajamos iš savo ar šeimos verslo, žemės ūkio veiklos, nuosavybės ar investicijų | — |
| `vanduo` | `string` | — | `4` | `open` | — | Butų, turinčių karštą vandenį, skaičius | — |
| `aukstesnys` | `string` | — | `4` | `open` | — | Gyventojų skaičius su aukštesniuoju ir spec. viduriniu išsilavinimu | — |
| `shape_area` | `number` | — | `4` | `open` | — | gardelės plotas | — |
| `vonia` | `string` | — | `4` | `open` | — | Butų, turinčių vonią, dušą, skaičius | — |
| `kita_k` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurių gimtoji kalba yra kita kalba | — |
| `kita_mk` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurie moka kitą kalbą | — |
| `nesusituok` | `string` | — | `4` | `open` | — | Niekada negyvenusių santuokoje gyventojų skaičius | — |
| `vyru_sk` | `string` | — | `4` | `open` | — | Vyrų skaičius | — |
| `pol_k` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurių gimtoji kalba yra lenkų | — |
| `ru_mk` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurie moka rusų kalbą | — |
| `susituoke` | `string` | — | `4` | `open` | — | Susituokusių gyventojų skaičius | — |
| `butas_` | `string` | — | `4` | `open` | — | Butų daugiabučiame name, butų negyvenamajame pastate skaičius | — |
| `darbas` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurių pragyvenimo šaltinis yra darbo užmokestis | — |
| `pensija` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurių pragyvenimo šaltinis yra pensija, pašalpa, stipendija ar gyventojas yra valstybės išlaikomas | — |
| `gyv_tankis` | `string` | — | `4` | `open` | — | Gyventojų tankis gardelėje | — |
| `en_mk` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurie moka anglų kalbą | — |
| `shape_length` | `number` | — | `4` | `open` | — | gardelės ilgis | — |
| `pol_mk` | `string` | — | `4` | `open` | — | Gyventojų skaičius, kurie moka lenkų kalbą | — |
| `objectid` | `integer` | — | `4` | `open` | — | Objekto įdentifikacinis numeris | — |
| `butas2` | `string` | — | `4` | `open` | — | Butų dviejų butų name skaičius | — |
| `amzius65` | `string` | — | `4` | `open` | — | 65 metų amžiaus ir vyresnių gyventojų skaičius | — |
| `nasliai` | `string` | — | `4` | `open` | — | Našlių skaičius | — |
| `butas1` | `string` | — | `4` | `open` | — | Vieno buto namų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/gyventojai_bustas.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/gyventojai_bustas.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/gyventojai_bustas (https://data.gov.lt/datasets/1911/)
