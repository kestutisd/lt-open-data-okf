---
type: Dataset
title: "Duomenys apie Seime vykusius renginius"
description: "Rinkinyje pateikiami duomenys apie Seime organizuotus renginius nuo 2015m."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/seimo_renginiai"
tags: [gov, lrsk, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/seimo_renginiai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lrsk/seimo_renginiai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2612/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrsk/seimo_renginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Duomenys apie Seime vykusius renginius

Rinkinyje pateikiami duomenys apie Seime organizuotus renginius nuo 2015m. Pateikiama informacija: renginio pavadinimas, kalba, pradžios ir pabaigos laikas ir renginio vieta.[^manifest]

- **Namespace:** `datasets/gov/lrsk/seimo_renginiai`[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/seimo_renginiai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/seimo_renginiai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/seimo_renginiai` (`deployed`)[^manifest]
- **Provider:** `lrsk` — Lietuvos Respublikos Seimo Kanceliarija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2612/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lrsk/seimo_renginiai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie Seime vykusius renginius[^dcat]
- **Portal Title (`@en`):** Data on events held in the Seimas[^dcat]
- **Issued (`dct:issued`):** `2024-04-15`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-04-15` .. `2026-09-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami duomenys apie Seime organizuotus renginius nuo 2015m. Pateikiama informacija: renginio pavadinimas, kalba, pradžios ir pabaigos laikas ir renginio vieta. Duomenų teikėjas – Lietuvos Respublikos Seimo kanceliarija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on events organised in the Seimas since 2015. Information is provided: name, language, start and end time of the event and venue. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Ivykis](seimo_renginiai/Ivykis.md) | Duomenys apie Seime vykusius renginius | `4` | `vda_id` | — | `6` | Rinkinyje pateikiami duomenys apie Seime organizuotus renginius nuo 2015m. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/seimo_renginiai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/seimo_renginiai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrsk/seimo_renginiai (https://data.gov.lt/datasets/2612/)
