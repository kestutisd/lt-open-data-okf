---
type: Table
title: "NtrAtributoReiksme — NTR atributų reikšmių klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_atributai/NtrAtributoReiksme (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributoReiksme"
tags: [gov, rc, ntratributoreiksme, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L17"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L17"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrAtributoReiksme — NTR atributų reikšmių klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_atributai/NtrAtributoReiksme`[^manifest]
- **Dataset:** [NTR atributų klasifikatoriai](../ntr_atributai.md) (`datasets/gov/rc/ntr/ntr_atributai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L17)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributoReiksme` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `atri_kodas, reik_reiksme`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atri_kodas` | `ref` | [NtrAtributas](NtrAtributas.md) (`level=4 UUID`: `atri_kodas._id`) | `4` | `open` | — | Atributo kodas | — |
| `reik_reiksme` | `integer` | — | `3` | `open` | — | Reikšmės kodas | — |
| `reik_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `reik_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `reik_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `reik_naudojama` | `integer` | — | `4` | `open` | — | Požymis, ar atributo reikšmė naudojama | — |
| `reik_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `reik_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `reik_naudojama` | `1` | — | — | Ne | — |
| `reik_naudojama` | `0` | — | — | Taip | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L17 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L17)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai (https://data.gov.lt/datasets/1896/)
