---
type: Dataset
title: "Juridinių asmenų registre įregistruotos nevyriausybinės organizacijos (pagal žymą „NEVYRIAUSYBINĖS ORGANIZACIJOS“)"
description: "Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, turinčius žymą „NEVYRIAUSYBINĖ ORGANIZACIJA“ (kodas, pavadinimas, žymos įregistravimo data)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/iregistruotos_nvo"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruotos_nvo.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/iregistruotos_nvo.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1566/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/iregistruotos_nvo"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Juridinių asmenų registre įregistruotos nevyriausybinės organizacijos (pagal žymą „NEVYRIAUSYBINĖS ORGANIZACIJOS“)

Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, turinčius žymą „NEVYRIAUSYBINĖ ORGANIZACIJA“ (kodas, pavadinimas, žymos įregistravimo data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Namespace:** `datasets/gov/rc/jar/iregistruotos_nvo`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/iregistruotos_nvo.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruotos_nvo.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/iregistruotos_nvo` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1566/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/iregistruotos_nvo`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų registre įregistruotos nevyriausybinės organizacijos (pagal žymą „NEVYRIAUSYBINĖS ORGANIZACIJOS“)[^dcat]
- **Portal Title (`@en`):** JAR registered non-governmental organizations (under the heading &quot;NON-GOVERNMENTAL ORGANIZATIONS&quot;)[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-09-24` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Aprašymas: Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, turinčius žymą „NEVYRIAUSYBINĖ ORGANIZACIJA“ (kodas, pavadinimas, žymos įregistravimo data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^dcat]

### Portal Description (`@en`)

Description: Data on legal entities registered in the Register of Legal Entities of the Republic of Lithuania with the tag “NON-GOVERNMENT ORGANIZATION” (code, name, date of registration of the tag). The names of individual enterprises, limited partnerships, real partnerships have been depersonalized. The geographical sample of data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IregistruotaNVO](iregistruotos_nvo/IregistruotaNVO.md) | Juridinių asmenų registre įregistruotos NVO | `4` | `juridinis_asmuo` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/iregistruotos_nvo.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruotos_nvo.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/iregistruotos_nvo (https://data.gov.lt/datasets/1566/)
