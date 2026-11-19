---
type: Dataset
title: "Nacionalinis saugomų augalų veislių sąrašas, Lietuvos Respublikoje saugomų augalų veislių sąrašas ir augalų veislių ūkinio vertingumo tyrimo duomenys"
description: "Pateikiama informacija apie į Nacionalinį sąrašą įrašytas veisles, išbrauktas veisles, veislių palaikytojų ir selekcininkų įgaliotųjų atstovų sąrašus."
resource: "https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1868/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/saugomos_veisles"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Nacionalinis saugomų augalų veislių sąrašas, Lietuvos Respublikoje saugomų augalų veislių sąrašas ir augalų veislių ūkinio vertingumo...

- **Namespace:** `datasets/gov/vat/saugomos_veisles`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/saugomos_veisles.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1868/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles`[^dcat]
- **Portal Title (`@lt`):** Nacionalinis saugomų augalų veislių sąrašas, Lietuvos Respublikoje saugomų augalų veislių sąrašas ir augalų veislių ūkinio vertingumo tyrimo duomenys[^dcat]
- **Portal Title (`@en`):** National List of Protected Plant Varieties, List of Plant Varieties Protected in the Republic of Lithuania and Data on the Study of the Economic Value of Plant Varieties[^dcat]
- **Issued (`dct:issued`):** `2023-05-30`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-05-30` .. `2026-09-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiama informacija apie į Nacionalinį sąrašą įrašytas veisles, išbrauktas veisles, veislių palaikytojų ir selekcininkų įgaliotųjų atstovų sąrašus. Pateikiama informacija apie atliktų ūkinio vertingumo tyrimo duomenis. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

National Plant Varieties 2021 list of plant varieties registered in 2021 2020. Economic value survey data[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Veisle](saugomos_veisles/Veisle.md) | Pateikiama informacija apie į Nacionalinį sąrašą įrašytas veisles, išbrauktas veisles, veislių palaikytojų ir selekcininkų įgaliotųjų atstovų sąrašus. | `4` | `id` | `open` | `14` | — |
| [Verte](saugomos_veisles/Verte.md) | Pateikiama informacija apie atlikto ūkinio vertingumo tyrimo duomenis. | `4` | `id` | `open` | `10` | — |
| [SaugVeisle](saugomos_veisles/SaugVeisle.md) | Saugomų augalų veislių sąrašas. | `4` | `eil_nr` | `open` | `7` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/saugomos_veisles (https://data.gov.lt/datasets/1868/)
