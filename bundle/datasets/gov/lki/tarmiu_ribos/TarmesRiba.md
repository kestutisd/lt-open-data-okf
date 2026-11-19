---
type: Table
title: "TarmesRiba — Tarmių ribos"
description: "Rinkinyje pateikiamos lietuviškų tarmių ribų geometrijos (https://maps.lki.lt/)."
resource: "https://get.data.gov.lt/datasets/gov/lki/tarmiu_ribos/TarmesRiba"
tags: [gov, lki, tarmesriba, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/tarmiu_ribos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lki/tarmiu_ribos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2936/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lki/tarmiu_ribos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# TarmesRiba — Tarmių ribos

Rinkinyje pateikiamos lietuviškų tarmių ribų geometrijos (https://maps.lki.lt/). Rinkinį sudaro tarmės pavadinimas, jos trumpinys ir tarmės ribų geometrija, pateikta dvejetainiu, LKS, WGS84 geometrijos formatais. Duomenis teikia Lietuvių kalbos institutas (LKI). Šis duomenų rinkinys šiuo metu pateikiamas tik informaciniais tikslais ir negali būti naudojamas moksliniams tyrimams. Jame gali būti preliminarių ar pasenusių duomenų. Atnaujinimas planuojamas 2026 m. balandį, apie kurį bus pranešta kartu su naujausia versija. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lki/tarmiu_ribos/TarmesRiba`[^manifest]
- **Dataset:** [Tarmių ribos](../tarmiu_ribos.md) (`datasets/gov/lki/tarmiu_ribos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lki/tarmiu_ribos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/tarmiu_ribos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/tarmiu_ribos/TarmesRiba` (`deployed`)[^manifest]
- **Provider:** `lki` — Lietuvių kalbos institutas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `tarmes_riba_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tarmes_riba_id` | `string` | — | `4` | `open` | — | Tarmės ribų identifikatorius | — |
| `tarme_trump` | `string` | — | `4` | `open` | — | Tarmės pavadinimo trumpinys | — |
| `tarme_pav` | `string` | — | `4` | `open` | — | Tarmės pavadinimas | — |
| `vda_geometrija_wgs` | `geometry(4326)` | — | `4` | `open` | — | Tarmės ribų geometrija (WGS84, platuma ir ilguma) | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/tarmiu_ribos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/tarmiu_ribos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lki/tarmiu_ribos (https://data.gov.lt/datasets/2936/)
