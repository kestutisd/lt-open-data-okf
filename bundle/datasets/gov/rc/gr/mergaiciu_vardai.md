---
type: Dataset
title: "Populiariausi mergaičių vardai Lietuvoje, TOP 20 (mergaitės vardas, gimimo metai, bendravardžių kiekis)"
description: "Gyventojų registro (GR) statistiniai duomenys."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/mergaiciu_vardai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/mergaiciu_vardai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/mergaiciu_vardai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1751/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/gr/mergaiciu_vardai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Populiariausi mergaičių vardai Lietuvoje, TOP 20 (mergaitės vardas, gimimo metai, bendravardžių kiekis)

- **Namespace:** `datasets/gov/rc/gr/mergaiciu_vardai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/gr/mergaiciu_vardai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/mergaiciu_vardai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/mergaiciu_vardai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1751/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/gr/mergaiciu_vardai`[^dcat]
- **Portal Title (`@lt`):** Populiariausi mergaičių vardai Lietuvoje, TOP 20 (mergaitės vardas, gimimo metai, bendravardžių kiekis)[^dcat]
- **Portal Title (`@en`):** The most popular names of girls in Lithuania, TOP 20 (girl&#39;s name, year of birth, number of names)[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-01-20` .. `2025-09-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Gyventojų registro (GR) statistiniai duomenys. Populiariausi mergaičių vardai Lietuvoje, TOP 20, t. y. mergaitės vardas, gimimo metai, bendravardžių kiekis.[^dcat]

### Portal Description (`@en`)

Population Register (GR) statistics. The most popular names of girls in Lithuania, TOP 20, ie girl&#39;s name, year of birth, number of names. Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MergaitesVardas](mergaiciu_vardai/MergaitesVardas.md) | Populiariausi mergaičių vardai Lietuvoje, TOP 20 (mergaitės vardas, gimimo metai, bendravardžių kiekis) | `4` | `gimimo_metai, gimimo_ketvirtis, nr` | — | `5` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/mergaiciu_vardai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/mergaiciu_vardai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/gr/mergaiciu_vardai (https://data.gov.lt/datasets/1751/)
