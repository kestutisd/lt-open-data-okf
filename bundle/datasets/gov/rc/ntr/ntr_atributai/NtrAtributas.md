---
type: Table
title: "NtrAtributas — NTR atributų klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_atributai/NtrAtributas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrAtributas — NTR atributų klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_atributai/NtrAtributas`[^manifest]
- **Dataset:** [NTR atributų klasifikatoriai](../ntr_atributai.md) (`datasets/gov/rc/ntr/ntr_atributai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrAtributas`
- **Primary Key (`ref`):** `atri_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atri_kodas` | `integer` | — | `4` | `open` | — | Atributo kodas | — |
| `atrt_tipas` | `ref` | [NtrAtributoTipas](NtrAtributoTipas.md) | `4` | `open` | — | Atributo tipas | — |
| `atri_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `atri_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `atri_eilnr` | `integer` | — | `4` | `open` | — | Eilės numeris aplikacijose | — |
| `vien_kodas` | `ref` | [/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrMatavimoVnt](../ntr_kiti_klasifikatoriai/NtrMatavimoVnt.md) | `4` | `open` | — | Matavimo vieneto kodas | — |
| `atri_koef` | `number` | — | `4` | `open` | — | Koeficientas | — |
| `atri_poz` | `ref` | [NtrAtributoPozymis](NtrAtributoPozymis.md) | `4` | `open` | — | Formatavimo požymis | — |
| `atri_formatas` | `string` | — | `3` | `open` | — | Įvedimo formatas | — |
| `atri_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `atri_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `atri_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv
