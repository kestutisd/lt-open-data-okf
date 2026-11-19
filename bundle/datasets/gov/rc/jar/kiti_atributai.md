---
type: Dataset
title: "Kiti juridinių asmenų registro atributų klasifikatoriai"
description: "Lietuvos Respublikos juridinių asmenų registro išregistravimo priežasčių ir naudojamų pareigų klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.)"
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/kiti_atributai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/kiti_atributai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/kiti_atributai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1628/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/kiti_atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Kiti juridinių asmenų registro atributų klasifikatoriai

Lietuvos Respublikos juridinių asmenų registro išregistravimo priežasčių ir naudojamų pareigų klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.)[^manifest]

- **Namespace:** `datasets/gov/rc/jar/kiti_atributai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/kiti_atributai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/kiti_atributai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/kiti_atributai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1628/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/kiti_atributai`[^dcat]
- **Portal Title (`@lt`):** Kiti Juridinių asmenų registro atributų klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Other classifications of JAR attributes[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2021-10-27` .. `2026-03-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos juridinių asmenų registro išregistravimo priežasčių ir naudojamų pareigų klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) ( JAR pareigų klasifikatorius; JAR išregistravimo priežasčių klasifikatorius).[^dcat]

### Portal Description (`@en`)

Classifiers of reasons for deregistration of the Register of Legal Entities of the Republic of Lithuania and duties used (group of data sets, 2 units in total) (JAR duty classifier; JAR classifier of reasons for deregistration). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IsregistravimoPriezastis](kiti_atributai/IsregistravimoPriezastis.md) | Juridinių asmenų registro išregistravimo priežasčių klasifikatorius | `4` | `kodas` | — | `3` | — |
| [Pareigos](kiti_atributai/Pareigos.md) | Juridinių asmenų registro pareigų klasifikatorius | `4` | `kodas` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/kiti_atributai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/kiti_atributai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/kiti_atributai (https://data.gov.lt/datasets/1628/)
