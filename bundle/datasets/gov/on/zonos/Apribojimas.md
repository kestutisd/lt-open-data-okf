---
type: Table
title: "Apribojimas — Oro erdvės apribojimų duomenys"
description: "Rinkinyje pateikiami duomenys apie oro erdvės Lietuvoje apribojimus nuo 2024m. kovo mėn. Nurodoma tiksli apribojimų pradžia ir pabaiga, specialiosios oro erdvės pavadinimas bei oro erdvės žemutinė ir viršutinė ribos."
resource: "https://get.data.gov.lt/datasets/gov/on/zonos/Apribojimas"
tags: [gov, on, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/on/zone_rezervations.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/zone_rezervations.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apribojimas — Oro erdvės apribojimų duomenys

Rinkinyje pateikiami duomenys apie oro erdvės Lietuvoje apribojimus nuo 2024m. kovo mėn. Nurodoma tiksli apribojimų pradžia ir pabaiga, specialiosios oro erdvės pavadinimas bei oro erdvės žemutinė ir viršutinė ribos.

- **Model:** `datasets/gov/on/zonos/Apribojimas`[^manifest]
- **Dataset:** [Oro erdvės apribojimų duomenys](../zonos.md) (`datasets/gov/on/zonos`)
- **Manifest CSV:** [datasets/gov/on/zone_rezervations.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/zone_rezervations.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/on/zonos/Apribojimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo unikalus identifikatorius | — |
| `create_date` | `datetime` | `S` | `4` | `open` | — | Sukūrimo data | — |
| `rezervation_date` | `date` | `D` | `4` | `open` | — | Erdvės apribojimo data | — |
| `est_from` | `time` | `T` | `4` | `open` | — | Galiojimas nuo (laikas) | — |
| `from_d0` | `string` | — | `4` | `open` | — | Realus oro erdvės panaudojimo pradžios laikas | — |
| `est_till` | `time` | `T` | `4` | `open` | — | Galiojimas iki | — |
| `till_d0` | `string` | — | `4` | `open` | — | Realus oro erdvės panaudojimo pabaigos laikas | — |
| `cancel_d0` | `datetime` | `S` | `4` | `open` | — | Jei oro erdvės panaudojimas atšauktas (tactical lygmenyje), šiame lauke atsiranda datos ir laiko įrašas | — |
| `zone_name` | `string` | — | `4` | `open` | — | Spec. veiklos oro erdvės pavadinimas | — |
| `zone_lower` | `string` | — | `4` | `open` | — | Erdvės žemutinė riba. Ribos nurodomos šiais dydžiais: MSL- Mean Sea Level , FL – Flight Level, AGL - Above Ground level, GND – Ground. | — |
| `zone_upper` | `string` | — | `4` | `open` | — | Erdvės viršutinė riba. Ribos nurodomos šiais dydžiais: MSL- Mean Sea Level , FL – Flight Level, AGL - Above Ground level, GND – Ground. | — |
| `name_svoe` | `string` | — | `4` | `open` | — | Oro erdvės klasifikacija pagal aukštį | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `name_svoe` | `"Žemiau FL95"` | — | — | — | — |
| `name_svoe` | `"Aukščiau FL95"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/on/zone_rezervations.csv
