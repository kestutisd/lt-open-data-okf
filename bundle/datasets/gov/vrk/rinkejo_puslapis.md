---
type: Dataset
title: "Rinkėjo puslapio naudotojo paveikslas"
description: "Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo puslapis“ seansų duomenų ir pasaulinio masto IP adresų pagal geografinę vietovę rinkinio."
resource: "https://get.data.gov.lt/datasets/gov/vrk/rinkejo_puslapis"
tags: [gov, vrk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rinkėjo puslapio naudotojo paveikslas

Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo puslapis“ seansų duomenų ir pasaulinio masto IP adresų pagal geografinę vietovę rinkinio. VRKIS duomenys saugomi nuo 2011 m. ir yra atnaujinami kasdien, o iki 2024 m. buvęs aktualus IP adresų rinkinys nebėra atnaujinamas. Duomenų rinkinį sudaro: prisijungimo seanso identifikatorius, pseudonimizuotas rinkėjo asmens kodas, gimimo metai, lytis, pagal IP adresą nustatytos tikėtina prisijungimo valstybė ir vietovė, prisijungimo ir atsijungimo laikas bei atsijungimo priežastis.

- **Namespace:** `datasets/gov/vrk/rinkejo_puslapis`[^manifest]
- **Manifest CSV:** [datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vrk/rinkejo_puslapis`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Vartotojas](rinkejo_puslapis/Vartotojas.md) | Rinkėjo puslapio naudotojo paveikslas | `4` | `sesijos_id` | — | 9 | Duomenų rinkinys sudarytas iš Vyriausiosios rinkimų komisijos informacinės sistemos (VRKIS) kaupiamų prisijungimo prie VRK tvarkomo projekto „Rinkėjo... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vrk/rinkejo_puslapio_vartotojas.csv
