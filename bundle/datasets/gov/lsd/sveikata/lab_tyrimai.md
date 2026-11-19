---
type: Dataset
title: "Laboratorinių tyrimų agreguoti skaičiai"
description: "\"Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai"
tags: [gov, lsd, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4129/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-02-18T00:00:00Z"
---

# Laboratorinių tyrimų agreguoti skaičiai

"Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių. Laboratorinių tyrimų agreguotas skaičius, koduojamų su LOINC ir be LOINC, pateiktas atskirai. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu sveikata@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/lsd/sveikata/lab_tyrimai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4129/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/lab_tyrimai`[^dcat]
- **Portal Title (`@lt`):** Laboratorinių tyrimų agreguoti skaičiai[^dcat]
- **Portal Title (`@en`):** Laboratory aggregated numbers[^dcat]
- **Issued (`dct:issued`):** `2026-02-18`[^dcat]
- **Last Modified (`dct:modified`):** `2026-02-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-02-18` .. `2026-02-18`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių. Laboratorinių tyrimų agreguotas skaičius, koduojamų su LOINC ir be LOINC, pateiktas atskirai. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu sveikata@stat.gov.lt.[^dcat]

### Portal Description (`@en`)

An aggregated number of laboratory tests performed in patients from laboratory sets of VDV IS integrated hospitals and clinics. The aggregated number of laboratory tests encoded with LOINC and without LOINC is presented separately. Please contact atviriduomenys@vssa.lt by e-mail for technical problems with the portal. Please contact sveikata@stat.gov.lt by e-mail for information.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [LaboratorinisTyrimas](lab_tyrimai/LaboratorinisTyrimas.md) | Laboratorinių tyrimų agreguoti skaičiai | `4` | `vda_id` | — | `5` | "Pacientams atliktų laboratorinių tyrimų agreguotas skaičius iš VDV IS integruotų ligoninių ir poliklinikų laboratorinių tyrimų rinkinių. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/lab_tyrimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/lab_tyrimai (https://data.gov.lt/datasets/4129/)
