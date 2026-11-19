---
type: Table
title: "IeskomuTransportoPriemoniuRegistras"
description: "Spinta table datasets/gov/pd/itpr/IeskomuTransportoPriemoniuRegistras (21 columns)."
tags: [gov, pd, ieskomutransportopriemoniuregistras, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/itpr.csv#L9"
    title: "atviriduomenys/manifest — datasets/gov/pd/itpr.csv#L9"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# IeskomuTransportoPriemoniuRegistras

- **Model:** `datasets/gov/pd/itpr/IeskomuTransportoPriemoniuRegistras`[^manifest]
- **Dataset:** [datasets/gov/pd/itpr](../itpr.md) (`datasets/gov/pd/itpr`)[^manifest]
- **Manifest CSV:** [datasets/gov/pd/itpr.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/itpr.csv#L9)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pd` — Policijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nationalid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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
| `marke` | `ref` | [TransportoPriemone](../../regitra/tp/TransportoPriemone.md) (`level=4 UUID` via `TransportoPriemone[marke]`: `marke._id`) | `4` | `open` | — | Transporto priemonės markė | — |
| `marke_kt` | `string` | — | `2` | `open` | — | Transporto priemonės markė (kita) | — |
| `modelis` | `ref` | [TransportoPriemone](../../regitra/tp/TransportoPriemone.md) (`level=4 UUID` via `TransportoPriemone[komercinis_pav]`: `modelis._id`) | `4` | `open` | — | Transporto priemonės modelis | — |
| `modelis_kt` | `string` | — | `2` | `open` | — | Transporto priemonės modelis (kita) | — |
| `degalu_tipas` | `string` | — | `3` | `open` | — | Degalų tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `'IESKOMA'` | — | — | Ieškoma | — |
| `statusas` | `'ARCHYVAS'` | — | — | Archyvas | — |
| `statusas` | `'NUTRAUKTA'` | — | — | Nutraukta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/itpr.csv#L9 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/itpr.csv#L9)
