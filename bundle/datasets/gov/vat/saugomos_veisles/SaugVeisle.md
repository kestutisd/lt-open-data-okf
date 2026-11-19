---
type: Table
title: "SaugVeisle — Saugomų augalų veislių sąrašas."
description: "Spinta table datasets/gov/vat/saugomos_veisles/SaugVeisle (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles/SaugVeisle"
tags: [gov, vat, saugveisle, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L61"
    title: "atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv#L61"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1868/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/saugomos_veisles"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# SaugVeisle — Saugomų augalų veislių sąrašas.

- **Model:** `datasets/gov/vat/saugomos_veisles/SaugVeisle`[^manifest]
- **Dataset:** [Nacionalinis saugomų augalų veislių sąrašas, Lietuvos Respublikoje saugomų augalų veislių...](../saugomos_veisles.md) (`datasets/gov/vat/saugomos_veisles`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/saugomos_veisles.csv#L61](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L61)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles/SaugVeisle` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eil Nr | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Paraiškos Nr | — |
| `rusis` | `string` | — | `2` | `open` | — | Augalo rūšis | — |
| `veisle` | `string` | — | `2` | `open` | — | Veislės pavadinimas | — |
| `selekcininkas` | `string` | — | `1` | `open` | — | Selekcininkas | — |
| `igaliotasis_atstovas` | `string` | — | `1` | `open` | — | Įgaliotasis atstovas | — |
| `galiojimas` | `string` | — | `1` | `open` | — | Galiojimo laikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv#L61 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L61)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/saugomos_veisles (https://data.gov.lt/datasets/1868/)
