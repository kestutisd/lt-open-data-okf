---
type: Dataset
title: "Duomenys apie politinių organizacijų narių skaičių"
description: "Politinių partijų narių sąrašų informacinės sistemos duomenys (PPNSIS) apie Lietuvos Respublikoje veikiančių ir/ ar veikusių politinių organizacijų narių skaičių (agreguoti duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariu_skaicius"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariu_skaicius.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariu_skaicius.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1737/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/nariu_skaicius"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie politinių organizacijų narių skaičių

- **Namespace:** `datasets/gov/rc/ppnsis/nariu_skaicius`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ppnsis/nariu_skaicius.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariu_skaicius.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariu_skaicius` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1737/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariu_skaicius/NariuSkaicius`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie politinių organizacijų narių skaičių[^dcat]
- **Portal Title (`@en`):** Data on the number of members of political parties[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-12-15` .. `2023-07-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Politinių partijų narių sąrašų informacinės sistemos duomenys (PPNSIS) apie Lietuvos Respublikoje veikiančių ir/ ar veikusių politinių organizacijų narių skaičių (agreguoti duomenys).[^dcat]

### Portal Description (`@en`)

Data of the Information System of Lists of Members of Political Parties (PPNSIS) on the number of members of political parties operating and / or operating in the Republic of Lithuania (aggregated data). Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NariuSkaicius](nariu_skaicius/NariuSkaicius.md) | PPNSIS duomenys apie politinių organizacijų narių skaičių | `4` | `politine_organizacija` | — | `3` | Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizacijų narių skaičių |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariu_skaicius.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariu_skaicius.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/nariu_skaicius (https://data.gov.lt/datasets/1737/)
