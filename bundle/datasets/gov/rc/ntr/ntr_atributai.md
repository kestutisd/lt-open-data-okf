---
type: Dataset
title: "NTR atributų klasifikatoriai"
description: "NTR atributų klasifikatoriai (duomenų rinkinių grupė, viso 5 vnt.) (NTR atributų klasifikatorius; NTR atributų reikšmių klasifikatorius; NTR atributų tipų klasifikatorius; NTR leistinų atributų klasifikatorius; NTR atributų požymių klasifikatorius)"
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai"
tags: [gov, rc, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NTR atributų klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_atributai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1896/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės įmonė Registrų centras[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/:ns`[^dcat]
- **Portal Title (`@lt`):** NTR atributų klasifikatoriai[^dcat]
- **Portal Title (`@en`):** NTR attribute classifiers[^dcat]
- **Issued (`dct:issued`):** `2023-07-24`[^dcat]
- **Last Modified (`dct:modified`):** `2025-12-18`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-04-01` .. `2023-06-30`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

NTR atributų klasifikatoriai (duomenų rinkinių grupė, viso 5 vnt.) (NTR atributų klasifikatorius; NTR atributų reikšmių klasifikatorius; NTR atributų tipų klasifikatorius; NTR leistinų atributų klasifikatorius; NTR atributų požymių klasifikatorius)[^dcat]

### Portal Description (`@en`)

NTR attribute classifiers (data set group, 5 units in total) (NTR attribute classifier; NTR attribute value classifier; NTR attribute type classifier; NTR attribute attribute classifier) Geographical sample of data - the whole territory of the country.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrAtributas](ntr_atributai/NtrAtributas.md) | NTR atributų klasifikatorius | `4` | `atri_kodas` | — | `12` | — |
| [NtrAtributoReiksme](ntr_atributai/NtrAtributoReiksme.md) | NTR atributų reikšmių klasifikatorius | `3` | `atri_kodas, reik_reiksme` | — | `8` | — |
| [NtrAtributoTipas](ntr_atributai/NtrAtributoTipas.md) | NTR atributų tipų (kiekybiniai, kokybiniai, vertinimo) klasifikatorius | `4` | `atrt_tipas` | — | `3` | — |
| [NtrLeistinasAtributas](ntr_atributai/NtrLeistinasAtributas.md) | NTR leistinų atributų klasifikatorius | `4` | `obje_tipas, atri_kodas` | — | `11` | — |
| [NtrAtributoPozymis](ntr_atributai/NtrAtributoPozymis.md) | NTR atributų požymių (būtinas, galimas) klasifikatorius | `4` | `atrp_poz` | — | `3` | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai (https://data.gov.lt/datasets/1896/)
