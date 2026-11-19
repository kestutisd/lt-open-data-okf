---
type: Dataset
title: "datasets/gov/lki/gyventoju_surasymas_2011"
description: "Rinkinyje pateikiami 2011 m. gyventojų surašymo sociodemografiniai rodikliai, susieti su skirtingais erdviniais vienetais: 1 km ir 2 km gardelėmis, gyvenvietėmis, seniūnijomis bei LKA Thiesseno poligonais."
resource: "https://get.data.gov.lt/datasets/gov/lki/gyventoju_surasymas_2011"
tags: [gov, lki, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/gyventoju_surasymas_2011.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lki/gyventoju_surasymas_2011.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/lki/gyventoju_surasymas_2011

Rinkinyje pateikiami 2011 m. gyventojų surašymo sociodemografiniai rodikliai, susieti su skirtingais erdviniais vienetais: 1 km ir 2 km gardelėmis, gyvenvietėmis, seniūnijomis bei LKA Thiesseno poligonais. Taip pat pateikiami LKA punktų erdviniai taškai ir jų atributai.[^manifest]

- **Namespace:** `datasets/gov/lki/gyventoju_surasymas_2011`[^manifest]
- **Manifest CSV:** [datasets/gov/lki/gyventoju_surasymas_2011.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/gyventoju_surasymas_2011.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/gyventoju_surasymas_2011` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `6` (6 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GRIDHexo1km2011](gyventoju_surasymas_2011/GRIDHexo1km2011.md) | 1 km heksagoninių gardelių 2011 m. gyventojų surašymo rodikliai | `4` | `feature_id` | — | `41` | Lentelėje pateikiami 1 km heksagoninių gardelių erdviniai objektai ir su jais susieti 2011 m. gyventojų surašymo sociodemografiniai rodikliai. |
| [GRIDHexo2km2011](gyventoju_surasymas_2011/GRIDHexo2km2011.md) | 2 km heksagoninių gardelių 2011 m. gyventojų surašymo rodikliai | `4` | `feature_id` | — | `41` | Lentelėje pateikiami 2 km heksagoninių gardelių erdviniai objektai ir su jais susieti 2011 m. gyventojų surašymo sociodemografiniai rodikliai. |
| [Gyvenviete2011GyvSuras](gyventoju_surasymas_2011/Gyvenviete2011GyvSuras.md) | Gyvenviečių 2011 m. gyventojų surašymo rodikliai | `4` | `feature_id` | — | `46` | Lentelėje pateikiami gyvenviečių erdviniai objektai ir su jais susieti 2011 m. gyventojų surašymo sociodemografiniai rodikliai. |
| [LKAPunktas](gyventoju_surasymas_2011/LKAPunktas.md) | LKA punktai | `4` | `feature_id` | — | `17` | Lentelėje pateikiami LKA punktų erdviniai taškai ir jų atributai: gyvenvietės pavadinimas, statusas, LKA punkto numeracija, savivaldybė, seniūnija, tarmės... |
| [LKAThiessenoPoligonas2011](gyventoju_surasymas_2011/LKAThiessenoPoligonas2011.md) | LKA Thiesseno poligonų 2011 m. gyventojų surašymo rodikliai | `4` | `feature_id` | — | `41` | Lentelėje pateikiami LKA Thiesseno poligonų erdviniai objektai ir su jais susieti 2011 m. gyventojų surašymo sociodemografiniai rodikliai. |
| [Seniunija2011GyvSuras](gyventoju_surasymas_2011/Seniunija2011GyvSuras.md) | Seniūnijų 2011 m. gyventojų surašymo rodikliai | `4` | `feature_id` | — | `42` | Lentelėje pateikiami seniūnijų erdviniai objektai ir su jais susieti 2011 m. gyventojų surašymo sociodemografiniai rodikliai. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/gyventoju_surasymas_2011.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/gyventoju_surasymas_2011.csv#L2)
