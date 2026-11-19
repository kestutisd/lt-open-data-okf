---
type: Dataset
title: "Išregistruotų Adresų registro objektų skaičius per mėnesį"
description: "Lietuvos Respublikos adresų registro statistinių duomenų rinknys - išregistruotų iš Adresų registro objektų skaičius per mėnesį (Lietuvos Respublikos adresų registro statistiką apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/isregobjektusk"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1556/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ar/isregobjektusk"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Išregistruotų Adresų registro objektų skaičius per mėnesį

- **Namespace:** `datasets/gov/rc/ar/isregobjektusk`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/isregobjektusk` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1556/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ar/isregobjektusk`[^dcat]
- **Portal Title (`@lt`):** Išregistruotų Adresų registro objektų skaičius per mėnesį[^dcat]
- **Portal Title (`@en`):** Number of deregistered Address Register objects per month[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2023-01-23` .. `2025-05-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos adresų registro statistinių duomenų rinknys - išregistruotų iš Adresų registro objektų skaičius per mėnesį (Lietuvos Respublikos adresų registro statistiką apibūdinantys duomenys).[^dcat]

### Portal Description (`@en`)

Statistical data set of the Address Register of the Republic of Lithuania - the number of objects deregistered from the Address Register per month (data describing the statistics of the Address Register of the Republic of Lithuania). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IsregistruotuObjektuSkaicius](isregobjektusk/IsregistruotuObjektuSkaicius.md) | Išregistruotų Adresų registro objektų skaičius per mėnesį | `3` | `savivaldybe, metai, menuo` | — | `11` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/isregistruotu_objektu_skaicius.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ar/isregobjektusk (https://data.gov.lt/datasets/1556/)
