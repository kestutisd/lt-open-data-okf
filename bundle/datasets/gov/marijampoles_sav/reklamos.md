---
type: Dataset
title: "Marijampolės savivaldybės reklamų įrengimai ir leidimai"
description: "Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys bei leidimai."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos"
tags: [gov, marijampoles_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2845/"
    title: "data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/reklamos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Marijampolės savivaldybės reklamų įrengimai ir leidimai

Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys bei leidimai. Duomenų rinkinį sudaro dvi lentelės, kuriuose yra pateikiama: įmonė, reklamos statusas, adresas, koordinates, tipas, zona, leidimo numeris bei leidimo galiojimo terminai. Lentelės jungiasi per „irenginio_id“ raktą. Viena eilutė atitinka vieną reklamos objektą arba viena leidimą. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/marijampoles_sav/reklamos`[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/reklamos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos` (`deployed`)[^manifest]
- **Provider:** `marijampoles_sav` — Marijampolės savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2845/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/reklamos`[^dcat]
- **Portal Title (`@lt`):** Marijampolės savivaldybės reklamų įrengimai ir leidimai[^dcat]
- **Portal Title (`@en`):** Advertising equipment and permits of Marijampole Municipality[^dcat]
- **Issued (`dct:issued`):** `2024-11-11`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-11-04` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai duomenys bei leidimai. Duomenų rinkinį sudaro dvi lentelės, kuriuose yra pateikiama: įmonė, reklamos statusas, adresas, koordinates, tipas, zona, leidimo numeris bei leidimo galiojimo terminai. Lentelės jungiasi per „irenginio_id“ raktą. Viena eilutė atitinka vieną reklamos objektą arba viena leidimą. Duomenų teikėjas – Marijampolės savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes geospatial data and permits of advertising devices, STANDS, signs and posters collected and stored in the application of advertisements by ARCGIS of Marijampolė Municipality from 2013. The dataset consists of two tables containing: company, advertising status, address, coordinates, type, zone, authorisation number, and expiration dates. Tables connect through the irenginio_id key. One line corresponds to one promotion object or one edition. Technical questions or possible errors may be referred to the atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Irenginys](reklamos/Irenginys.md) | Marijampolės savivaldybės reklamų įrengimai | `4` | `vda_prime_key` | — | `13` | Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi reklamos įrenginių, stendų, iškabų geoerdviniai... |
| [Leidimas](reklamos/Leidimas.md) | Marijampolės savivaldybės reklamų leidimai | `4` | `vda_prime_key` | — | `5` | Rinkinyje pateikiami Marijampolės savivaldybės ARCGIS reklamų aplikacijoje nuo 2013 metų kaupiami ir saugomi lauko reklamų leidimai. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/reklamos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/reklamos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/reklamos (https://data.gov.lt/datasets/2845/)
