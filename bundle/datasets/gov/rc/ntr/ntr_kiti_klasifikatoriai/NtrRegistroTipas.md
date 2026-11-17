---
type: Table
title: "NtrRegistroTipas — NTR registrų tipai"
description: "Spinta table datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrRegistroTipas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrRegistroTipas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L40"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrRegistroTipas — NTR registrų tipai

- **Model:** `datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrRegistroTipas`[^manifest]
- **Dataset:** [Kiti NTR klasifikatoriai](../ntr_kiti_klasifikatoriai.md) (`datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv#L40)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai/NtrRegistroTipas`
- **Primary Key (`ref`):** `regt_tipas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `regt_tipas` | `integer` | — | `4` | `open` | — | Registro tipas | — |
| `regt_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `regt_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `regt_generuoti` | `integer` | — | `4` | `open` | — | Registro tipo generavimo požymis (0-leidžia pasirinkti, 1-neleidžia pasirinkti) | — |
| `regt_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `regt_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `regt_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |
| `regt_santrumpa` | `string` | — | `3` | `open` | — | Santrumpa | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `regt_generuoti` | `0` | — | — | Leidžia pasirinkti | — |
| `regt_generuoti` | `1` | — | — | Neleidžia pasirinkti | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_kiti_klasifikatoriai.csv
