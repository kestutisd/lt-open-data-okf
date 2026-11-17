---
type: Table
title: "Testamentas"
description: "Spinta table datasets/gov/rc/tr/testamentai/Testamentas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/testamentai/Testamentas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/testamentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamentai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Testamentas

- **Model:** `datasets/gov/rc/tr/testamentai/Testamentas`[^manifest]
- **Dataset:** [Testamentų registro (TR) duomenys apie testamentus](../testamentai.md) (`datasets/gov/rc/tr/testamentai`)
- **Manifest CSV:** [datasets/gov/rc/tr/testamentai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamentai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/testamentai/Testamentas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Registro objekto identifikavimo kodas šiame duomenų rinkinyje | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Registro objekto pavadinimas | — |
| `testamento_rusis` | `ref` | [/datasets/gov/rc/tr/tr_klasifikatoriai/TrRusis](../tr_klasifikatoriai/TrRusis.md) | `4` | `open` | — | Testamento rūšis | — |
| `sudaryta_uzs` | `integer` | — | `4` | `open` | — | Ar sudarytas užsienyje | — |
| `reg_data` | `string` | — | `3` | `open` | — | Testamento įregistravimo laikotarpis (metai - ketvirtis) | — |
| `isreg_data` | `string` | — | `3` | `open` | — | Testamento išregistravimo laikotarpis (metai - ketvirtis) | — |
| `busena_id` | `integer` | — | `4` | `open` | — | Testamento būsenos identifikatorius | — |
| `bus_pavadinimas` | `string` | — | `3` | `open` | — | Testamento būsenos pavadinimas | — |
| `teikejas` | `string` | — | `3` | `open` | — | Duomenų teikėjas | — |
| `testatorius_lytis` | `string` | — | `4` | `open` | — | Testatoriaus Lytis | — |
| `uzsienietis` | `integer` | — | `4` | `open` | — | Požymis ar užsienietis | — |
| `testatorius_amzius` | `string` | — | `3` | `open` | — | Testatoriaus amžiaus grupė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sudaryta_uzs` | `1` | — | — | Testamentas sudarytas užsienyje | — |
| `sudaryta_uzs` | `0` | — | — | Testamentas sudarytas Lietuvoje | — |
| `testatorius_lytis` | `"V"` | — | — | Vyras | — |
| `testatorius_lytis` | `"M"` | — | — | Moteris | — |
| `testatorius_lytis` | `"ND"` | — | — | Nėra duomenų | — |
| `uzsienietis` | `1` | — | — | Užsienietis | — |
| `uzsienietis` | `0` | — | — | Lietuvos Respublikos pilietis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/testamentai.csv
