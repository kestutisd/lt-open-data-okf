---
type: Dataset
title: "Transporto priemonių sandorių duomenys"
description: "AB „Regitra“ Transporto priemonių savininkų apskaitos informacinė sistema kaupia transporto priemonių savininkų bei jų vykdytų sandorių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/regitra/tpsais"
tags: [gov, regitra, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tpsais.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/regitra/tpsais.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2812/"
    title: "data.gov.lt DCAT-AP — datasets/gov/regitra/tpsais"
    author: "team:vda"
    last_modified: "2026-08-27T00:00:00Z"
---

# Transporto priemonių sandorių duomenys

- **Namespace:** `datasets/gov/regitra/tpsais`[^manifest]
- **Manifest CSV:** [datasets/gov/regitra/tpsais.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tpsais.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/regitra/tpsais` (`deployed`)[^manifest]
- **Provider:** `regitra` — AB „Regitra“ *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2812/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/regitra/tpsais`[^dcat]
- **Portal Title (`@lt`):** Transporto priemonių sandorių duomenys[^dcat]
- **Portal Title (`@en`):** Vehicle Transaction Data[^dcat]
- **Issued (`dct:issued`):** `2024-09-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-08-27`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-09-24` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

AB „Regitra“ Transporto priemonių savininkų apskaitos informacinė sistema kaupia transporto priemonių savininkų bei jų vykdytų sandorių duomenis. Duomenys kaupiami nuo 2021-05-01 ir yra atnaujinami. Duomenų rinkinį sudaro: pseudonimizuoti dokumento identifikatoriaus ir išorinio rakto į sisteminę veikla, sandorio pobūdį nurodanti dokumento rūšis, dokumento išdavimo data, sandorio šalis, suma, valiuta, atsiskaitymo būdo bei įrašo modifikavimo laikas. Vienas įrašas rinkinyje atitinka vieną sandorio dokumentą. Duomenų teikėjas – AB „Regitra“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Regitra AB's vehicle owners' accounting information system collects data on vehicle owners (hereinafter TP) and the transactions carried out by them. Data shall be collected from 01-05-2021 and shall be updated. The dataset consists of a pseudonymized document identifier and an external key to the system activity, a type of document indicating the nature of the santor, the date of issue of the document, the counterparty, amount, currency, settlement method, and the time of modification of the record. One entry in a set corresponds to one transaction document. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sandoris](tpsais/Sandoris.md) | Transporto priemonių sandorių duomenys | `4` | `dok_id` | — | `9` | AB „Regitra“ Transporto priemonių savininkų apskaitos informacinė sistema kaupia transporto priemonių (toliau TP) savininkų bei jų vykdytų sandorių duomenis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/regitra/tpsais.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/regitra/tpsais.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/regitra/tpsais (https://data.gov.lt/datasets/2812/)
