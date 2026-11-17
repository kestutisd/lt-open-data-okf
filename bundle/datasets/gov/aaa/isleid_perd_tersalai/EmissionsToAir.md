---
type: Table
title: "EmissionsToAir — Emisijos į orą"
description: "Didelių kurą deginančių įrenginių duomenys"
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/EmissionsToAir"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# EmissionsToAir — Emisijos į orą

Didelių kurą deginančių įrenginių duomenys

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/EmissionsToAir`[^manifest]
- **Dataset:** [datasets/gov/aaa/isleid_perd_tersalai](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/EmissionsToAir`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Emisijų į orą Id | Emisijų į orą identifikacinis numeris (Eil. Nr.) |
| `localid` | `string` | — | `4` | `open` | — | Gamybos įrengimo Id | Gamybos įrengimo identifikacinis numeris |
| `pollutant` | `string` | — | `2` | `open` | — | Teršalas | Teršalo kodas pagal https://dd.eionet.europa.eu/vocabulary/EPRTRandLCP/EPRTRPollutantCodeValue/view |
| `quantity` | `number` | `t` | `4` | `open` | — | Visas teršalo kiekis | Teršalo kiekis, tonomis per ataskaitinius metus |
| `year` | `integer` | — | `2` | `open` | — | Ataskaitiniai metai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `year` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv
