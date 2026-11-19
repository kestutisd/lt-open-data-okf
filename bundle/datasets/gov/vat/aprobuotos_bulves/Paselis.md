---
type: Table
title: "Paselis — Pateikiama informacija apie sėkinių bulvių aprobuotus pasėlius (veislę, aprobuotą plotą, ha, pripažintą kategoriją, išbrokuotą plotą, ha, iš viso aprobuotą plotą (su išbrokuotais), ha)"
description: "Spinta table datasets/gov/vat/aprobuotos_bulves/Paselis (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/aprobuotos_bulves/Paselis"
tags: [gov, vat, paselis, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r29_bulv_aprob.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r29_bulv_aprob.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1885/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/aprobuotos_bulves"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Paselis — Pateikiama informacija apie sėkinių bulvių aprobuotus pasėlius (veislę, aprobuotą plotą, ha, pripažintą kategoriją, išbrokuotą...

- **Model:** `datasets/gov/vat/aprobuotos_bulves/Paselis`[^manifest]
- **Dataset:** [Ataskaita apie sėklinių bulvių aprobuotus pasėlius](../aprobuotos_bulves.md) (`datasets/gov/vat/aprobuotos_bulves`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r29_bulv_aprob.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r29_bulv_aprob.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/aprobuotos_bulves/Paselis` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Aprobavimo eilės numeris | — |
| `veisle` | `string` | — | `2` | `open` | — | Augalo veislė | — |
| `kategorija` | `string` | — | `3` | `open` | — | Kategorijos kodas | — |
| `aprobuotas_plotas` | `number` | `ha` | `4` | `open` | — | Aprobuotas plotas, ha | — |
| `isbrokuotas_plotas` | `number` | `ha` | `4` | `open` | — | Išbrokuotas plotas, ha | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veisle` | `update(base: "/datasets/gov/vat/saugomos_veisles/Veisles", type: "ref", ref: "/datasets/gov/vat/saugomos_veisles/Veisles")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r29_bulv_aprob.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r29_bulv_aprob.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/aprobuotos_bulves (https://data.gov.lt/datasets/1885/)
