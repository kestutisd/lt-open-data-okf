---
type: Table
title: "GyvenamuVietuSkirtumas2021 — Duomenų rinkinys apima 2021 m. pradžioje Lietuvoje gyvenusius nuolatinius gyventojus, kurių deklaruota gyvenamoji vieta (Gyventojų registras, 2021-01-01) nesutapo su 2021 m. gyventojų..."
description: "Spinta table datasets/gov/lsd/rc/sur/GyvenamuVietuSkirtumas2021 (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/rc/sur/GyvenamuVietuSkirtumas2021"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/rc/rc_surasymo_2021.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/rc/rc_surasymo_2021.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyvenamuVietuSkirtumas2021 — Duomenų rinkinys apima 2021 m. pradžioje Lietuvoje gyvenusius nuolatinius gyventojus, kurių deklaruota gyvenamoji vieta (Gyventojų registras, 2021-01-01) nesutapo su 2021 m. gyventojų...

- **Model:** `datasets/gov/lsd/rc/sur/GyvenamuVietuSkirtumas2021`[^manifest]
- **Dataset:** [2021 m. nuolatinių gyventojų, kurių deklaruota ir surašymo metu nustatyta gyvenamoji vieta skyrėsi, duomenų rinkinys](../sur.md) (`datasets/gov/lsd/rc/sur`)
- **Manifest CSV:** [datasets/gov/lsd/rc/rc_surasymo_2021.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/rc/rc_surasymo_2021.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/rc/sur/GyvenamuVietuSkirtumas2021`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus asmens identifikatorius | — |
| `asm_lytis` | `string` | — | `4` | `open` | — | Asmens lytis | — |
| `amzius_noise` | `integer` | — | `4` | `open` | — | Asmens amžius (daliai gyventojų triukšmintas ±1 metai dėl konfidencialumo) | — |
| `x_koord_hgridsur` | `integer` | — | `4` | `open` | — | Gardelės, į kurią patenka surašymo metu nustatyta gyvenamoji vieta, centro LKS X koordinatė | — |
| `y_koord_hgridsur` | `integer` | — | `4` | `open` | — | Gardelės, į kurią patenka surašymo metu nustatyta gyvenamoji vieta, centro LKS Y koordinatė | — |
| `n_koord_hgridsur` | `number` | — | `4` | `open` | — | Gardelės, į kurią patenka surašymo metu nustatyta gyvenamoji vieta, centro WGS84 platuma | — |
| `e_koord_hgridsur` | `number` | — | `4` | `open` | — | Gardelės, į kurią patenka surašymo metu nustatyta gyvenamoji vieta, centro WGS84 ilguma | — |
| `grid_id_sur` | `string` | — | `4` | `open` | — | Gardelės identifikatorius, susijęs su surašymo metu nustatyta gyvenamąja vieta | — |
| `x_koord_hgridgr` | `integer` | — | `4` | `open` | — | Gardelės, į kurią patenka deklaruota gyvenamoji vieta (Gyventojų registras, 2021-01-01), centro LKS X koordinatė | — |
| `y_koord_hgridgr` | `integer` | — | `4` | `open` | — | Gardelės, į kurią patenka deklaruota gyvenamoji vieta, centro LKS Y koordinatė | — |
| `n_koord_hgridgr` | `number` | — | `4` | `open` | — | Gardelės, į kurią patenka deklaruota gyvenamoji vieta, centro WGS84 platuma | — |
| `e_koord_hgridgr` | `number` | — | `4` | `open` | — | Gardelės, į kurią patenka deklaruota gyvenamoji vieta, centro WGS84 ilguma | — |
| `grid_id_gr` | `string` | — | `4` | `open` | — | Gardelės identifikatorius, susijęs su deklaruota gyvenamąja vieta | — |
| `sav_kodas_sur` | `string` | — | `4` | `open` | — | Savivaldybės, į kurią patenka gardelės centras pagal surašymo duomenis, kodas | — |
| `sav_pav_sur` | `string` | — | `4` | `open` | — | Savivaldybės, į kurią patenka gardelės centras pagal surašymo duomenis, pavadinimas | — |
| `sav_kodas_gr` | `string` | — | `4` | `open` | — | Savivaldybės, į kurią patenka gardelės centras pagal deklaruotą adresą, kodas | — |
| `sav_pav_gr` | `string` | — | `4` | `open` | — | Savivaldybės, į kurią patenka gardelės centras pagal deklaruotą adresą, pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asm_lytis` | `"M"` | — | `open` | Moteris | — |
| `asm_lytis` | `"V"` | — | `open` | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/rc/rc_surasymo_2021.csv
