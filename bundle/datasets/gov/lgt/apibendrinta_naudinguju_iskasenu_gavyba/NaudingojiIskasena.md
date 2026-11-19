---
type: Table
title: "NaudingojiIskasena — Apibendrinti naudingųjų iškasenų gavybos duomenys"
description: "Spinta table datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba/NaudingojiIskasena (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba/NaudingojiIskasena"
tags: [gov, lgt, naudingojiiskasena, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1340/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NaudingojiIskasena — Apibendrinti naudingųjų iškasenų gavybos duomenys

- **Model:** `datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba/NaudingojiIskasena`[^manifest]
- **Dataset:** [Apibendrinti naudingųjų iškasenų gavybos duomenys](../apibendrinta_naudinguju_iskasenu_gavyba.md) (`datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba`)[^manifest]
- **Manifest CSV:** [datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba/NaudingojiIskasena` (`deployed`)[^manifest]
- **Provider:** `lgt` — Lietuvos geologijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Išteklių rūšies kodas | — |
| `rusis` | `string` | — | `4` | `open` | — | Išteklių rušis | — |
| `mato_vnt` | `string` | — | `2` | `open` | — | Mato vienetas | — |
| `metai` | `integer` | — | `2` | `open` | — | Gavybos metai | — |
| `kiekis` | `integer` | — | `2` | `open` | — | Išgautas kiekis | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba (https://data.gov.lt/datasets/1340/)
