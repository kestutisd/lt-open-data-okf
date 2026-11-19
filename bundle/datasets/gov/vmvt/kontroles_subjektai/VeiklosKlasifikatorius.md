---
type: Table
title: "VeiklosKlasifikatorius — VMVT veiklos klasifikatorius"
description: "Spinta table datasets/gov/vmvt/kontroles_subjektai/VeiklosKlasifikatorius (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai/VeiklosKlasifikatorius"
tags: [gov, vmvt, veiklosklasifikatorius, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/kontroles_subjektai.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1679/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/kontroles_subjektai"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# VeiklosKlasifikatorius — VMVT veiklos klasifikatorius

- **Model:** `datasets/gov/vmvt/kontroles_subjektai/VeiklosKlasifikatorius`[^manifest]
- **Dataset:** [Valstybinės veterinarinės kontrolės subjektų duomenys](../kontroles_subjektai.md) (`datasets/gov/vmvt/kontroles_subjektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/kontroles_subjektai.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/kontroles_subjektai/VeiklosKlasifikatorius` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | VMVT veiklos kodas | — |
| `kategorija` | `string` | — | `4` | `open` | — | VMVT veiklos kategorija | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | VMVT veiklos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/kontroles_subjektai.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/kontroles_subjektai.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/kontroles_subjektai (https://data.gov.lt/datasets/1679/)
