---
type: Dataset
title: "Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys"
description: "Vyriausybės strateginio projektų portfelio duomenų rinkinyje pateikiami duomenys apie įgyvendinamus ir baigtus įgyvendinti Vyriausybės strateginius projektus."
resource: "https://get.data.gov.lt/datasets/gov/lrvk/portfeliai"
tags: [gov, lrvk, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1550/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrvk/portfeliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys

Vyriausybės strateginio projektų portfelio duomenų rinkinyje pateikiami duomenys apie įgyvendinamus ir baigtus įgyvendinti Vyriausybės strateginius projektus. Atskirai pateikiami duomenys apie projektus, jų teikiamas naudas ir pasiektus rezultatus. Duomenys apima laikotarpį nuo 2011 m. iki šių dienų. Duomenų teikėjas: Lietuvos Respublikos Vyriausybės Kanceliarija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Namespace:** `datasets/gov/lrvk/portfeliai`[^manifest]
- **Manifest CSV:** [datasets/gov/lrvk/portfeliai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrvk/portfeliai` (`deployed`)[^manifest]
- **Provider:** `lrvk` — Lietuvos Respublikos Vyriausybės Kanceliarija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1550/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lrvk/portfeliai`[^dcat]
- **Portal Title (`@lt`):** Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys[^dcat]
- **Portal Title (`@en`):** Monitoring data of the Prime Minister&#39;s portfolio and projects[^dcat]
- **Issued (`dct:issued`):** `2024-08-29`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2024-08-13` .. `2025-10-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Vyriausybės strateginio projektų portfelio duomenų rinkinyje pateikiami duomenys apie įgyvendinamus ir baigtus įgyvendinti Vyriausybės strateginius projektus. Atskirai pateikiami duomenys apie projektus, jų teikiamas naudas ir pasiektus rezultatus. Duomenys apima laikotarpį nuo 2011 m. iki šių dienų. Duomenų teikėjas – Lietuvos Respublikos Vyriausybės Kanceliarija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Source: Portfolio and Project Information System. Information is provided on the projects funded by the Prime Minister&#39;s Portfolio and the Government Chancellery with EU funding. Project data: project name, duration, start date, end date, short project description, program if the project is included in the program, project phase (initiation, planning, implementation and monitoring, completion, benefit assessment), project goal (s), strategic purpose. Project budget data: planned budget according to the selected object (project, program or portfolio), source of financing according to the selected object (project, program or portfolio). Project risk data: risk, type of risk, description, consequences, risk management measures. Project benefit data: name of the benefit, description, target value of the benefit indicator, unit of measurement of the target value of the indicator. Aimed results of the project: name of the result, description, description of the requirements of the results. Data are updated quarterly.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Projektas](portfeliai/Projektas.md) | Lietuvos Respublikos Vyriausybės strateginio projektų portfelio valdymo duomenys | `4` | `vda_id` | — | `14` | Lentelės objektas - vienas vykdomas ar baigtas vykdyti projektas. |
| [Nauda](portfeliai/Nauda.md) | Lietuvos Respublikos Vyriausybės strateginio projektų portfelio teikiamų naudų duomenys | `4` | `naudos_id` | — | `12` | Lentelės objektas - projekto teikiama nauda. |
| [Rezultatas](portfeliai/Rezultatas.md) | Lietuvos Respublikos Vyriausybės strateginio projektų portfelio rezultatai | `4` | `vda_id` | — | `12` | Lentelės objektas - projekto rezultatas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrvk/portfeliai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrvk/portfeliai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrvk/portfeliai (https://data.gov.lt/datasets/1550/)
