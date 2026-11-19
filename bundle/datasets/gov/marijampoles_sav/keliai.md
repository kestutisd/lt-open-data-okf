---
type: Dataset
title: "Marijampolės savivaldybės techninių eismo reguliavimo priemonių informacinės sistemos duomenys"
description: "Šiame rinkinyje pateikti Marijampolės savivaldybės kelio ženklai bei jų lokacijos."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/keliai"
tags: [gov, marijampoles_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/kelio_zenklas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/kelio_zenklas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2756/"
    title: "data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/keliai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Marijampolės savivaldybės techninių eismo reguliavimo priemonių informacinės sistemos duomenys

Šiame rinkinyje pateikti Marijampolės savivaldybės kelio ženklai bei jų lokacijos.[^manifest]

- **Namespace:** `datasets/gov/marijampoles_sav/keliai`[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/kelio_zenklas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/kelio_zenklas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/keliai` (`deployed`)[^manifest]
- **Provider:** `marijampoles_sav` — Marijampolės savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2756/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/keliai`[^dcat]
- **Portal Title (`@lt`):** Marijampolės savivaldybės techninių eismo reguliavimo priemonių informacinės sistemos duomenys[^dcat]
- **Portal Title (`@en`):** Data of the information system of technical traffic regulation measures of Marijampole Municipality[^dcat]
- **Issued (`dct:issued`):** `2024-08-21`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-06` .. `2026-08-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šiame rinkinyje pateikti Marijampolės savivaldybės kelio ženklai bei jų lokacijos. Rinkinyje viena eilutė nurodo viena kelio ženklą. Duomenų teikėjas – Marijampolės savivaldybė. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

This package includes road signs of Marijampole Municipality and their localities. In the set, one line indicates one road sign. Contact the atverimas@stat.gov.lt for technical questions or possible errors[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KelioZenklas](keliai/KelioZenklas.md) | Kelio ženklai | `4` | `vda_primary_key` | — | `21` | Šiame rinkinyje pateikti Marijampolės savivaldybės kelio ženklai bei jų lokacijos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/kelio_zenklas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/kelio_zenklas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/keliai (https://data.gov.lt/datasets/2756/)
