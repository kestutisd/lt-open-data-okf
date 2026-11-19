---
type: Dataset
title: "Eksporto sertifikatų ir prekių duomenų rinkinys"
description: "Rinkinyje pateikiami Valstybinės maisto ir veterinarijos tarnybos Eksporto sertifikavimo sistemoje kaupiami ir saugomi duomenys apie prašymus išduoti veterinarinius sertifikatus eksportui."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/eksportas"
tags: [gov, vmvt, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/eksportas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/eksportas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4106/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/eksportas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Eksporto sertifikatų ir prekių duomenų rinkinys

- **Namespace:** `datasets/gov/vmvt/eksportas`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/eksportas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/eksportas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/eksportas` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4106/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmvt/eksportas`[^dcat]
- **Portal Title (`@lt`):** Eksporto sertifikatų ir prekių duomenų rinkinys[^dcat]
- **Portal Title (`@en`):** Data Set of Export Certificates and Goods[^dcat]
- **Issued (`dct:issued`):** `2026-01-22`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-01` .. `2026-10-01`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami Valstybinės maisto ir veterinarijos tarnybos Eksporto sertifikavimo sistemoje kaupiami ir saugomi duomenys apie prašymus išduoti veterinarinius sertifikatus eksportui. Duomenys apima informaciją apie eksportuojamus gyvūninės ir negyvūninės kilmės produktus, įskaitant pašarus, sertifikatų numerius ir galiojimą, produktų kiekius, gavėjus, paskirties šalis, ekonominės veiklos vykdytojus bei Kombinuotosios nomenklatūros (KN) kodus. Sertifikatų galiojimas yra ribotas ir susijęs su konkrečia siunta – sertifikatas galioja tik vienai partijai ir vienam eksportui. Su duomenimis susijusiais klausimais prašome kreiptis el. Paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Eksportas](eksportas/Eksportas.md) | Eksporto sertifikatų ir prekių duomenų rinkinys | `4` | `vda_id` | `open` | `23` | Duomenų rinkinyje registruojami prašymai išduoti veterinarinius sertifikatus maisto, gyvūnų ir pašarų eksportui bei pateikiama informacija apie... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/eksportas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/eksportas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/eksportas (https://data.gov.lt/datasets/4106/)
