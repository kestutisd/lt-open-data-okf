---
type: Dataset
title: "Studijų baigiamieji darbai"
description: "Rinkinyje pateikti nuo 2001 m. apgintų studijų baigiamųjų darbų duomenys iš Nacionalinės švietimo agentūros (NŠA) Diplomų, atestatų ir kvalifikacijos pažymėjimų registro (DAKPR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/dakpr/baigiamieji_darbai"
tags: [gov, nsa, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2722/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/dakpr/baigiamieji_darbai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Studijų baigiamieji darbai

- **Namespace:** `datasets/gov/nsa/dakpr/baigiamieji_darbai`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/dakpr/baigiamieji_darbai` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2722/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/nsa/dakpr/baigiamieji_darbai`[^dcat]
- **Portal Title (`@lt`):** Studijų baigiamieji darbai[^dcat]
- **Portal Title (`@en`):** Graduation work[^dcat]
- **Issued (`dct:issued`):** `2024-07-30`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-07-26` .. `2026-10-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikti nuo 2001 m. apgintų studijų baigiamųjų darbų duomenys iš Nacionalinės švietimo agentūros (NŠA) Diplomų, atestatų ir kvalifikacijos pažymėjimų registro (DAKPR). Duomenų atnaujinimas – mėnesinis. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes data from the National Education Agency (NSA) Register of Diplomas, Certificates and Qualifications Certificates (DAKPR) for COMPLETED studies defended since 2001. Data update - Monthly. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BaigiamasisDarbas](baigiamieji_darbai/BaigiamasisDarbas.md) | Studijų baigiamieji darbai | `4` | `iraso_id` | — | `13` | Lentelėje pateikti studijų apgintų baigiamųjų darbų duomenys nuo 2001 metų iš Nacionalinės švietimo agentūros (NŠA) diplomų, atestatų ir kvalifikacijos... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/dakpr/baigiamieji_darbai (https://data.gov.lt/datasets/2722/)
