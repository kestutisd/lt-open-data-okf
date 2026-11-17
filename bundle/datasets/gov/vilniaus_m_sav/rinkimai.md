---
type: Dataset
title: "Vilniaus miesto savivaldybės seniūnaičių rinkimų rezultatai"
description: "Rinkinyje pateikiami Vilniaus mieste savivaldybėje vykusių seniūnaičių rinkimų duomenys nuo 2019m. Vilniaus miesto teritorija yra padalinta į seniūnijas, o seniūnijos savo ruožtu yra skirstomos į mažesnius administracinius vienetus –..."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/rinkimai"
tags: [gov, vilniaus_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/seniunaiciai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vilniaus miesto savivaldybės seniūnaičių rinkimų rezultatai

Rinkinyje pateikiami Vilniaus mieste savivaldybėje vykusių seniūnaičių rinkimų duomenys nuo 2019m. Vilniaus miesto teritorija yra padalinta į seniūnijas, o seniūnijos savo ruožtu yra skirstomos į mažesnius administracinius vienetus – seniūnaitijas. Seniūnaitis – tai visuomeniniais pagrindais dirbantis gyvenamosios vietovės ar bendruomenės išrinktas atstovas, vykdantis įstatymo nustatytas teises ir pareigas. Vilniaus miesto tarybos sprendimu seniūnaičiui skiriama 30 eurų mėnesio išmoka, skirta su seniūnaičio veikla susijusioms išlaidos apmokėti. Daugiau informacijos apie seniūnaičių teises ir pareigas: https://vilnius.lt/savivaldybe/seniunijos-ir-bendruomenes/seniunaiciai

Rinkinio objektas – rinkimuose dalyvavusio kandidato rezultatai. Duomenyse nurodyti duomenys apie seniūnaičių rinkimus (rinkimų data, balsavimo pradžios ir pabaigos datos, turas) ir kandidatus į seniūnaičius (seniūnija, seniūnaitija, kandidato (-ės) vardas ir pavardė, rinkiminės programos tikslai, surinktų balsų skaičius ir požymis, ar buvo išrinktas(-a)).

Duomenų teikėjas – Vilniaus miesto savivaldybės administracija.

- **Namespace:** `datasets/gov/vilniaus_m_sav/rinkimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/seniunaiciai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/rinkimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kandidatas](rinkimai/Kandidatas.md) | Vilniaus miesto savivaldybės seniūnaičių rinkimų rezultatai | `4` | `vda_id` | — | 12 | Rinkinyje pateikiami Vilniaus mieste savivaldybėje vykusių seniūnaičių rinkimų duomenys nuo 2019m. Vilniaus miesto teritorija yra padalinta į seniūnijas, o... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/seniunaiciai.csv
