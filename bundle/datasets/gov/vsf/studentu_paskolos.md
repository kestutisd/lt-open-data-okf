---
type: Dataset
title: "Studentų paskolų informacija"
description: "Duomenų rinkinyje pateikiama informacija apie studentų studijas, mokymosi įstaigas ir suteiktas paskolas bei jų sąlygas ir grąžinimą."
resource: "https://get.data.gov.lt/datasets/gov/vsf/studentu_paskolos"
tags: [gov, vsf, deployed, cadence-bimonthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/studentu_paskolos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vsf/studentu_paskolos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4132/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vsf/studentu_paskolos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Studentų paskolų informacija

Duomenų rinkinyje pateikiama informacija apie studentų studijas, mokymosi įstaigas ir suteiktas paskolas bei jų sąlygas ir grąžinimą.[^manifest]

- **Namespace:** `datasets/gov/vsf/studentu_paskolos`[^manifest]
- **Manifest CSV:** [datasets/gov/vsf/studentu_paskolos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/studentu_paskolos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vsf/studentu_paskolos` (`deployed`)[^manifest]
- **Provider:** `vsf` — Valstybinis studijų fondas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4132/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vsf/studentu_paskolos`[^dcat]
- **Portal Title (`@lt`):** Studentų paskolų informacija[^dcat]
- **Portal Title (`@en`):** Student loan information[^dcat]
- **Issued (`dct:issued`):** `2026-02-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `BIMONTHLY` (`http://publications.europa.eu/resource/authority/frequency/BIMONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-02-18` .. `2026-02-20`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami studentų paskolų paraiškų anketų ir išduotų paskolų duomenys, kuriuos teikia Valstybinis studijų fondas (https://vsf.lrv.lt/). Rinkinyje nurodytos paskolos, suteiktos 1998–2013 m. Kiekviena rinkinio eilutė atitinka vieną unikalią studentui suteiktą paskolą. Rinkinį sudaro anketos duomenys, kuriuose nurodoma studento mokymosi įstaiga ir pateikiama šifruota asmeninė informacija, bei suteiktų paskolų duomenys, kuriuose nurodoma paskolos suma, jos grąžinimo terminai ir nustatyti delspinigiai. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paskola](studentu_paskolos/Paskola.md) | Studentų paskolų informacija | `4` | `vda_prime_key` | — | `23` | Duomenų rinkinyje pateikiami studentų paskolų paraiškų anketų ir išduotų paskolų duomenys, kuriuos teikia Valstybinis studijų fondas (https://vsf.lrv.lt/). |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsf/studentu_paskolos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/studentu_paskolos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vsf/studentu_paskolos (https://data.gov.lt/datasets/4132/)
