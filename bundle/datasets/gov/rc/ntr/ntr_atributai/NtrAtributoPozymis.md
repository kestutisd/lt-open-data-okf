---
type: Table
title: "NtrAtributoPozymis — NTR atributų požymių (būtinas, galimas) klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_atributai/NtrAtributoPozymis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributoPozymis"
tags: [gov, rc, ntratributopozymis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L48"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L48"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrAtributoPozymis — NTR atributų požymių (būtinas, galimas) klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_atributai/NtrAtributoPozymis`[^manifest]
- **Dataset:** [NTR atributų klasifikatoriai](../ntr_atributai.md) (`datasets/gov/rc/ntr/ntr_atributai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L48)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributoPozymis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `atrp_poz`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atrp_poz` | `integer` | — | `4` | `open` | — | Atributo požymis | — |
| `atrp_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `atrp_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L48 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L48)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai (https://data.gov.lt/datasets/1896/)
