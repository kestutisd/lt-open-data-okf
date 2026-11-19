---
type: Dataset
title: "Vilniaus žinomumo tyrimų apklausų duomenų rinkinys"
description: "\"Rinkinys iš \"GO Vilnius\" rengtos apklausos 2023 m. apie Vilniaus žinomumą."
resource: "https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas"
tags: [gov, go_vilnius, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2792/"
    title: "data.gov.lt DCAT-AP — datasets/gov/go_vilnius/vilniaus_zinomumas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilniaus žinomumo tyrimų apklausų duomenų rinkinys

"Rinkinys iš "GO Vilnius" rengtos apklausos 2023 m. apie Vilniaus žinomumą. Apklausos atliktos skirtingose rinkose (Vokietijoje, Latvijoje, Lenkijoje, Didžiojoje Britanijoje). Vieną lentelės eilutę sudaro informacija apie respondentą ir jo atsakymai į pateiktus apklausos klausimus. Paskutinis stulpelis įvertine kiekvieno korespondento statistinį svorį apklausoje. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt"[^manifest]

- **Namespace:** `datasets/gov/go_vilnius/vilniaus_zinomumas`[^manifest]
- **Manifest CSV:** [datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas` (`deployed`)[^manifest]
- **Provider:** `go_vilnius` — VšĮ GO Vilnius *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2792/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas`[^dcat]
- **Portal Title (`@lt`):** Vilniaus žinomumo tyrimų apklausų duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** Vilnius Audiology Survey Data Set[^dcat]
- **Issued (`dct:issued`):** `2024-09-20`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2024-09-13` .. `2024-10-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinys iš VšĮ "GO Vilnius" rengtos apklausos 2023 m. apie Vilniaus žinomumą. Apklausos atliktos skirtingose rinkose (Vokietijoje, Latvijoje, Lenkijoje, Didžiojoje Britanijoje). Vieną lentelės eilutę sudaro informacija apie respondentą ir jo atsakymai į pateiktus apklausos klausimus. Paskutinis stulpelis įvertina kiekvieno korespondento statistinį svorį apklausoje. Duomenų teikėjas – VšĮ Go Vilnius. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Collection from a survey conducted by the Public Company “GO Vilnius” in 2023 about the visibility of Vilnius. Surveys have been conducted in different markets (Germany, Latvia, Poland, Britain). One row in the table consists of information about the respondent and his answers to the questions asked in the survey. The last column evaluates the statistical weight of each correspondent in the survey. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VokietijosRinka](vilniaus_zinomumas/VokietijosRinka.md) | Vilniaus žinomumo apklausų rezultatai Vokietijos rinkoje | `4` | `dalyv_id` | — | `21` | — |
| [LatvijosRinka](vilniaus_zinomumas/LatvijosRinka.md) | Vilniaus žinomumo apklausų rezultatai Latvijos rinkoje | `4` | `dalyv_id` | — | `19` | — |
| [LenkijosRinka](vilniaus_zinomumas/LenkijosRinka.md) | Vilniaus žinomumo apklausų rezultatai Lenkijos rinkoje | `4` | `dalyv_id` | — | `19` | — |
| [DidzBritRinka](vilniaus_zinomumas/DidzBritRinka.md) | Vilniaus žinomumo apklausų rezultatai Didžiosios Britanijos rinkoje | — | `dalyv_id` | — | `20` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/go_vilnius/vilniaus_zinomumas (https://data.gov.lt/datasets/2792/)
