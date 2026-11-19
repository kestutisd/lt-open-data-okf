---
type: Dataset
title: "Savivaldybių kapinių duomenys"
description: "Rinkinyje pateikiama Lietuvos savivaldybių kapinių bendro pobūdžio informacija, atvaizduojama kapinių skaitmeninimo ir duomenų valdymo sistemose „CEMETY“ ir „LIKSGIS“: kapinių pavadinimas, adresas, savivaldybė, kontaktiniai duomenys ir kt."
resource: "https://get.data.gov.lt/datasets/gov/kapines"
tags: [gov, kapines, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/informacija.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kapines/informacija.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2778/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kapines"
    author: "team:vda"
    last_modified: "2026-02-20T00:00:00Z"
---

# Savivaldybių kapinių duomenys

Rinkinyje pateikiama Lietuvos savivaldybių kapinių bendro pobūdžio informacija, atvaizduojama kapinių skaitmeninimo ir duomenų valdymo sistemose „CEMETY“ ir „LIKSGIS“: kapinių pavadinimas, adresas, savivaldybė, kontaktiniai duomenys ir kt. Rinkinio objektas – įrašas apie vienerias kapines. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/kapines`[^manifest]
- **Manifest CSV:** [datasets/gov/kapines/informacija.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/informacija.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kapines` (`deployed`)[^manifest]
- **Provider:** `kapines`[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2778/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kapines`[^dcat]
- **Portal Title (`@lt`):** Savivaldybių kapinių duomenys[^dcat]
- **Portal Title (`@en`):** Municipal cemetery data[^dcat]
- **Issued (`dct:issued`):** `2024-09-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-02-20`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-09-06` .. `2026-09-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiama Lietuvos savivaldybių kapinių bendro pobūdžio informacija, atvaizduojama kapinių skaitmeninimo ir duomenų valdymo sistemose „CEMETY“ ir "LIKSGIS": kapinių pavadinimas, adresas, savivaldybė, kontaktiniai duomenys ir kt. Rinkinio objektas – įrašas apie vienerias kapines. Duomenų teikėjas – Savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains general information of the Lithuanian municipal cemetery, depicted in the CEMETERY digitisation and data management system “CEMETY”: cemetery name, address, municipality, contact details, etc. The object of the kit is a record of one cemetery. This collection will be common to all municipalities of Lithuania which have a Register of Delivery and Cemetery, i.e. when the data is received this collection will be filled in with data from each municipality.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Teritorija](kapines/Teritorija.md) | Savivaldybių kapinių duomenys | `4` | `vda_id` | — | `21` | Rinkinyje pateikiama Lietuvos savivaldybių kapinių bendro pobūdžio informacija, atvaizduojama kapinių skaitmeninimo ir duomenų valdymo sistemose „CEMETY“ ir... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kapines/informacija.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/informacija.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kapines (https://data.gov.lt/datasets/2778/)
