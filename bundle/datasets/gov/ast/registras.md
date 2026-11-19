---
type: Dataset
title: "Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras"
description: "Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/ast/registras"
tags: [gov, ast, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/konsultacijos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ast/konsultacijos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2768/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ast/registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras

Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys. Rinkinio objektas – įmonės kliento kreipimasis į Alytaus šilumos tinklus. Rinkinyje nurodoma iškvietimo informacija – gatvė, namo numeris ir iškvietimo priežastis. Taip pat pateikiama pagal iškvietimą vykdytų darbų informacija: darbus atlikusio asmens identifikatorius (sudarytas užšifravus atsakingo darbuotojo vardą ir pavardę), darbų trukmė valandos ir minučių tikslumu, pabaigos žyma, identifikuota gedimo priežastis ir bendra darbų trukmė nuo iškvietimo momento iki darbų užbaigimo. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/ast/registras`[^manifest]
- **Manifest CSV:** [datasets/gov/ast/konsultacijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/konsultacijos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ast/registras` (`deployed`)[^manifest]
- **Provider:** `ast` — Alytaus šilumos tinklai *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2768/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ast/registras`[^dcat]
- **Portal Title (`@lt`):** Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registro duomenys[^dcat]
- **Portal Title (`@en`):** Data of Alytus heat network call, complaint and consultation register[^dcat]
- **Issued (`dct:issued`):** `2024-08-30`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2024-08-28` .. `2024-08-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys. Rinkinio objektas – įmonės kliento kreipimasis į Alytaus šilumos tinklus. Rinkinyje nurodoma iškvietimo informacija – gatvė, namo numeris ir iškvietimo priežastis. Taip pat pateikiama pagal iškvietimą vykdytų darbų informacija: darbus atlikusio asmens identifikatorius (sudarytas užšifravus atsakingo darbuotojo vardą ir pavardę), darbų trukmė valandos ir minučių tikslumu, pabaigos žyma, identifikuota gedimo priežastis ir bendra darbų trukmė nuo iškvietimo momento iki darbų užbaigimo. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set contains data from the Alytus heat network customer complaints, consultations and call log accumulated since 2024. The object of the kit is the application of the client of the company to the Alytus heat networks. The collection shall contain the call information: street, house number and reason for the call. Information on the work carried out on the call shall also be provided: the identification of the person who carried out the work (compiled by encrypting the name of the person responsible), the duration of the work to the nearest hour and minute, the end mark, the identified cause of the failure and the total duration of the work from the moment of the call to the completion of the work. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Iskvietimas](registras/Iskvietimas.md) | Alytaus šilumos tinklų iškvietimų, nusiskundimų ir konsultacijų registras | `4` | `vda_id` | — | `11` | Duomenų rininyje pateikiami nuo 2024 m. kaupiami Alytaus šilumos tinklų klientų nusiskundimų, konsultacijų ir iškvietimų žurnalo duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ast/konsultacijos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ast/konsultacijos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ast/registras (https://data.gov.lt/datasets/2768/)
