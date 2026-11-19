---
type: Table
title: "Bendrieji — Užkrečiamųjų ligų atvejai bendrieji"
description: "Spinta table datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Bendrieji (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Bendrieji"
tags: [gov, nvsc, bendrieji, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1852/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nvsc/uzkreciamos_ligos/atvejai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Bendrieji — Užkrečiamųjų ligų atvejai bendrieji

- **Model:** `datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Bendrieji`[^manifest]
- **Dataset:** [Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenys](../atvejai.md) (`datasets/gov/nvsc/uzkreciamos_ligos/atvejai`)[^manifest]
- **Manifest CSV:** [datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai/Bendrieji` (`deployed`)[^manifest]
- **Provider:** `nvsc` — Nacionalinis visuomenės sveikatos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `centras` | `string` | — | `2` | `open` | — | NVSC departamenas | — |
| `registravimo_vieta` | `string` | — | `2` | `open` | — | NVSC skyrius | — |
| `miestas` | `string` | — | `2` | `open` | — | Savivaldybe | Savivaldybes, kurioje yra registruotas pacientas, pavadinimas |
| `tlk` | `ref` | [Tlk10am](../../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[code]`: `tlk._id`) | `4` | `open` | — | Galutinės diagnozės kodas | Pagal TLK-10-AM |
| `galutine_diagnoze` | `string` | — | `4` | `open` | — | Galutinė diagnozė | — |
| `ligonis_hospitalizuotas` | `boolean` | — | `4` | `open` | — | Hospitalizacija | Požymis, ar pacientas buvo hospitalizuotas |
| `socialiai_apdraustas` | `boolean` | — | `4` | `open` | — | Valstybinis socialinis draudimas | Požymis, ar pacientas turi valstybinį socialinį draudimą |
| `infekcijos_tipas` | `string` | — | `4` | `open` | — | Infekcijos tipas | — |
| `is_salies` | `string` | — | `3` | `open` | — | "Užsienio valstybė, kurioje paskutinį kartą buvo pacientas" | — |
| `ligos_klinikine_eiga` | `string` | — | `4` | `open` | — | Ligos klinikinė eiga | — |
| `atvyk` | `integer` | `d` | `4` | `open` | — | Dienų skaičius nuo atvykimo iš užsienio valstybės | — |
| `kreip_diag` | `integer` | `d` | `4` | `open` | — | Dienų skaičius praėjęs nuo kreipimosi iki diagnozės | — |
| `susirgimo_pranesimo_arba_mirties_data` | `date` | `D` | `4` | `open` | — | Pranešimo data | — |
| `sukelejo_rusis` | `string` | — | `2` | `open` | — | Sukelėjo rūšis | — |
| `susirgimo_atveju_skaicius` | `integer` | — | `4` | `open` | — | Susirgimo atvejų skaičius | — |
| `mirties_atveju_skaicius` | `integer` | `U` | `4` | `open` | — | Mirties atvejų skaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `infekcijos_tipas` | `'ūmi liga'` | — | — | ūmi liga | — |
| `infekcijos_tipas` | `'lėtinė infekcija'` | — | — | lėtinė infekcija | — |
| `infekcijos_tipas` | `'besimptomis viruso nešiojimas'` | — | — | besimptomis viruso nešiojimas | — |
| `infekcijos_tipas` | `'besimptomis ligos nešiojimas'` | — | — | besimptomis ligos nešiojimas | — |
| `infekcijos_tipas` | `'kita'` | — | — | kita | — |
| `ligos_klinikine_eiga` | `'vidutinė'` | — | — | vidutinė | — |
| `ligos_klinikine_eiga` | `'lengva'` | — | — | lengva | — |
| `ligos_klinikine_eiga` | `'sunki'` | — | — | sunki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nvsc/uzkreciamos_ligos/atvejai (https://data.gov.lt/datasets/1852/)
