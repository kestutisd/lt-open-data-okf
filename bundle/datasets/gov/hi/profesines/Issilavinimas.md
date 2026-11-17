---
type: Table
title: "Issilavinimas — Profesinių ligų atvejai pagal išsilavinimą"
description: "Spinta table datasets/gov/hi/profesines/Issilavinimas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/profesines/Issilavinimas"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/profesines.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Issilavinimas — Profesinių ligų atvejai pagal išsilavinimą

- **Model:** `datasets/gov/hi/profesines/Issilavinimas`[^manifest]
- **Dataset:** [Lietuvos Respublikos profesinių ligų valstybės registro duomenys](../profesines.md) (`datasets/gov/hi/profesines`)
- **Manifest CSV:** [datasets/gov/hi/profesines.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/profesines/Issilavinimas`
- **Primary Key (`ref`):** `atvejis_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atvejis_id` | `string` | — | `4` | `open` | — | Profesinės ligos atvejo identifikatorius | Lietuvos Respublikos profesinių ligų valstybės registro objekto įregistravimo data |
| `pagr_tlk_kodas` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Pagrindinės profesinės ligos kodas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `pagr_tlk_pav` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[name]](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Pagrindinės profesinės ligos pavadinimas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `lyties_kodas` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `lpk` | `string` | — | `4` | `open` | — | Paciento profesija | Pagal Lietuvos profesijų klasifikatorių |
| `evrk` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis[kodas]](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) | `4` | `open` | — | EVRK kodas | Ekonominės veiklos rūšies klasifikatoriaus kodas. Nurodo, kuriame sektoriuje pacientas dirba |
| `year` | `integer` | `yr` | `2` | `open` | — | Metai | Profesinės ligos užregistravimo metai |
| `quarter` | `integer` | `3mo` | `2` | `open` | — | Ketvirtis | Profesinės ligos užregistravimo ketvirtis |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lyties_kodas` | `'1'` | — | — | Vyras | — |
| `lyties_kodas` | `'2'` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/profesines.csv
