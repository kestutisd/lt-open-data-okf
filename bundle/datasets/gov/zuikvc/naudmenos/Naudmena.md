---
type: Table
title: "Naudmena — Naudmenų ribų duomeys"
description: "Pasikeitusių apleistų žemės ūkio naudmenų ribų duomeys"
tags: [gov, zuikvc, naudmena, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/naudmenos.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/naudmenos.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Naudmena — Naudmenų ribų duomeys

Pasikeitusių apleistų žemės ūkio naudmenų ribų duomeys[^manifest]

- **Model:** `datasets/gov/zuikvc/naudmenos/Naudmena`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/naudmenos](../naudmenos.md) (`datasets/gov/zuikvc/naudmenos`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/naudmenos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/naudmenos.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `aprasymas`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas` | `string` | — | `2` | `open` | — | Naudmenų ribų aprašymas | Pasikeitusių apleistų žemės ūkio naudmenų ribų aprašymas |
| `ivestas` | `datetime` | `S` | `4` | `open` | — | Naudmenų ribų žymėjimo data ir laikas | Pasikeitusių apleistų žemės ūkio naudmenų ribų žymėjimo data ir laikas |
| `koordinates` | `geometry(point,3346)` | — | `3` | `open` | — | Naudmenų taško koordinatės WKT formatu | Pasikeitusių apleistų žemės ūkio naudmenų taško koordinatės WKT formatu |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/naudmenos.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/naudmenos.csv#L8)
