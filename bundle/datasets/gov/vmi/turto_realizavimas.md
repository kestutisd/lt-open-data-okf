---
type: Dataset
title: "Valstybei perduoto turto duomenys"
description: "Struktūrizuoti duomenys apie valstybei perduoto turto apskaitymą ir realizavimą pagal apskritis, turto grupes bei kategorijas, apie realizuoto turto kiekius, sumas ir patirtas turto administravimo išlaidas."
resource: "https://get.data.gov.lt/datasets/gov/vmi/turto_realizavimas"
tags: [gov, vmi, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/turto_realizavimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/turto_realizavimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1193/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/turto_realizavimas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Valstybei perduoto turto duomenys

- **Namespace:** `datasets/gov/vmi/turto_realizavimas`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/turto_realizavimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/turto_realizavimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/turto_realizavimas` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1193/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/turto_realizavimas`[^dcat]
- **Portal Title (`@lt`):** Valstybei perduoto turto duomenys[^dcat]
- **Portal Title (`@en`):** Data on assets transferred to the state[^dcat]
- **Issued (`dct:issued`):** `2023-05-04`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2023-05-03` .. `2026-07-04`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Struktūrizuoti duomenys apie valstybei perduoto turto apskaitymą ir realizavimą pagal apskritis, turto grupes bei kategorijas, apie realizuoto turto kiekius, sumas ir patirtas turto administravimo išlaidas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Structured data on the accounting and realization of assets transferred to the state by counties, asset groups and categories, on the quantities, amounts and realized administration costs of realized assets.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ValstPerduotasTurtas](turto_realizavimas/ValstPerduotasTurtas.md) | — | — | — | — | `18` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/turto_realizavimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/turto_realizavimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/turto_realizavimas (https://data.gov.lt/datasets/1193/)
