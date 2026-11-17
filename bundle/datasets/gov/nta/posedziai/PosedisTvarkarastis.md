---
type: Table
title: "PosedisTvarkarastis"
description: "Spinta table datasets/gov/nta/posedziai/PosedisTvarkarastis (15 columns)."
tags: [gov, nta, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nta/posedziai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/posedziai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PosedisTvarkarastis

- **Model:** `datasets/gov/nta/posedziai/PosedisTvarkarastis`[^manifest]
- **Dataset:** [datasets/gov/nta/posedziai](../posedziai.md) (`datasets/gov/nta/posedziai`)
- **Manifest CSV:** [datasets/gov/nta/posedziai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nta/posedziai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teismo_rumai` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Teismo rūmai | — |
| `sale` | `string` | — | `3` | `open` | — | Teismo rūmų salė | — |
| `data_laikas` | `datetime` | `S` | `4` | `open` | — | Posėdžio data ir laikas | — |
| `bylos_numeris` | `string` | — | `2` | `open` | — | Bylos numeris | — |
| `procesinis_numeris` | `string` | — | `3` | `open` | — | Procesinis numeris | — |
| `esme` | `string` | — | `3` | `open` | — | Posėdžio tikslas | — |
| `id` | `string` | — | `4` | `open` | — | Posėdžio ID | — |
| `ar_uzdaras_posedis` | `string` | — | `4` | `open` | — | Uždaras/Neuždaras posėdis | — |
| `instancija` | `string` | — | `4` | `open` | — | Instancija | — |
| `bylos_id` | `string` | — | `2` | `open` | — | Bylos ID | — |
| `kolegija` | `string` | — | `3` | `public` | — | Kolegija | — |
| `tipas` | `string` | — | `2` | `open` | — | Bylos tipas | — |
| `procesas` | `string` | — | `4` | `open` | — | — | — |
| `rezultatas` | `string` | — | `3` | `open` | — | — | — |
| `ar_nuotolinis` | `string` | — | `4` | `open` | — | — | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ar_uzdaras_posedis` | `"ne"` | — | — | Neuždaras | — |
| `ar_uzdaras_posedis` | `"taip"` | — | — | Uždaras | — |
| `instancija` | `"I-a instancija"` | — | — | I-a instancija | — |
| `instancija` | `"Apeliacinė instancija"` | — | — | Apeliacinė instancija | — |
| `instancija` | `"Kasacinė instancija"` | — | — | Kasacinė instancija | — |
| `instancija` | `"Vienintelė instancija"` | — | — | Vienintelė instancija | — |
| `tipas` | `"administracinė byla"` | — | — | Administracinė byla | — |
| `tipas` | `"civilinė byla"` | — | — | Civilinė byla | — |
| `tipas` | `"baudžiamoji byla"` | — | — | Baudžiamoji byla | — |
| `tipas` | `"administracinių nusižengimų byla"` | — | — | Administracinių nusižengimų byla | — |
| `tipas` | `"Dėl bylos teisingumo (specialioji kolegija)"` | — | — | Dėl bylos teisingumo (specialioji kolegija) | — |
| `procesas` | `"rašytinis"` | — | — | Rašytinis procesas | — |
| `procesas` | `"žodinis"` | — | — | Žodinis procesas | — |
| `ar_nuotolinis` | `"ne"` | — | — | Ne nuotolinis | — |
| `ar_nuotolinis` | `"taip"` | — | — | Nuotolinis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bylos_numeris` | `update(property: "byla.numeris", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `bylos_id` | `create(property: "byla", type: "ref", ref: "Byla")` | `property` | `4` | `open` | — | — | — |
| `bylos_id` | `update(property: "byla.id", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |
| `tipas` | `update(property: "byla.tipas", type: "")` | `type` | `4` | `open` | `spinta: 216` | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nta/posedziai.csv
