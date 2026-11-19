---
type: Dataset
title: "Pranešimai"
description: "Rinkinyje pateikiami nuo 2024 m. balandžio mėn."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/pranesimai"
tags: [gov, vmvt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3817/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/pranesimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pranešimai

- **Namespace:** `datasets/gov/vmvt/pranesimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/rasff/pranesimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/pranesimai` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3817/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmvt/pranesimai`[^dcat]
- **Portal Title (`@lt`):** Skubūs pranešimai apie nesaugų maistą ir pašarus[^dcat]
- **Portal Title (`@en`):** Urgent notifications of unsafe food and feed[^dcat]
- **Issued (`dct:issued`):** `2025-04-02`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-04-01` .. `2026-10-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami nuo 2024 m. balandžio mėn. Skubių pranešimų apie nesaugų maistą ir pašarus sistemoje (RASFF – Rapid Alert System for Food and Feed) paskelbtų pranešimų duomenys. Rinkinį sudaro trys lentelės: „Pranešimai“, „Siuntos informacija“ ir „Siuntos subjektai“. Lentelę „Pranešimai“ sudaro: sistemos identifikatorius, pranešimo data, nustatyto pažeidimo aprašymas, pažeidimo rūšis, pavojus, tipas, aptikimo tipas, išplatinimo ribos, rizikos tipas, rizikos taikymo ribos. Lentelę „Siuntos informacija“ sudaro: produktas, produkto grupė, kilmės šalis, partijos numeris ir tinkamumo vartoti terminas. Lentelę „Siuntos subjektai“ sudaro: siuntos ūkio subjekto pavadinimas, tipas (gamintojas, tiekėjas, siuntos gavėjas, importuotojas ir pan.), subjekto šalies kodas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package provides data on notifications issued in the Rapid Alert System for Food and Feed (RASFF) Rapid Alert System for Food and Feed as of April 2024. The package consists of three tables: “Messages”, “Shipping Information” and “Shipping Entities”. The “Notifications” table consists of: system identifier, reporting date, description of the detected infringement, type of infringement, hazard, type, detection type, distribution limits, risk type, risk application limits. The “Shipping information” table consists of: product, product group, country of origin, lot number and shelf life. The table “Shipping entities” shall comprise: name, type (manufacturer, supplier, consignee, importer, etc.) of the entity of the consignment, country code of the entity. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pranesimas](pranesimai/Pranesimas.md) | Pranešimų duomenys | `4` | `pranesimo_id` | — | `11` | Pateikiami pranešimai apie nustatytus pažeidimus, pažeidimo rūšį, pavojų, pažeidimo tipą, aptikimo tipą, išplatinimo ribas, rizikos tipą ir rizikos taikymo... |
| [Siunta](pranesimai/Siunta.md) | Siuntų duomenys | `4` | `siuntos_id` | — | `8` | Pateikiami siuntų duomenys: kilmės šalis, produkto grupė, produkto pavadinimas, partijos numeris, tinkamumo terminas ir tinkamumo tipas. |
| [Subjektas](pranesimai/Subjektas.md) | Subjektų duomenys | `4` | `id` | — | `6` | Pateikiama informacija apie ukio subjektus: subjekto pavadinimas, tipas ir šalis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/pranesimai (https://data.gov.lt/datasets/3817/)
