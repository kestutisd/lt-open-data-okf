---
type: Dataset
title: "Vaistinių preparatų vartojimo ir sudėties parametrai"
description: "Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo ir sudėties parametrus."
resource: "https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai"
tags: [gov, vvkt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vaistinių preparatų vartojimo ir sudėties parametrai

Duomenų rinkinyje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo ir sudėties parametrus. Duomenų rinkinį sudaro dvi lentelės:

1. Vaistinių preparatų vartojimo parametrai,

2. Vaistinių preparatų sudėties parametrai,

Duomenų teikėjas - Valstybinė vaistų kontrolės tarnyba.

Rinkinyje pateikiami nuo 2017 m. kaupiami duomenys.

- **Namespace:** `datasets/gov/vvkt/vaistu_parametrai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvkt/vaistu_parametrai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkt/vaistu_parametrai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkt/vaistu_parametrai`
- **Parent Namespace (`ns`):** Valstybinė vaistų kontrolės tarnyba (`datasets/gov/vvkt`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VaistoDoze](vaistu_parametrai/VaistoDoze.md) | Vaistinių preparatų vartojimo parametrai | `4` | `vda_prime_key` | — | 7 | Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų vartojimo parametrus. |
| [VaistoSudetis](vaistu_parametrai/VaistoSudetis.md) | Vaistinių preparatų sudėties parametrai | `4` | `vda_prime_key` | — | 12 | Lentelėje pateikiami Valstybinės vaistų kontrolės tarnybos (VVKT) duomenys apie vaistinių preparatų sudėties parametrus. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkt/vaistu_parametrai.csv
