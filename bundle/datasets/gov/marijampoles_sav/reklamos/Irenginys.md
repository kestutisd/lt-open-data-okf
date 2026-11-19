---
type: Table
title: "Irenginys — Marijampolės savivaldybės reklamų įrengimai"
description: "Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos/Irenginys"
tags: [gov, marijampoles_sav, irenginys, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2845/"
    title: "data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/reklamos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Irenginys — Marijampolės savivaldybės reklamų įrengimai

Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys. Duomenų rinkinį sudaro: įmonė, reklamos statusas, adresas, koordinatės, tipas, zona. Viena eilutė atitinka vieną reklamos objektą. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/marijampoles_sav/reklamos/Irenginys`[^manifest]
- **Dataset:** [Marijampolės savivaldybės reklamų įrengimai ir leidimai](../reklamos.md) (`datasets/gov/marijampoles_sav/reklamos`)[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/reklamos.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos/Irenginys` (`deployed`)[^manifest]
- **Provider:** `marijampoles_sav` — Marijampolės savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `irenginio_id` | `string` | — | `4` | `open` | — | Įrenginio identifikatorius | — |
| `imone` | `string` | — | `4` | `open` | — | Įmonė | — |
| `galiojimo_statusas` | `string` | — | `4` | `open` | — | Galiojimo statusas | — |
| `galiojimo_statuso_data` | `date` | `D` | `4` | `open` | — | Galiojimo statuso data | — |
| `reklamos_adresas` | `string` | — | `4` | `open` | — | Reklamos adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Geometrija | — |
| `reklamos_tipas` | `string` | — | `4` | `open` | — | Reklamos tipas | — |
| `reklamos_zona` | `string` | — | `4` | `open` | — | Reklamos zona | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L9)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/reklamos (https://data.gov.lt/datasets/2845/)
