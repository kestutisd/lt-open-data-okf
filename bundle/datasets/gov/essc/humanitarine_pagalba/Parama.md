---
type: Table
title: "Parama — Humanitarinės pagalbos teikimas trečiosioms šalims"
description: "Spinta table datasets/gov/essc/humanitarine_pagalba/Parama (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/essc/humanitarine_pagalba/Parama"
tags: [gov, essc, parama, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/humanitarine_pagalba.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/essc/humanitarine_pagalba.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Parama — Humanitarinės pagalbos teikimas trečiosioms šalims

- **Model:** `datasets/gov/essc/humanitarine_pagalba/Parama`[^manifest]
- **Dataset:** [Humanitarinės pagalbos teikimas trečiosioms šalims](../humanitarine_pagalba.md) (`datasets/gov/essc/humanitarine_pagalba`)[^manifest]
- **Manifest CSV:** [datasets/gov/essc/humanitarine_pagalba.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/humanitarine_pagalba.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/essc/humanitarine_pagalba/Parama` (`deployed`)[^manifest]
- **Provider:** `essc` — Ekstremalių sveikatai situacijų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Donuotos priemonės identifikatorius | — |
| `paramos_gavejas` | `string` | — | `4` | `open` | — | Paskirtos paramos gavėjas | — |
| `paramos_teikejas` | `string` | — | `4` | `open` | — | Paskirtos paramos teikėjas | — |
| `data` | `date` | `D` | `4` | `open` | — | Paramos teikimo data | — |
| `paramos_rusis` | `string` | — | `4` | `open` | — | Paramos rūšis | — |
| `donuojamu_priemoniu_aprasymas` | `string` | — | `3` | `open` | — | Apibūdinamos donuojamos priemonės | — |
| `verte_eur` | `number` | — | `2` | `open` | — | Donuojamų priemonių vertė eurais | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `verte_eur` | `update(type: "money", ref: "EUR")` | `type, ref` | `4` | — | `spinta: 40` | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/essc/humanitarine_pagalba.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/humanitarine_pagalba.csv#L4)
