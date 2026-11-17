---
type: Table
title: "SocialineGrupe — Užkrečiamųjų ligų atvejai pagal socialines grupes"
description: "Spinta table datasets/gov/nvsc/uzkreciamos_ligos/atvejai/SocialineGrupe (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/SocialineGrupe"
tags: [gov, nvsc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L75"
    last_modified: "2026-11-11T14:39:20Z"
---

# SocialineGrupe — Užkrečiamųjų ligų atvejai pagal socialines grupes

- **Model:** `datasets/gov/nvsc/uzkreciamos_ligos/atvejai/SocialineGrupe`[^manifest]
- **Dataset:** [Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenys](../atvejai.md) (`datasets/gov/nvsc/uzkreciamos_ligos/atvejai`)
- **Manifest CSV:** [datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L75](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L75)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/SocialineGrupe`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `socialine_grupe` | `string` | — | `4` | `open` | — | Socialinė grupė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Amžiaus grupė | — |
| `tlk` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Galutinės diagnozės kodas | — |
| `galutine_diagnoze` | `string` | — | `4` | `open` | — | Galutinė diagnozė | — |
| `socialiai_apdraustas` | `boolean` | — | `4` | `open` | — | Valstybinis socialinis draudimas | Požymis, ar pacientas turi valstybinį socialinį draudimą |
| `ligonis_hospitalizuotas` | `boolean` | — | `4` | `open` | — | Hospitalizacija | Požymis, ar pacientas buvo hospitalizuotas |
| `susirgimo_menuo` | `date` | `M` | `4` | `open` | — | Susirgimuo mėnuo | — |
| `mirtis` | `boolean` | — | `4` | `open` | — | Mirtis | Požymis, ar pacientas mirė |
| `infekcijos_tipas` | `string` | — | `4` | `open` | — | Infekcijos tipas | — |
| `ligos_klinikine_eiga` | `string` | — | `4` | `open` | — | Ligos klinikinė eiga | — |
| `lygos_atvejis_nustatytas` | `string` | — | `2` | `open` | — | Nustatymas | Požymis nurodantis, kada ligos atvejis nustatytas |
| `salytis_su_gyvunu` | `boolean` | — | `4` | `open` | — | Sąlytis su gyvūnu | Požymis nurodantis, ar buvo paciento sąlytis su gyvūnu. Svarbu tiriant, ar užsikrėsta nuo gyvūno. |
| `diagnozuota_per` | `integer` | `d` | `4` | `open` | — | Dienų skaičius praėjęs nuo kreipimosi iki diagnozės | — |
| `dirbta_pries` | `boolean` | — | `4` | `open` | — | Darbas | Požymis nurodytas, ar po susirgimo pacientas atvyko į darbą |
| `atvejai` | `integer` | `U` | `4` | `open` | — | Atvejų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `socialine_grupe` | `'ikimokyklinukas'` | — | — | ikimokyklinukas | — |
| `socialine_grupe` | `'moksleivis'` | — | — | moksleivis | — |
| `socialine_grupe` | `'neorganizuotas'` | — | — | neorganizuotas | — |
| `socialine_grupe` | `'kita'` | — | — | kita | — |
| `socialine_grupe` | `'darbininkas'` | — | — | darbininkas | — |
| `socialine_grupe` | `'pensininkas'` | — | — | pensininkas | — |
| `socialine_grupe` | `'tarnautojas'` | — | — | tarnautojas | — |
| `socialine_grupe` | `'bedarbis'` | — | — | bedarbis | — |
| `socialine_grupe` | `'studentas'` | — | — | studentas | — |
| `socialine_grupe` | `'neįgalusis'` | — | — | neįgalusis | — |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |
| `amziaus_grupe` | `"0-9"` | — | — | — | — |
| `amziaus_grupe` | `"10-19"` | — | — | — | — |
| `amziaus_grupe` | `"20-29"` | — | — | — | — |
| `amziaus_grupe` | `"30-39"` | — | — | — | — |
| `amziaus_grupe` | `"40-49"` | — | — | — | — |
| `amziaus_grupe` | `"50-59"` | — | — | — | — |
| `amziaus_grupe` | `"60-69"` | — | — | — | — |
| `amziaus_grupe` | `"70-79"` | — | — | — | — |
| `amziaus_grupe` | `"80-89"` | — | — | — | — |
| `amziaus_grupe` | `"90+"` | — | — | — | — |
| `infekcijos_tipas` | `'ūmi liga'` | — | — | ūmi liga | — |
| `infekcijos_tipas` | `'lėtinė infekcija'` | — | — | lėtinė infekcija | — |
| `infekcijos_tipas` | `'besimptomis viruso nešiojimas'` | — | — | besimptomis viruso nešiojimas | — |
| `infekcijos_tipas` | `'besimptomis ligos nešiojimas'` | — | — | besimptomis ligos nešiojimas | — |
| `infekcijos_tipas` | `'kita'` | — | — | kita | — |
| `ligos_klinikine_eiga` | `'vidutinė'` | — | — | vidutinė | — |
| `ligos_klinikine_eiga` | `'lengva'` | — | — | lengva | — |
| `ligos_klinikine_eiga` | `'sunki'` | — | — | sunki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv
