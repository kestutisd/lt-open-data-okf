---
type: Dataset
title: "Objektų pritaikomumo negalią turintiems asmenims vertinimai"
description: "Rinkinyje pateikiami nuo 2022 metų gruodžio 1 dienos kaupiami duomenys iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio."
resource: "https://get.data.gov.lt/datasets/gov/anta/stasis"
tags: [gov, anta, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/anta/anta_stasis_objektu_vertinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Objektų pritaikomumo negalią turintiems asmenims vertinimai

Rinkinyje pateikiami nuo 2022 metų gruodžio 1 dienos kaupiami duomenys iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. Duomenų rinkinį sudaro dvi lentelės:

1. „Objektai“ – duomenys apie vertinamus pastatus,

2. „Objektų vertinimai“ – objektų pritaikomumo negalią turintiems asmenis vertinimai.

Duomenų teikėjas – Asmens su negalia teisių apsaugos agentūra prie Lietuvos Respublikos socialinės apsaugos ir darbo ministerijos.

- **Namespace:** `datasets/gov/anta/stasis`[^manifest]
- **Manifest CSV:** [datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/anta/anta_stasis_objektu_vertinimas.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/anta/stasis`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Objektas](stasis/Objektas.md) | Objektai | `4` | `objekto_id` | — | 10 | Duomenys apie įvairios paskirties objektus iš Asmens su negalia teisių apsaugos agentūros statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. |
| [Vertinimas](stasis/Vertinimas.md) | Objektų vertinimai | `4` | `vda_prime_key` | — | 5 | Objektų pritaikomumo negaliai įverčiai iš Asmens su negalia teisių apsaugos agentūros, statinių prieinamumo neįgaliems stebėsenos ir kontrolės įrankio. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/anta/anta_stasis_objektu_vertinimas.csv
