---
type: Table
title: "TarmesRiba — Tarmių ribos"
description: "Rinkinyje pateikiamos lietuviškų tarmių ribų geometrijos (https://maps.lki.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/lki/tarmiu_ribos/TarmesRiba"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/tarmiu_ribos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/tarmiu_ribos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TarmesRiba — Tarmių ribos

Rinkinyje pateikiamos lietuviškų tarmių ribų geometrijos (https://maps.lki.lt/). Rinkinį sudaro tarmės pavadinimas, jos trumpinys ir tarmės ribų geometrija, pateikta dvejetainiu, LKS, WGS84 geometrijos formatais. Duomenis teikia Lietuvių kalbos institutas (LKI). Šis duomenų rinkinys šiuo metu pateikiamas tik informaciniais tikslais ir negali būti naudojamas moksliniams tyrimams. Jame gali būti preliminarių ar pasenusių duomenų. Atnaujinimas planuojamas 2026 m. balandį, apie kurį bus pranešta kartu su naujausia versija.

- **Model:** `datasets/gov/lki/tarmiu_ribos/TarmesRiba`[^manifest]
- **Dataset:** [Tarmių ribos](../tarmiu_ribos.md) (`datasets/gov/lki/tarmiu_ribos`)
- **Manifest CSV:** [datasets/gov/lki/tarmiu_ribos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/tarmiu_ribos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/tarmiu_ribos/TarmesRiba`
- **Primary Key (`ref`):** `tarmes_riba_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tarmes_riba_id` | `string` | — | `4` | `open` | — | Tarmės ribų identifikatorius | — |
| `tarme_trump` | `string` | — | `4` | `open` | — | Tarmės pavadinimo trumpinys | — |
| `tarme_pav` | `string` | — | `4` | `open` | — | Tarmės pavadinimas | — |
| `vda_geometrija_wgs` | `geometry(4326)` | — | `4` | `open` | — | Tarmės ribų geometrija (WGS84, platuma ir ilguma) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/tarmiu_ribos.csv
