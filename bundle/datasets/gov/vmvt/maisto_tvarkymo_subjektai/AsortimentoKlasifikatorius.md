---
type: Table
title: "AsortimentoKlasifikatorius — Produkto asortimento klasifikatorius pagal VMVT FIS"
description: "Spinta table datasets/gov/vmvt/maisto_tvarkymo_subjektai/AsortimentoKlasifikatorius (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai/AsortimentoKlasifikatorius"
tags: [gov, vmvt, asortimentoklasifikatorius, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L21"
    title: "atviriduomenys/manifest — datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L21"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/802/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmvt/maisto_tvarkymo_subjektai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# AsortimentoKlasifikatorius — Produkto asortimento klasifikatorius pagal VMVT FIS

- **Model:** `datasets/gov/vmvt/maisto_tvarkymo_subjektai/AsortimentoKlasifikatorius`[^manifest]
- **Dataset:** [Duomenys apie maisto tvarkymo subjektus](../maisto_tvarkymo_subjektai.md) (`datasets/gov/vmvt/maisto_tvarkymo_subjektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L21)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/maisto_tvarkymo_subjektai/AsortimentoKlasifikatorius` (`deployed`)[^manifest]
- **Provider:** `vmvt` — Valstybinė maisto ir veterinarijos tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Asortimento kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Asortimento pavadinimas pagal VMVT FIS sąrašą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L21 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/maisto_tvarkymo_subjektai.csv#L21)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmvt/maisto_tvarkymo_subjektai (https://data.gov.lt/datasets/802/)
