---
type: Table
title: "JettyOrPier — Duomenys apie prieplaukas"
description: "Šiame sluoksnyje pateikiami duomenys apie prieplaukas Nemune nuo Baltarusijos pasienio iki Kauno."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/JettyOrPier"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L48"
    last_modified: "2026-11-11T14:39:20Z"
---

# JettyOrPier — Duomenys apie prieplaukas

Šiame sluoksnyje pateikiami duomenys apie prieplaukas Nemune nuo Baltarusijos pasienio iki Kauno.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/JettyOrPier`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L48)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/JettyOrPier`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `fid_1` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `x` | `number` | `m` | `4` | `open` | — | x koordinatė | — |
| `y` | `number` | `m` | `4` | `open` | — | y koordinatė | — |
| `name_lt` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `notes_lt` | `string` | — | `4` | `open` | — | Pastabos | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name_lt` | `update(property: "name_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `notes_lt` | `update(property: "notes_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
