---
type: Table
title: "DidzBritRinka — Vilniaus žinomumo apklausų rezultatai Didžiosios Britanijos rinkoje"
description: "\"Rinkinys iš \"GO Vilnius\" rengtos apklausos 2023 m. apie Vilniaus žinomumą."
resource: "https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas/DidzBritRinka"
tags: [gov, go_vilnius, didzbritrinka, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L132"
    title: "atviriduomenys/manifest — datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L132"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2792/"
    title: "data.gov.lt DCAT-AP — datasets/gov/go_vilnius/vilniaus_zinomumas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# DidzBritRinka — Vilniaus žinomumo apklausų rezultatai Didžiosios Britanijos rinkoje

**Dataset Context:** "Rinkinys iš "GO Vilnius" rengtos apklausos 2023 m. apie Vilniaus žinomumą. Apklausos atliktos skirtingose rinkose (Vokietijoje, Latvijoje, Lenkijoje, Didžiojoje Britanijoje). Vieną lentelės eilutę sudaro informacija apie respondentą ir jo atsakymai į pateiktus apklausos klausimus. Paskutinis stulpelis įvertine kiekvieno korespondento statistinį svorį apklausoje. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt"[^manifest]

- **Model:** `datasets/gov/go_vilnius/vilniaus_zinomumas/DidzBritRinka`[^manifest]
- **Dataset:** [Vilniaus žinomumo tyrimų apklausų duomenų rinkinys](../vilniaus_zinomumas.md) (`datasets/gov/go_vilnius/vilniaus_zinomumas`)[^manifest]
- **Manifest CSV:** [datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L132](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L132)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas/DidzBritRinka` (`deployed`)[^manifest]
- **Provider:** `go_vilnius` — VšĮ GO Vilnius *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `dalyv_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dalyv_id` | `string` | — | `4` | `open` | — | Dalyvio ID | Atsakymo identifikatorius. Apklausos dalyvio - respondento - ID numeris. |
| `data` | `date` | `1D` | `4` | `open` | — | Apklausos data | Apklausos pildymo data |
| `rinka` | `string` | — | `4` | `open` | — | Apklausos rinka | "Šalis, kurioje atliekama apklausa" |
| `lytis` | `string` | — | `4` | `open` | — | Respondento lytis | — |
| `amzius` | `integer` | — | `4` | `open` | — | Respondento amžius | — |
| `kilmes_salis` | `string` | — | `4` | `open` | — | Respondento kilmė | "Respondento kilmės šalis - vieta, kurioje gimė." |
| `gyvenamoji_vt` | `string` | — | `4` | `open` | — | Respondento gyvenamoji vieta | Dabartinė respondento gyvenamoji vieta: miestas |
| `gyv_vt_pop` | `string` | — | `4` | `open` | — | Respondento gyvenamosios vietos populiacija | — |
| `issilavinimas` | `string` | — | `4` | `open` | — | Respondento išsilavinimas | — |
| `ekonom_padetis` | `string` | — | `4` | `open` | — | Ekonominė respondento padėtis | — |
| `kelioniu_dazn` | `string` | — | `4` | `open` | — | Respondento kelionių dažnis | Nurodo kaip dažnai respondentas keliauja į užsienį |
| `zino_bratislava` | `boolean` | — | `4` | `open` | — | Žinios apie Bratislavą | Ar respondentas girdėjęs apie Bratislavą? |
| `zino_krokuva` | `boolean` | — | `4` | `open` | — | Žinios apie Krokuvą | Ar respondentas girdėjęs apie Krokuvą? |
| `zino_helsinki` | `boolean` | — | `4` | `open` | — | Žinios apie Helsinkį | Ar respondentas girdėjęs apie Helsinkį? |
| `zino_ryga` | `boolean` | — | `4` | `open` | — | Žinios apie Rygą | Ar respondentas girdėjęs apie Rygą? |
| `zino_liublijana` | `boolean` | — | `4` | `open` | — | Žinios apie Liublijaną | Ar respondentas girdėjęs apie Liublijaną? |
| `zino_vilniu` | `boolean` | — | `4` | `open` | — | Žinios apie Vilnių | Ar respondentas girdėjęs apie Vilnių? |
| `zino_varsuva` | `boolean` | — | `4` | `open` | — | Žinios apie Varšuvą | Ar respondentas girdėjęs apie Varšuvą? |
| `zino_talina` | `boolean` | — | `4` | `open` | — | Žinios apie Taliną | Ar respondentas girdėjęs apie Taliną? |
| `stat_svoris` | `number` | — | `4` | `open` | — | Statistinis svoris | Respondento statistinis svoris apklausoje (techninis įvertis) |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `rinka` | `"Didžioji Britanija"` | — | — | Didžioji Britanija | — |
| `lytis` | `"Vyras"` | — | — | Vyras | — |
| `lytis` | `"Moteris"` | — | — | Moteris | — |
| `kilmes_salis` | `"Vietinis"` | — | — | Vietinis | — |
| `kilmes_salis` | `"Kita"` | — | — | Kita | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L132 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L132)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/go_vilnius/vilniaus_zinomumas (https://data.gov.lt/datasets/2792/)
