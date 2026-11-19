---
type: Table
title: "UkioSubjNustatytPazeidimas — Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai"
description: "Duomenų rinkinyje pateikiama informacija apie ūkio subjektus, juridinius ir fizinius (įskaitant ūkininkus) asmenis, kurių vykdomoje veikloje naudojamų matavimo priemonių arba fasuotų prekių patikrinimo metu Lietuvos metrologijos inspekcija nustatė pažeidimus."
resource: "https://get.data.gov.lt/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus/UkioSubjNustatytPazeidimas"
tags: [gov, lmi, ukiosubjnustatytpazeidimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2909/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# UkioSubjNustatytPazeidimas — Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų pažeidimai

Duomenų rinkinyje pateikiama informacija apie ūkio subjektus, juridinius ir fizinius (įskaitant ūkininkus) asmenis, kurių vykdomoje veikloje naudojamų matavimo priemonių arba fasuotų prekių patikrinimo metu Lietuvos metrologijos inspekcija nustatė pažeidimus. Fizinių asmenų duomenys yra užšifruoti. Jeigu įmonės kodas yra negaliojantis, įmonės kodo ir pavadinimo stulpeliai yra šifruojami. Taip pat, jeigu pažeidimą įvykdžiusios įmonės kodas nurodytas klaidingai, įmonės pavadinimo ir kodo stulpeliai gali būti užšifruoti. Ekonominės veiklos rūšių klasifikatoriaus (EVRK) kodai pateikti pagal EVRK 2 redakciją. Viena duomenų rinkinio eilutė atitinka vieną pažeidimą. Geografinė aprėptis – visa Lietuva. Duomenų aprėptis – nuo 2020 metų sausio 1 d. Duomenų teikėjas – Lietuvos metrologijos inspekcija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus/UkioSubjNustatytPazeidimas`[^manifest]
- **Dataset:** [Ūkio subjektai, kurių vykdomoje veikloje nustatyti Lietuvos metrologijos inspekcijos reikalavimų...](../us_kur_lmi_nustate_pazeidimus.md) (`datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus`)[^manifest]
- **Manifest CSV:** [datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus/UkioSubjNustatytPazeidimas` (`deployed`)[^manifest]
- **Provider:** `lmi` — Lietuvos metrologijos inspekcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `patikrinimo_akto_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kas_buvo_tikrinama` | `"Matavimo priemonės"` | — | — | Buvo tikrintos matavimo priemonės | — |
| `kas_buvo_tikrinama` | `"Fasuotos prekės"` | — | — | Buvo tikrintos fasuotos prekės | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lmi/us_kur_lmi_nustate_pazeidimus (https://data.gov.lt/datasets/2909/)
