---
type: Table
title: "Laboratorija — Įgaliotos sėklų kokybės tyrimo laboratorijos"
description: "Spinta table datasets/gov/vat/seklu_laboratorijos/Laboratorija (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/seklu_laboratorijos/Laboratorija"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/seklu_laboratorijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_laboratorijos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Laboratorija — Įgaliotos sėklų kokybės tyrimo laboratorijos

- **Model:** `datasets/gov/vat/seklu_laboratorijos/Laboratorija`[^manifest]
- **Dataset:** [datasets/gov/vat/seklu_laboratorijos](../seklu_laboratorijos.md) (`datasets/gov/vat/seklu_laboratorijos`)
- **Manifest CSV:** [datasets/gov/vat/seklu_laboratorijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/seklu_laboratorijos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/seklu_laboratorijos/Laboratorija`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`
- **Access:** `open`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/seklu_laboratorijos.csv
