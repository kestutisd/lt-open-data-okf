---
type: Dataset
title: "Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų"
description: "Duomenys iš Higienos Instituto apie pacientus, kurie kreipėsi į gydymo įstaigas dėl traumų ir apsinuodijimų, ir kuriems buvo priskirtas stacionarus arba ambulatorinis gydymo tipas."
resource: "https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai"
tags: [gov, hi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Stacionaro ir ambulatoriniai ligoniai, gydyti nuo traumų ir apsinuodijimų

Duomenys iš Higienos Instituto apie pacientus, kurie kreipėsi į gydymo įstaigas dėl traumų ir apsinuodijimų, ir kuriems buvo priskirtas stacionarus arba ambulatorinis gydymo tipas. Duomenų rinkinys yra sudarytas iš trijų lentelių:

1. Traumas ir apsinuodijimus patyrusių pacientų duomenys,

2. Traumų ir apsinuodijimų atvejai dėl kurių kreiptasi į gydymo įstaigą,

3. Gydymo įstaigų duomenys.

Duomenų teikėjas – Higienos institutas

- **Namespace:** `datasets/gov/hi/traumos_apsinuodijimai`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/traumos_apsinuodijimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/traumos_apsinuodijimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/traumos_apsinuodijimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pacientas](traumos_apsinuodijimai/Pacientas.md) | Traumas ir apsinuodijimus patyrusių pacientų duomenys | `4` | `vda_pk` | — | 14 | Duomenys iš Higienos instituto apie traumas arba apsinuodijimus patyrusius pacientus. |
| [Ligonine](traumos_apsinuodijimai/Ligonine.md) | Traumų ir apsinuodijimų atvejai dėl kurių kreiptasi į gydymo įstaigą | `4` | `vda_pk` | — | 7 | Duomenys iš Higienos instituto apie traumų ir apsinuodijimų atvejus dėl kurių buvo kreiptasi į gydymo įstaigą. |
| [GydymoIstaiga](traumos_apsinuodijimai/GydymoIstaiga.md) | Gydymo įstaigų duomenys | `4` | `gist_id` | — | 7 | Duomenys iš Higienos instituto apie gydymo įstaigas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/traumos_apsinuodijimai.csv
