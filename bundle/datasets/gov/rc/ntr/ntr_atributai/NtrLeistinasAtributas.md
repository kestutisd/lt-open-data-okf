---
type: Table
title: "NtrLeistinasAtributas — NTR leistinų atributų klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_atributai/NtrLeistinasAtributas (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrLeistinasAtributas"
tags: [gov, rc, ntrleistinasatributas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L34"
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L34"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1896/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# NtrLeistinasAtributas — NTR leistinų atributų klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_atributai/NtrLeistinasAtributas`[^manifest]
- **Dataset:** [NTR atributų klasifikatoriai](../ntr_atributai.md) (`datasets/gov/rc/ntr/ntr_atributai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L34)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai/NtrLeistinasAtributas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `obje_tipas, atri_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obje_tipas` | `ref` | [NtrObjektoTipas](../ntr_objektai/NtrObjektoTipas.md) (`level=4 UUID`: `obje_tipas._id`) | `4` | `open` | — | Turto objekto tipas | — |
| `atri_kodas` | `ref` | [NtrAtributas](NtrAtributas.md) (`level=4 UUID`: `atri_kodas._id`) | `4` | `open` | — | Atributo kodas | — |
| `atrp_poz` | `ref` | [NtrAtributoPozymis](NtrAtributoPozymis.md) (`level=4 UUID`: `atrp_poz._id`) | `4` | `open` | — | Atributo pozymis | — |
| `latr_eilnr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `latr_istorijos_poz` | `integer` | — | `3` | `open` | — | Atributo laikymo istorijoje požymis | — |
| `latr_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Leistino atributo koregavimo data | — |
| `latr_grupe` | `integer` | — | `4` | `open` | — | Atributo grupė | — |
| `funk_kodas` | `integer` | — | `4` | `open` | — | Funkcijos kodas (nuoroda į kitą klasifikatorių, kuris yra tuščias) | — |
| `latr_data_nuo` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja nuo | — |
| `latr_data_iki` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja iki | — |
| `latr_kopijos_poz` | `integer` | — | `4` | `open` | — | Atributo reikšmės kopijavimo iš pastato į patalpą požymis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `latr_kopijos_poz` | `1` | — | — | Kopijuoti | — |
| `latr_kopijos_poz` | `0` | — | — | Nekopijuoti | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv#L34 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L34)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ntr/ntr_atributai (https://data.gov.lt/datasets/1896/)
