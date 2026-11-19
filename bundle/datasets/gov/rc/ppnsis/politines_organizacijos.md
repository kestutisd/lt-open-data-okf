---
type: Dataset
title: "Lietuvos Respublikos politinių organizacijų duomenys"
description: "Politinių partijų narių sąrašų informacinės sistemos (PPNSIS) duomenys apie Lietuvos Respublikoje veikiančias ar veikusias politines organizacijas."
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/politines_organizacijos"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/politines_organizacijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/politines_organizacijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1735/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/politines_organizacijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Lietuvos Respublikos politinių organizacijų duomenys

- **Namespace:** `datasets/gov/rc/ppnsis/politines_organizacijos`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ppnsis/politines_organizacijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/politines_organizacijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/politines_organizacijos` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1735/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/politines_organizacijos/PolitineOrganizacija`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos politinių organizacijų duomenys[^dcat]
- **Portal Title (`@en`):** Data of political parties of the Republic of Lithuania[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-12-15` .. `2023-07-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Politinių partijų narių sąrašų informacinės sistemos (PPNSIS) duomenys apie Lietuvos Respublikoje veikiančias ar veikusias politines organizacijas.[^dcat]

### Portal Description (`@en`)

Data of the Information System of Lists of Members of Political Parties (PPNSIS) on political parties operating or having operated in the Republic of Lithuania. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PolitineOrganizacija](politines_organizacijos/PolitineOrganizacija.md) | PPNSIS duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas | `4` | `juridinis_asmuo` | — | `5` | Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikoje veikiančias politines organizacijas |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/politines_organizacijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/politines_organizacijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/politines_organizacijos (https://data.gov.lt/datasets/1735/)
