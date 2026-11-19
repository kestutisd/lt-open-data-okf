---
type: Dataset
title: "Viešųjų pirkimų ataskaitų duomenys"
description: "Rinkinyje pateikiami Viešųjų pirkimų tarnybos Pirkimo procedūrų (ATN1) ir Papildomos viešojo pirkimo ir pirkimo procedūrų (ATN2) ataskaitų duomenys nuo 2017m."
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/ataskaitos"
tags: [gov, lsd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/ataskaitos.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/ataskaitos.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2858/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/ataskaitos"
    author: "team:vda"
    last_modified: "2026-06-12T00:00:00Z"
---

# Viešųjų pirkimų ataskaitų duomenys

Rinkinyje pateikiami Viešųjų pirkimų tarnybos Pirkimo procedūrų (ATN1) ir Papildomos viešojo pirkimo ir pirkimo procedūrų (ATN2) ataskaitų duomenys nuo 2017m. iki šių dienų. Rinkinio objektas - paskelbta ataskaita. Pateikiama detali informacija apie ataskaitą, viešajame pirkime dalyvavusią perkančiąją arba įgaliotąją organizacijas, pirkimo objektą bei vykdytą pirkimą. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/lsd/vpt/ataskaitos`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/vpt/ataskaitos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/ataskaitos.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/ataskaitos` (`deployed`)[^manifest]
- **Provider:** `lsd` — Viešųjų pirkimų tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2858/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lsd/vpt/ataskaitos`[^dcat]
- **Portal Title (`@lt`):** Viešųjų pirkimų ataskaitų duomenys[^dcat]
- **Portal Title (`@en`):** Procurement reports of the Public Procurement Office[^dcat]
- **Issued (`dct:issued`):** `2024-11-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-06-12`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-11-15` .. `2025-10-21`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Viešųjų pirkimų tarnybos Pirkimo procedūrų (ATN1) ir Papildomos viešojo pirkimo ir pirkimo procedūrų (ATN2) ataskaitų duomenys nuo 2017m. iki šių dienų. Rinkinio objektas - paskelbta ataskaita. Pateikiama detali informacija apie ataskaitą, viešajame pirkime dalyvavusią perkančiąją arba įgaliotąją organizacijas, pirkimo objektą bei vykdytą pirkimą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes data from the Public Procurement Office's Procurement Procedures (ATN1) and Additional Procurement and Procurement Procedures (ATN2) reports from 2017 to the present day. The object of the kit is a published report. Detailed information shall be provided on the report, the contracting or authorised organisations involved in the procurement, the subject matter of the procurement and the procurement carried out. If you have any questions about the dataset, please contact the State Data Control Opening Team by e-mail atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pirkimas](ataskaitos/Pirkimas.md) | Ataskaitų duomenys | `4` | `vda_id` | — | `35` | Rinkinyje pateikiami Viešųjų pirkimų tarnybos Pirkimo procedūrų (ATN1) ir Papildomos viešojo pirkimo ir pirkimo procedūrų (ATN2) ataskaitų duomenys nuo 2017m. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/ataskaitos.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/ataskaitos.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/vpt/ataskaitos (https://data.gov.lt/datasets/2858/)
