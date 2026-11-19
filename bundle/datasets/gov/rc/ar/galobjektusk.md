---
type: Dataset
title: "Adresų registro galiojančių objektų kiekiai mėnesio pradžiai"
description: "Lietuvos Respublikos adresų registro statistinių duomenų rinkinys - įregistruotų, galiojančių Adresų registro objektų skaičius mėnesio pradžiai (Lietuvos Respublikos adresų registro statistiką apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/galobjektusk"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1553/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/galobjektusk"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Adresų registro galiojančių objektų kiekiai mėnesio pradžiai

- **Namespace:** `datasets/gov/rc/ar/galobjektusk`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/galobjektusk` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1553/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/galobjektusk`[^dcat]
- **Portal Title (`@lt`):** Adresų registro galiojančių objektų kiekiai mėnesio pradžiai[^dcat]
- **Portal Title (`@en`):** Quantities of valid objects in the address register at the beginning of the month[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-01-23` .. `2025-05-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos adresų registro statistinių duomenų rinkinys - įregistruotų, galiojančių Adresų registro objektų skaičius mėnesio pradžiai (Lietuvos Respublikos adresų registro statistiką apibūdinantys duomenys).[^dcat]

### Portal Description (`@en`)

Statistical data set of the Address Register of the Republic of Lithuania - the number of registered, valid Address Register objects for the beginning of the month (data describing the statistics of the Address Register of the Republic of Lithuania). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ObjektuSkaicius](galobjektusk/ObjektuSkaicius.md) | Adresų registro galiojančių objektų kiekiai mėnesio pradžiai | `3` | `savivaldybe, metai, menuo` | — | `15` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/galobjektusk (https://data.gov.lt/datasets/1553/)
