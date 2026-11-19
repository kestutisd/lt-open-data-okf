---
type: Dataset
title: "Politinių organizacijų narių duomenys apie lytį, amžių, pilietybę, geografinę padėtį ir narystę"
description: "Politinių partijų narių sąrašų informacinės sistemos (PPNSIS) duomenys apie Lietuvos Respublikoje veikiančių politinių organizacijų narių lytį, amžių, pilietybę, geografinę padėtį ir narystę."
resource: "https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariai"
tags: [gov, rc, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1736/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/nariai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Politinių organizacijų narių duomenys apie lytį, amžių, pilietybę, geografinę padėtį ir narystę

- **Namespace:** `datasets/gov/rc/ppnsis/nariai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ppnsis/nariai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1736/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ppnsis/nariai/Narys`[^dcat]
- **Portal Title (`@lt`):** Politinių organizacijų narių duomenys apie lytį, amžių, pilietybę, geografinę padėtį ir narystę[^dcat]
- **Portal Title (`@en`):** Data on members of political parties on gender, age, citizenship, geographical location and membership[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2021-12-15` .. `2023-07-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Politinių partijų narių sąrašų informacinės sistemos (PPNSIS) duomenys apie Lietuvos Respublikoje veikiančių politinių organizacijų narių lytį, amžių, pilietybę, geografinę padėtį ir narystę.[^dcat]

### Portal Description (`@en`)

Data on the Information System of Lists of Members of Political Parties (PPNSIS) on the gender, age, citizenship, geographical location and membership of members of political parties operating in the Republic of Lithuania. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Narys](nariai/Narys.md) | PPNSIS duomenys apie politinių organizacijų narius | `3` | `nr, politine_organizacija` | — | `8` | Politinių partijų narių sąrašų informacinės sistemos duomenys apie Lietuvos Respublikos veikiančių politinių organizcijų narius - jų lytį, amžių, pilietybę... |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ppnsis/nariai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ppnsis/nariai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ppnsis/nariai (https://data.gov.lt/datasets/1736/)
