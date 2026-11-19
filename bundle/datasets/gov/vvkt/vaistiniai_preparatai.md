---
type: Dataset
title: "Valstybinės vaistų kontrolės registruotų vaistinių preparatų duomenų rinkinys"
description: "\"Rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos kaupiami vaistinių preparatų duomenys: pavadinimas, preparate esanti veiklioji medžiaga, stiprumas, vaistinio preparato farmacinė forma ir vartojimo būdai, vaistinio preparato grupė ir pogrupis, recepto poreikis..."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai"
tags: [gov, vvkt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistiniai_preparatai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2853/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistiniai_preparatai"
    author: "team:vda"
    last_modified: "2026-10-14T00:00:00Z"
---

# Valstybinės vaistų kontrolės registruotų vaistinių preparatų duomenų rinkinys

"Rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos kaupiami vaistinių preparatų duomenys: pavadinimas, preparate esanti veiklioji medžiaga, stiprumas, vaistinio preparato farmacinė forma ir vartojimo būdai, vaistinio preparato grupė ir pogrupis, recepto poreikis, stebėjimo ir kontrolės būsenos, pirmos registracijos ir paskutinio perregistravimo data, dabartinė preparato stadija, preparatą registruojančios įmonės pavadinimas ir šalis. Rinkinyje taip pat nurodoma informacija apie vaistinių preparatų pakuotes – pakuotės tiekimo būsena, tipas ir aprašymas. Duomenų rinkinį sudaro dvi lentelės: „Vaistinis preparatas“ (informacija apie vaistinį preparatą ir jo pakuotes) ir „Vaistinio preparato stadijos“ (informacija apie vaistinio preparato stadijų pokyčius laike). Pirmojoje lentelėje viena eilutė atitinka vieną vaistinį preparatą ir jo pakuotę. Antrosios lentelės vienoje eilutėje pateikiama vieno vaistinio preparato informacija apie jo stadijos pasikeitimą. Abi lenteles galima sujungti per vaistinio preparato identifikacinio numerio (vid) stulpelį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/vvkt/vaistiniai_preparatai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/vaistiniai_preparatai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai` (`deployed`)[^manifest]
- **Provider:** `vvkt` — Valstybinė vaistų kontrolės tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2853/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vvkt/vaistiniai_preparatai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Valstybinės vaistų kontrolės registruotų vaistinių preparatų duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** Data Set of Registered Medicinal Products of the State Medicines Control[^dcat]
- **Issued (`dct:issued`):** `2024-11-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-14`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-12` .. `2026-10-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos kaupiami vaistinių preparatų duomenys: pavadinimas, preparate esanti veiklioji medžiaga, stiprumas, vaistinio preparato farmacinė forma ir vartojimo būdai, vaistinio preparato grupė ir pogrupis, recepto poreikis, stebėjimo ir kontrolės būsenos, pirmos registracijos ir paskutinio perregistravimo data, dabartinė preparato stadija, preparatą registruojančios įmonės pavadinimas ir šalis. Rinkinyje taip pat nurodoma informacija apie vaistinių preparatų pakuotes – pakuotės tiekimo būsena, tipas ir aprašymas. Duomenų rinkinį sudaro dvi lentelės: „Vaistinis preparatas“ (informacija apie vaistinį preparatą ir jo pakuotes) ir „Vaistinio preparato stadijos“ (informacija apie vaistinio preparato stadijų pokyčius laike). Pirmojoje lentelėje viena eilutė atitinka vieną vaistinį preparatą ir jo pakuotę. Antrosios lentelės vienoje eilutėje pateikiama vieno vaistinio preparato informacija apie jo stadijos pasikeitimą. Abi lenteles galima sujungti per vaistinio preparato identifikacinio numerio (vid) stulpelį. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package shall contain the data of medicinal products accumulated by the State Medicines Control Agency: name, active substance in the preparation, strength, pharmaceutical form and routes of administration of the medicinal product, group and subset of the medicinal product, need for prescription, state of monitoring and control, date of first registration and last re-registration, current stage of the medicinal product, name and country of the undertaking registering the product. The package shall also contain information on the packaging of medicinal products, such as the state, type and description of the packaging. The dataset consists of two tables: “medicinal product” (information on the medicinal product and its packaging) and “Phase of medicinal product” (information on changes in the stages of the medicinal product in time). In the first table, one line corresponds to one medicinal product and its packaging. One row of the second table contains information about a change in the stage of one medicinal product. Both tables can be combined through the product identification number (vid) column. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PreparatasPakuote](vaistiniai_preparatai/PreparatasPakuote.md) | Valstybinės vaistų kontrolės tarnybos duomenys apie vaistinius preparatus ir jų pakuotes | `4` | `vda_id` | — | `31` | "Duomenys apie VVKT (Valstybinės vaistų kontrolės tarnybos) registruotus vaistinius preparatus ir jų pakuotes. |
| [PreparatasStadija](vaistiniai_preparatai/PreparatasStadija.md) | Valstybinės vaistų kontrolės tarnybos duomenys apie vaistinių preparatų stadijos pokyčius laike | `4` | `vda_id` | — | `7` | "Duomenys apie VVKT (Valstybinės vaistų kontrolės tarnybos) registruotus vaistinius preparatus ir stadijos pokyčius. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistiniai_preparatai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistiniai_preparatai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistiniai_preparatai (https://data.gov.lt/datasets/2853/)
