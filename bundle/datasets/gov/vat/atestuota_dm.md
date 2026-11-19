---
type: Dataset
title: "Atestuotų dauginamosios medžiagos tiekėjų sąrašas"
description: "Atestuotų dauginamosios medžiagos tiekėjų sąrašas."
resource: "https://get.data.gov.lt/datasets/gov/vat/atestuota_dm"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r23_atestuota_dm.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/r23_atestuota_dm.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2574/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/atestuota_dm"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Atestuotų dauginamosios medžiagos tiekėjų sąrašas

- **Namespace:** `datasets/gov/vat/atestuota_dm`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r23_atestuota_dm.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r23_atestuota_dm.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/atestuota_dm` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2574/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/atestuota_dm/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Atestuotų dauginamosios medžiagos tiekėjų sąrašas[^dcat]
- **Portal Title (`@en`):** List of certified suppliers of propagating material[^dcat]
- **Issued (`dct:issued`):** `2024-03-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-05-02` .. `2024-03-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Atestuotų dauginamosios medžiagos tiekėjų sąrašas. Pateikiama informacija apie dauginamąją medžiagą tiekiančius ūkio subjektus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

List of certified suppliers of propagating material. Information on operators supplying propagating material shall be provided.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Subjektas](atestuota_dm/Subjektas.md) | Pateikiama informacija apie dauginamąją medžiagą tiekiančius ūkio subjektus (vardas, pavardė/ pavadinimas, tiekiamos augalų grupės, veiklos rūšys, dauginamosios medžiagos pažymėjimo numeris, įsakymo data) | `4` | `eil_nr` | `open` | `6` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r23_atestuota_dm.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r23_atestuota_dm.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/atestuota_dm (https://data.gov.lt/datasets/2574/)
