---
type: Dataset
title: "VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys"
description: "Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/projektai"
tags: [gov, cpva, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_projektai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_projektai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3839/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/ignalinos_programos/projektai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys

Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu. Duomenys pateikiami iš Projektų valdymo informacinės sistemos „Medici“, skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su Ignalinos programos projektais. Rinkinį sudaro 1 lentelė, kurioje pateikiamas užbaigtų projektų sąrašas. Rinkinyje galima rasti tokią informaciją kaip projektą vykdžiusi įstaiga, projekto pavadinimas, projekto tikslas, finansavimo būdai ir pan. Duomenų atnaujinimas numatomas kas 3 mėn. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/cpva/ignalinos_programos/projektai`[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_projektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_projektai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/projektai` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3839/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/projektai`[^dcat]
- **Portal Title (`@lt`):** VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos užbaigtų projektų ir dotacijų duomenys[^dcat]
- **Portal Title (`@en`):** Data on projects and grants completed by the Ignalina Programme administered by the Central Project Management Agency of the Public Projects Agency[^dcat]
- **Issued (`dct:issued`):** `2025-05-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2025-05-15` .. `2026-09-12`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų ir dotacijų įgyvendinimu. Duomenys pateikiami iš Projektų valdymo informacinės sistemos „Medici“, skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su Ignalinos programos projektais ir dotacijomis. Rinkinį sudaro 1 lentelė, kurioje pateikiamas užbaigtų projektų ir dotacijų sąrašas. Rinkinyje galima rasti tokią informaciją kaip projektą / dotaciją įgyvendinusi įstaiga, projekto / dotacijos pavadinimas, projekto / dotacijos tikslas, finansavimo būdai ir pan. Duomenų atnaujinimas numatomas kas 3 mėn. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall include data relating to the implementation of projects and grants of the Ignalina Programme administered by the Central Project Management Agency of the Public Projects Agency. The data are provided from the Project Management Information System Medici for the collection, processing and storage of statistical and financial data related to projects and grants of the Ignalina Programme. The package consists of Table 1, which provides a list of completed projects and grants. The package contains information such as the body implementing the project/grant, the name of the project/grant, the purpose of the project/grant, the methods of financing, etc. Data updates are expected every 3 months. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Projektas](projektai/Projektas.md) | VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Medici“ projektų sąrašas | `4` | `id` | — | `13` | Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_projektai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_projektai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/ignalinos_programos/projektai (https://data.gov.lt/datasets/3839/)
