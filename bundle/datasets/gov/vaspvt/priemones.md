---
type: Dataset
title: "Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys"
description: "Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/priemones"
tags: [gov, vaspvt, deployed, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2310/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/priemones"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys

- **Namespace:** `datasets/gov/vaspvt/priemones`[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_iranga.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/priemones` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `5` (5 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2310/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vaspvt/priemones`[^dcat]
- **Portal Title (`@lt`):** Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys[^dcat]
- **Portal Title (`@en`):** Assessment and management data of healthcare technologies related to medical devices[^dcat]
- **Issued (`dct:issued`):** `2023-06-13`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `QUARTERLY` (`http://publications.europa.eu/resource/authority/frequency/QUARTERLY`)[^dcat]
- **Distribution Date Span:** `2023-06-13` .. `2026-08-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Assessment and management data of healthcare technologies related to medical devices[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MedicinosPriemone](priemones/MedicinosPriemone.md) | Brangių medicinos priemonių sąrašas | `4` | `id` | `open` | `32` | — |
| [IstaigosAtaskaituDuomenys](priemones/IstaigosAtaskaituDuomenys.md) | Istaigų Ataskaitų Duomenys | `4` | `vda_prime_key` | `open` | `72` | — |
| [IstaigosDuomenys](priemones/IstaigosDuomenys.md) | Istaigu_Duomenys | `4` | `vda_prime_key` | `open` | `57` | — |
| [MedicinosPriemoniuAtaskaita](priemones/MedicinosPriemoniuAtaskaita.md) | Ataskaitų Apie Brangias Priemones Sąrašas | `4` | `id` | `open` | `18` | — |
| [Ataskaita](priemones/Ataskaita.md) | Ataskaita | `4` | `id` | `open` | `16` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/priemones (https://data.gov.lt/datasets/2310/)
