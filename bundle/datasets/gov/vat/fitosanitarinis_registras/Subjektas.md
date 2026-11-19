---
type: Table
title: "Subjektas — Pateikiama informacija apie ūkio subjektus, įregistruotus Fitosanitariniame registe (ūkio subjekto atpažinties kodas; pavadinimas; veiklos vykdymo adresas; veiklos ir produkcijos rūšis)"
description: "Spinta table datasets/gov/vat/fitosanitarinis_registras/Subjektas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarinis_registras/Subjektas"
tags: [gov, vat, subjektas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1858/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarinis_registras"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Subjektas — Pateikiama informacija apie ūkio subjektus, įregistruotus Fitosanitariniame registe (ūkio subjekto atpažinties kodas...

- **Model:** `datasets/gov/vat/fitosanitarinis_registras/Subjektas`[^manifest]
- **Dataset:** [Fitosanitarinio registro viešieji duomenys](../fitosanitarinis_registras.md) (`datasets/gov/vat/fitosanitarinis_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarinis_registras/Subjektas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `subjektas` | `string` | — | `2` | `open` | — | Subjekto pavadinimas | — |
| `juridinis` | `boolean` | — | `4` | `open` | — | Ūkio subjekto tipas | — |
| `tel_nr` | `string` | — | `1` | `open` | — | Telefono numeris | — |
| `adresas` | `string` | — | `2` | `open` | — | Ūkio subjekto adresas | — |
| `fitosanitarinis_nr` | `string` | — | `1` | `open` | — | Fitosanitarinio registro Nr. | — |
| `specializacija` | `string` | — | `2` | `open` | — | Subjekto specializacija | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Ūkio subjekto koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `specializacija` | `"update(property: ""specializacija[]"", type: ""array"", source: ""Specializacija"")"` | `property` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r2_fitosanitarinis_registras.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarinis_registras (https://data.gov.lt/datasets/1858/)
