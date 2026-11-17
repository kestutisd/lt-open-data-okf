---
type: Dataset
title: "Vilniaus miesto tarybos balsavimai"
description: "Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai"
tags: [gov, vilniaus_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus miesto tarybos balsavimai

Rinkinyje pateikiama informacija apie Vilniaus miesto tarybos posėdžiuose svarstytus klausimus ir balsavimus. Rinkinį sudaro dvi pagrindinės lentelės: viena reprezentuoja posėdžių ir klausimų informaciją su apibendrintais balsavimo duomenimis, kita – detalius kiekvieno tarybos nario balsus dėl individualaus klausimo. Rinkinyje pateikiami duomenys apie įvykusį posėdį (laiko žyma, posėdžio pirmininkas ir sekretorius), balsavimus (iškeltas klausimas, svarstymo tvarka, balsavimo rezultatai) ir priimtus sprendimus. Pažymėtina, jog abi rinkinio lentelės siejasi tarpusavyje per lauką "balsavimo_id".

- **Namespace:** `datasets/gov/vilniaus_m_sav/balsavimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/balsavimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/balsavimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/balsavimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Klausimas](balsavimai/Klausimas.md) | Vilniaus miesto tarybos posėdžių duomenys ir apibendrinti rezultatai | `4` | `vda_id` | — | 17 | — |
| [Balsas](balsavimai/Balsas.md) | Vilniaus miesto tarybos narių individualūs balsavimų duomenys | `4` | `vda_id` | — | 5 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/balsavimai.csv
