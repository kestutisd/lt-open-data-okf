---
type: Table
title: "UkioSubjNustatytPazeidimas — Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai"
description: "Duomenų rinkinyje pateikiama informacija apie ūkio subjektus, juridinius ir fizinius (įskaitant ūkininkus) asmenis, kurių vykdomoje veikloje naudojamų matavimo priemonių arba fasuotų prekių patikrinimo metu Lietuvos metrologijos..."
resource: "https://get.data.gov.lt/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus/UkioSubjNustatytPazeidimas"
tags: [gov, lmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# UkioSubjNustatytPazeidimas — Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai

Duomenų rinkinyje pateikiama informacija apie ūkio subjektus, juridinius ir fizinius (įskaitant ūkininkus) asmenis, kurių vykdomoje veikloje naudojamų matavimo priemonių arba fasuotų prekių patikrinimo metu Lietuvos metrologijos inspekcija nustatė pažeidimus. Fizinių asmenų duomenys yra užšifruoti. Jeigu įmonės kodas yra negaliojantis, įmonės kodo ir pavadinimo stulpeliai yra šifruojami. Taip pat, jeigu pažeidimą įvykdžiusios įmonės kodas nurodytas klaidingai, įmonės pavadinimo ir kodo stulpeliai gali būti užšifruoti. Ekonominės veiklos rūšių klasifikatoriaus (EVRK) kodai pateikti pagal EVRK 2 redakciją. Viena duomenų rinkinio eilutė atitinka vieną pažeidimą.

Geografinė aprėptis – visa Lietuva.

Duomenų aprėptis – nuo 2020 metų sausio 1 d.

Duomenų teikėjas – Lietuvos metrologijos inspekcija.

- **Model:** `datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus/UkioSubjNustatytPazeidimas`[^manifest]
- **Dataset:** [Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai](../us_kur_lmi_nustate_pazeidimus.md) (`datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus`)
- **Manifest CSV:** [datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus/UkioSubjNustatytPazeidimas`
- **Primary Key (`ref`):** `patikrinimo_akto_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patikrinimo_akto_kodas` | `string` | — | `4` | `open` | — | Patikrinimo akto kodas, unikalus eilutės įrašo identifikatorius | — |
| `patikrinimo_data` | `date` | `D` | `4` | `open` | — | Data, kada buvo atliktas patikrinimas | — |
| `kas_buvo_tikrinama` | `string` | — | `4` | `open` | — | Kas buvo tikrinama (matavimo priemonės ar fasuotos prekės) | — |
| `patikrinta_mp_ukio_subj_uzsakymu` | `integer` | `U` | `4` | `open` | — | Matavimo priemonių skaičius, kurioms buvo atlikta privalomoji metrologinė patikra, užsakyta ūkio subjekto/įmonės, gavus Lietuvos metrologijos inspekcijos pranešimą apie artėjantį patikrinimą | — |
| `patikrinta_mp_patikros_metu` | `integer` | `U` | `4` | `open` | — | Patikros metu patikrintų matavimo priemonių skaičius | — |
| `tikrinamo_obj_tipas` | `string` | — | `4` | `open` | — | Tikrinto objekto tipas | — |
| `tikrinama_imone` | `string` | — | `4` | `open` | — | Tikrinto ūkio subjekto/įmonės pavadinimas | — |
| `tikrinamos_im_kodas` | `string` | — | `4` | `open` | — | Tikrinto ūkio subjekto/įmonės kodas juridinių asmenų registre | — |
| `tikrinamos_im_teis_form_pavad` | `string` | — | `4` | `open` | — | Tikrinto ūkio subjekto/įmonės teisinės formos pavadinimas | — |
| `im_evrk_kodas` | `string` | — | `4` | `open` | — | Tikrinamo ūkio subjekto/įmonės ekonominės veiklos rūšies pavadinimas pagal EVRK 2 redakciją | — |
| `tikrinto_obj_adresas` | `string` | — | `4` | `open` | — | Tikrinto ūkio subjekto/įmonės adresas juridinių asmenų registre | — |
| `valdanti_imone` | `string` | — | `4` | `open` | — | Tikrintą objektą valdančio ūkio subjekto/įmonės pavadinimas | — |
| `valdancios_im_adresas` | `string` | — | `4` | `open` | — | Tikrintą objektą valdančio ūkio subjekto/įmonės adresas juridinių asmenų registre | — |
| `valdancios_im_savivaldybe` | `string` | — | `4` | `open` | — | Tikrintą objektą valdančio ūkio subjekto/įmonės savivaldybė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kas_buvo_tikrinama` | `"Matavimo priemonės"` | — | — | Buvo tikrintos matavimo priemonės | — |
| `kas_buvo_tikrinama` | `"Fasuotos prekės"` | — | — | Buvo tikrintos fasuotos prekės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv
