---
type: Dataset
title: "Informacija apie muitinės mėginių klasifikavimo aktus"
description: "informacija apie muitinio įforminimo metu paimtus prekių pavyzdžius ir pagal juos suformuotus prekių klasifikavimo aktus"
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_meginiai"
tags: [gov, muitine, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_meginiai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_meginiai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2834/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_meginiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Informacija apie muitinės mėginių klasifikavimo aktus

informacija apie muitinio įforminimo metu paimtus prekių pavyzdžius ir pagal juos suformuotus prekių klasifikavimo aktus[^manifest]

- **Namespace:** `datasets/gov/muitine/muitines_meginiai`[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_meginiai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_meginiai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_meginiai` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2834/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/muitine/muitines_meginiai`[^dcat]
- **Portal Title (`@lt`):** Informacija apie muitinės prekių klasifikavimo aktus[^dcat]
- **Portal Title (`@en`):** Information on customs goods classification acts[^dcat]
- **Issued (`dct:issued`):** `2024-10-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-10-25` .. `2026-10-03`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiama informacija apie muitinės paimtus prekių mėginius, siekiant įvertinti prekių tarifinį klasifikavimą taikant Kombinuotąją prekių ir ES integruoto tarifo nomenklatūrą arba nustatyti prekių sudėtį (parametrus), ir pagal juos suformuotus prekių klasifikavimo aktus. Duomenys renkami nuo 2009 metų. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The dataset shall contain information on samples of goods taken by the customs authorities in order to assess the tariff classification of goods by applying the Combined Nomenclature of the Integrated Tariff of Goods and the EU or to determine the composition (parameters) of the goods and the classification acts resulting therefrom. Data has been collected since 2009. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AktoNumeris](muitines_meginiai/AktoNumeris.md) | Informacija apie muitinės mėginių klasifikavimo aktus | `4` | `prekiu_klasifikavimo_akto_numeris` | — | `37` | informacija apie muitinio įforminimo metu paimtus prekių pavyzdžius ir pagal juos suformuotus prekių klasifikavimo aktus |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_meginiai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_meginiai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_meginiai (https://data.gov.lt/datasets/2834/)
