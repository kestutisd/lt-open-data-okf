---
type: Dataset
title: "Objektų pritaikomumo negalią turintiems asmenims vertinimai"
description: "\"Rinkinyje pateikiami nuo 2022 metų gruodžio 1 dienos kaupiami duomenys iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio."
resource: "https://get.data.gov.lt/datasets/gov/anta/stasis"
tags: [gov, anta, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3870/"
    title: "data.gov.lt DCAT-AP — datasets/gov/anta/stasis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Objektų pritaikomumo negalią turintiems asmenims vertinimai

"Rinkinyje pateikiami nuo 2022 metų gruodžio 1 dienos kaupiami duomenys iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. Duomenų rinkinį sudaro dvi lentelės: 1. „Objektai“ – duomenys apie vertinamus pastatus, 2. „Objektų vertinimai“ – objektų pritaikomumo negalią turintiems asmenis vertinimai. Duomenų teikėjas – Asmens su negalia teisių apsaugos agentūra prie Lietuvos Respublikos socialinės apsaugos ir darbo ministerijos. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. "[^manifest]

- **Namespace:** `datasets/gov/anta/stasis`[^manifest]
- **Manifest CSV:** [datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anta/stasis` (`deployed`)[^manifest]
- **Provider:** `anta` — Asmens su negalia teisių apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3870/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/anta/stasis`[^dcat]
- **Portal Title (`@lt`):** Objektų pritaikomumo negalią turintiems asmenims vertinimai[^dcat]
- **Portal Title (`@en`):** Assessment of accessibility of objects to persons with disabilities[^dcat]
- **Issued (`dct:issued`):** `2025-07-17`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-03` .. `2026-10-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami nuo 2022 metų gruodžio 1 dienos kaupiami duomenys iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. Duomenų rinkinį sudaro dvi lentelės: 1. „Objektai“ – duomenys apie vertinamus pastatus, 2. „Objektų vertinimai“ – objektų pritaikomumo negalią turintiems asmenis vertinimai. Duomenų teikėjas – Asmens su negalia teisių apsaugos agentūra prie Lietuvos Respublikos socialinės apsaugos ir darbo ministerijos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package includes data collected from December 1, 2022, from the tool for monitoring and controlling the accessibility of structures of the Agency for the Protection of the Rights of Persons with Disabilities. The dataset consists of two tables: 1. '“Objects” means data on buildings under assessment, 2.' “Object assessments” means assessments of the applicability of objects to persons with disabilities. Data provider shall mean the Agency for the Protection of Rights of Persons with Disabilities under the Ministry of Social Security and Labour of the Republic of Lithuania. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Objektas](stasis/Objektas.md) | Objektai | `4` | `objekto_id` | — | `10` | "Duomenys apie įvairios paskirties objektus iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. |
| [Vertinimas](stasis/Vertinimas.md) | Objektų vertinimai | `4` | `vda_prime_key` | — | `5` | "Objektų pritaikomumo negaliai įverčiai iš Asmens su negalia teisių apsaugos agentūros, statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/anta/stasis (https://data.gov.lt/datasets/3870/)
