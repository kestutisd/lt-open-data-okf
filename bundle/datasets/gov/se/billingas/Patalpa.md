---
type: Table
title: "Patalpa — Patalpos"
description: "Patalpos ir pastato, kuriame yra patalpa informacija, kur teikiamos Šiaulių energijos paslaugos."
resource: "https://get.data.gov.lt/datasets/gov/se/billingas/Patalpa"
tags: [gov, se, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/se/registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# Patalpa — Patalpos

Patalpos ir pastato, kuriame yra patalpa informacija, kur teikiamos Šiaulių energijos paslaugos. Rinkinyje pateikiama patalpos plotas, pastato statybos metai, aukštų skaičius, pastato tipas, jo paskirtis. Dėl konfidencialumo užtikrinimo pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes – triukšmą.

- **Model:** `datasets/gov/se/billingas/Patalpa`[^manifest]
- **Dataset:** [Sistema skirta AB Šiaulių energija klientų duomenų valdymui, karšto vandens bei šildymo tiekimo paslaugų apskaičiavimui, sąskaitų leidimui ir skolų valdymui.](../billingas.md) (`datasets/gov/se/billingas`)
- **Manifest CSV:** [datasets/gov/se/registras.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/se/billingas/Patalpa`
- **Primary Key (`ref`):** `patalpos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patalpos_id` | `string` | — | `4` | `open` | — | Unikalus patalpos identifikatorius | — |
| `pastato_id` | `string` | — | `4` | `open` | — | Unikalus pastato identitfikatorius | — |
| `patalpos_plotas` | `number` | — | `4` | `open` | — | Patalpos plotas | — |
| `statybos_metai` | `date` | `Y` | `4` | `open` | — | Statybos metai, gauti iš Registrų Centro | — |
| `pastato_aukstu_skaicius` | `number` | — | `4` | `open` | — | Pastato aukštų skaičius, gautas iš Registrų Centro | — |
| `pastato_tipas` | `string` | — | `4` | `open` | — | Pastato tipas, gautas iš Registrų Centro | — |
| `pastato_paskirtis` | `string` | — | `4` | `open` | — | Pastato paskirtis, gautas iš Registrų Centro | — |
| `x_koord_lks` | `number` | — | `4` | `open` | — | X koordinatės LKS sistemoje. Dėl konfidencialumo užtikrinimo pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą. | — |
| `y_koord_lks` | `number` | — | `4` | `open` | — | Y koordinatės LKS sistemoje. Dėl konfidencialumo užtikrinimo pateiktų koordinačių įrašai yra modifikuoti pridedant atsitiktines vertes - triukšmą. | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Geometrija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/se/registras.csv
