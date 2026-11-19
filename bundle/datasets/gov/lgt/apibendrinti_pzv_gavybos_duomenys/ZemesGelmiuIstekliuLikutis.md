---
type: Table
title: "ZemesGelmiuIstekliuLikutis — Apibendrinti Žemės gelmių išteklių likučiai pagal Žemės gelmių išteklių rūšis"
description: "Spinta table datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis"
tags: [gov, lgt, zemesgelmiuistekliulikutis, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/lgt/pzm_vandens_gavyba.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2043/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ZemesGelmiuIstekliuLikutis — Apibendrinti Žemės gelmių išteklių likučiai pagal Žemės gelmių išteklių rūšis

- **Model:** `datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis`[^manifest]
- **Dataset:** [Apibendrinti požeminio vandens gavybos duomenys](../apibendrinti_pzv_gavybos_duomenys.md) (`datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/pzm_vandens_gavyba.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys/ZemesGelmiuIstekliuLikutis` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rusis` | `string` | — | `3` | `open` | — | Rušis | — |
| `kodas` | `integer` | — | `4` | `open` | — | Įrašo kodas | — |
| `metai` | `date` | `D` | `4` | `open` | — | Metai | — |
| `kiekis` | `number` | `m^3` | `4` | `open` | — | Požeminių išteklių likutis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/pzm_vandens_gavyba.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/pzm_vandens_gavyba.csv#L18)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/apibendrinti_pzv_gavybos_duomenys (https://data.gov.lt/datasets/2043/)
