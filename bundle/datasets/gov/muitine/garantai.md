---
type: Dataset
title: "Informacija apie muitinės garantus"
description: "Informacija apie muitinės garanto statusą turinčias banko įstaigas ar draudimo bendroves"
resource: "https://get.data.gov.lt/datasets/gov/muitine/garantai"
tags: [gov, muitine, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/garantai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/garantai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2837/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/garantai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Informacija apie muitinės garantus

Informacija apie muitinės garanto statusą turinčias banko įstaigas ar draudimo bendroves[^manifest]

- **Namespace:** `datasets/gov/muitine/garantai`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/garantai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/garantai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/garantai` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2837/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/garantai`[^dcat]
- **Portal Title (`@lt`):** Įstaigos turinčios muitinės garanto statusą Lietuvoje[^dcat]
- **Portal Title (`@en`):** Institutions having the status of customs guarantor in Lithuania[^dcat]
- **Issued (`dct:issued`):** `2024-10-28`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-10-28` .. `2024-10-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie muitinės garanto statusą turinčias banko įstaigas ar draudimo bendroves, kurios išduoda garantijas muitinės procedūrų vykdymui užtikrinti ar atidedant mokesčių sumokėjimą muitinei. Duomenys apie garantus renkami nuo 2004 m. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The dataset shall contain information on bank institutions or insurance companies having the status of customs guarantor which issue guarantees for the enforcement of customs procedures or for the deferral of payment of taxes to the customs authorities. Data on guarantors have been collected since 2004. Please contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Garantas](garantai/Garantas.md) | Informacija apie muitinės garantus | `4` | `vda_prime_key` | — | `13` | Informacija apie muitinės garanto statusą turinčias banko įstaigas ar draudimo bendroves |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/garantai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/garantai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/garantai (https://data.gov.lt/datasets/2837/)
