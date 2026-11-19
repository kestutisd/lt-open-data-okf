---
type: Dataset
title: "Vaistinių preparatų vartojimo ir sudėties parametrai"
description: "\"Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo ir sudėties parametrus."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai"
tags: [gov, vvkt, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3802/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistu_parametrai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vaistinių preparatų vartojimo ir sudėties parametrai

"Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo ir sudėties parametrus. Duomenų rinkinį sudaro dvi lentelės: 1. Vaistinių preparatų vartojimo parametrai, 2. Vaistinių preparatų sudėties parametrai, Duomenų teikėjas - Valstybinė vaistų kontrolės tarnyba. Rinkinyje pateikiami nuo 2017 m. kaupiami duomenys. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt."[^manifest]

- **Namespace:** `datasets/gov/vvkt/vaistu_parametrai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/vaistu_parametrai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai` (`deployed`)[^manifest]
- **Provider:** `vvkt` — Valstybinė vaistų kontrolės tarnyba *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3802/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Vaistinių preparatų vartojimo ir sudėties parametrai[^dcat]
- **Portal Title (`@en`):** Parameters of administration and composition of medicinal products[^dcat]
- **Issued (`dct:issued`):** `2025-03-25`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-03-21` .. `2026-10-28`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo ir sudėties parametrus. Duomenų rinkinį sudaro dvi lentelės: 1. Vaistinių preparatų vartojimo parametrai, 2. Vaistinių preparatų sudėties parametrai. Rinkinyje pateikiami nuo 2017 m. kaupiami duomenys. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The data set contains data from the State Medicines Control Agency (IWC) on the parameters of use and composition of medicinal products. The dataset consists of two tables: 1. Parameters of administration of medicinal products, 2. Parameters of the composition of medicinal products. The package contains data that has been collected since 2017. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VaistoDoze](vaistu_parametrai/VaistoDoze.md) | Vaistinių preparatų vartojimo parametrai | `4` | `vda_prime_key` | — | `7` | "Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo parametrus. |
| [VaistoSudetis](vaistu_parametrai/VaistoSudetis.md) | Vaistinių preparatų sudėties parametrai | `4` | `vda_prime_key` | — | `12` | "Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų sudėties parametrus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkt/vaistu_parametrai (https://data.gov.lt/datasets/3802/)
