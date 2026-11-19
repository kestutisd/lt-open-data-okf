---
type: Dataset
title: "Kauno miesto savivaldybės vaikų vasaros renginių duomenys"
description: "Šiame rinkinyje pateikti Kauno miesto savivaldybės vaikų vasaros renginių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai"
tags: [gov, kauno_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2737/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Kauno miesto savivaldybės vaikų vasaros renginių duomenys

Šiame rinkinyje pateikti Kauno miesto savivaldybės vaikų vasaros renginių duomenis. Rinkinys talpina pačių renginių aprašymus, dalyvavusius vaikus bei asmenis kurie registravo vaikus į šiuos renginius.[^manifest]

- **Namespace:** `datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai`[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2737/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai`[^dcat]
- **Portal Title (`@lt`):** Kauno miesto savivaldybės vaikų vasaros renginių duomenys[^dcat]
- **Portal Title (`@en`):** Summer events data of Kaunas City Municipality[^dcat]
- **Issued (`dct:issued`):** `2024-08-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-08-15` .. `2026-10-10`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių dalyvių sąrašas. Pateikiamos dvi lentelės – „renginiu_dalyviai“ ir „renginiu_sarasas“. Rinkinyje nurodomi renginiai, datos ir asmenys, kurie dalyvavo atitinkamuose renginiuose. Lentelės jungiasi per renginio_id raktą. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

This package includes a list of participants of Kaunas City Municipality Children's Summer Events. Two tables are presented for “events” and “events”. The package shall include events, dates and persons who participated in the relevant events. Tables connect through the event/id key. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dalyvis](vasaros_vaiku_renginiai/Dalyvis.md) | Dalyvių sąrašas | `4` | `vda_primary_key` | — | `10` | Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių dalyvių sąrašas. |
| [Renginys](vasaros_vaiku_renginiai/Renginys.md) | Renginių sąrašas | `4` | `renginio_id` | — | `25` | Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių sąrašas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai (https://data.gov.lt/datasets/2737/)
