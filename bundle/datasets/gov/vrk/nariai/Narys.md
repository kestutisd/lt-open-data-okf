---
type: Table
title: "Narys"
description: "Spinta table datasets/gov/vrk/nariai/Narys (12 columns)."
tags: [gov, vrk, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/nariai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/nariai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Narys

- **Model:** `datasets/gov/vrk/nariai/Narys`[^manifest]
- **Dataset:** [datasets/gov/vrk/nariai](../nariai.md) (`datasets/gov/vrk/nariai`)
- **Manifest CSV:** [datasets/gov/vrk/nariai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/nariai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `nariai_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nariai_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `org_tipas` | `string` | — | `4` | `open` | — | Organizacijos tipas (Politinė partija | Politinis komitetas) |
| `org_ja_kodas` | `integer` | — | `4` | `open` | — | Politinės organizacijos juridinio asmens kodas Juridinių asmenų registre | Politinės organizacijos juridinio asmens kodas Juridinių asmenų registre. Sąsaja su RC atvertu duomenų rinkiniu: https://data.gov.lt/dataset/lietuvos-respublikos-politiniu-partiju-duomenys |
| `org_pavadinimas` | `string` | — | `4` | `open` | — | Politinės organizacijos pavadinimas | Pateikiami visi registruoti ir priimti/nepriimti nario mokesčio mokėjimai visose politinėse organizacijose. Sąsaja su RC atvertu duomenų rinkiniu: https://data.gov.lt/dataset/lietuvos-respublikos-politiniu-partiju-duomenys |
| `ataskaitiniai_metai` | `integer` | — | `4` | `open` | — | Nario mokesčio mokėjimo metai | — |
| `moketojas` | `string` | — | `4` | `open` | — | Politinės organizacijos narys, sumokėjęs mokestį | Naudojamas HASH kodas duomenų rinkiniui, t. y. vienodas HASH kodas (ar ID) sugeneruojamas konkrečiam asmeniui ir jis yra vienodas duomenų rinkinyje |
| `mok_data` | `date` | `D` | `4` | `open` | — | Mokėjimo data | Formatas (mmmm-mm-dd) |
| `mok_suma` | `number` | — | `4` | `open` | — | Įmokos dydis | Sumokėto partijos nario mokesčio dydis (EUR) |
| `mok_busena` | `string` | — | `4` | `open` | — | Nario mokesčio priėmimo būsena | Nario mokesčių priėmimo būsena (Priimti mokesčiai / Nepriimti mokesčiai) |
| `mok_budas` | `string` | — | `4` | `open` | — | Nario mokesčio mokėjimo būdas | Nario mokesčių mokėjimo būdas (Pavedimu / Grynaisiais) |
| `lytis` | `string` | — | `4` | `open` | — | Politinės organizacijos nario lytis | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Politinės organizacijos nario amžiaus grupė (nario mokesčio mokėjimo dieną) | Rodomas politinės organizacijos nario amžiaus grupė intervalais (nuo - iki), kas 5 metai. Amžiaus grupė nustatoma nario mokesčio mokėjimo dieną. |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `org_tipas` | `"Partija"` | — | — | Partija | — |
| `org_tipas` | `"Politinis komitetas (SAV)"` | — | — | Politinis komitetas (SAV) | — |
| `mok_busena` | `"P"` | — | — | Priimti mokesčiai | — |
| `mok_busena` | `"A"` | — | — | Nepriimti mokesčiai | — |
| `mok_budas` | `"P"` | — | — | Pavedimu | — |
| `mok_budas` | `"G"` | — | — | Grynaisiais | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `amziaus_grupe` | `"18-24"` | — | — | Amžiaus grupė nuo 18 iki 24 metų | — |
| `amziaus_grupe` | `"25-29"` | — | — | Amžiaus grupė nuo 25 iki 29 metų | — |
| `amziaus_grupe` | `"30-34"` | — | — | Amžiaus grupė nuo 30 iki 34 metų | — |
| `amziaus_grupe` | `"35-39"` | — | — | Amžiaus grupė nuo 35 iki 39 metų | — |
| `amziaus_grupe` | `"40-44"` | — | — | Amžiaus grupė nuo 40 iki 44 metų | — |
| `amziaus_grupe` | `"45-49"` | — | — | Amžiaus grupė nuo 45 iki 49 metų | — |
| `amziaus_grupe` | `"50-54"` | — | — | Amžiaus grupė nuo 50 iki 54 metų | — |
| `amziaus_grupe` | `"55-59"` | — | — | Amžiaus grupė nuo 55 iki 59 metų | — |
| `amziaus_grupe` | `"60-64"` | — | — | Amžiaus grupė nuo 60 iki 64 metų | — |
| `amziaus_grupe` | `"65-69"` | — | — | Amžiaus grupė nuo 65 iki 69 metų | — |
| `amziaus_grupe` | `"70-74"` | — | — | Amžiaus grupė nuo 70 iki 74 metų | — |
| `amziaus_grupe` | `"75-79"` | — | — | Amžiaus grupė nuo 75 iki 79 metų | — |
| `amziaus_grupe` | `"80+"` | — | — | Amžiaus grupė nuo 80 metų | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/nariai.csv
