---
type: Table
title: "NtrAtributas — NTR atributų klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_atributai/NtrAtributas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributas"
tags: [gov, rc, ntratributas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrAtributas — NTR atributų klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_atributai/NtrAtributas`[^manifest]
- **Dataset:** [NTR atributų klasifikatoriai](../ntr_atributai.md) (`datasets/gov/rc/ntr/ntr_atributai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `atri_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atri_kodas` | `integer` | — | `4` | `open` | — | Atributo kodas | — |
| `atrt_tipas` | `ref` | [NtrAtributoTipas](NtrAtributoTipas.md) (`level=4 UUID`: `atrt_tipas._id`) | `4` | `open` | — | Atributo tipas | — |
| `atri_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `atri_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `atri_eilnr` | `integer` | — | `4` | `open` | — | Eilės numeris aplikacijose | — |
| `vien_kodas` | `ref` | [NtrMatavimoVnt](../ntr_kiti_klasifikatoriai/NtrMatavimoVnt.md) (`level=4 UUID`: `vien_kodas._id`) | `4` | `open` | — | Matavimo vieneto kodas | — |
| `atri_koef` | `number` | — | `4` | `open` | — | Koeficientas | — |
| `atri_poz` | `ref` | [NtrAtributoPozymis](NtrAtributoPozymis.md) (`level=4 UUID`: `atri_poz._id`) | `4` | `open` | — | Formatavimo požymis | — |
| `atri_formatas` | `string` | — | `3` | `open` | — | Įvedimo formatas | — |
| `atri_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `atri_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `atri_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai (https://data.gov.lt/datasets/1896/)
