---
type: Dataset
title: "Marijampolės savivaldybės reklamų įrengimai ir leidimai"
description: "Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys bei leidimai."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos"
tags: [gov, marijampoles_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Marijampolės savivaldybės reklamų įrengimai ir leidimai

Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys bei leidimai. Duomenų rinkinį sudaro dvi lentelės, kuriuose yra pateikiama: įmonė, reklamos statusas, adresas, koordinates, tipas, zona, leidimo numeris bei leidimo galiojimo terminai. Lentelės jungiasi per „irenginio_id“ raktą.

Viena eilutė atitinka vieną reklamos objektą arba viena leidimą.

- **Namespace:** `datasets/gov/marijampoles_sav/reklamos`[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/reklamos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Irenginys](reklamos/Irenginys.md) | Marijampolės savivaldybės reklamų įrengimai | `4` | `vda_prime_key` | — | 13 | Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai... |
| [Leidimas](reklamos/Leidimas.md) | Marijampolės savivaldybės reklamų leidimai | `4` | `vda_prime_key` | — | 5 | Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi lauko reklamų leidimai. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv
