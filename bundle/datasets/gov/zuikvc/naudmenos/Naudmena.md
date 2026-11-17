---
type: Table
title: "Naudmena — Naudmenų ribų duomeys"
description: "Pasikeitusių apleistų žemės ūkio naudmenų ribų duomeys"
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/naudmenos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/naudmenos.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Naudmena — Naudmenų ribų duomeys

Pasikeitusių apleistų žemės ūkio naudmenų ribų duomeys

- **Model:** `datasets/gov/zuikvc/naudmenos/Naudmena`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/naudmenos](../naudmenos.md) (`datasets/gov/zuikvc/naudmenos`)
- **Manifest CSV:** [datasets/gov/zuikvc/naudmenos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/naudmenos.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `aprasymas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas` | `string` | — | `2` | `open` | — | Naudmenų ribų aprašymas | Pasikeitusių apleistų žemės ūkio naudmenų ribų aprašymas |
| `ivestas` | `datetime` | `S` | `4` | `open` | — | Naudmenų ribų žymėjimo data ir laikas | Pasikeitusių apleistų žemės ūkio naudmenų ribų žymėjimo data ir laikas |
| `koordinates` | `geometry(point,3346)` | — | `3` | `open` | — | Naudmenų taško koordinatės WKT formatu | Pasikeitusių apleistų žemės ūkio naudmenų taško koordinatės WKT formatu |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/naudmenos.csv
