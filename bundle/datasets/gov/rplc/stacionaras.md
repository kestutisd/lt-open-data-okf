---
type: Dataset
title: "Respublikinio Priklausomybės Ligų Centro Vilniaus filialo stacionaro skyriuose gydytų pacientų duomenys"
description: "Šiame duomenų rinkinyje pateikiami RPLC Vilniaus filiale stacionarines paslaugas gavusių pacientų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/rplc/stacionaras"
tags: [gov, rplc, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/stacionaro_apsilankymai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rplc/stacionaro_apsilankymai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2382/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rplc/stacionaras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Respublikinio Priklausomybės Ligų Centro Vilniaus filialo stacionaro skyriuose gydytų pacientų duomenys

- **Namespace:** `datasets/gov/rplc/stacionaras`[^manifest]
- **Manifest CSV:** [datasets/gov/rplc/stacionaro_apsilankymai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/stacionaro_apsilankymai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rplc/stacionaras` (`deployed`)[^manifest]
- **Provider:** `rplc` — Respublikinis priklausomybės ligų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2382/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rplc/stacionaras`[^dcat]
- **Portal Title (`@lt`):** Respublikinio Priklausomybės Ligų Centro Vilniaus filialo stacionaro skyriuose gydytų pacientų duomenys[^dcat]
- **Portal Title (`@en`):** Data of patients treated in the stationary departments of the Vilnius branch of the Republican Centre for Disease Responsibility[^dcat]
- **Issued (`dct:issued`):** `2023-11-08`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2023-12-12` .. `2025-04-14`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šiame duomenų rinkinyje pateikiami RPLC Vilniaus filiale stacionarines paslaugas gavusių pacientų duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

This dataset provides data of patients who have received hospital services at the RPLC Vilnius branch. For technical questions or possible errors, contact atverimas@stat.gov.lt[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Kortele](stacionaras/Kortele.md) | Pateikiami Respublikinio Priklausomybės Ligų Centro Vilniaus filialo stacionaro skyriuose gydytų pacientų duomenys nuo 2016m. Duomenys apima pacientų demografinę (gyvenamoji vieta, gimimo metų ir amžiaus grupės, lytis, išsilavinimas, užimtumas, sveikatos draudimas) ir su gydymu susijusią (sutrikimas, taikytas gydymas, duomenys apie paciento būklę ir išrašymą) informaciją. | `4` | `vda_id` | — | `16` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/rplc/stacionaro_apsilankymai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rplc/stacionaro_apsilankymai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rplc/stacionaras (https://data.gov.lt/datasets/2382/)
