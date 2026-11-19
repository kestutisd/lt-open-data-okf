---
type: Table
title: "NtrTeisesPotipis — NTR teisių ir suvaržymų potipiai"
description: "Spinta table datasets/gov/rc/ntr/ntr_teises/NtrTeisesPotipis (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises/NtrTeisesPotipis"
tags: [gov, rc, ntrteisespotipis, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L14"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv#L14"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1899/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_teises"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrTeisesPotipis — NTR teisių ir suvaržymų potipiai

- **Model:** `datasets/gov/rc/ntr/ntr_teises/NtrTeisesPotipis`[^manifest]
- **Dataset:** [NTR teisių tipų ir teisių potipių klasifikatoriai](../ntr_teises.md) (`datasets/gov/rc/ntr/ntr_teises`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_teises.csv#L14](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L14)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises/NtrTeisesPotipis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `teit_tipas, teip_potipis`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `teit_tipas` | `ref` | [NtrTeisesTipas](NtrTeisesTipas.md) (`level=4 UUID`: `teit_tipas._id`) | `4` | `open` | — | Teisės (suvaržymo) tipas | — |
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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `teip_poz` | `0` | — | — | Būtinas | — |
| `teip_poz` | `1` | — | — | Galimas | — |
| `teip_poz` | `2` | — | — | Nenurodomas | — |
| `teip_naudojama` | `0` | — | — | Nenaudojama | — |
| `teip_naudojama` | `1` | — | — | Naudojama | — |
| `teip_ak_kodo_poz` | `0` | — | — | Nerodyti asmens kodo | — |
| `teip_ak_kodo_poz` | `1` | — | — | Rodyti asmens kodą | — |
| `teip_ak_kodo_poz` | `2` | — | — | Nerodyti asmens kodo ir gimimo datos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv#L14 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L14)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_teises (https://data.gov.lt/datasets/1899/)
