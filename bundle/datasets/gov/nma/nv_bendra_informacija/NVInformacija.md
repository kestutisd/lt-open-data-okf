---
type: Table
title: "NVInformacija — Lietuvos kaimo plėtros programos 2014-2020 priemonė \"Parama Nykstančių Lietuvos senųjų veislių gyvulių ir naminių paukščių išsaugojimui\" bendra informacija"
description: "Spinta table datasets/gov/nma/nv_bendra_informacija/NVInformacija (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/nv_bendra_informacija/NVInformacija"
tags: [gov, nma, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/nv_bendra_informacija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_bendra_informacija.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# NVInformacija — Lietuvos kaimo plėtros programos 2014-2020 priemonė "Parama Nykstančių Lietuvos senųjų veislių gyvulių ir naminių paukščių išsaugojimui" bendra informacija

- **Model:** `datasets/gov/nma/nv_bendra_informacija/NVInformacija`[^manifest]
- **Dataset:** [datasets/gov/nma/nv_bendra_informacija](../nv_bendra_informacija.md) (`datasets/gov/nma/nv_bendra_informacija`)
- **Manifest CSV:** [datasets/gov/nma/nv_bendra_informacija.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/nv_bendra_informacija.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/nv_bendra_informacija/NVInformacija`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `programa` | `string` | — | `3` | `open` | — | Priemonės pavadinimas | — |
| `veiklos_sritis` | `string` | — | `3` | `open` | — | Veiklos sritis | — |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Projekto įgyvendinimo vieta | — |
| `bylos_etapas` | `string` | — | `3` | `open` | — | Bylos etapas | — |
| `sutarties_pasirasymo_data` | `date` | `D` | `4` | `open` | — | Paramos sutarties pasirašymo data | — |
| `ismoketa_paramos_suma` | `number` | — | `2` | `open` | — | Išmokėta paramos suma, Eur | — |
| `sankciju_suma` | `number` | — | `2` | `open` | — | Bendra pritaikytų sankcijų suma, Eur | — |
| `paraiskos_nutr_data` | `date` | `D` | `4` | `open` | — | Paraiškos nutraukimo data | — |
| `kvietimo_pradzia` | `date` | `D` | `4` | `open` | — | Kvietimo pradžia | — |
| `kvietimo_pabaiga` | `date` | `D` | `4` | `open` | — | Kvietimo pabaiga | — |
| `bylos_numeris` | `string` | — | `4` | `open` | — | Projektas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `ismoketa_paramos_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `sankciju_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/nv_bendra_informacija.csv
