---
type: Dataset
title: "Pacientų anoniminės apklausos"
description: "Vadovaujantis Lietuvos Respublikos sveikatos apsaugos ministro 2012 m. lapkričio 29 d."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3902/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/apklausos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Pacientų anoniminės apklausos

- **Namespace:** `datasets/gov/lsd/sveikata/apklausos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3902/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/apklausos`[^dcat]
- **Portal Title (`@lt`):** Paciento pasitenkinimo asmens sveikatos priežiūros paslaugomis vertinimo anketų duomenys su atsakymais[^dcat]
- **Portal Title (`@en`):** Patient satisfaction assessment questionnaires with answers[^dcat]
- **Issued (`dct:issued`):** `2025-10-15`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-10-15` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vadovaujantis Lietuvos Respublikos sveikatos apsaugos ministro 2012 m. lapkričio 29 d. įsakymu Nr. V-1073 ,,Dėl asmens sveikatos priežiūros įstaigų, teikiančių stacionarines asmens sveikatos priežiūros paslaugas, veiklos kokybės ir veiklos efektyvumo vertinimo rodiklių sąrašų ir šių rodiklių duomenų suvestinių formų patvirtinimo” ir 2018 m. balandžio 16 d. įsakymu Nr. V-419 „Dėl asmens sveikatos priežiūros įstaigų, teikiančių ambulatorines asmens sveikatos priežiūros paslaugas, veiklos kokybės ir efektyvumo vertinimo rodiklių sąrašo ir šių rodiklių duomenų suvestinių formų patvirtinimo“ gydymo įstaigose vykdomas pacientų pasitenkinimo teikiamomis paslaugomis tyrimas. Rinkinyje pateikiami atsakytų vertinimo anketų duomenys. Anketos apima įvairius klausimus apie suteiktas paslaugas sveikatos priežiūros įstaigoje, įskaitant vertinamos įstaigos pavadinimą, paslaugas suteikusio specialisto kvalifikaciją, suteiktos paslaugos pavadinimą, vizito ir apklausos užpildymo datas, apklausos klausimus bei įvestus atsakymus apie įstaigos pasiekiamumą, tvarkingumą, gydytojo ir slaugytojo darbą, atsiskaitymą iš asmeninių lėšų. Duomenų šaltinis – Išankstinė pacientų registracijos informacinė sistema. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package provides the data for the assessment of the patient's satisfaction with outpatient and inpatient personal health care services. According to Order No V-1073 of 29 November 2012 of the Minister of Health of the Republic of Lithuania on the Approval of the List of Performance and Performance Evaluation Indicators of Individual Health Care Institutions Providing Inpatient Personal Health Care Services and the Summaries of these Indicators, Order No V-419 of 16 April 2018 on the List of Performance and Performance Evaluation Indicators of Indicators Providing Out-patient Health Care hereby conducted in medical institutions.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [StacionaroPacientuApklausa](apklausos/StacionaroPacientuApklausa.md) | Stacionaro pacientų anoniminės apklausos | — | `vda_id` | — | `8` | Anketų, pateiktų pacientams po gydymo stacionare, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais. |
| [AmbulatorijosPacientuApklausa](apklausos/AmbulatorijosPacientuApklausa.md) | Ambulatorijos pacientų anoniminės apklausos | — | `vda_id` | — | `9` | Anketų, pateiktų pacientams po gautų ambulatorinių paslaugų, skirtų įvertinti gautų sveikatos paslaugų kokybę, duomenys su atsakymais. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/apklausos/apklausos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/apklausos (https://data.gov.lt/datasets/3902/)
