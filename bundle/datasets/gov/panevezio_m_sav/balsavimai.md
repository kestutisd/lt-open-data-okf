---
type: Dataset
title: "Panevėžio miesto tarybos posėdžių balsavimų rezultatai"
description: "Rinkinyje pateikiami Panevėžio miesto tarybos bendri rezultatai ir asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų."
resource: "https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai"
tags: [gov, panevezio_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Panevėžio miesto tarybos posėdžių balsavimų rezultatai

Rinkinyje pateikiami Panevėžio miesto tarybos bendri rezultatai ir asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų. Duomenys apima laikotarpį nuo 2023m. balandžio iki šių dienų.

- **Namespace:** `datasets/gov/panevezio_m_sav/balsavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/panevezio_m_sav/balsavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/panevezio_m_sav/balsavimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/panevezio_m_sav/balsavimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Balsavimas](balsavimai/Balsavimas.md) | Panevėžio miesto tarybos narių asmeniniai balsavimų rezultatai | `4` | `vda_id` | — | 9 | Lentelėje pateikiami Panevėžio miesto tarybos narių asmeniniai balsavimai dėl Tarybos posėdžiuose teikiamų klausimų. |
| [Sesija](balsavimai/Sesija.md) | Panevėžio miesto tarybos posėdžių balsavimų rezultatai | `4` | `vda_id` | — | 14 | Lentelėje pateikiami agreguoti Panevėžio miesto tarybos narių balsavimų rezultatai dėl posėdžių metu iškeltų klausimų nuo 2023m. iki šių dienų. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/panevezio_m_sav/balsavimai.csv
