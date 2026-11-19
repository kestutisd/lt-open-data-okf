---
type: Dataset
title: "Juridinių asmenų registre įregistruotų juridinių asmenų buveinių (adresų) duomenys (raw data)"
description: "Įregistruotų juridinių asmenų buveinių (adresų) duomenų rinkinys iš Lietuvos Respublikos juridinių asmenų registro (juridinius asmenis apibūdinantys duomenys (kodas, pavadinimas, adreso identifikatorius iš Adresų registro, adresas)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/buveines"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/buveines.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/buveines.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1562/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/buveines"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Juridinių asmenų registre įregistruotų juridinių asmenų buveinių (adresų) duomenys (raw data)

Įregistruotų juridinių asmenų buveinių (adresų) duomenų rinkinys iš Lietuvos Respublikos juridinių asmenų registro (juridinius asmenis apibūdinantys duomenys (kodas, pavadinimas, adreso identifikatorius iš Adresų registro, adresas). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Namespace:** `datasets/gov/rc/jar/buveines`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/buveines.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/buveines.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/buveines` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1562/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/buveines`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų registre įregistruotų juridinių asmenų buveinių (adresų) duomenys (RAW data)[^dcat]
- **Portal Title (`@en`):** Data on registered offices (addresses) of legal persons registered in the Register of Legal Entities (RAW date)[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-09-24` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Data set of registered offices (addresses) of registered legal entities from the Register of Legal Entities of the Republic of Lithuania (data describing legal entities (code, name, address identifier from the Register of Addresses, address). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Buveine](buveines/Buveine.md) | — | `4` | `juridinis_asmuo` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/buveines.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/buveines.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/buveines (https://data.gov.lt/datasets/1562/)
