---
type: Table
title: "Vilkas — Duomenys apie sumedžiotus vilkus"
description: "Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles/Vilkas"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilkas — Duomenys apie sumedžiotus vilkus

Rinkinyje pateikiami išsamūs nuo 2018 m. iki dabar kaupiami vilkų medžioklės Lietuvos Respublikos teritorijoje duomenys. Rinkinio objektas - vienas sumedžiotas vilkas. Nurodomas medžioklės laikas, vieta, būdas, duomenys apie vilką (amžius, lytis, sveikatos būklė) ir gaują (jauniklių ir suaugusių vilkų skaičius). Duomenų teikėjas: Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos.

- **Model:** `datasets/gov/vstt/vilku_medziokles/Vilkas`[^manifest]
- **Dataset:** [Sumedžioti vilkai Lietuvoje](../vilku_medziokles.md) (`datasets/gov/vstt/vilku_medziokles`)
- **Manifest CSV:** [datasets/gov/vstt/medziokles.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles/Vilkas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `iraso_data` | `datetime` | `L` | `4` | `open` | — | Įrašo sukūrimo data | — |
| `medziokles_laikas` | `datetime` | `L` | `4` | `open` | — | Vilko sumedžiojimo laiko žyma | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė, kurioje įvyko medžioklė. Požymis buvo išskaičiuotas vilko sumedžiojimo vietos koordinatę prijungiant prie 10x10 km gardelių, kuriomis suskirstyta Lietuvos Respublikos teritorija. Kiekviena gardelė yra priskirta tam tikrai savivaldybei, tad pagal šį požymį buvo išskaičiuota vilko sumedžiojimo vietos savivaldybė. | — |
| `medziojimo_budas` | `string` | — | `4` | `open` | — | Vilko medžiojimo būdas | — |
| `amzius` | `string` | — | `4` | `open` | — | Vilko amžius | — |
| `lytis` | `string` | — | `4` | `open` | — | Vilko lytis | — |
| `ar_pazeistas_niezu` | `boolean` | — | `4` | `open` | — | Požymis, ar vilkas buvo pažeistas niežų | — |
| `ar_kiti_defektai` | `boolean` | — | `4` | `open` | — | Požymis, ar vilkas turėjo kitų defektų | — |
| `ar_priklause_gaujai` | `boolean` | — | `4` | `open` | — | Požymis, ar vilkas priklausė gaujai | — |
| `viso_gaujoje_vnt` | `integer` | `U` | `4` | `open` | — | Bendras vilkų skaičius gaujoje | — |
| `suaugusiu_gaujoje_vnt` | `integer` | `U` | `4` | `open` | — | Bendras suaugusių vilkų skaičius gaujoje | — |
| `jaunikliu_gaujoje_vnt` | `integer` | `U` | `4` | `open` | — | Bendras jauniklių skaičius gaujoje | — |
| `geometrija` | `geometry(point, 4326)` | — | `4` | `open` | — | Sumedžioto vilko taško koordinatė. | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `medziojimo_budas` | `"tykojant"` | — | — | — | — |
| `medziojimo_budas` | `"varant"` | — | — | — | — |
| `medziojimo_budas` | `"kita"` | — | — | — | — |
| `medziojimo_budas` | `"su vėliavėlėmis"` | — | — | — | — |
| `amzius` | `"Vyresnis nei 1 metų amžiaus"` | — | — | — | — |
| `amzius` | `"Jauniklis iki 1 metų amžiaus"` | — | — | — | — |
| `lytis` | `"Patinas"` | — | — | — | — |
| `lytis` | `"Patelė"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv
