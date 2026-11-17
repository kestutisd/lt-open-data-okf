---
type: Table
title: "LigoniniuDuomenys — COVID-19 ligoninių duomenys"
description: "Turimos bei užimtos stacionaro lovos, deguonies tiekimu aprūpintos lovos, intensyvios terapijos ir reanimacijos skyrių lovos, dirbtinės plaučių ventiliacijos įranga ir jos panaudojimas, ECMO sistemos ir jų užimtumas, pacientų srautas..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19/LigoniniuDuomenys"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L52"
    last_modified: "2026-11-11T14:39:20Z"
---

# LigoniniuDuomenys — COVID-19 ligoninių duomenys

Turimos bei užimtos stacionaro lovos, deguonies tiekimu aprūpintos lovos, intensyvios terapijos ir reanimacijos skyrių lovos, dirbtinės plaučių ventiliacijos įranga ir jos panaudojimas, ECMO sistemos ir jų užimtumas, pacientų srautas, darbingo ir nedarbingo personalo kiekiai, skiriamo Remdesivir kiekiai. Duomenys yra agreguoti pagal datą ir regionus (penkias teritorines ligonių kasas).

- **Model:** `datasets/gov/lsd/covid19/LigoniniuDuomenys`[^manifest]
- **Dataset:** [datasets/gov/lsd/covid19](../covid19.md) (`datasets/gov/lsd/covid19`)
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L52](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L52)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19/LigoniniuDuomenys`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `date` | `string` | — | `2` | `open` | — | Ataskaitinė para (ataskaitinio laikotarpio 16:00-16:00 pabaigos data) | — |
| `hospital_name` | `string` | — | `2` | `open` | — | Ligoninės pavadinimas | — |
| `healthcare_region` | `string` | — | `2` | `open` | — | Regionas (penkias teritorines ligonių kasas) | — |
| `hospital_beds_total_r7mean` | `number` | `U` | `4` | `open` | — | Bendras ligoninių stacionaro aktyvaus gydymo lovų skaičius (be RITS!) | — |
| `hospital_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtų ligoninių stacionaro aktyvaus gydymo lovų skaičius (be RITS!) | — |
| `oxygen_beds_total_r7mean` | `number` | `U` | `4` | `open` | — | Visos lovos su deguonies tiekimu (hospital_beds_total dalis) | — |
| `oxygen_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos lovos su deguonies tiekimu | — |
| `mv_beds_total_r7mean` | `number` | `U` | `4` | `open` | — | Visos lovos su dirbtinės plaučių ventiliacijos (DPV) galimybėmis (hospital_beds_total dalis) | — |
| `mv_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos lovos su DPV galimybėmis | — |
| `icu_beds_total_r7mean` | `number` | `U` | `4` | `open` | — | Reanimacijos ir intensyvios terapijos skyrių (RITS) lovos (nėra hospital_beds_total dalis!) | — |
| `icu_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos RITS lovos (nėra hospital_beds_occupied dalis!) | — |
| `icu_ecmo_systems_total_r7mean` | `number` | `U` | `4` | `open` | — | Bendras RITS lovų su ECMO sistemomis skaičius | — |
| `icu_ecmo_systems_in_use_r7mean` | `number` | `U` | `4` | `open` | — | Užimtų RITS lovų su ECMO sistemomis skaičius | — |
| `cv19_hospital_beds_assigned_r7mean` | `number` | `U` | `4` | `open` | — | COVID pacientams skirtų lovų skaičius | — |
| `cv19_hospital_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtų COVID pacientams skirtų lovų skaičius | — |
| `cv19_oxygen_beds_assigned_r7mean` | `number` | `U` | `4` | `open` | — | COVID pacientams skirtos lovos su deguonies tiekimu | — |
| `cv19_oxygen_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos COVID pacientams skirtos lovos su deguonies tiekimu | — |
| `cv19_mv_beds_assigned_r7mean` | `number` | `U` | `4` | `open` | — | COVID pacientams skirtos lovos su dirbtinės plaučių ventiliacijos (DPV) galimybėmis | — |
| `cv19_mv_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos COVID pacientams skirtos lovos su DPV galimybėmis | — |
| `cv19_icu_beds_assigned_r7mean` | `number` | `U` | `4` | `open` | — | COVID pacientams skirtos reanimacijos ir intensyvios terapijos skyrių (RITS) lovos | — |
| `cv19_icu_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos COVID pacientams skirtos RITS lovos | — |
| `cv19_icu_mv_beds_assigned_r7mean` | `number` | `U` | `4` | `open` | — | COVID pacientams skirtos RITS lovos su dirbtinės plaučių ventiliacijos (DPV) galimybėmis | — |
| `cv19_icu_mv_beds_occupied_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos COVID pacientams skirtos RITS lovos su DPV galimybėmis | — |
| `cv19_icu_highflow_systems_total_r7mean` | `number` | `U` | `4` | `open` | — | COVID pacientams skirtos RITS lovos su high-flow sistema | — |
| `cv19_icu_highflow_systems_in_use_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos COVID pacientams skirtos RITS lovos su high-flow sistema | — |
| `cv19_icu_ecmo_assigned_r7mean` | `number` | `U` | `4` | `open` | — | COVID pacientams skirtos RITS lovos su EKMO sistema | — |
| `cv19_icu_ecmo_in_use_r7mean` | `number` | `U` | `4` | `open` | — | Užimtos COVID pacientams skirtos RITS lovos su EKMO sistema | — |
| `cv19_admissions_r7mean` | `number` | `U` | `4` | `open` | — | nauji COVID pacientai (per parą) | — |
| `cv19_admissions_oxygen_r7mean` | `number` | `U` | `4` | `open` | — | Nauji COVID pacientai, kuriems tiekiamas deguonis | — |
| `cv19_admissions_mv_r7mean` | `number` | `U` | `4` | `open` | — | Nauji COVID pacientai su dirbtine plaučių ventiliacija | — |
| `cv19_discharges_r7mean` | `number` | `U` | `4` | `open` | — | COVID pacientų išrašymai / išvykimai | — |
| `remdesivir_vials_used_r7mean` | `number` | `U` | `4` | `open` | — | Sunaudota Remdesivir flakonų | — |
| `remdesivir_patients_total_r7mean` | `number` | `U` | `4` | `open` | — | Pacientų, gaunančių Remdesivir, skaičius | — |
| `remdesivir_patients_new_r7mean` | `number` | `U` | `4` | `open` | — | Naujų pacientų, gaunančių Remdesivir, skaičius | — |
| `koord` | `geometry(point,4326)` | `m` | `4` | `open` | — | Ligoninės koordinatės (WGS) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv
