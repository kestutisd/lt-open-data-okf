---
type: Dataset
title: "Licencijuoti grūdų sandėliai"
description: "Pateikiama informacija (adresas, pavadinimas, licencijos išdavimo data, leistinos sandėliuoti grūdų rūšys bei kiekiai) apie ūkio subjektų licencijuotus grūdų sandėlius."
resource: "https://get.data.gov.lt/datasets/gov/vat/grudu_sandeliai"
tags: [gov, vat, deployed, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_sandeliai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vat/grudu_sandeliai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1872/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/grudu_sandeliai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Licencijuoti grūdų sandėliai

- **Namespace:** `datasets/gov/vat/grudu_sandeliai`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/grudu_sandeliai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_sandeliai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/grudu_sandeliai` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1872/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybinė augalininkystės tarnyba prie Žemės ūkio ministerijos[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vat/grudu_sandeliai`[^dcat]
- **Portal Title (`@lt`):** Licencijuoti grūdų sandėliai[^dcat]
- **Portal Title (`@en`):** Licensed grain warehouses[^dcat]
- **Issued (`dct:issued`):** `2023-04-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-19`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `IRREG` (`http://publications.europa.eu/resource/authority/frequency/IRREG`)[^dcat]
- **Distribution Date Span:** `2023-04-27` .. `2023-10-06`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Pateikiama informacija (adresas, pavadinimas, licencijos išdavimo data, leistinos sandėliuoti grūdų rūšys bei kiekiai) apie ūkio subjektų licencijuotus grūdų sandėlius. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Provide information (address, name, date of issue of the license, types and quantities of grain permitted for storage) on the grain warehouses licensed by the operators[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sandelis](grudu_sandeliai/Sandelis.md) | Pateikiama informacija (adresas, pavadinimas, licencijos išdavimo data, leistinos sandėliuoti grūdų rūšys bei kiekiai) apie ūkio subjektų licencijuotus grūdų sandėlius | `4` | `licencijos_nr` | `open` | `6` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/grudu_sandeliai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/grudu_sandeliai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/grudu_sandeliai (https://data.gov.lt/datasets/1872/)
