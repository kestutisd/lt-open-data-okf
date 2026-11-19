---
type: Dataset
title: "Juridinių asmenų registre įregistruoti paramos gavėjai (pagal išregistruotą statusą „PARAMOS GAVĖJAI“)"
description: "Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, turinčius išregistruotą žymą „PARAMOS GAVĖJAI“ (kodas, pavadinimas, žymos įregistravimo data)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/isregistruoti_paramos_gavejai"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1569/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/isregistruoti_paramos_gavejai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Juridinių asmenų registre įregistruoti paramos gavėjai (pagal išregistruotą statusą „PARAMOS GAVĖJAI“)

Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, turinčius išregistruotą žymą „PARAMOS GAVĖJAI“ (kodas, pavadinimas, žymos įregistravimo data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Namespace:** `datasets/gov/rc/jar/isregistruoti_paramos_gavejai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/isregistruoti_paramos_gavejai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1569/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/isregistruoti_paramos_gavejai`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų registre išregistruoti paramos gavėjai (pagal išregistruotą statusą „PARAMOS GAVĖJAI“)[^dcat]
- **Portal Title (`@en`):** Beneficiaries deregistered in the JAR (according to the deregistered status &quot;BENEFICIARIES&quot;)[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-09-24` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, turinčius išregistruotą žymą „PARAMOS GAVĖJAI“ (kodas, pavadinimas, žymos išregistravimo data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^dcat]

### Portal Description (`@en`)

Data on legal entities registered in the Register of Legal Entities of the Republic of Lithuania with the deregistered tag “BENEFICIARIES” (code, name, date of registration of the tag). The names of individual enterprises, limited partnerships, real partnerships have been depersonalized. The geographical sample of data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IsregistruotasParamosGavejas](isregistruoti_paramos_gavejai/IsregistruotasParamosGavejas.md) | Juridinių asmenų registre įregistruoti paramos gavėjai | `4` | `juridinis_asmuo` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/isregistruoti_paramos_gavejai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/isregistruoti_paramos_gavejai (https://data.gov.lt/datasets/1569/)
