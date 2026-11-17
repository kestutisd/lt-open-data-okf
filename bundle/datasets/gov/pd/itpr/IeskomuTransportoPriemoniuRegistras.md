---
type: Table
title: "IeskomuTransportoPriemoniuRegistras"
description: "Spinta table datasets/gov/pd/itpr/IeskomuTransportoPriemoniuRegistras (21 columns)."
tags: [gov, pd, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pd/itpr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/itpr.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# IeskomuTransportoPriemoniuRegistras

- **Model:** `datasets/gov/pd/itpr/IeskomuTransportoPriemoniuRegistras`[^manifest]
- **Dataset:** [datasets/gov/pd/itpr](../itpr.md) (`datasets/gov/pd/itpr`)
- **Manifest CSV:** [datasets/gov/pd/itpr.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/itpr.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `nationalid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nationalid` | `integer` | — | `4` | `open` | — | Nacionalinis ID | — |
| `nscode` | `string` | — | `3` | `open` | — | Paieškos priežasties kodas | — |
| `nstitle` | `string` | — | `3` | `open` | — | Paieškos priežastis | — |
| `objekto_tipas` | `string` | — | `3` | `open` | — | Objekto tipas | — |
| `nutraukimo_data` | `date` | `T` | `4` | `open` | — | Paieškos nutraukimo data | — |
| `paieskos_pradzia` | `date` | `T` | `4` | `open` | — | Paieškos pradžios data | — |
| `paieskos_pabaiga` | `date` | `T` | `4` | `open` | — | Paiškos pabaigos data | — |
| `statusas` | `string` | — | `4` | `open` | — | Paieškos statusas | — |
| `praradimo_data` | `date` | `T` | `4` | `open` | — | Praradimo data | — |
| `suradimo_laikas` | `date` | `T` | `4` | `open` | — | Suradimo data | — |
| `veiks_suradus` | `string` | — | `3` | `open` | — | Veiksmai suradus | — |
| `valstybe` | `string` | — | `3` | `open` | — | Valstybė | — |
| `nutraukimo_pagrindas` | `string` | — | `3` | `open` | — | Paieškos nutraukimo pagrindas | — |
| `nutraukimo_pagrindas_kt` | `string` | — | `3` | `open` | — | Paieškos butraukimo pagrindas (kita) | — |
| `tipas` | `string` | — | `3` | `open` | — | Transporto priemonės tipas | — |
| `tipas_kt` | `string` | — | `3` | `open` | — | Transporto priemonės tipas (kita) | — |
| `marke` | `ref` | [/datasets/gov/regitra/tp/TransportoPriemone[marke]](../../regitra/tp/TransportoPriemone.md) | `4` | `open` | — | Transporto priemonės markė | — |
| `marke_kt` | `string` | — | `2` | `open` | — | Transporto priemonės markė (kita) | — |
| `modelis` | `ref` | [/datasets/gov/regitra/tp/TransportoPriemone[komercinis_pav]](../../regitra/tp/TransportoPriemone.md) | `4` | `open` | — | Transporto priemonės modelis | — |
| `modelis_kt` | `string` | — | `2` | `open` | — | Transporto priemonės modelis (kita) | — |
| `degalu_tipas` | `string` | — | `3` | `open` | — | Degalų tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `'IESKOMA'` | — | — | Ieškoma | — |
| `statusas` | `'ARCHYVAS'` | — | — | Archyvas | — |
| `statusas` | `'NUTRAUKTA'` | — | — | Nutraukta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/itpr.csv
