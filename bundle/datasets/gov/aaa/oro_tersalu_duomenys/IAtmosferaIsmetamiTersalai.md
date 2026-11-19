---
type: Table
title: "IAtmosferaIsmetamiTersalai — Į atmosferą išmestų teršalų kiekis"
description: "Spinta table datasets/gov/aaa/oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai"
tags: [gov, aaa, iatmosferaismetamitersalai, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/aaa/oro_tersalu_duomenys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/884/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/oro_tersalu_duomenys"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# IAtmosferaIsmetamiTersalai — Į atmosferą išmestų teršalų kiekis

- **Model:** `datasets/gov/aaa/oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai`[^manifest]
- **Dataset:** [Į aplinkos orą išmetamų teršalų apskaitos duomenys](../oro_tersalu_duomenys.md) (`datasets/gov/aaa/oro_tersalu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/oro_tersalu_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/oro_tersalu_duomenys/IAtmosferaIsmetamiTersalai` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/oro_tersalu_duomenys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/oro_tersalu_duomenys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/oro_tersalu_duomenys (https://data.gov.lt/datasets/884/)
