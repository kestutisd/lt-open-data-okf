---
type: Table
title: "Asmuo — Profesinių ligų įvykių pagrindiniai duomenys"
description: "Spinta table datasets/gov/hi/profesines/Asmuo (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/profesines.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L37"
    last_modified: "2026-11-11T14:39:20Z"
---

# Asmuo — Profesinių ligų įvykių pagrindiniai duomenys

- **Model:** `datasets/gov/hi/profesines/Asmuo`[^manifest]
- **Dataset:** [Lietuvos Respublikos profesinių ligų valstybės registro duomenys](../profesines.md) (`datasets/gov/hi/profesines`)
- **Manifest CSV:** [datasets/gov/hi/profesines.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L37)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo`
- **Primary Key (`ref`):** `m_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m_id` | `string` | — | `4` | `open` | — | Paciento ID | — |
| `pagr_tlk_kodas` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Pagrindinės profesinės ligos kodas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `pagr_tlk_pav` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[name]](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Pagrindinės profesinės ligos pavadinimas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `papild_tlk_kodas` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Papildomas profesinės ligos kodas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `papild_tlk_pav` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[name]](../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Papildomas profesinės ligos pavadinimas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `ligos_eiga` | `string` | — | `4` | `open` | — | Ligos eiga | — |
| `itarta_pav` | `string` | — | `4` | `open` | — | Profesinės ligos įtarimo pavadinimas | — |
| `itarta_kodas` | `string` | — | `4` | `open` | — | Profesinės ligos įtarimo kodas | — |
| `priezasties_kodas` | `string` | — | `4` | `open` | — | Profesinės ligos priežasties kodas | — |
| `priezasties_pav` | `string` | — | `4` | `open` | — | Profesinės ligos priežasties pavadinimas | — |
| `lyties_kodas` | `string` | — | `4` | `open` | — | Paciento lyties kodas | — |
| `lyties_pavadinimas` | `string` | — | `4` | `open` | — | Paciento lyties pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | Užregistruota profesinė liga |
| `year` | `integer` | `yr` | `2` | `open` | — | Metai | Profesinės ligos užregistravimo metai |
| `quarter` | `integer` | `3mo` | `2` | `open` | — | Ketvirtis | Profesinės ligos užregistravimo ketvirtis |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/profesines.csv
