---
type: Dataset
title: "Duomenys apie akcizais apmokestinamas prekes"
description: "Einamojo mėnesio ir kaupiamieji nuo metų pradžios akcizais apmokestinamų prekių, išleistų į Lietuvos rinką, deklaruoti kiekiai ir akcizai, pateikti pagal atskiras tarifines grupes ir produktų kategorijas."
resource: "https://get.data.gov.lt/datasets/gov/vmi/akcizai"
tags: [gov, vmi, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/akcizai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/akcizai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1176/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/akcizai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Duomenys apie akcizais apmokestinamas prekes

- **Namespace:** `datasets/gov/vmi/akcizai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/akcizai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/akcizai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/akcizai` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1176/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/akcizai`[^dcat]
- **Portal Title (`@lt`):** Duomenys apie akcizais apmokestinamas prekes[^dcat]
- **Portal Title (`@en`):** Data on excisable goods[^dcat]
- **Issued (`dct:issued`):** `2022-12-06`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2022-12-05` .. `2026-06-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Einamojo mėnesio ir kaupiamieji nuo metų pradžios akcizais apmokestinamų prekių, išleistų į Lietuvos rinką, deklaruoti kiekiai ir akcizai, pateikti pagal atskiras tarifines grupes ir produktų kategorijas. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Declared quantities and excise duties of excisable goods released for the Lithuanian market for the current month and from the beginning of the year, presented by separate tariff groups and product categories.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AkcizoMokestis](akcizai/AkcizoMokestis.md) | Akcizų deklaracijų duomenys | `4` | `eiles_nr` | — | `6` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/akcizai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/akcizai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/akcizai (https://data.gov.lt/datasets/1176/)
