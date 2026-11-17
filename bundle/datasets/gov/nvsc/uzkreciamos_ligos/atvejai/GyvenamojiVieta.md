---
type: Table
title: "GyvenamojiVieta — Užkrečiamųjų ligų atvejai pagal gyvenamąją vietą"
description: "Spinta table datasets/gov/nvsc/uzkreciamos_ligos/atvejai/GyvenamojiVieta (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/GyvenamojiVieta"
tags: [gov, nvsc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyvenamojiVieta — Užkrečiamųjų ligų atvejai pagal gyvenamąją vietą

- **Model:** `datasets/gov/nvsc/uzkreciamos_ligos/atvejai/GyvenamojiVieta`[^manifest]
- **Dataset:** [Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenys](../atvejai.md) (`datasets/gov/nvsc/uzkreciamos_ligos/atvejai`)
- **Manifest CSV:** [datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/GyvenamojiVieta`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `gyvenamoji_vieta` | `string` | — | `4` | `open` | — | Gyvenamosios vietos tipas | Požymis nurodantis, ar pacientas gyvena kaime ar mieste |
| `namo_tipas` | `string` | — | `4` | `open` | — | Namo tipas | Požymis nurodantis, ar pacientas gyvena individualiame name, daugiabutyje, ar bendrabutyje |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Amžiaus grupė | — |
| `tlk` | `ref` | [/datasets/gov/vlk/tlk10am/Tlk10am[code]](../../../vlk/tlk10am/Tlk10am.md) | `4` | `open` | — | Galutinės diagnozės kodas | — |
| `galutine_diagnoze` | `string` | — | `4` | `open` | — | Galutinė diagnozė | — |
| `salytis_su_gyvunu` | `boolean` | — | `4` | `open` | — | Sąlytis su gyvūnu | Požymis nurodantis, ar buvo paciento sąlytis su gyvūnu. Svarbu tiriant, ar užsikrėsta nuo gyvūno. |
| `susirgimo_menuo` | `date` | `M` | `4` | `open` | — | Susirgimuo mėnuo | — |
| `socialiai_apdraustas` | `boolean` | — | `4` | `open` | — | Valstybinis socialinis draudimas | Požymis, ar pacientas turi valstybinį socialinį draudimą |
| `ligonis_hospitalizuotas` | `boolean` | — | `4` | `open` | — | Hospitalizacija | Požymis, ar pacientas buvo hospitalizuotas |
| `infekcijos_tipas` | `string` | — | `4` | `open` | — | Infekcijos tipas | — |
| `ligos_klinikine_eiga` | `string` | — | `4` | `open` | — | Ligos klinikinė eiga | — |
| `mirtis` | `boolean` | — | `4` | `open` | — | Mirtis | Požymis, ar pacientas mirė |
| `lygos_atvejis_nustatytas` | `string` | — | `2` | `open` | — | Nustatymas | Požymis nurodantis, kada ligos atvejis nustatytas |
| `atvejai` | `integer` | `U` | `4` | `open` | — | Atvejų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gyvenamoji_vieta` | `'kaimas'` | — | — | kaimas | — |
| `gyvenamoji_vieta` | `'miestas'` | — | — | miestas | — |
| `namo_tipas` | `'daugiabutis'` | — | — | daugiabutis | — |
| `namo_tipas` | `'bendrabutis'` | — | — | bendrabutis | — |
| `namo_tipas` | `'individualus'` | — | — | individualus | — |
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
