---
type: Table
title: "TeisMetrolPatikrinimPlanas — Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai"
description: "Duomenų rinkinyje kaupiami Lietuvos metrologijos inspekcijos įmonių patikrinimo ketvirčio planų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lmi/teis_metrol_patikrinimu_planai/TeisMetrolPatikrinimPlanas"
tags: [gov, lmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# TeisMetrolPatikrinimPlanas — Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai

Duomenų rinkinyje kaupiami Lietuvos metrologijos inspekcijos įmonių patikrinimo ketvirčio planų duomenys. Viena eilutė rinkinyje atitinka vieną planuojamą patikrinimą. Rinkinyje nurodomos įmonės, jų rizika, adresas ir (arba) veiklos vieta, veiklos rūšis pagal ekonominės veiklos rūšies klasifikatoriaus antrąją redakciją. Rinkinį sudaro nuo 2021 metų sausio 1 dienos sukaupti duomenys.

- **Model:** `datasets/gov/lmi/teis_metrol_patikrinimu_planai/TeisMetrolPatikrinimPlanas`[^manifest]
- **Dataset:** [Lietuvos metrologijos inspekcijos įmonių patikrinimų ketvirčio planai](../teis_metrol_patikrinimu_planai.md) (`datasets/gov/lmi/teis_metrol_patikrinimu_planai`)
- **Manifest CSV:** [datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmi/teis_metrol_patikrinimu_planai/TeisMetrolPatikrinimPlanas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikacinis kodas | — |
| `plano_metai` | `date` | `Y` | `4` | `open` | — | Metai, kada pateiktas patikrinimų planas | — |
| `plano_ketvirtis` | `integer` | — | `4` | `open` | — | Ketvirtis, kada pateiktas patikrinimų planas | — |
| `numatomas_patikrinimo_menuo` | `string` | — | `4` | `open` | — | Numatomas patikrinimo mėnuo | — |
| `skyrius` | `string` | — | `4` | `open` | — | Skyrius | — |
| `rizika` | `string` | — | `4` | `open` | — | Įmonės rizika (kuo įmonės veikla gali sukelti didesnę žalą, tuo jos rizika yra didesnė ir patikrinimai yra vykdomi dažniau) | — |
| `imones_kodas` | `string` | — | `4` | `open` | — | Įmonės kodas | — |
| `ukio_subjekto_pavadinimas` | `string` | — | `4` | `open` | — | Ūkio subjekto/įmonės pavadinimas | — |
| `ekonomines_veiklos_rusis_pagal_evrk_2_red` | `string` | — | `4` | `open` | — | Tikrinamos įmonės ekonominės veiklos rūšies pavadinimas pagal EVRK 2 redakciją | — |
| `ukio_subjekto_adresas_jar` | `string` | — | `4` | `open` | — | Ūkio subjekto/įmonės adresas juridinių asmenų registre | — |
| `veiklaviete` | `string` | — | `4` | `open` | — | Įmonės veiklos vietos adresas | — |
| `pastabos` | `string` | — | `4` | `open` | — | Profesijos kodas pagal Lietuvos profesijų klasifikatorių | — |
| `plano_pataisymo_nr` | `integer` | — | `2` | `open` | — | Plano pataisymo numeris (jei yra) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `skyrius` | `"Rytų regiono skyrius"` | — | — | Rytų regiono skyrius | — |
| `skyrius` | `"Vakarų regiono skyrius"` | — | — | Vakarų regiono skyrius | — |
| `rizika` | `"Didelės rizikos"` | — | — | Didelė įmonės rizika | — |
| `rizika` | `"Vidutinės rizikos"` | — | — | Vidutinė įmonės rizika | — |
| `rizika` | `"Mažos rizikos"` | — | — | Maža įmonės rizika | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lmi/teis_metrol_patikrinimu_planai.csv
