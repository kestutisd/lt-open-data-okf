---
type: Dataset
title: "Duomenys apie Kauno miesto daugiabučius"
description: "Pateikiami Kauno miesto savivaldybės duomenys apie Kauno mieste stovinčius daugiabučius pastatus."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/daugiabuciai"
tags: [gov, kauno_m_sav, deployed, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/daugiabuciai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/daugiabuciai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2744/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/daugiabuciai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Duomenys apie Kauno miesto daugiabučius

Pateikiami Kauno miesto savivaldybės duomenys apie Kauno mieste stovinčius daugiabučius pastatus. Rinkinio objektas - daugiabutis pastatas. Rinkinį sudaro informacija apie daugiabučio pastatymo laikotarpį, namo ir aplink jį esančios žemės plotus, namo pastatymo metus, valdymo formą ir esamą valdytoją, renovacijos būklę bei renovacijos metu atliktus darbus. Taip pat nurodytas namo adresas bei jo koordinatės. Pasiteiravimui kreiptis į Valstybės duomenų valdysenos komandą: vdv@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/kauno_m_sav/daugiabuciai`[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/daugiabuciai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/daugiabuciai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/daugiabuciai` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2744/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/daugiabuciai`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie Kauno miesto daugiabučius[^dcat]
- **Portal Title (`@en`):** Data on apartment blocks in Kaunas city[^dcat]
- **Issued (`dct:issued`):** `2024-08-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL_2` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL_2`)[^dcat]
- **Distribution Date Span:** `2024-08-13` .. `2026-05-15`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Kauno miesto savivaldybės duomenys apie Kauno mieste stovinčius daugiabučius pastatus. Rinkinio objektas - daugiabutis pastatas. Rinkinį sudaro informacija apie daugiabučio pastatymo laikotarpį, namo ir aplink jį esančios žemės plotus, namo pastatymo metus, valdymo formą ir esamą valdytoją, renovacijos būklę bei renovacijos metu atliktus darbus. Taip pat nurodytas namo adresas ir jo koordinatės. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The collection includes data of Kaunas City Municipality on apartment buildings in Kaunas City. The object of the kit is an apartment building. The kit consists of information about the period of construction of an apartment building, the areas of the house and the surrounding land, the year of construction of the house, the form of management and the current manager, the state of renovation and the work carried out during renovation. The address of the house and its coordinates are also indicated. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pastatas](daugiabuciai/Pastatas.md) | Duomenys apie Kauno miesto daugiabučius | `4` | `vda_id` | — | `18` | Pateikiami Kauno miesto savivaldybės duomenys apie Kauno mieste stovinčius daugiabučius pastatus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/daugiabuciai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/daugiabuciai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/daugiabuciai (https://data.gov.lt/datasets/2744/)
