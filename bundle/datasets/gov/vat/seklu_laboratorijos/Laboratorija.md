---
type: Table
title: "Laboratorija — Įgaliotos sėklų kokybės tyrimo laboratorijos"
description: "Spinta table datasets/gov/vat/seklu_laboratorijos/Laboratorija (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/seklu_laboratorijos/Laboratorija"
tags: [gov, vat, laboratorija, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_laboratorijos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/seklu_laboratorijos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1870/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/seklu_laboratorijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Laboratorija — Įgaliotos sėklų kokybės tyrimo laboratorijos

- **Model:** `datasets/gov/vat/seklu_laboratorijos/Laboratorija`[^manifest]
- **Dataset:** [Įgaliotos sėklų kokybės tyrimo laboratorijos](../seklu_laboratorijos.md) (`datasets/gov/vat/seklu_laboratorijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/seklu_laboratorijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_laboratorijos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/seklu_laboratorijos/Laboratorija` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `laboratorija` | `string` | — | `2` | `open` | — | Įgaliotosios laboratorijos pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Įgaliotosios laboratorijos adresas | — |
| `pazymejimo_nr` | `string` | — | `2` | `open` | — | Pažymėjimo Nr. | — |
| `pazymejimo_data` | `date` | `D` | `4` | `open` | — | Pažymėjimo data | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Laboratorijos koordinatės (LKS) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `laboratorija` | `update(base: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `adresas` | `update(base: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas", type: "ref", ref: "/datasets/gov/rc/ar/adresotaskas/AdresoTaskas")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/seklu_laboratorijos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_laboratorijos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/seklu_laboratorijos (https://data.gov.lt/datasets/1870/)
