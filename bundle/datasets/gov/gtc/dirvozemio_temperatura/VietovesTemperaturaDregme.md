---
type: Table
title: "VietovesTemperaturaDregme — Vietovės dirvožemio temperatūra ir drėgmė"
description: "Informacija apie Gamtos Tyrimų Centro mokslinių darbuotojų tiriamą dirvožemio temperatūrą ir drėgmę įvairiose vietovėse Lietuvos teritorijoje"
resource: "https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura/VietovesTemperaturaDregme"
tags: [gov, gtc, vietovestemperaturadregme, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2638/"
    title: "data.gov.lt DCAT-AP — datasets/gov/gtc/dirvozemio_temperatura"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VietovesTemperaturaDregme — Vietovės dirvožemio temperatūra ir drėgmė

Informacija apie Gamtos Tyrimų Centro mokslinių darbuotojų tiriamą dirvožemio temperatūrą ir drėgmę įvairiose vietovėse Lietuvos teritorijoje[^manifest]

- **Model:** `datasets/gov/gtc/dirvozemio_temperatura/VietovesTemperaturaDregme`[^manifest]
- **Dataset:** [Dirvožemio temperatūra ir drėgmė bei dirvožemyje augantys augalai](../dirvozemio_temperatura.md) (`datasets/gov/gtc/dirvozemio_temperatura`)[^manifest]
- **Manifest CSV:** [datasets/gov/gtc/dirvozemio_temperatura.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/gtc/dirvozemio_temperatura/VietovesTemperaturaDregme` (`deployed`)[^manifest]
- **Provider:** `gtc` — Gamtos tyrimų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `atvejo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `apytiksle_vietoves_klasifikacija` | `"1"` | — | — | Miškas | — |
| `apytiksle_vietoves_klasifikacija` | `"3"` | — | — | Krūmynai | — |
| `apytiksle_vietoves_klasifikacija` | `"4"` | — | — | Pievos | — |
| `apytiksle_vietoves_klasifikacija` | `"5"` | — | — | Pelkė | — |
| `apytiksle_vietoves_klasifikacija` | `"13"` | — | — | Jūrinė pakrantė | — |
| `apytiksle_vietoves_klasifikacija` | `"14"` | — | — | Dirbtinis dirvožemis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/gtc/dirvozemio_temperatura.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/gtc/dirvozemio_temperatura.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/gtc/dirvozemio_temperatura (https://data.gov.lt/datasets/2638/)
