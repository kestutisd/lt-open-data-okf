---
type: Dataset
title: "Finansinės atskaitomybės dokumentų nepateikusios įmonės"
description: "Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, nevykdančius prievolės teikti registro tvarkytojui finansinės atskaitomybės dokumentus (kodas, pavadinimas, juridinio asmens forma, įregistravimo data, reikšmė,"
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/fa_dokumentu_nepateike"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1571/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/fa_dokumentu_nepateike"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Finansinės atskaitomybės dokumentų nepateikusios įmonės

Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, nevykdančius prievolės teikti registro tvarkytojui finansinės atskaitomybės dokumentus (kodas, pavadinimas, juridinio asmens forma, įregistravimo data, reikšmė,[^manifest]

- **Namespace:** `datasets/gov/rc/jar/fa_dokumentu_nepateike`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_dokumentu_nepateike` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1571/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/fa_dokumentu_nepateike`[^dcat]
- **Portal Title (`@lt`):** Finansinės atskaitomybės dokumentų nepateikusios įmonės[^dcat]
- **Portal Title (`@en`):** Companies that have not submitted financial statements[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-11-08` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie Lietuvos Respublikos juridinių asmenų registre įregistruotus juridinius asmenis, nevykdančius prievolės teikti registro tvarkytojui finansinės atskaitomybės dokumentus (kodas, pavadinimas, juridinio asmens forma, įregistravimo data, reikšmė, valiuta). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^dcat]

### Portal Description (`@en`)

Data on legal entities registered in the Register of Legal Entities of the Republic of Lithuania that do not fulfill the obligation to submit financial reporting documents to the register manager (code, name, legal entity form, date of registration, meaning, currency). The names of individual enterprises, limited partnerships, real partnerships have been depersonalized. The geographical sample of data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Nepateikes](fa_dokumentu_nepateike/Nepateikes.md) | Juridinių asmenų registre įregistruoti juridiniai asmenys | `4` | `juridinis_asmuo` | `open` | `5` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/fa_dokumentu_nepateike.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/fa_dokumentu_nepateike (https://data.gov.lt/datasets/1571/)
