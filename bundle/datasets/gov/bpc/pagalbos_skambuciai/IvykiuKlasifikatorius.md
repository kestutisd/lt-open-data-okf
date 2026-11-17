---
type: Table
title: "IvykiuKlasifikatorius — BPC įvykių klasifikatorius"
description: "Bendrojo pagalbos centro registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, tipų klasifikatorius."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuKlasifikatorius"
tags: [gov, bpc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# IvykiuKlasifikatorius — BPC įvykių klasifikatorius

Bendrojo pagalbos centro registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, tipų klasifikatorius. Tai yra pagalbinė lentelė, kurią reikia prijungti prie likusių trijų šio rinkinio lentelių. Laikui bėgant klasifikatoriaus apimtis ir detalumas gali plėstis (svarbu žinoti, analizuojant įvykių dinamiką).

- **Model:** `datasets/gov/bpc/pagalbos_skambuciai/IvykiuKlasifikatorius`[^manifest]
- **Dataset:** [Bendrojo pagalbos centro 112 skambučių duomenų rinkinys](../pagalbos_skambuciai.md) (`datasets/gov/bpc/pagalbos_skambuciai`)
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_skambuciai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuKlasifikatorius`
- **Primary Key (`ref`):** `ivykio_tipo_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykio_tipo_kodas` | `string` | — | `4` | `open` | — | Įvykio tipo kodas | — |
| `aukstesnis_ivykio_tipas` | `string` | — | `2` | `open` | — | Aukštesnis įvykio hierarchinis lygmuo (mažiau detalus) | — |
| `zemesnis_ivykio_tipas` | `string` | — | `4` | `open` | — | Žemesnis įvykio hierarchinis lygmuo (detalesnis) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv
