---
type: Dataset
title: "Juridinių asmenų registro dokumentų klasifikatoriai"
description: "Lietuvos Respublikos juridinių asmenų registro dokumentų tipų ir dokumentų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR dokumentų tipų klasifikatorius; JAR dokumentų potipių klasifikatorius)"
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/dokumentu_tipai_potipiai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1625/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/dokumentu_tipai_potipiai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Juridinių asmenų registro dokumentų klasifikatoriai

Lietuvos Respublikos juridinių asmenų registro dokumentų tipų ir dokumentų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR dokumentų tipų klasifikatorius; JAR dokumentų potipių klasifikatorius)[^manifest]

- **Namespace:** `datasets/gov/rc/jar/dokumentu_tipai_potipiai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/dokumentu_tipai_potipiai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1625/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/dokumentu_tipai_potipiai`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų registro dokumentų klasifikatoriai[^dcat]
- **Portal Title (`@en`):** Classifications of JAR documents[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2021-10-27` .. `2026-03-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos Respublikos juridinių asmenų registro dokumentų tipų ir dokumentų potipių klasifikatoriai (duomenų rinkinių grupė, viso 2 vnt.) (JAR dokumentų tipų klasifikatorius; JAR dokumentų potipių klasifikatorius).[^dcat]

### Portal Description (`@en`)

Classifiers of document types and document subtypes of the Register of Legal Entities of the Republic of Lithuania (group of data sets, total 2 units) (JAR document type classifier; JAR document subtype classifier). The geographical sample of the data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [DokumentoTipas](dokumentu_tipai_potipiai/DokumentoTipas.md) | Juridinių asmenų registro dokumentų tipų klasifikatorius | `4` | `kodas` | — | `3` | — |
| [DokumentoPotipis](dokumentu_tipai_potipiai/DokumentoPotipis.md) | Juridinių asmenų registro dokumentų potipių klasifikatorius | `4` | `kodas` | — | `4` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/dokumentu_tipai_potipiai (https://data.gov.lt/datasets/1625/)
