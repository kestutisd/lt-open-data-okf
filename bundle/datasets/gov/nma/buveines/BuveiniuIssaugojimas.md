---
type: Table
title: "BuveiniuIssaugojimas — Lietuvos kaimo plėtros programos 2014-2020 priemonė \"Meldinės nendrinukės buveinių išsaugojimas\" bendra informacija"
description: "Spinta table datasets/gov/nma/buveines/BuveiniuIssaugojimas (20 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/buveines/BuveiniuIssaugojimas"
tags: [gov, nma, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/buveines.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/buveines.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# BuveiniuIssaugojimas — Lietuvos kaimo plėtros programos 2014-2020 priemonė "Meldinės nendrinukės buveinių išsaugojimas" bendra informacija

- **Model:** `datasets/gov/nma/buveines/BuveiniuIssaugojimas`[^manifest]
- **Dataset:** [datasets/gov/nma/buveines](../buveines.md) (`datasets/gov/nma/buveines`)
- **Manifest CSV:** [datasets/gov/nma/buveines.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/buveines.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/buveines/BuveiniuIssaugojimas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priemone` | `string` | — | `4` | `open` | — | Priemonė | — |
| `veiklos_sritis` | `string` | — | `4` | `open` | — | Veiklos sritis | — |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_gavimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos gavimo data | — |
| `projekto_igyvendinimo_vieta` | `string` | — | `2` | `open` | — | Projekto įgyvendinimo vieta | — |
| `prasoma_paramos_suma` | `number` | — | `2` | `open` | — | Prašoma paramos suma | — |
| `bylos_etapas` | `string` | — | `4` | `open` | — | Bylos etapas | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Sutarties pasirašymo data | — |
| `skirta_paramos_suma` | `number` | — | `2` | `open` | — | Skirta pasirašymo suma | — |
| `es_paramos_dalis` | `number` | — | `2` | `open` | — | ES paramos dalis | — |
| `lt_paramos_dalis` | `number` | — | `2` | `open` | — | LT paramos dalis | — |
| `ismoketa_paramos_suma` | `number` | — | `2` | `open` | — | Išmokėta paramos suma | — |
| `sankciju_suma` | `number` | — | `2` | `open` | — | Sankscijų suma | — |
| `projekto_pradzia` | `date` | `D` | `4` | `open` | — | Projekto pradžia | — |
| `projekto_pabaiga` | `date` | `D` | `4` | `open` | — | Projekto pabaiga | — |
| `projekto_isip_pabaigos_data` | `date` | `D` | `4` | `open` | — | Projekto įsipareigojimų pabaigos data | — |
| `paraiskos_nutr_data` | `date` | `D` | `4` | `open` | — | Paraiškos nutraukimo data | — |
| `kvietimo_pradzia` | `date` | `D` | `4` | `open` | — | Kvietimo pradžia | — |
| `kvietimo_pabaiga` | `date` | `D` | `4` | `open` | — | Kvietimo pabaiga | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |
| `bylos_etapas` | `"Išregistravimas"` | — | — | Išregistravimas | — |
| `bylos_etapas` | `"Atmetimas"` | — | — | Atmetimas | — |
| `bylos_etapas` | `"Paramos administravimas"` | — | — | Paramos administravimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `projekto_igyvendinimo_vieta` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `prasoma_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `skirta_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `es_paramos_dalis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `lt_paramos_dalis` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ismoketa_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sankciju_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/buveines.csv
