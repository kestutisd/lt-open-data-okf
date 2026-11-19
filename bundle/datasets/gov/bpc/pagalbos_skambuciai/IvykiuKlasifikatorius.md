---
type: Table
title: "IvykiuKlasifikatorius — BPC įvykių klasifikatorius"
description: "Bendrojo pagalbos centro registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, tipų klasifikatorius."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuKlasifikatorius"
tags: [gov, bpc, ivykiuklasifikatorius, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1763/"
    title: "data.gov.lt DCAT-AP — datasets/gov/bpc/pagalbos_skambuciai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IvykiuKlasifikatorius — BPC įvykių klasifikatorius

Bendrojo pagalbos centro registruotų įvykių, apie kuriuos gauti pranešimai pagalbos telefonu 112, tipų klasifikatorius. Tai yra pagalbinė lentelė, kurią reikia prijungti prie likusių trijų šio rinkinio lentelių. Laikui bėgant klasifikatoriaus apimtis ir detalumas gali plėstis (svarbu žinoti, analizuojant įvykių dinamiką).[^manifest]

- **Model:** `datasets/gov/bpc/pagalbos_skambuciai/IvykiuKlasifikatorius`[^manifest]
- **Dataset:** [Bendrojo pagalbos centro 112 skambučių duomenų rinkinys](../pagalbos_skambuciai.md) (`datasets/gov/bpc/pagalbos_skambuciai`)[^manifest]
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_skambuciai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_skambuciai/IvykiuKlasifikatorius` (`deployed`)[^manifest]
- **Provider:** `bpc` — Bendrasis pagalbos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ivykio_tipo_kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykio_tipo_kodas` | `string` | — | `4` | `open` | — | Įvykio tipo kodas | — |
| `aukstesnis_ivykio_tipas` | `string` | — | `2` | `open` | — | Aukštesnis įvykio hierarchinis lygmuo (mažiau detalus) | — |
| `zemesnis_ivykio_tipas` | `string` | — | `4` | `open` | — | Žemesnis įvykio hierarchinis lygmuo (detalesnis) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_skambuciai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_skambuciai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/bpc/pagalbos_skambuciai (https://data.gov.lt/datasets/1763/)
