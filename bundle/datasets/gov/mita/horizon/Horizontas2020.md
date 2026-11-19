---
type: Table
title: "Horizontas2020 — Duomenys apie Lietuvos pareiškėjų finansuotas paraiškas mokslinių tyrimų ir inovacijų programoje „Horizontas 2020“"
description: "Spinta table datasets/gov/mita/horizon/Horizontas2020 (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/mita/horizon/Horizontas2020"
tags: [gov, mita, horizontas2020, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/horizon.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/mita/horizon.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1446/"
    title: "data.gov.lt DCAT-AP — datasets/gov/mita/horizon"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Horizontas2020 — Duomenys apie Lietuvos pareiškėjų finansuotas paraiškas mokslinių tyrimų ir inovacijų programoje „Horizontas 2020“

- **Model:** `datasets/gov/mita/horizon/Horizontas2020`[^manifest]
- **Dataset:** [Duomenys apie Lietuvos pareiškėjų finansuotas paraiškas ES mokslinių tyrimų ir inovacijų...](../horizon.md) (`datasets/gov/mita/horizon`)[^manifest]
- **Manifest CSV:** [datasets/gov/mita/horizon.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/horizon.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/mita/horizon/Horizontas2020` (`deployed`)[^manifest]
- **Provider:** `mita` — Mokslo, inovacijų ir technologijų agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `projekto_nr` | `string` | — | `3` | `open` | — | Projekto ID | — |
| `projekto_akronimas` | `string` | — | `3` | `open` | — | Projekto akronimas | — |
| `lietuvos_dalyvis_projekte` | `string` | — | `3` | `open` | — | Lietuvos dalyvis projekte | — |
| `organizacijos_tipas` | `string` | — | `3` | `open` | — | Organizacijos tipas | — |
| `projekto_pavadinimas` | `string` | — | `3` | `open` | — | Projekto pavadinimas | — |
| `projekto_aprasymas` | `string` | — | `3` | `open` | — | Projekto aprašymas | — |
| `kvietimo_nr` | `string` | — | `3` | `open` | — | Kvietimo Nr. | — |
| `projekto_vykdymo_pradzia` | `date` | — | `3` | `open` | — | Projekto vykdymo pradžia | — |
| `projekto_vykdymo_pabaiga` | `date` | — | `3` | `open` | — | Projekto vykdymo pabaiga | — |
| `projekto_dalyviu_skaicius` | `integer` | — | `3` | `open` | — | Projekto dalyvių skaičius | — |
| `lietuvos_dalyvio_role_projekte` | `string` | — | `3` | `open` | — | Lietuvos dalyvio rolė projekte | — |
| `projekto_tematika` | `string` | — | `3` | `open` | — | Projekto tematika | — |
| `bendras_projekto_biudzetas` | `number` | — | `3` | `open` | — | Bendras projekto biudžetas | — |
| `bendras_gautas_projekto_finansavimas_is_ek` | `number` | — | `3` | `open` | — | Bendras gautas projekto finansavimas iš EK | — |
| `lietuvos_dalyvio_biudzetas_projekte` | `number` | — | `3` | `open` | — | Lietuvos dalyvio biudžetas projekte | — |
| `lietuvos_dalyvio_gautas_finansavimas_is_ek` | `number` | — | `3` | `open` | — | Lietuvos dalyvio gautas finansavimas iš EK | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/mita/horizon.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/horizon.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/mita/horizon (https://data.gov.lt/datasets/1446/)
