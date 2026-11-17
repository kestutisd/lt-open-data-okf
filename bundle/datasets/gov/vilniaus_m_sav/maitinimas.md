---
type: Dataset
title: "Maitinimo duomenys Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose"
description: "Rinkinyje skelbiamos dviejų tipų ataskaitos – apie Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose vykdytus maitinimus ir apie maitinimui sunaudotus maisto produktus."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/maitinimas"
tags: [gov, vilniaus_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/maitinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/maitinimas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Maitinimo duomenys Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose

Rinkinyje skelbiamos dviejų tipų ataskaitos – apie Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose vykdytus maitinimus ir apie maitinimui sunaudotus maisto produktus. Duomenys teikiami nuo 2014 m. rugsėjo mėnesio iki dabar.

Pirmoje ataskaitoje pateikiami duomenys apie suteiktas maitinimo paslaugas švietimo įstaigoje pagal maitinimo kategoriją ataskaitine data. Nurodoma ataskaitinė diena, ugdymo įstaiga, maitinimo tipas ir maitinimą gavusių asmenų skaičius.

Antroje ataskaitoje skelbiama informacija apie maisto gamybai sunaudotus maisto produktus. Šiuos duomenis įstaigos skelbia nereguliariu dažniu, todėl viena eilutė identifikuoja situaciją apie sunaudotus maisto produktus nuo paskutinės pateiktos ataskaitos. Nurodoma ataskaitą teikusi švietimo įstaiga, deklaruotas produktas ir sunaudotas kiekis maisto gamyboje.

Duomenų teikėjas – Vilniaus miesto savivaldybės administracija.

- **Namespace:** `datasets/gov/vilniaus_m_sav/maitinimas`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/maitinimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/maitinimas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/maitinimas`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Produktas](maitinimas/Produktas.md) | Sunaudoti maisto produktai Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigose | `4` | `vda_id` | — | 6 | Skelbiama informacija apie maisto gamybai sunaudotus maisto produktus. |
| [Valgis](maitinimas/Valgis.md) | Vilniaus miesto ikimokyklinio ir priešmokyklinio švietimo įstaigų maitinimo ataskaitos | `4` | `vda_id` | — | 5 | Pateikiami duomenys apie suteiktas maitinimo paslaugas švietimo įstaigoje pagal maitinimo kategoriją ataskaitine data. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/maitinimas.csv
