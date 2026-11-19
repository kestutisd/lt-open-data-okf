---
type: Table
title: "NtrTeisesTipas — NTR teisių ir suvaržymų tipai"
description: "Spinta table datasets/gov/rc/ntr/ntr_teises/NtrTeisesTipas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises/NtrTeisesTipas"
tags: [gov, rc, ntrteisestipas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1899/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_teises"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrTeisesTipas — NTR teisių ir suvaržymų tipai

- **Model:** `datasets/gov/rc/ntr/ntr_teises/NtrTeisesTipas`[^manifest]
- **Dataset:** [NTR teisių tipų ir teisių potipių klasifikatoriai](../ntr_teises.md) (`datasets/gov/rc/ntr/ntr_teises`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_teises.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises/NtrTeisesTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `teit_tipas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teit_tipas` | `integer` | — | `4` | `open` | — | Teisės (suvaržymo) tipas | — |
| `teit_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `teit_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `teit_eilnr` | `integer` | — | `4` | `open` | — | Eilės numeris aplikacijose | — |
| `teit_poz` | `integer` | — | `3` | `open` | — | Aplikacijos požymis | — |
| `teit_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `teit_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `teit_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai (ilgas) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_teises (https://data.gov.lt/datasets/1899/)
