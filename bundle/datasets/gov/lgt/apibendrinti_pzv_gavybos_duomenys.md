---
type: Dataset
title: "Apibendrinti požeminio vandens gavybos duomenys"
description: "Apibendrinti naudingųjų iškasenų (anhidrito/gipso, dolomito, klinties, kreidos mergelio, molio, opokos, sapropelio, žvyro, smėlio, durpės, naftos) požeminio vandens (gėlo ir mineralinio) gavybos duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys"
tags: [gov, lgt, deployed, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/lgt/pzm_vandens_gavyba.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2043/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Apibendrinti požeminio vandens gavybos duomenys

- **Namespace:** `datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/pzm_vandens_gavyba.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2043/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys`[^dcat]
- **Portal Title (`@lt`):** Apibendrinti naudingųjų iškasenų ir požeminio vandens gavybos duomenys[^dcat]
- **Portal Title (`@en`):** Summary of mineral and groundwater extraction data[^dcat]
- **Issued (`dct:issued`):** `2022-10-31`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `ANNUAL` (`http://publications.europa.eu/resource/authority/frequency/ANNUAL`)[^dcat]
- **Distribution Date Span:** `2022-10-14` .. `2024-12-31`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Apibendrinti naudingųjų iškasenų (anhidrito/gipso, dolomito, klinties, kreidos mergelio, molio, opokos, sapropelio, žvyro, smėlio, durpės, naftos) požeminio vandens (gėlo ir mineralinio) gavybos duomenys. Išgautas išteklių kiekis pateikiamas tūkst. kubinių metrų per metus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Summarized data on groundwater (fresh and mineral) extraction of minerals (anhydrite/gypsum, dolomite, limestone, chalk marl, clay, shale, sapropel, gravel, sand, peat, oil). The extracted amount of resources is given in thousands. cubic meters per year.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PozeminioVandensGavybaKiekis](apibendrinti_pzv_gavybos_duomenys/PozeminioVandensGavybaKiekis.md) | Apibendrinti požeminio vandens gavybos duomenys | `4` | `id` | `open` | `6` | — |
| [ZemesGelmiuIstekliuLikutis](apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis.md) | Apibendrinti Žemės gelmių išteklių likučiai pagal Žemės gelmių išteklių rūšis | `2` | — | — | `4` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/pzm_vandens_gavyba.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys (https://data.gov.lt/datasets/2043/)
