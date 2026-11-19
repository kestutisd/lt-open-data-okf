---
type: Table
title: "EmissionsToAir — Emisijos į orą"
description: "Didelių kurą deginančių įrenginių duomenys"
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/EmissionsToAir"
tags: [gov, aaa, emissionstoair, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/665/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# EmissionsToAir — Emisijos į orą

Didelių kurą deginančių įrenginių duomenys[^manifest]

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/EmissionsToAir`[^manifest]
- **Dataset:** [Išleidžiamų ir perduodamų teršalų duomenys](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/EmissionsToAir` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai (https://data.gov.lt/datasets/665/)
