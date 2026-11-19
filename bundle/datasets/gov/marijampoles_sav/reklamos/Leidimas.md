---
type: Table
title: "Leidimas — Marijampolės savivaldybės reklamų leidimai"
description: "Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi lauko reklamų leidimai."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos/Leidimas"
tags: [gov, marijampoles_sav, leidimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L26"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv#L26"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2845/"
    title: "data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/reklamos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Leidimas — Marijampolės savivaldybės reklamų leidimai

Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi lauko reklamų leidimai. Duomenų rinkinį sudaro: leidimo numeris bei leidimo galiojimo terminai. Viena eilutė atitinka vieną leidimą. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/marijampoles_sav/reklamos/Leidimas`[^manifest]
- **Dataset:** [Marijampolės savivaldybės reklamų įrengimai ir leidimai](../reklamos.md) (`datasets/gov/marijampoles_sav/reklamos`)[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/reklamos.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L26)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos/Leidimas` (`deployed`)[^manifest]
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
| `leidimo_nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pradžia | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimo galiojimo pabaiga | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv#L26 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L26)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/reklamos (https://data.gov.lt/datasets/2845/)
