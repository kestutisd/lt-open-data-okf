---
type: Dataset
title: "Juridinių asmenų registro faktų tipų ir potipių klasifikatoriai"
description: "Lietuvos Respublikos juridinių asmenų registro faktų tipų ir faktų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR faktų tipų klasifikatorius; JAR faktų potipių klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/faktu_tipai_potipiai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1626/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/faktu_tipai_potipiai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Juridinių asmenų registro faktų tipų ir potipių klasifikatoriai

Lietuvos Respublikos juridinių asmenų registro faktų tipų ir faktų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR faktų tipų klasifikatorius; JAR faktų potipių klasifikatorius).[^manifest]

- **Namespace:** `datasets/gov/rc/jar/faktu_tipai_potipiai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/faktu_tipai_potipiai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1626/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/faktu_tipai_potipiai`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų registro faktų tipų ir potipių klasifikatoriai[^dcat]
- **Portal Title (`@en`):** JAR fact type and subtype classifiers[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2021-10-27` .. `2026-03-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Classifications of fact types and fact subtypes in the Register of Legal Entities of the Republic of Lithuania (data set group, 2 units in total) (JAR fact type classification; JAR fact subtype classification). The geographical sample of data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [FaktoTipas](faktu_tipai_potipiai/FaktoTipas.md) | Juridinių asmenų registro faktų tipų klasifikatorius | — | `kodas` | — | `3` | — |
| [FaktoPotipis](faktu_tipai_potipiai/FaktoPotipis.md) | Juridinių asmenų registro faktų potipių klasifikatorius | — | `kodas` | — | `4` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/faktu_tipai_potipiai (https://data.gov.lt/datasets/1626/)
