---
type: Table
title: "SklypoRiba — KŽS ribų pasikeitimų duomeys"
description: "Išankstinių kontrolinių žemės sklypų (KŽS) ribų pasikeitimų duomeys"
tags: [gov, zuikvc, sklyporiba, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/sklypu_ribos.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/sklypu_ribos.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# SklypoRiba — KŽS ribų pasikeitimų duomeys

Išankstinių kontrolinių žemės sklypų (KŽS) ribų pasikeitimų duomeys[^manifest]

- **Model:** `datasets/gov/zuikvc/sklypu_ribos/SklypoRiba`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/sklypu_ribos](../sklypu_ribos.md) (`datasets/gov/zuikvc/sklypu_ribos`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/sklypu_ribos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/sklypu_ribos.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas` | `string` | — | `3` | `open` | — | KŽS ribų pasikeitimų aprašymas | — |
| `ivestas` | `datetime` | `S` | `4` | `open` | — | KŽS ribų pasikeitimų aprašymo data ir laikas | — |
| `koordinates` | `geometry(point,3346)` | — | `3` | `open` | — | KŽS ribų pasikeitimų orientacinė vieta WKT formatu | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/sklypu_ribos.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/sklypu_ribos.csv#L8)
