---
type: Dataset
title: "Nekilnojamo turto mokesčio duomenų rinkinys"
description: "Nekilnojamo turto mokesčio (toliau - NTM) duomenų rinkinys"
resource: "https://get.data.gov.lt/datasets/gov/vmi/nt"
tags: [gov, vmi, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/nt.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1185/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/nt"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Nekilnojamo turto mokesčio duomenų rinkinys

Nekilnojamo turto mokesčio (toliau - NTM) duomenų rinkinys[^manifest]

- **Namespace:** `datasets/gov/vmi/nt`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/nt.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/nt` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1185/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/nt`[^dcat]
- **Portal Title (`@lt`):** Nekilnojamo turto mokesčio duomenys[^dcat]
- **Portal Title (`@en`):** Real estate tax data[^dcat]
- **Issued (`dct:issued`):** `2022-07-21`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2022-07-21` .. `2026-10-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Nekilnojamojo turto mokesčio duomenys (pagal apskritis ir savivaldybes) apie deklaruotas apskaičiuotas mokesčio sumas bei taikomas deklaruotas mokesčio lengvatos sumas už mokestinį laikotarpį (metus). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Year and details of the declared estimated Real Estate Tax, the amounts of relief indicated[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BendrasNtMokestis](nt/BendrasNtMokestis.md) | NT mokesčio mokėtojo ir NT bendri duomenys | `2` | — | — | `13` | Nekilnojamojo turto (toliau - NT) mokesčio mokėtojo ir NT bendri duomenys |
| [AvansinisNtMokestis](nt/AvansinisNtMokestis.md) | Avansinio NT mokesčio duomenys | `2` | — | — | `10` | — |
| [SavivaldybeNtMokestis](nt/SavivaldybeNtMokestis.md) | NT mokesčio duomenys pagal savivaldybes | `3` | — | — | `20` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/nt.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/nt (https://data.gov.lt/datasets/1185/)
