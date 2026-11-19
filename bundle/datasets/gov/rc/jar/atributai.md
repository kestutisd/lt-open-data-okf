---
type: Dataset
title: "Juridinių asmenų registro atributų klasifikatoriai"
description: "Lietuvos Respublikos juridinių asmenų registro atributų klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.) (JAR atributų klasifikatorius; JAR kokybinių atributų klasifikatorius; JAR leistinų atributų klasifikatorius; JAR tekstinių atributų klasifikatorius)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/atributai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1627/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/jar/atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Juridinių asmenų registro atributų klasifikatoriai

Lietuvos Respublikos juridinių asmenų registro atributų klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.) (JAR atributų klasifikatorius; JAR kokybinių atributų klasifikatorius; JAR leistinų atributų klasifikatorius; JAR tekstinių atributų klasifikatorius).[^manifest]

- **Namespace:** `datasets/gov/rc/jar/atributai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/atributai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/atributai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1627/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/jar/atributai`[^dcat]
- **Portal Title (`@lt`):** Juridinių asmenų registro atributų klasifikatoriai[^dcat]
- **Portal Title (`@en`):** JAR attribute classifiers[^dcat]
- **Issued (`dct:issued`):** `2023-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2021-10-27` .. `2026-03-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@en`)

Attribute classifications of the Register of Legal Entities of the Republic of Lithuania (data set group, 4 units in total) (JAR attribute classification; JAR qualitative attribute classification; JAR allowable attribute classification; JAR text attribute classification). The geographical sample of data is the entire territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Atributas](atributai/Atributas.md) | Juridinių asmenų registro atributų klasifikatorius | `4` | `kodas` | — | `6` | — |
| [LeistinasAtributas](atributai/LeistinasAtributas.md) | Juridinių asmenų registro leistinų atributų klasifikatorius pagal teisines formas | `4` | `forma,atributas` | — | `2` | — |
| [TekstinisAtributas](atributai/TekstinisAtributas.md) | Juridinių asmenų registro tekstinių atributų klasifikatorius | `4` | `kodas` | — | `3` | — |
| [AtributoTipas](atributai/AtributoTipas.md) | Juridinių asmenų registro atributų tipų klasifikatorius | `4` | `kodas` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/jar/atributai (https://data.gov.lt/datasets/1627/)
