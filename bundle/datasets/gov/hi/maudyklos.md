---
type: Dataset
title: "Maudyklų vandens kokybės duomenys"
description: "Stebimų Lietuvos maudyklų sąrašas, pateikiama informacija apie: maudymosi sezono metus, maudyklos identifikavimo unikalų kodą, maudymosi sezono pradžią ir pabaigą, vandens kokybės klasę, nuorodos į maudyklos charakteristikų aprašus, maudyklos stebėjimo vietos koordinates..."
resource: "https://get.data.gov.lt/datasets/gov/hi/maudyklos"
tags: [gov, hi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/maudyklos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/hi/maudyklos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2644/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/maudyklos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Maudyklų vandens kokybės duomenys

- **Namespace:** `datasets/gov/hi/maudyklos`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/maudyklos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/maudyklos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/maudyklos` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2644/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/maudyklos`[^dcat]
- **Portal Title (`@lt`):** Maudyklų vandens kokybės duomenys[^dcat]
- **Portal Title (`@en`):** Bathing water quality data[^dcat]
- **Issued (`dct:issued`):** `2024-05-03`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-05-17` .. `2026-01-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Stebimų Lietuvos maudyklų sąrašas, pateikiama informacija apie: maudymosi sezono metus, maudyklos identifikavimo unikalų kodą, maudymosi sezono pradžią ir pabaigą, vandens kokybės klasę, nuorodos į maudyklos charakteristikų aprašus, maudyklos stebėjimo vietos koordinates, mėginio ėmimo datą, parametrų: žarninių enterokokų ir žarninių lazdelių vertes. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

List of Lithuania's monitored bathing waters, information on: year of the bathing season, unique code of the bathing water identification, start and end of the bathing season, water quality class, references to bathing description, coordinates of the bathing area, date of sampling, parameters: intestinal enterococci and intestinal sticks.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kokybe](maudyklos/Kokybe.md) | Maudyklų vandens kokybės duomenys | `4` | `vda_id` | — | `16` | Stebimų Lietuvos maudyklų sąrašas, pateikiama informacija apie: maudymosi sezono metus, maudyklos identifikavimo unikalų kodą, maudymosi sezono pradžią ir... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/maudyklos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/maudyklos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/maudyklos (https://data.gov.lt/datasets/2644/)
