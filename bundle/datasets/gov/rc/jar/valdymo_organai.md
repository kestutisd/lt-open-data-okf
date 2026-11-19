---
type: Dataset
title: "Juridinių asmenų registre įregistruotų juridinių asmenų valdymo organai, jų formos (raw data)"
description: "Duomenys, apibūdinantys Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų valdymo organus ir jų formas (juridinius asmenis apibūdinantys duomenys (kodas, valdymo organai)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/valdymo_organai"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/valdymo_organai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/valdymo_organai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1564/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/valdymo_organai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Juridinių asmenų registre įregistruotų juridinių asmenų valdymo organai, jų formos (raw data)

Duomenys, apibūdinantys Lietuvos Respublikos juridinių asmenų registre įregistruotų juridinių asmenų valdymo organus ir jų formas (juridinius asmenis apibūdinantys duomenys (kodas, valdymo organai). Individualių įmonių, komanditinių ūkinių bendrijų, tikrųjų ūkinių bendrijų pavadinimai nuasmeninti.[^manifest]

- **Namespace:** `datasets/gov/rc/jar/valdymo_organai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/valdymo_organai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/valdymo_organai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/valdymo_organai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1564/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/valdymo_organai`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų registre įregistruotų juridinių asmenų valdymo organai, jų formos (RAW data)[^dcat]
- **Portal Title (`@en`):** Management bodies of legal entities registered in the Register of Legal Entities, their forms (RAW date)[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-01-05`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-09-24` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Data describing the management bodies of legal entities registered in the Register of Legal Entities of the Republic of Lithuania and their forms (data describing legal entities), names of individual enterprises, limited partnerships, real partnerships depersonalized. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ValdymoOrganas](valdymo_organai/ValdymoOrganas.md) | Juridinių asmenų valdymo organai | `4` | `juridinis_asmuo` | — | `9` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/valdymo_organai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/valdymo_organai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/valdymo_organai (https://data.gov.lt/datasets/1564/)
