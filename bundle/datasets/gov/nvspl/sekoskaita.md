---
type: Dataset
title: "SARS-CoV-2 viruso sekoskaitos duomenys"
description: "\"Duomenų rinkinys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 atliktus testų ir sekoskaitos rezultatus."
resource: "https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita"
tags: [gov, nvspl, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3899/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nvspl/sekoskaita"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SARS-CoV-2 viruso sekoskaitos duomenys

"Duomenų rinkinys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 atliktus testų ir sekoskaitos rezultatus. Duomenų rinkinį sudaro trys lentelės: 1. Žmonėms atlikti SARS-CoV-2 PGR ir antigeno testai, 2. SARS-CoV-2 sekoskaitos Nextclade rezultatų ataskaita, 3. SARS-CoV-2 sekoskaitos Pangolin rezultatų ataskaita. Duomenų teikėjas – Nacionalinė visuomenės sveikatos priežiūros laboratorija. Duomenys kaupiami nuo 2022 m. lapkričio 1 d. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/nvspl/sekoskaita`[^manifest]
- **Manifest CSV:** [datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita` (`deployed`)[^manifest]
- **Provider:** `nvspl` — Nacionalinė visuomenės sveikatos priežiūros laboratorija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3899/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nvspl/sekoskaita`[^dcat]
- **Portal Title (`@lt`):** SARS-CoV-2 viruso sekoskaitos duomenys[^dcat]
- **Portal Title (`@en`):** Sars-cov-2 virus sequencing data[^dcat]
- **Issued (`dct:issued`):** `2025-09-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2025-09-23` .. `2026-05-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinys iš Nacionalinės visuomenės sveikatos laboratorijos, sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 atliktus testų ir sekoskaitos rezultatus. Duomenų rinkinį sudaro trys lentelės: 1. Žmonėms atlikti SARS-CoV-2 PGR ir antigeno testai; 2. SARS-CoV-2 sekoskaitos Nextclade rezultatų ataskaita; 3. SARS-CoV-2 sekoskaitos Pangolin rezultatų ataskaita. Duomenų teikėjas – Nacionalinė visuomenės sveikatos priežiūros laboratorija. Duomenys kaupiami nuo 2022 m. lapkričio 1 d. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

A dataset from the National Public Health Laboratory, a database of tracing studies on the results of tests and sequencing carried out by SARS-CoV-2. The dataset consists of three tables: 1. SARS-CoV-2 PCR and antigen tests have been performed in humans; 2. Sars-cov-2 report on the results of the Nextclade sequencing; 3. Sars-cov-2 report on the results of the Pangolin sequencing. Data provider means the National Public Health Care Laboratory. Data shall be collected from 1 November 2022.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SARSCoVTestas](sekoskaita/SARSCoVTestas.md) | Žmonėms atlikti SARS-CoV-2 PGR ir antigeno testai | `4` | `iraso_id` | — | `9` | "Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie žmonėms atliktus SARS-CoV-2 polimerazinės... |
| [NextcladeAtaskaita](sekoskaita/NextcladeAtaskaita.md) | SARS-CoV-2 sekoskaitos Nextclade rezultatų ataskaita | `4` | `meg_id` | — | `97` | "Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 viruso atliktos sekoskaitos rezultatus. |
| [PangolinAtaskaita](sekoskaita/PangolinAtaskaita.md) | SARS-CoV-2 sekoskaitos Pangolin rezultatų ataskaita | `4` | `meg_id` | — | `15` | "Duomenys iš Nacionalinės visuomenės sveikatos priežiūros laboratorijos sekoskaitos tyrimų duomenų bazės apie SARS-CoV-2 viruso atliktos sekoskaitos rezultatus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvspl/sars_cov_sekoskaitos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nvspl/sekoskaita (https://data.gov.lt/datasets/3899/)
