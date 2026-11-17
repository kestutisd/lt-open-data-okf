---
type: Table
title: "IAtmosferaIsmetamiTersalai — Į atmosferą išmestų teršalų kiekis"
description: "Spinta table datasets/gov/aaa/oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_tersalu_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# IAtmosferaIsmetamiTersalai — Į atmosferą išmestų teršalų kiekis

- **Model:** `datasets/gov/aaa/oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai`[^manifest]
- **Dataset:** [datasets/gov/aaa/oro_tersalu_duomenys](../oro_tersalu_duomenys.md) (`datasets/gov/aaa/oro_tersalu_duomenys`)
- **Manifest CSV:** [datasets/gov/aaa/oro_tersalu_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės nr. | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai, kuriais įvertintas išmetamų teršalų kiekis | — |
| `tersalai` | `string` | — | `2` | `open` | — | Oro teršalai | Į atmosferą išmetamų teršalų pavadinimai |
| `nfr_kodas` | `string` | — | `4` | `open` | — | Teršalų išmetimo šaltinis | Kodiniai teršalų išmetimo šaltinių pavadinimai. NFR kodai ir metodologija, pagal kurią atliekami skaičiavimai yra nurodyti EMEP/EEA Emission inventory guidebook. |
| `kiekis` | `number` | — | `4` | `open` | — | Į atmosferą išmestų teršalų kiekis | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Matavimo vienetai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_tersalu_duomenys.csv
