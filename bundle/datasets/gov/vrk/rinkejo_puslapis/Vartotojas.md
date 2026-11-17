---
type: Table
title: "Vartotojas — Rinkėjo puslapio naudotojo paveikslas"
description: "Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo puslapis“ seansų duomenų ir pasaulinio masto IP adresų pagal geografinę vietovę rinkinio."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkejo_puslapis/Vartotojas"
tags: [gov, vrk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vartotojas — Rinkėjo puslapio naudotojo paveikslas

Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo puslapis“ seansų duomenų ir pasaulinio masto IP adresų pagal geografinę vietovę rinkinio. VRKIS duomenys saugomi nuo 2011 m. ir yra atnaujinami kasdien, o iki 2024 m. buvęs aktualus IP adresų rinkinys nebėra atnaujinamas. Duomenų rinkinį sudaro: prisijungimo seanso identifikatorius, pseudonimizuotas rinkėjo asmens kodas, gimimo metai, lytis, pagal IP adresą nustatytos tikėtina prisijungimo valstybė ir vietovė, prisijungimo ir atsijungimo laikas bei atsijungimo priežastis.

- **Model:** `datasets/gov/vrk/rinkejo_puslapis/Vartotojas`[^manifest]
- **Dataset:** [Rinkėjo puslapio naudotojo paveikslas](../rinkejo_puslapis.md) (`datasets/gov/vrk/rinkejo_puslapis`)
- **Manifest CSV:** [datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkejo_puslapis/Vartotojas`
- **Primary Key (`ref`):** `sesijos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sesijos_id` | `string` | — | `4` | `open` | — | Seanso identifikatorius | — |
| `rinkejo_asmens_kodas` | `string` | — | `4` | `open` | — | Prisijungusio rinkėjo pseudonimizuotas asmens kodas | — |
| `rinkejo_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Prisijungusio rinkėjo gimimo metai | — |
| `rinkejo_lytis` | `string` | — | `4` | `open` | — | Prisijungusio rinkėjo lytis | — |
| `tiketina_prisijungimo_salis` | `string` | — | `4` | `open` | — | Tikėtina prisijungimo valstybė sprendžiant iš IP adreso | — |
| `tiketina_prisijungimo_vietove` | `string` | — | `4` | `open` | — | Tikėtina prisijungimo vietovė sprendžiant iš IP adreso | — |
| `prisijungimo_laikas` | `datetime` | `S` | `4` | `open` | — | Vartotojo prisijungimo prie sistemos data ir laikas | — |
| `atsijungimo_laikas` | `datetime` | `S` | `4` | `open` | — | Vartotojo atsijungimo nuo sistemos data ir laikas | — |
| `atsijungimo_priezastis` | `string` | — | `4` | `open` | — | Vartotojo atsijungimo nuo sistemos priežastis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rinkejo_lytis` | `"Vyras"` | `V` | — | Vyras | — |
| `rinkejo_lytis` | `"Moteris"` | `M` | — | Moteris | — |
| `atsijungimo_priezastis` | `"Seansas nustojo galioti"` | `Seansas nustojo galioti` | — | Seansas nustojo galioti | — |
| `atsijungimo_priezastis` | `"Sistemos klaida"` | `Sistemos klaida` | — | Sistemos klaida | — |
| `atsijungimo_priezastis` | `"Seansas nutrauktas vartotojo"` | `Seansas nutrauktas vartotojo` | — | Seansas nutrauktas vartotojo | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv
