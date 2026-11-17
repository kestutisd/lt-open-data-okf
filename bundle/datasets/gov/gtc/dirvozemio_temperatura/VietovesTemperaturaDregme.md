---
type: Table
title: "VietovesTemperaturaDregme — Vietovės dirvožemio temperatūra ir drėgmė"
description: "Informacija apie Gamtos Tyrimų Centro mokslinių darbuotojų tiriamą dirvožemio temperatūrą ir drėgmę įvairiose vietovėse Lietuvos teritorijoje"
resource: "https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura/VietovesTemperaturaDregme"
tags: [gov, gtc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# VietovesTemperaturaDregme — Vietovės dirvožemio temperatūra ir drėgmė

Informacija apie Gamtos Tyrimų Centro mokslinių darbuotojų tiriamą dirvožemio temperatūrą ir drėgmę įvairiose vietovėse Lietuvos teritorijoje

- **Model:** `datasets/gov/gtc/dirvozemio_temperatura/VietovesTemperaturaDregme`[^manifest]
- **Dataset:** [Dirvožemio temperatūra ir drėgmė bei dirvožemyje augantys augalai](../dirvozemio_temperatura.md) (`datasets/gov/gtc/dirvozemio_temperatura`)
- **Manifest CSV:** [datasets/gov/gtc/dirvozemio_temperatura.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura/VietovesTemperaturaDregme`
- **Primary Key (`ref`):** `atvejo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atvejo_id` | `string` | — | `4` | `open` | — | Stebėjimo atvejo identifikatorius | — |
| `vietoves_registratoriaus_id` | `string` | — | `4` | `open` | — | Vietovės registratoriaus identifikatorius | — |
| `laikas` | `datetime` | `T` | `4` | `open` | — | Stebėjimo laikas | — |
| `temperatura_8cm_gylyje_dirvozemyje` | `number` | `°C` | `4` | `open` | — | Temperatūra 8 cm gylyje dirvožemyje | — |
| `temperatura_dirvozemio_pavirsiuje` | `number` | `°C` | `4` | `open` | — | Temperatūra dirvožemio paviršiuje | — |
| `temperatura_15cm_virs_dirvozemio` | `number` | `°C` | `4` | `open` | — | Temperatūra 15 cm virš dirvožemio | — |
| `dirvozemio_dregme` | `integer` | — | `3` | `open` | — | Neapdorotas dirvožemio drėgmės matas | — |
| `platuma` | `number` | `°` | `4` | `open` | — | Tiksli registratoriaus buvimo vietos platuma dešimtainiais laipsniais | — |
| `ilguma` | `number` | `°` | `4` | `open` | — | Tiksli registratoriaus buvimo vietos ilguma dešimtainiais laipsniais | — |
| `apytiksle_vietoves_klasifikacija` | `string` | — | `4` | `open` | — | Apytikslė vietovės klasifikacija pagal https://www.iucnredlist.org/resources/habitat-classification-scheme. Klasifikacija yra svari jutiklių duomenų naudingumui. | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `apytiksle_vietoves_klasifikacija` | `"1"` | — | — | Miškas | — |
| `apytiksle_vietoves_klasifikacija` | `"3"` | — | — | Krūmynai | — |
| `apytiksle_vietoves_klasifikacija` | `"4"` | — | — | Pievos | — |
| `apytiksle_vietoves_klasifikacija` | `"5"` | — | — | Pelkė | — |
| `apytiksle_vietoves_klasifikacija` | `"13"` | — | — | Jūrinė pakrantė | — |
| `apytiksle_vietoves_klasifikacija` | `"14"` | — | — | Dirbtinis dirvožemis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv
