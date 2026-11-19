---
type: Table
title: "NtrNaudojimoPubudis — NTR naudojimo pobūdžiai"
description: "Spinta table datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoPubudis (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoPubudis"
tags: [gov, rc, ntrnaudojimopubudis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1898/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_naudojimo_budai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrNaudojimoPubudis — NTR naudojimo pobūdžiai

- **Model:** `datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoPubudis`[^manifest]
- **Dataset:** [NTR paskirčių klasifikatoriai](../ntr_naudojimo_budai.md) (`datasets/gov/rc/ntr/ntr_naudojimo_budai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_naudojimo_budai/NtrNaudojimoPubudis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `npob_pobudis`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `npob_pobudis` | `integer` | — | `4` | `open` | — | Naudojimo pobūdis | — |
| `naub_budas` | `ref` | [NtrNaudojimoBudas](NtrNaudojimoBudas.md) (`level=4 UUID`: `naub_budas._id`) | `4` | `open` | — | Naudojimo būdas | — |
| `npob_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `npob_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `npob_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `npob_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `npob_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai (ilgas) | — |
| `npob_data_nuo` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja nuo | — |
| `npob_data_iki` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_naudojimo_budai.csv#L12)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_naudojimo_budai (https://data.gov.lt/datasets/1898/)
