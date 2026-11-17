---
type: Table
title: "KaimoGyventojas2kmNuoKelio — Kaimo gyventojų, gyvenančių 2 km spinduliu nuo visus metus funkcionuojančio kelio, dalis, 1 km stačiakampėse gardelėse"
description: "Jungtinių Tautų 70-ojoje sesijoje 2015 m. rugsėjo 25 d. priimta Generalinės Asamblėjos rezoliucija „Keiskime mūsų pasaulį: Darnaus vystymosi darbotvarkė iki 2030 metų“."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sdg/KaimoGyventojas2kmNuoKelio"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sdg/sdg.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sdg/sdg.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# KaimoGyventojas2kmNuoKelio — Kaimo gyventojų, gyvenančių 2 km spinduliu nuo visus metus funkcionuojančio kelio, dalis, 1 km stačiakampėse gardelėse

Jungtinių Tautų 70-ojoje sesijoje 2015 m. rugsėjo 25 d. priimta Generalinės Asamblėjos rezoliucija „Keiskime mūsų pasaulį: Darnaus vystymosi darbotvarkė iki 2030 metų“. Vienas iš darnaus vystymosi rodiklių, parengtas detaliu, 1 km gardelių, lygmeniu: 9.1.1. Kaimo gyventojų, gyvenančių 2 km spinduliu nuo visus metus funkcionuojančio kelio, dalis.

- **Model:** `datasets/gov/lsd/sdg/KaimoGyventojas2kmNuoKelio`[^manifest]
- **Dataset:** [Darnaus vystymosi rodikliai](../sdg.md) (`datasets/gov/lsd/sdg`)
- **Manifest CSV:** [datasets/gov/lsd/sdg/sdg.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sdg/sdg.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sdg/KaimoGyventojas2kmNuoKelio`
- **Primary Key (`ref`):** `grid_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grid_id` | `ref` | [/datasets/gov/lsd/grid/Grid1KmSq](../grid/Grid1KmSq.md) | `4` | `open` | — | Stačiakampės gardelės unikalus kodas | Susideda iš gardelės dydžio (pvz., 1x1km) ir X ir Y koordinačių pirmųjų penkių skaičių (pvz., 1x1kmX30000Y60000) |
| `pop_2km` | `integer` | — | `4` | `open` | — | Tikslinių metų gyventojų, patenkančių į 2 km spindulį nuo visus metus funkcionuojančio kelio skaičius. Jei atitinkamoje gardelėje gyventojų yra mažiau nei 3 - nuasmeninant duomenis įrašomas skaičius - 3, jei gyventojų gardelėje nėra - 0, jei gyventojų daugiau nei trys - įrašomas tikras gyventojų skaičius atitinkamoje gardelėje | Jei atitinkamoje gardelėje gyventojų yra mažiau nei 3 - nuasmeninant duomenis įrašomas skaičius - 3, jei gyventojų gardelėje nėra - 0, jei gyventojų daugiau nei trys - įrašomas tikras gyventojų skaičius atitinkamoje gardelėje. |
| `pop_percent_2km` | `number` | `%` | `4` | `open` | — | Tikslinių metų gyventojų, patenkančių į 2 km spindulį nuo visus metus funkcionuojančio kelio dalis, nuo visų gyventojų atitinkamoje gardelėje | — |
| `year` | `integer` | `yr` | `4` | `open` | — | Tiksliniai metai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sdg/sdg.csv
