---
type: Table
title: "Statistika"
description: "Spinta table datasets/gov/nta/statistika/Statistika (19 columns)."
tags: [gov, nta, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nta/statistika.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/statistika.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Statistika

- **Model:** `datasets/gov/nta/statistika/Statistika`[^manifest]
- **Dataset:** [datasets/gov/nta/statistika](../statistika.md) (`datasets/gov/nta/statistika`)
- **Manifest CSV:** [datasets/gov/nta/statistika.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/statistika.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `bylos_numeris`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teismo_rumai` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Teismo rūmai | — |
| `bylos_numeris` | `string` | — | `2` | `open` | — | Bylos numeris | — |
| `procesinis_numeris` | `string` | — | `3` | `open` | — | Procesinis numeris | — |
| `gauta` | `date` | `D` | `4` | `open` | — | Gavimo data | — |
| `baigta` | `date` | `D` | `4` | `open` | — | Baigimo data | — |
| `teisejo_numeris` | `integer` | — | `3` | `open` | — | Teisėjo numeris | — |
| `teisejas` | `string` | — | `3` | `public` | — | Teisėjas | — |
| `instancija` | `string` | — | `4` | `open` | — | Instancija | — |
| `tipas` | `string` | — | `2` | `open` | — | Bylos tipas | — |
| `potipis` | `string` | — | `2` | `open` | — | Bylos potipis | — |
| `rezultatas` | `string` | — | `3` | `open` | — | Rezultatas/Sprendimas | — |
| `nagrinejimo_trukme` | `integer` | — | `3` | `open` | — | Nagrinėjimo trukmė | — |
| `kreiptasi_ett` | `boolean` | — | `3` | `open` | — | Kreiptąsi į ETT (Europos Sąjungos teisingumo teismą) | — |
| `kreiptasi_kt` | `boolean` | — | `3` | `open` | — | Kreiptąsi į Konstitucinį teismą | — |
| `naudotos_es_teises_normos` | `boolean` | — | `3` | `open` | — | Naudotos ES teisės normos | — |
| `europos_aresto_orderis` | `boolean` | — | `3` | `open` | — | Europos arešto orderis | — |
| `kategorijos_kodas` | `string` | — | `4` | `open` | — | Bylos kategorijos kodas | — |
| `kategorija` | `string` | — | `3` | `open` | — | Bylos kategorija | — |
| `klasifikatorius` | `string` | — | `4` | `open` | — | Bylos kategorijos klasifikatorius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `instancija` | `"I-a instancija"` | — | — | I-a instancija | — |
| `instancija` | `"Apeliacinė instancija"` | — | — | Apeliacinė instancija | — |
| `instancija` | `"Kasacinė instancija"` | — | — | Kasacinė instancija | — |
| `instancija` | `"Vienintelė instancija"` | — | — | Vienintelė instancija | — |
| `tipas` | `"administracinė byla"` | — | — | Administracinė byla | — |
| `tipas` | `"civilinė byla"` | — | — | Civilinė byla | — |
| `tipas` | `"baudžiamoji byla"` | — | — | Baudžiamoji byla | — |
| `tipas` | `"administracinių teisės pažeidimų/administracinių nusižengimų byla"` | — | — | Administracinių teisės pažeidimų/administracinių nusižengimų byla | — |
| `klasifikatorius` | `"Administracinių bylų kategorijų klasifikatorius (N)"` | — | — | Administracinių bylų kategorijų klasifikatorius (N) | — |
| `klasifikatorius` | `"Baudžiamųjų bylų kategorijų klasifikatorius (N)"` | — | — | Baudžiamųjų bylų kategorijų klasifikatorius (N) | — |
| `klasifikatorius` | `"Civilinių bylų kategorijų klasifikatorius (N)"` | — | — | Civilinių bylų kategorijų klasifikatorius (N) | — |
| `klasifikatorius` | `"Administracinių nusižengimų bylų klasifikatorius (N)"` | — | — | Administracinių nusižengimų bylų klasifikatorius (N) | — |
| `klasifikatorius` | `"Administracinių bylų kategorijos"` | — | — | Administracinių bylų kategorijos | — |
| `klasifikatorius` | `"Administracinių bylų kategorijų klasifikatorius"` | — | — | Administracinių bylų kategorijų klasifikatorius | — |
| `klasifikatorius` | `"Baudžiamųjų bylų kategorijų klasifikatorius"` | — | — | Baudžiamųjų bylų kategorijų klasifikatorius | — |
| `klasifikatorius` | `"Civilinių bylų kategorijų klasifikatorius"` | — | — | Civilinių bylų kategorijų klasifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bylos_numeris` | `create(property: "byla", type: "ref", ref: "Byla")` | `property` | `4` | `open` | — | — | — |
| `bylos_numeris` | `update(property: "byla.numeris", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `tipas` | `update(property: "byla.tipas", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `potipis` | `update(property: "byla.potipis", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nta/statistika.csv
