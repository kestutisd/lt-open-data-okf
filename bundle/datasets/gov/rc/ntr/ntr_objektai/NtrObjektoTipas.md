---
type: Table
title: "NtrObjektoTipas — NT objektų tipų klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_objektai/NtrObjektoTipas (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoTipas"
tags: [gov, rc, ntrobjektotipas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1895/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_objektai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrObjektoTipas — NT objektų tipų klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_objektai/NtrObjektoTipas`[^manifest]
- **Dataset:** [NTR objektus apibūdinantys klasifikatoriai](../ntr_objektai.md) (`datasets/gov/rc/ntr/ntr_objektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoTipas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `obje_tipas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obje_tipas` | `integer` | — | `4` | `open` | — | Turto objekto tipas | — |
| `objg_grupe` | `ref` | [NtrTurtoGrupe](NtrTurtoGrupe.md) (`level=4 UUID`: `objg_grupe._id`) | `4` | `open` | — | Turto objekto grupė | — |
| `obje_pav` | `string` | — | `3` | `open` | — | Pavadinimas | — |
| `obje_pav_i` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) | — |
| `obje_santrumpa` | `string` | — | `3` | `open` | — | Santrumpa | — |
| `obje_eilnr` | `integer` | — | `4` | `open` | — | Eilės numeris aplikacijose | — |
| `obje_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `obje_leisti_prideti` | `integer` | — | `4` | `open` | — | Pridėjimo požymis. Naudojamas aplikacijose | — |
| `obje_pav_vard` | `string` | — | `3` | `open` | — | Pavadinimas (trumpas), vardininko linksnis | — |
| `obje_pav_kilm` | `string` | — | `3` | `open` | — | Pavadinimas (trumpas), kilmininko linksnis | — |
| `obje_pav_naud` | `string` | — | `3` | `open` | — | Pavadinimas (trumpas), naudininko linksnis | — |
| `obje_pav_en` | `string` | — | `3` | `open` | — | Pavadinimas angliškai | — |
| `obje_pav_i_en` | `string` | — | `3` | `open` | — | Pavadinimas (ilgas) angliškai | — |
| `obje_pav_kilm_en` | `string` | — | `3` | `open` | — | Pavadinimas (trumpas) angliškai, vardininko linksnis | — |
| `obje_pav_naud_en` | `string` | — | `3` | `open` | — | Pavadinimas (trumpas) angliškai, kilmininko linksnis | — |
| `obje_pav_vard_en` | `string` | — | `3` | `open` | — | Pavadinimas (trumpas) angliškai, naudininko linksnis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `obje_leisti_prideti` | `1` | — | — | Galima | — |
| `obje_leisti_prideti` | `0` | — | — | Negalima | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_objektai (https://data.gov.lt/datasets/1895/)
