---
type: Table
title: "TeismasSprendimas"
description: "Spinta table datasets/gov/nta/teismu_sprendimai/TeismasSprendimas (21 columns)."
tags: [gov, nta, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nta/teismu_sprendimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/teismu_sprendimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TeismasSprendimas

- **Model:** `datasets/gov/nta/teismu_sprendimai/TeismasSprendimas`[^manifest]
- **Dataset:** [datasets/gov/nta/teismu_sprendimai](../teismu_sprendimai.md) (`datasets/gov/nta/teismu_sprendimai`)
- **Manifest CSV:** [datasets/gov/nta/teismu_sprendimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/teismu_sprendimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teismo_rumai` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Teismo rūmai | — |
| `id` | `string` | — | `4` | `open` | — | Bylos id | — |
| `bylos_nr` | `string` | — | `2` | `open` | — | Bylos numeris | — |
| `bylos_eiles_nr` | `string` | — | `2` | `open` | — | Bylos eilės numeris | — |
| `procesinis_numeris` | `string` | — | `3` | `open` | — | Procesinis numeris | — |
| `gauta` | `date` | `D` | `4` | `open` | — | Gavimo data | — |
| `baigta` | `date` | `D` | `4` | `open` | — | Baigimo data | — |
| `teisejo_kodas` | `string` | — | `3` | `open` | — | Teisėjo kodas | — |
| `teisejas` | `string` | — | `3` | `public` | — | Teisėjas | — |
| `kolegija` | `string` | — | `3` | `open` | — | Kolegija | — |
| `instancija` | `string` | — | `4` | `open` | — | Instancija | — |
| `tipas` | `string` | — | `2` | `open` | — | Tipas | — |
| `rezultatas` | `string` | — | `3` | `open` | — | Rezultatas/Sprendimas | — |
| `nagrinejimo_trukme` | `integer` | — | `3` | `open` | — | Nagrinėjimo trukmė | — |
| `sablonine_byla` | `boolean` | — | `3` | `open` | — | Ar tai šabloninė byla | — |
| `naudotos_es_teises_normos` | `boolean` | — | `3` | `open` | — | Ar buvo naudotos ES teisės normos | — |
| `dokumento_id` | `string` | — | `4` | `open` | — | Dokumento ID | — |
| `nuoroda` | `url` | — | `3` | `open` | — | Nuoroda į bylą | — |
| `dokumento_data` | `datetime` | `S` | `4` | `open` | — | Dokumento data | — |
| `salys` | `string` | — | `3` | `open` | — | Šalys | — |
| `kategorijos` | `string` | — | `3` | `open` | — | Kategorijos | — |

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
| `tipas` | `"Dėl bylos teisingumo (specialioji kolegija)"` | — | — | Dėl bylos teisingumo (specialioji kolegija) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bylos_nr` | `create(property: "byla", type: "ref", ref: "Byla")` | `property` | `4` | `open` | — | — | — |
| `bylos_nr` | `update(property: "byla.numeris", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `bylos_eiles_nr` | `update(property: "byla.eiles_nr", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `tipas` | `update(property: "byla.tipas", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nta/teismu_sprendimai.csv
