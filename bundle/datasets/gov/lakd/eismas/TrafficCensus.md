---
type: Table
title: "TrafficCensus — Eismo intensyvumas"
description: "Spinta table datasets/gov/lakd/eismas/TrafficCensus (27 columns)."
tags: [gov, lakd, trafficcensus, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lakd/eismas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# TrafficCensus — Eismo intensyvumas

- **Model:** `datasets/gov/lakd/eismas/TrafficCensus`[^manifest]
- **Dataset:** [datasets/gov/lakd/eismas](../eismas.md) (`datasets/gov/lakd/eismas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/eismas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **URI:** `vadovas:dsa/dimensijos.html#model.ref`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | ID | — |
| `geometry` | `geometry(linestring,4326)` | `m` | `4` | `open` | — | Geometrija | — |
| `objectid` | `integer` | — | `4` | `open` | — | Identifikatorius | — |
| `kelionr` | `ref` | [StateRoad](../keliai/StateRoad.md) (`level=4 UUID` via `StateRoad[kelionr]`: `kelionr._id`) | `4` | `open` | — | Kelio numeris | — |
| `pradziakm` | `number` | `km` | `4` | `open` | — | Ruožo pradžia | — |
| `pabaigakm` | `number` | `km` | `4` | `open` | — | Ruožo pabaiga | — |
| `postovieta` | `number` | `km` | `4` | `open` | — | Matavimo vieta | — |
| `transporto_klasifikatorius` | `string` | — | `4` | `open` | — | Transporto klasifikatorius | — |
| `periodo_pradzia` | `date` | — | `2` | `open` | — | Matavimo periodo pradžia | — |
| `periodo_pabaiga` | `date` | — | `2` | `open` | — | Matavimo periodo pabaiga | — |
| `eismointensyvumas_ruoze` | `integer` | — | `4` | `open` | — | Bendras vidutinis metinis paros eismo intensyvumas ruože aut./parą | — |
| `vmpei_sunk` | `integer` | — | `4` | `open` | — | Sunkaus transporto vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `vmpei_lengv` | `integer` | — | `4` | `open` | — | Lengvojo transporto vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `esa` | `number` | — | `4` | `open` | — | Ekvivalentinis standartinių apkrovų skaičius | — |
| `esa_lengv` | `number` | — | `4` | `open` | — | Lengvojo transporto ekvivalentinis standartinių apkrovų skaičius | — |
| `esa_sunk` | `number` | — | `4` | `open` | — | Sunkaus transporto ekvivalentinis standartinių apkrovų skaičius | — |
| `l_automob` | `integer` | — | `4` | `open` | — | Lengvųjų automobilių vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `lengv_sun_minbus` | `integer` | — | `4` | `open` | — | Lengvųjų sunkių automobilių vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `krov_be_priek` | `integer` | — | `4` | `open` | — | Krovininių be priekabų vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `krov_su_priek` | `integer` | — | `4` | `open` | — | Krovininių su priekaba vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `krov_su_puspriek` | `integer` | — | `4` | `open` | — | Krovininių su puspriekabe vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `autob` | `integer` | — | `4` | `open` | — | Autobusų vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `kiti` | `integer` | — | `4` | `open` | — | Kitų vidutinis metinis paros eismo intensyvumas aut./parą | — |
| `matavimo_metai` | `date` | `Y` | `4` | `open` | — | Matavimo metai | — |
| `statusas` | `integer` | — | `3` | `open` | — | Galiojimo statusas | — |
| `matavo` | `string` | — | `3` | `open` | — | Matavimus atliko | — |
| `pastabos` | `string` | — | `3` | `open` | — | Pastabos | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/eismas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismas.csv#L6)
