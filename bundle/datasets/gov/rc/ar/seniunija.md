---
type: Dataset
title: "Adresų registras"
description: "Seniūnijų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/seniunija"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/seniunija.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/seniunija.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1288/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/seniunija"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registras

- **Namespace:** `datasets/gov/rc/ar/seniunija`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/seniunija.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/seniunija.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/seniunija` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1288/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/seniunija`[^dcat]
- **Portal Title (`@lt`):** Adresų registro seniūnijų tekstinių duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** Textual data set of address register elderships[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-08-18` .. `2026-03-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Seniūnijų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys duomenys).[^dcat]

### Portal Description (`@en`)

Textual data collection of elderships from the address register of the Republic of Lithuania (data describing administrative units of the Republic of Lithuania - elderships). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Seniunija](seniunija/Seniunija.md) | Adresų registro seniūnijų tekstinių duomenų rinkinys | `4` | `sen_kodas` | — | `7` | Seniūnijų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys... |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/seniunija.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/seniunija.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/seniunija (https://data.gov.lt/datasets/1288/)
