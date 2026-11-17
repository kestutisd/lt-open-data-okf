---
type: Table
title: "LatvijosRinka — Vilniaus žinomumo apklausų rezultatai Latvijos rinkoje"
description: "Spinta table datasets/gov/go_vilnius/vilniaus_zinomumas/LatvijosRinka (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas/LatvijosRinka"
tags: [gov, go_vilnius, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/go_vilnius/vilniaus_zinomumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L52"
    last_modified: "2026-11-11T14:39:20Z"
---

# LatvijosRinka — Vilniaus žinomumo apklausų rezultatai Latvijos rinkoje

- **Model:** `datasets/gov/go_vilnius/vilniaus_zinomumas/LatvijosRinka`[^manifest]
- **Dataset:** [Vilniaus žinomumo tyrimų apklausų duomenų rinkinys](../vilniaus_zinomumas.md) (`datasets/gov/go_vilnius/vilniaus_zinomumas`)
- **Manifest CSV:** [datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L52](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L52)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas/LatvijosRinka`
- **Primary Key (`ref`):** `dalyv_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dalyv_id` | `string` | — | `4` | `open` | — | Dalyvio ID | Atsakymo identifikatorius. Apklausos dalyvio - respondento - ID numeris |
| `data` | `date` | `1D` | `4` | `open` | — | Apklausos data | Apklausos pildymo data |
| `rinka` | `string` | — | `4` | `open` | — | Apklausos rinka | Šalis, kurioje atliekama apklausa" |
| `lytis` | `string` | — | `4` | `open` | — | Respondento lytis | — |
| `amzius` | `integer` | — | `4` | `open` | — | Respondento amžius | — |
| `kilmes_salis` | `string` | — | `4` | `open` | — | Respondento kilmė | Respondento kilmės šalis - vieta, kurioje gimė |
| `gyvenamoji_vt` | `string` | — | `4` | `open` | — | Respondento gyvenamoji vieta | Dabartinė respondento gyvenamoji vieta: miestas |
| `gyv_vt_pop` | `string` | — | `4` | `open` | — | Respondento gyvenamosios vietos populiacija | — |
| `issilavinimas` | `string` | — | `4` | `open` | — | Respondento išsilavinimas | — |
| `ekonom_padetis` | `string` | — | `4` | `open` | — | Ekonominė respondento padėtis | — |
| `kelioniu_dazn` | `string` | — | `4` | `open` | — | Respondento kelionių dažnis | Nurodo kaip dažnai respondentas keliauja į užsienį |
| `zino_bratislava` | `boolean` | — | `4` | `open` | — | Žinios apie Bratislavą | Ar respondentas girdėjęs apie Bratislavą? |
| `zino_krokuva` | `boolean` | — | `4` | `open` | — | Žinios apie Krokuvą | Ar respondentas girdėjęs apie Krokuvą? |
| `zino_helsinki` | `boolean` | — | `4` | `open` | — | Žinios apie Helsinkį | Ar respondentas girdėjęs apie Helsinkį? |
| `zino_liublijana` | `boolean` | — | `4` | `open` | — | Žinios apie Liublijaną | Ar respondentas girdėjęs apie Liublijaną? |
| `zino_vilniu` | `boolean` | — | `4` | `open` | — | Žinios apie Vilnių | Ar respondentas girdėjęs apie Vilnių? |
| `zino_varsuva` | `boolean` | — | `4` | `open` | — | Žinios apie Varšuvą | Ar respondentas girdėjęs apie Varšuvą? |
| `zino_talina` | `boolean` | — | `4` | `open` | — | Žinios apie Taliną | Ar respondentas girdėjęs apie Taliną? |
| `stat_svoris` | `number` | — | `4` | `open` | — | Statistinis svoris | Respondento statistinis svoris apklausoje (techninis įvertis) |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rinka` | `"Latvija"` | — | — | Latvija | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `kilmes_salis` | `"Vietinis"` | — | — | Vietinis | — |
| `kilmes_salis` | `"Kita"` | — | — | Kita | — |
| `gyv_vt_pop` | `"Mažiau nei 5 tūkst. gyventojų"` | — | — | Mažiau nei 5 tūkst. gyventojų | — |
| `gyv_vt_pop` | `"5 tūkst. - 99 tūkst. gyventojų"` | — | — | 5 tūkst. - 99 tūkst. gyventojų | — |
| `gyv_vt_pop` | `"100 tūkst. - 299 tūkst. gyventojų"` | — | — | 100 tūkst. - 299 tūkst. gyventojų | — |
| `gyv_vt_pop` | `"500 tūkst. - 999 tūkst. gyventojų"` | — | — | 500 tūkst. - 999 tūkst. gyventojų | — |
| `issilavinimas` | `"Žemesnis nei aukštasis"` | — | — | Žemesnis nei aukštasis | — |
| `issilavinimas` | `"Aukštasis"` | — | — | Aukštasis | — |
| `ekonom_padetis` | `"Turintys santaupų"` | — | — | Turintys santaupų | — |
| `ekonom_padetis` | `"Pasiturintys"` | — | — | Pasiturintys | — |
| `ekonom_padetis` | `"Skaičiuoja"` | — | — | Skaičiuoja | — |
| `ekonom_padetis` | `"Skolinasi"` | — | — | Skolinasi | — |
| `ekonom_padetis` | `"Kita"` | — | — | Kita | — |
| `kelioniu_dazn` | `"Rečiau nei kartą per metus"` | — | — | Rečiau nei kartą per metus | — |
| `kelioniu_dazn` | `"Kartą per metus"` | — | — | Kartą per metus | — |
| `kelioniu_dazn` | `"2-3 kartus per metus"` | — | — | 2-3 kartus per metus | — |
| `kelioniu_dazn` | `"4-5 kartus per metus"` | — | — | 4-5 kartus per metus | — |
| `kelioniu_dazn` | `"Daugiau nei 5 kartus per metus"` | — | — | Daugiau nei 5 kartus per metus | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/go_vilnius/vilniaus_zinomumas.csv
