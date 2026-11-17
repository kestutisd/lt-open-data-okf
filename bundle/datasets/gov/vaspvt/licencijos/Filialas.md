---
type: Table
title: "Filialas — Sveikatos priežiūros įstaigų filialai"
description: "Spinta table datasets/gov/vaspvt/licencijos/Filialas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Filialas"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L61"
    last_modified: "2026-11-11T14:39:20Z"
---

# Filialas — Sveikatos priežiūros įstaigų filialai

- **Model:** `datasets/gov/vaspvt/licencijos/Filialas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L61](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L61)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Filialas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `3` | `open` | — | Eilutės dirbtinis unikalus identifikatorius | — |
| `filialo_id` | `string` | — | `2` | `open` | — | Filialo identifikatorius | — |
| `istaiga` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaiga | — |
| `juridinio_asmens_kodas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos juridinio asmens kodas | — |
| `filialo_pavadinimas` | `string` | — | `2` | `open` | — | Filialo pavadinimas | — |
| `adresas` | `string` | — | `1` | `open` | — | Buveinės adresas | — |
| `veiklos_adresas` | `string` | — | `1` | `open` | — | Veiklos adresas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `filialo_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `juridinio_asmens_kodas` | `update(property: "istaiga.ja_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `filialo_pavadinimas` | `update(property: "pavadinimas")` | `property` | `4` | `open` | — | — | — |
| `filialo_pavadinimas` | `update(property: "pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `adresas` | `update(type: "ref", ref: "/datasets/gov/rc/ar/patalpa/Patalpa")` | `type` | `4` | `open` | — | — | — |
| `veiklos_adresas` | `update(type: "ref", ref: "/datasets/gov/rc/ar/patalpa/Patalpa")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv
