---
type: Table
title: "TIPaseliai2020 — Tiesioginės ir kompensacinės išmokos už deklaruotos plotus ir (arba) gyvulius. Pasėlio rūšis. 2020 m."
description: "Spinta table datasets/gov/nma/ti_paseliai_2020/TIPaseliai2020 (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/ti_paseliai_2020/TIPaseliai2020"
tags: [gov, nma, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/ti_paseliai_2020.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/ti_paseliai_2020.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# TIPaseliai2020 — Tiesioginės ir kompensacinės išmokos už deklaruotos plotus ir (arba) gyvulius. Pasėlio rūšis. 2020 m.

- **Model:** `datasets/gov/nma/ti_paseliai_2020/TIPaseliai2020`[^manifest]
- **Dataset:** [datasets/gov/nma/ti_paseliai_2020](../ti_paseliai_2020.md) (`datasets/gov/nma/ti_paseliai_2020`)
- **Manifest CSV:** [datasets/gov/nma/ti_paseliai_2020.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/ti_paseliai_2020.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/ti_paseliai_2020/TIPaseliai2020`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `paselio_rusis` | `string` | — | `3` | `open` | — | Pasėlio rūšis | — |
| `deklaruoti_hektarai` | `number` | `ha` | `4` | `open` | — | Deklaruoti hektarai pagal programą | — |
| `valdymo_forma` | `string` | — | `3` | `open` | — | Valdymo forma | — |
| `pareiskejas` | `string` | — | `4` | `open` | — | Pareiškėjas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `"Fizinis"` | — | — | Fizinis asmuo | — |
| `pareiskejo_tipas` | `"Juridinis"` | — | — | Juridinis asmuo | — |
| `pareiskejo_lytis` | `"V"` | — | — | Vyras | — |
| `pareiskejo_lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/ti_paseliai_2020.csv
