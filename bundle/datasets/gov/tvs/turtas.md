---
type: Dataset
title: "Duomenys apie savyvaldybės turtą"
description: "Rinkinys pateikia informaciją apie savivaldybių valdomą nekilnojamąjį turtą."
resource: "https://get.data.gov.lt/datasets/gov/tvs/turtas"
tags: [gov, tvs, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/tvs/turtas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Duomenys apie savyvaldybės turtą

Rinkinys pateikia informaciją apie savivaldybių valdomą nekilnojamąjį turtą. Duomenyse nurodomas turto identifikatorius, NT registro kodas, objekto pavadinimas, statybos pabaigos metai, objekto paskirtis, plotas kvadratiniais metrais, bei geografinė vieta. Geografinė informacija pateikiama tiek geografinių koordinačių, tiek LKS-94 plokštuminių koordinačių formatais. Taip pat įtrauktas objekto adreso informacijos aktualumas bei geografinio koordinavimo patikimumo procentas. Duomenų teikėjas: Savivaldybių administracija.

- **Namespace:** `datasets/gov/tvs/turtas`[^manifest]
- **Manifest CSV:** [datasets/gov/tvs/turtas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tvs/turtas`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TelsiuRajSav](turtas/TelsiuRajSav.md) | — | `4` | `id` | — | 13 | — |
| [KedainiuRajSav](turtas/KedainiuRajSav.md) | — | `4` | `id` | — | 13 | — |
| [MarijampolesRajSav](turtas/MarijampolesRajSav.md) | — | `4` | `id` | — | 13 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/tvs/turtas.csv
