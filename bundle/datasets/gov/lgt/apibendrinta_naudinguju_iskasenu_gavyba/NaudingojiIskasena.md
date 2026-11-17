---
type: Table
title: "NaudingojiIskasena — Apibendrinti naudingųjų iškasenų gavybos duomenys"
description: "Spinta table datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba/NaudingojiIskasena (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba/NaudingojiIskasena"
tags: [gov, lgt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# NaudingojiIskasena — Apibendrinti naudingųjų iškasenų gavybos duomenys

- **Model:** `datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba/NaudingojiIskasena`[^manifest]
- **Dataset:** [Apibendrinti naudingųjų iškasenų gavybos duomenys](../apibendrinta_naudinguju_iskasenu_gavyba.md) (`datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba`)
- **Manifest CSV:** [datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lgt/apibendrinta_naudinguju_iskasenu_gavyba/NaudingojiIskasena`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lgt/naudinguju_iskasenu_gavyba.csv
