---
type: Dataset
title: "Oro erdvės apribojimų duomenys"
description: "Rinkinyje pateikiami duomenys apie oro erdvės Lietuvoje apribojimus nuo 2024m."
resource: "https://get.data.gov.lt/datasets/gov/on/zonos"
tags: [gov, "on", deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/zone_rezervations.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/on/zone_rezervations.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2667/"
    title: "data.gov.lt DCAT-AP — datasets/gov/on/zonos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Oro erdvės apribojimų duomenys

Rinkinyje pateikiami duomenys apie oro erdvės Lietuvoje apribojimus nuo 2024m. kovo mėn. Nurodoma tiksli apribojimų pradžia ir pabaiga, specialiosios oro erdvės pavadinimas bei oro erdvės žemutinė ir viršutinė ribos.[^manifest]

- **Namespace:** `datasets/gov/on/zonos`[^manifest]
- **Manifest CSV:** [datasets/gov/on/zone_rezervations.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/zone_rezervations.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/on/zonos` (`deployed`)[^manifest]
- **Provider:** `on` — Oro Navigacija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2667/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/on/zonos`[^dcat]
- **Portal Title (`@lt`):** Oro erdvės apribojimų duomenys[^dcat]
- **Portal Title (`@en`):** Airspace Restriction Data (csv)[^dcat]
- **Issued (`dct:issued`):** `2024-05-24`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `WEEKLY` (`http://publications.europa.eu/resource/authority/frequency/WEEKLY`)[^dcat]
- **Distribution Date Span:** `2024-05-24` .. `2026-10-18`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami duomenys apie oro erdvės Lietuvoje apribojimus nuo 2024 m. kovo mėn. Nurodoma tiksli apribojimų pradžia ir pabaiga, specialiosios oro erdvės pavadinimas bei oro erdvės žemutinė ir viršutinė ribos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on restrictions on airspace in Lithuania. Specify the exact beginning and end of the restrictions, the name of the special airspace and the lower and upper limits of the airspace.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Apribojimas](zonos/Apribojimas.md) | Oro erdvės apribojimų duomenys | `4` | `vda_id` | — | `12` | Rinkinyje pateikiami duomenys apie oro erdvės Lietuvoje apribojimus nuo 2024m. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/on/zone_rezervations.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/on/zone_rezervations.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/on/zonos (https://data.gov.lt/datasets/2667/)
