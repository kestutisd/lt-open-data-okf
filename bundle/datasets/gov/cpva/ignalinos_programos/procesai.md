---
type: Dataset
title: "VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys"
description: "Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai"
tags: [gov, cpva, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3838/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/ignalinos_programos/procesai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų duomenys

Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų įgyvendinimu. Duomenys pateikiami iš Projektų valdymo informacinės sistemos „Apecs“, skirtos automatizuotai valdyti Ignalinos programos procesus ir kontrolės sistemą. Procesai suskirstyti į 3 kategorijas – procesus, subprocesus ir mikroprocesus, kurie ir pateikiami rinkinio atskirose 3-se lentelėse. „Procesas“ yra pati stambiausia procesų hierarchijos dalis. Jam priklauso subprocesai, o savo ruožtu, subprocesams priklauso mikroprocesai. Lentelės tarpusavyje jungiasi: mikroprocesai su subprocesais – mikroprocesai.priklauso_subprocesui = subprocesai.id; subrocesai su procesais – subprocesai.priklauso_procesui = procesai.id Duomenų atnaujinimas numatomas kas 3 mėn. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/cpva/ignalinos_programos/procesai`[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/ignalinos_programu_procesai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3838/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/cpva/ignalinos_programos/procesai`[^dcat]
- **Portal Title (`@lt`):** VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos projektų ir dotacijų administravimo CPVA procesai[^dcat]
- **Portal Title (`@en`):** CPVA processes for project and grant administration of the Ignalina Programme administered by the Central Project Management Agency of the Public Projects Agency[^dcat]
- **Issued (`dct:issued`):** `2025-05-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2025-05-15` .. `2026-09-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami duomenys, susiję su VšĮ Centrinės projektų valdymo agentūros administruojamų Ignalinos programos projektų ir dotacijų įgyvendinimu. Duomenys pateikiami iš Projektų valdymo informacinės sistemos „Apecs“, skirtos automatizuotai valdyti Ignalinos programos procesus ir kontrolės sistemą. Procesai suskirstyti į 3 kategorijas – procesus, subprocesus ir mikroprocesus, kurie ir pateikiami rinkinio atskirose 3-se lentelėse. „Procesas“ yra pati stambiausia procesų hierarchijos dalis. Jam priklauso subprocesai, o savo ruožtu, subprocesams priklauso mikroprocesai. Lentelės tarpusavyje jungiasi: mikroprocesai su subprocesais – mikroprocesai.priklauso_subprocesui = subprocesai.id; subrocesai su procesais – subprocesai.priklauso_procesui = procesai.id Duomenų atnaujinimas numatomas kas 3 mėn. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set shall include data relating to the implementation of projects and grants of the Ignalina Programme administered by the Central Project Management Agency of the Public Projects Agency. Data are provided from the Project Management Information System “Apecs” for automated management of the Ignalina Programme processes and control system. Processes are divided into 3 categories: processes, sub-processes and micro-processes, which are presented in the set's separate tables 3. 'Process” is the largest part of the process hierarchy. It owns subprocesses, and in turn, subprocesses include microprocesses. Tables connect with each other: microprocesses with subprocesss—microprocesss_belonging to the subprocess = subprocesai.id; subroces/processs/subprocessings_Process = procesai.id Data updates are expected every 3 months. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Procesas](procesai/Procesas.md) | VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ procesų sąrašas | `4` | `id` | — | `6` | — |
| [Subprocesas](procesai/Subprocesas.md) | VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ subprocesų sąrašas | `4` | `id` | — | `8` | — |
| [Mikroprocesas](procesai/Mikroprocesas.md) | VšĮ Centrinės projektų valdymo agentūros administruojamos Ignalinos programos informacinės sistemos „Apecs“ mikroprocesų sąrašas | `4` | `id` | — | `9` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/ignalinos_programu_procesai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/ignalinos_programu_procesai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/ignalinos_programos/procesai (https://data.gov.lt/datasets/3838/)
