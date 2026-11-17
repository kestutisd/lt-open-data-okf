---
type: Table
title: "NtrLeistinasAtributas — NTR leistinų atributų klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_atributai/NtrLeistinasAtributas (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrLeistinasAtributas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L34"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrLeistinasAtributas — NTR leistinų atributų klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_atributai/NtrLeistinasAtributas`[^manifest]
- **Dataset:** [NTR atributų klasifikatoriai](../ntr_atributai.md) (`datasets/gov/rc/ntr/ntr_atributai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L34)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrLeistinasAtributas`
- **Primary Key (`ref`):** `obje_tipas, atri_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obje_tipas` | `ref` | [/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoTipas](../ntr_objektai/NtrObjektoTipas.md) | `4` | `open` | — | Turto objekto tipas | — |
| `atri_kodas` | `ref` | [NtrAtributas](NtrAtributas.md) | `4` | `open` | — | Atributo kodas | — |
| `atrp_poz` | `ref` | [NtrAtributoPozymis](NtrAtributoPozymis.md) | `4` | `open` | — | Atributo pozymis | — |
| `latr_eilnr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `latr_istorijos_poz` | `integer` | — | `3` | `open` | — | Atributo laikymo istorijoje požymis | — |
| `latr_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Leistino atributo koregavimo data | — |
| `latr_grupe` | `integer` | — | `4` | `open` | — | Atributo grupė | — |
| `funk_kodas` | `integer` | — | `4` | `open` | — | Funkcijos kodas (nuoroda į kitą klasifikatorių, kuris yra tuščias) | — |
| `latr_data_nuo` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja nuo | — |
| `latr_data_iki` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja iki | — |
| `latr_kopijos_poz` | `integer` | — | `4` | `open` | — | Atributo reikšmės kopijavimo iš pastato į patalpą požymis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `latr_kopijos_poz` | `1` | — | — | Kopijuoti | — |
| `latr_kopijos_poz` | `0` | — | — | Nekopijuoti | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv
