---
type: Table
title: "TIInformacija2021 — Tiesioginės ir kompensacinės išmokos už deklaruotos plotus ir (arba) gyvulius. Bendra informacija. 2021 m."
description: "Spinta table datasets/gov/nma/ti_informacija_2021/TIInformacija2021 (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/nma/ti_informacija_2021/TIInformacija2021"
tags: [gov, nma, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nma/ti_informacija_2021.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/ti_informacija_2021.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# TIInformacija2021 — Tiesioginės ir kompensacinės išmokos už deklaruotos plotus ir (arba) gyvulius. Bendra informacija. 2021 m.

- **Model:** `datasets/gov/nma/ti_informacija_2021/TIInformacija2021`[^manifest]
- **Dataset:** [datasets/gov/nma/ti_informacija_2021](../ti_informacija_2021.md) (`datasets/gov/nma/ti_informacija_2021`)
- **Manifest CSV:** [datasets/gov/nma/ti_informacija_2021.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nma/ti_informacija_2021.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nma/ti_informacija_2021/TIInformacija2021`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pareiskejo_tipas` | `string` | — | `4` | `open` | — | Pareiškėjo tipas | — |
| `pareiskejo_lytis` | `string` | — | `4` | `open` | — | Pareiškėjo lytis | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `programa` | `string` | — | `3` | `open` | — | Programa | — |
| `deklaruoti_hektarai` | `number` | `ha` | `4` | `open` | — | Deklaruoti hektarai pagal programą | — |
| `patvirtinti_hektarai` | `number` | `ha` | `4` | `open` | — | Patvirtinti hektarai pagal programą | — |
| `prasoma_suma` | `number` | — | `2` | `open` | — | Prašoma paramos suma | — |
| `ismoketa_suma` | `number` | — | `2` | `open` | — | Išmokėta paramos suma | — |
| `valda` | `string` | — | `4` | `open` | — | Valda | — |

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
| `prasoma_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ismoketa_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nma/ti_informacija_2021.csv
