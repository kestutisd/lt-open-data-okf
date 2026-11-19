---
type: Dataset
title: "Pacientams atliktų laboratorinių tyrimų rezultatai"
description: "Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami LSMULKK laboratorijoje atliktų tyrimų, jų užsakymų ir atsakymų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lsmu/lab_tyrimai"
tags: [gov, lsmu, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/lab_tyrimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsmu/lab_tyrimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3864/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsmu/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pacientams atliktų laboratorinių tyrimų rezultatai

Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMULKK) laboratorijos informacinėje sistemoje (LIS) kaupiami LSMULKK laboratorijoje atliktų tyrimų, jų užsakymų ir atsakymų duomenys. Rinkinyje pateikiama pacientų informacija: pseudonimizuotas asmens kodas, gimimo metai, lytis, tyrimų duomenys – tyrimo grupė, užsakymo laikas, pavadinimas, trumpinys; taip pat tyrimų atsakymai – rezultato reikšmė, tipas, matavimo vienetai, normos ir jų ribos. Duomenyse asmenų gimimo metai „triukšminti“ (gimimo metai nurodomi su +-1 metų paklaida). Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/lsmu/lab_tyrimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsmu/lab_tyrimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/lab_tyrimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsmu/lab_tyrimai` (`deployed`)[^manifest]
- **Provider:** `lsmu` — Lietuvos sveikatos mokslų universitetas *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3864/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsmu/lab_tyrimai`[^dcat]
- **Portal Title (`@lt`):** LSMU Kauno Klinikų laboratorijoje pacientams atliktų laboratorinių tyrimų rezultatai[^dcat]
- **Portal Title (`@en`):** Results of laboratory tests performed in patients in Kaunas Clinics[^dcat]
- **Issued (`dct:issued`):** `2025-07-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-07-07` .. `2025-07-09`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Lietuvos sveikatos mokslų universiteto ligoninės Kauno klinikų (LSMU KK) laboratorijos informacinėje sistemoje (LIS) kaupiami LSMU KK laboratorijoje atliktų tyrimų, jų užsakymų ir atsakymų duomenys. Rinkinyje pateikiama pacientų informacija: pseudonimizuotas asmens kodas, gimimo metai, lytis, tyrimų duomenys – tyrimo grupė, užsakymo laikas, pavadinimas, trumpinys; taip pat tyrimų atsakymai – rezultato reikšmė, tipas, matavimo vienetai, normos ir jų ribos. Duomenyse asmenų gimimo metai „triukšminti“ (gimimo metai nurodomi su +-1 metų paklaida). Duomenų laiko aprėptis nuo 2015 m. rugpjūčio mėn. Duomenų teikėjas – Lietuvos sveikatos mokslų universiteto ligoninė Kauno klinikos Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The information system of the Kaunas Clinical (LSMULKK) Laboratory of the Lithuanian UNIVERSITY of Health Sciences Hospital (LIS) shall accumulate details of the studies carried out in the Laboratory, their orders and answers. The kit contains patient information: pseudonymized personal number, year of birth, gender, test data – study group, order time, title, abbreviation; as well as study responses – result value, type, units of measure, rates and limits. In the data, the year of birth of persons is “noisy” (year of birth is indicated with an error of + -1 years). Data time coverage as of August 2015 Data provider – hospital of the Lithuanian University of Health Sciences Kauno klinikos. Refer to for technical questions or possible errors. atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LaboratorinisTyrimas](lab_tyrimai/LaboratorinisTyrimas.md) | LSMU Kauno Klinikų laboratorijoje pacientams atliktų laboratorinių tyrimų rezultatai | — | `vda_prime_key` | — | `20` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsmu/lab_tyrimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsmu/lab_tyrimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsmu/lab_tyrimai (https://data.gov.lt/datasets/3864/)
