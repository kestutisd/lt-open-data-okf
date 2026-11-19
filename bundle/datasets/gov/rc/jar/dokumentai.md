---
type: Dataset
title: "Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentų, pateiktų registro tvarkytojui, duomenys (raw data)"
description: "Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų registro tvarkytojui pateiktus dokumentus (kodas, pavadinimas, dokumentų rūšis, dokumentų data, įregistravimo data)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/dokumentai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/dokumentai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1565/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/dokumentai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentų, pateiktų registro tvarkytojui, duomenys (raw data)

Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų registro tvarkytojui pateiktus dokumentus (kodas, pavadinimas, dokumentų rūšis, dokumentų data, įregistravimo data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Namespace:** `datasets/gov/rc/jar/dokumentai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/dokumentai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/dokumentai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1565/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/dokumentai`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentų, pateiktų registro tvarkytojui, duomenys (RAW data)[^dcat]
- **Portal Title (`@en`):** Documents of legal entities registered in the Register of Legal Entities submitted to the Registrar (RAW date)[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2021-09-24` .. `2026-03-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų registro tvarkytojui pateiktus steigimo dokumentus (kodas, pavadinimas, dokumentų rūšis, dokumentų data, įregistravimo data). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^dcat]

### Portal Description (`@en`)

Data on the documents submitted to the manager of the register of legal persons registered in the Register of Legal Entities of the Republic of Lithuania (code, name, type of documents, date of documents, date of registration). The names of individual enterprises, limited partnerships, real partnerships have been depersonalized. The geographical sample of data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](dokumentai/Dokumentas.md) | Juridinių asmenų registre įregistruotų juridinių asmenų steigimo dokumentai | `4` | `juridinis_asmuo` | — | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/dokumentai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/dokumentai (https://data.gov.lt/datasets/1565/)
