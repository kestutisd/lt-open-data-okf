---
type: Dataset
title: "Stacionaro lovų skaičius ir jų veiklos rodikliai"
description: "Pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupes, savivaldybes"
resource: "https://get.data.gov.lt/datasets/gov/hi/lovos"
tags: [gov, hi, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/hi/lovos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1230/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/lovos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Stacionaro lovų skaičius ir jų veiklos rodikliai

Pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupes, savivaldybes[^manifest]

- **Namespace:** `datasets/gov/hi/lovos`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/lovos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/lovos` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1230/`[^dcat]
- **Publisher (`dct:publisher`):** Higienos institutas[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/hi/lovos`[^dcat]
- **Portal Title (`@lt`):** Stacionaro lovų skaičius ir jų veiklos rodikliai[^dcat]
- **Portal Title (`@en`):** Number of hospital beds and hospital beds activities indicators[^dcat]
- **Issued (`dct:issued`):** `2021-04-12`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2023-06-12` .. `2025-04-25`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Stacionaro lovų skaičius ir jų veiklos rodikliai pagal asmens sveikatos priežiūros įstaigą, lovų specialybės grupės, savivaldybes. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Number of hospital beds and hospital beds activities indicators by health care institution, bed speciality and regions.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Istaiga](lovos/Istaiga.md) | Įstaigos | `4` | `istg_id` | — | `3` | — |
| [Savivaldybe](lovos/Savivaldybe.md) | Savivaldybės | `4` | `kod` | — | `3` | — |
| [LovosProfilis](lovos/LovosProfilis.md) | Lovų profiliai | `4` | `prof_kod` | — | `4` | — |
| [VeiklosRodiklis](lovos/VeiklosRodiklis.md) | Lovos veiklos rodikliai | `3` | — | — | `18` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/lovos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/lovos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/lovos (https://data.gov.lt/datasets/1230/)
