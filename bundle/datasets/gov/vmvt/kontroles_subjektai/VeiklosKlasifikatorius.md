---
type: Table
title: "VeiklosKlasifikatorius — VMVT veiklos klasifikatorius"
description: "Spinta table datasets/gov/vmvt/kontroles_subjektai/VeiklosKlasifikatorius (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai/VeiklosKlasifikatorius"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/kontroles_subjektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# VeiklosKlasifikatorius — VMVT veiklos klasifikatorius

- **Model:** `datasets/gov/vmvt/kontroles_subjektai/VeiklosKlasifikatorius`[^manifest]
- **Dataset:** [Valstybinės veterinarinės kontrolės subjektų duomenys](../kontroles_subjektai.md) (`datasets/gov/vmvt/kontroles_subjektai`)
- **Manifest CSV:** [datasets/gov/vmvt/kontroles_subjektai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai/VeiklosKlasifikatorius`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | VMVT veiklos kodas | — |
| `kategorija` | `string` | — | `4` | `open` | — | VMVT veiklos kategorija | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | VMVT veiklos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/kontroles_subjektai.csv
