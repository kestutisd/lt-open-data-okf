---
type: Table
title: "NtrTeisesPotipis — NTR teisių ir suvaržymų potipiai"
description: "Spinta table datasets/gov/rc/ntr/ntr_teises/NtrTeisesPotipis (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises/NtrTeisesPotipis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L14"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrTeisesPotipis — NTR teisių ir suvaržymų potipiai

- **Model:** `datasets/gov/rc/ntr/ntr_teises/NtrTeisesPotipis`[^manifest]
- **Dataset:** [NTR teisių tipų ir teisių potipių klasifikatoriai](../ntr_teises.md) (`datasets/gov/rc/ntr/ntr_teises`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_teises.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L14)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises/NtrTeisesPotipis`
- **Primary Key (`ref`):** `teit_tipas, teip_potipis`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teit_tipas` | `ref` | [NtrTeisesTipas](NtrTeisesTipas.md) | `4` | `open` | — | Teisės (suvaržymo) tipas | — |
| `teip_potipis` | `integer` | — | `4` | `open` | — | Teisės (suvaržymo) potipis | — |
| `teip_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `teip_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `teip_eilnr` | `integer` | — | `4` | `open` | — | Eilės numeris aplikacijose | — |
| `teip_poz` | `integer` | — | `4` | `open` | — | Teisės potipio požymis | — |
| `teip_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `teip_naudojama` | `integer` | — | `4` | `open` | — | Teisės potipis naudojimo požymis | — |
| `teip_plotas_pav` | `string` | — | `3` | `open` | — | Ploto pavadinimas | — |
| `teip_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `teip_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai (ilgas) | — |
| `teip_plotas_pav_en` | `string` | — | `3` | `open` | — | Ploto pavadinimas angliškai | — |
| `teip_ak_kodo_poz` | `integer` | — | `4` | `open` | — | Asmens kodo rodymas išraše. | — |
| `teip_istorine_nuo` | `datetime` | `S` | `4` | `open` | — | Teisės potipio istorijos požymis, nuo kada nenaudojamas teisės potipis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `teip_poz` | `0` | — | — | Būtinas | — |
| `teip_poz` | `1` | — | — | Galimas | — |
| `teip_poz` | `2` | — | — | Nenurodomas | — |
| `teip_naudojama` | `0` | — | — | Nenaudojama | — |
| `teip_naudojama` | `1` | — | — | Naudojama | — |
| `teip_ak_kodo_poz` | `0` | — | — | Nerodyti asmens kodo | — |
| `teip_ak_kodo_poz` | `1` | — | — | Rodyti asmens kodą | — |
| `teip_ak_kodo_poz` | `2` | — | — | Nerodyti asmens kodo ir gimimo datos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv
