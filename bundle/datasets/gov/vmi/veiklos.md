---
type: Dataset
title: "Fizinių asmenų, vykdančių individualią veiklą pagal pažymą, duomenys"
description: "Duomenys apie asmenis, vykdančius individualią veiklą pagal pažymą, pagal savivaldybes, veiklos kodą ir kt."
resource: "https://get.data.gov.lt/datasets/gov/vmi/veiklos"
tags: [gov, vmi, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/individuali_veikla.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vmi/individuali_veikla.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1912/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/veiklos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Fizinių asmenų, vykdančių individualią veiklą pagal pažymą, duomenys

- **Namespace:** `datasets/gov/vmi/veiklos`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/individuali_veikla.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/individuali_veikla.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/veiklos` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1912/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė mokesčių inspekcija prie Finansų ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vmi/veiklos`[^dcat]
- **Portal Title (`@lt`):** Fizinių asmenų, vykdančių individualią veiklą pagal pažymą, duomenys[^dcat]
- **Portal Title (`@en`):** Data on natural persons performing individual activities on the basis of a certificate[^dcat]
- **Issued (`dct:issued`):** `2022-04-26`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2022-10-14` .. `2026-07-16`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenys apie asmenis, vykdančius individualią veiklą pagal pažymą, pagal savivaldybes, veiklos kodą ir kt. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Data on persons performing individual activities by certificate, by municipalities, code of activity, etc.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IndividualiVeikla](veiklos/IndividualiVeikla.md) | Duomenys apie asmenis vykdančius individualias veiklas | `4` | `eiles_nr` | `open` | `16` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/individuali_veikla.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/individuali_veikla.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/veiklos (https://data.gov.lt/datasets/1912/)
