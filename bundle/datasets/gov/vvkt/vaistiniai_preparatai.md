---
type: Dataset
title: "Valstybinės vaistų kontrolės registruotų vaistinių preparatų duomenų rinkinys"
description: "Rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos kaupiami vaistinių preparatų duomenys: pavadinimas, preparate esanti veiklioji medžiaga, stiprumas, vaistinio preparato farmacinė forma ir vartojimo būdai, vaistinio preparato..."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai"
tags: [gov, vvkt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistiniai_preparatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Valstybinės vaistų kontrolės registruotų vaistinių preparatų duomenų rinkinys

Rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos kaupiami vaistinių preparatų duomenys: pavadinimas, preparate esanti veiklioji medžiaga, stiprumas, vaistinio preparato farmacinė forma ir vartojimo būdai, vaistinio preparato grupė ir pogrupis, recepto poreikis, stebėjimo ir kontrolės būsenos, pirmos registracijos ir paskutinio perregistravimo data, dabartinė preparato stadija, preparatą registruojančios įmonės pavadinimas ir šalis. Rinkinyje taip pat nurodoma informacija apie vaistinių preparatų pakuotes – pakuotės tiekimo būsena, tipas ir aprašymas. Duomenų rinkinį sudaro dvi lentelės: „Vaistinis preparatas“ (informacija apie vaistinį preparatą ir jo pakuotes) ir „Vaistinio preparato stadijos“ (informacija apie vaistinio preparato stadijų pokyčius laike). Pirmojoje lentelėje viena eilutė atitinka vieną vaistinį preparatą ir jo pakuotę. Antrosios lentelės vienoje eilutėje pateikiama vieno vaistinio preparato informacija apie jo stadijos pasikeitimą. Abi lenteles galima sujungti per vaistinio preparato identifikacinio numerio (vid) stulpelį.

- **Namespace:** `datasets/gov/vvkt/vaistiniai_preparatai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/vaistiniai_preparatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai`
- **Parent Namespace (`ns`):** Valstybinė vaistų kontrolės tarnyba (`datasets/gov/vvkt`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PreparatasPakuote](vaistiniai_preparatai/PreparatasPakuote.md) | Valstybinės vaistų kontrolės tarnybos duomenys apie vaistinius preparatus ir jų pakuotes | `4` | `vda_id` | — | 31 | "Duomenys apie VVKT (Valstybinės vaistų kontrolės tarnybos) registruotus vaistinius preparatus ir jų pakuotes. |
| [PreparatasStadija](vaistiniai_preparatai/PreparatasStadija.md) | Valstybinės vaistų kontrolės tarnybos duomenys apie vaistinių preparatų stadijos pokyčius laike | `4` | `vda_id` | — | 7 | Duomenys apie VVKT (Valstybinės vaistų kontrolės tarnybos) registruotus vaistinius preparatus ir stadijos pokyčius. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistiniai_preparatai.csv
