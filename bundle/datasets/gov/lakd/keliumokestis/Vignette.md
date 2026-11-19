---
type: Table
title: "Vignette — Kelių naudotojų mokesčio pardavimų statistika"
description: "Spinta table datasets/gov/lakd/keliumokestis/Vignette (5 columns)."
tags: [gov, lakd, vignette, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliumokestis.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lakd/keliumokestis.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Vignette — Kelių naudotojų mokesčio pardavimų statistika

- **Model:** `datasets/gov/lakd/keliumokestis/Vignette`[^manifest]
- **Dataset:** [datasets/gov/lakd/keliumokestis](../keliumokestis.md) (`datasets/gov/lakd/keliumokestis`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/keliumokestis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliumokestis.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vinjetes_rusis, vinjetes_serija`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kilmes_salis` | `string` | — | `2` | `open` | — | Transporto priemonės registracijos šalis | — |
| `kategorija` | `string` | — | `2` | `open` | — | Transporto priemonės kategorija | — |
| `vinjetes_rusis` | `string` | — | `4` | `open` | — | Vinjetės laikotarpis | — |
| `vinjetes_serija` | `string` | — | `4` | `open` | — | Vinjetės serija | — |
| `kiekis` | `integer` | `U` | `4` | `open` | — | Pardavimų kiekis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vinjetes_rusis` | `"Diena"` | — | — | Diena | — |
| `vinjetes_rusis` | `"Savaitė"` | — | — | Savaitė | — |
| `vinjetes_rusis` | `"Menuo"` | — | — | Mėnuo | — |
| `vinjetes_rusis` | `"Metai"` | — | — | Metai | — |
| `vinjetes_serija` | `"A"` | — | — | M2; N1; N1–N3 (iki 16 t. įsk. ž. ū. v. subjektai); SPEC. TR. PR. | — |
| `vinjetes_serija` | `"B"` | — | — | M3; N2; N3 | — |
| `vinjetes_serija` | `"C"` | — | — | M2; N1; N1–N3 (iki 16 t. įsk. ž. ū. v. subjektai); SPEC. TR. PR. | — |
| `vinjetes_serija` | `"D"` | — | — | M3 (> 8 ≤ 22 sėdimos vietos keleiviams, ≥ 5t.); N2 (≥ EURO IV) | — |
| `vinjetes_serija` | `"E"` | — | — | M3 (> 22 sėdimos vietos keleiviams); N2 (EURO 0, I, II, III); N3 (≥ EURO IV) | — |
| `vinjetes_serija` | `"F"` | — | — | N3 (EURO 0, I, II, III) | — |
| `vinjetes_serija` | `"G"` | — | — | M2; N1; N1–N3 (iki 16 t. įsk. ž. ū. v. subjektai); SPEC. TR. PR. | — |
| `vinjetes_serija` | `"H"` | — | — | M3 (> 8 ≤ 22 sėdimos vietos keleiviams, ≥ 5t.); N2 (≥ EURO IV) | — |
| `vinjetes_serija` | `"I"` | — | — | M3 (> 22 sėdimos vietos keleiviams); N2 (EURO 0, I, II, III); N3 (≥ EURO IV) | — |
| `vinjetes_serija` | `"J"` | — | — | N3 (EURO 0, I, II, III) | — |
| `vinjetes_serija` | `"K"` | — | — | M2; N1; N1–N3 (iki 16 t. įsk. ž. ū. v. subjektai) ir N1 SPEC. TR. PR. | — |
| `vinjetes_serija` | `"L"` | — | — | SPEC. TR. PR., išskyrus N1 kategoriją | — |
| `vinjetes_serija` | `"M"` | — | — | M3 (> 8 ≤ 22 sėdimos vietos keleiviams, ≥ 5t.); N2 (≥ EURO IV) | — |
| `vinjetes_serija` | `"N"` | — | — | M3 (> 22 sėdimos vietos keleiviams); N2 (EURO 0, I, II, III); N3 (≥ EURO IV) | — |
| `vinjetes_serija` | `"O"` | — | — | N3 (EURO 0, I, II, III) | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kilmes_salis` | `create(property: "tp", type: "ref", ref: "/datasets/gov/regitra/tp/TransportoPriemone[kilmes_salis]")` | `type` | `4` | — | — | — | — |
| `kilmes_salis` | `update(property: "tp.kilmes_salis", type: "")` | `property` | `4` | — | — | — | — |
| `kategorija` | `update(property: "tp.kategorija", type: "")` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/keliumokestis.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/keliumokestis.csv#L6)
