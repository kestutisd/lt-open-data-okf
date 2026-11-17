---
type: Dataset
title: "Vilniaus žinomumo tyrimų apklausų duomenų rinkinys"
description: "\"Rinkinys iš \"GO Vilnius\" rengtos apklausos 2023 m. apie Vilniaus žinomumą."
resource: "https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas"
tags: [gov, go_vilnius, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/go_vilnius/vilniaus_zinomumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus žinomumo tyrimų apklausų duomenų rinkinys

"Rinkinys iš "GO Vilnius" rengtos apklausos 2023 m. apie Vilniaus žinomumą. Apklausos atliktos skirtingose rinkose (Vokietijoje, Latvijoje, Lenkijoje, Didžiojoje Britanijoje). Vieną lentelės eilutę sudaro informacija apie respondentą ir jo atsakymai į pateiktus apklausos klausimus. Paskutinis stulpelis įvertine kiekvieno korespondento statistinį svorį apklausoje.

- **Namespace:** `datasets/gov/go_vilnius/vilniaus_zinomumas`[^manifest]
- **Manifest CSV:** [datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/go_vilnius/vilniaus_zinomumas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/go_vilnius/vilniaus_zinomumas`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VokietijosRinka](vilniaus_zinomumas/VokietijosRinka.md) | Vilniaus žinomumo apklausų rezultatai Vokietijos rinkoje | `4` | `dalyv_id` | — | 21 | — |
| [LatvijosRinka](vilniaus_zinomumas/LatvijosRinka.md) | Vilniaus žinomumo apklausų rezultatai Latvijos rinkoje | `4` | `dalyv_id` | — | 19 | — |
| [LenkijosRinka](vilniaus_zinomumas/LenkijosRinka.md) | Vilniaus žinomumo apklausų rezultatai Lenkijos rinkoje | `4` | `dalyv_id` | — | 19 | — |
| [DidzBritRinka](vilniaus_zinomumas/DidzBritRinka.md) | Vilniaus žinomumo apklausų rezultatai Didžiosios Britanijos rinkoje | — | `dalyv_id` | — | 20 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/go_vilnius/vilniaus_zinomumas.csv
