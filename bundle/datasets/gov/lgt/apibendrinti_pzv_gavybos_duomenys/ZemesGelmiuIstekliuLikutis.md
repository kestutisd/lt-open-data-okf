---
type: Table
title: "ZemesGelmiuIstekliuLikutis — Apibendrinti Žemės gelmių išteklių likučiai pagal Žemės gelmių išteklių rūšis"
description: "Spinta table datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis"
tags: [gov, lgt, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/pzm_vandens_gavyba.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZemesGelmiuIstekliuLikutis — Apibendrinti Žemės gelmių išteklių likučiai pagal Žemės gelmių išteklių rūšis

- **Model:** `datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis`[^manifest]
- **Dataset:** [Apibendrinti požeminio vandens gavybos duomenys](../apibendrinti_pzv_gavybos_duomenys.md) (`datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys`)
- **Manifest CSV:** [datasets/gov/lgt/pzm_vandens_gavyba.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rusis` | `string` | — | `3` | `open` | — | Rušis | — |
| `kodas` | `integer` | — | `4` | `open` | — | Įrašo kodas | — |
| `metai` | `date` | `D` | `4` | `open` | — | Metai | — |
| `kiekis` | `number` | `m^3` | `4` | `open` | — | Požeminių išteklių likutis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/pzm_vandens_gavyba.csv
