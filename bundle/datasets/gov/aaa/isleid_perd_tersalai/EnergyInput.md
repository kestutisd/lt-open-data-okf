---
type: Table
title: "EnergyInput — Energijos sąnaudos"
description: "Spinta table datasets/gov/aaa/isleid_perd_tersalai/EnergyInput (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/EnergyInput"
tags: [gov, aaa, energyinput, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L12"
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L12"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/665/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# EnergyInput — Energijos sąnaudos

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/EnergyInput`[^manifest]
- **Dataset:** [Išleidžiamų ir perduodamų teršalų duomenys](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L12)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/EnergyInput` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Energijos sąnaudų Id | Energijos sąnaudų identifikacinis numeris (Eil. Nr.) |
| `localid` | `string` | — | `4` | `open` | — | Gamybos įrengimo Id | Gamybos įrengimo identifikacinis numeris |
| `fuelinput` | `string` | — | `4` | `open` | — | Kuro rūšis | Naudojamo kuro rūšis pagal Direktyvą Nr. 2010/75/EU |
| `othersolidfuel` | `string` | — | `2` | `open` | — | Kito kieto kūro rūšis | Kito kieto kuro rūšis (išskyrus - anglis, lignitas, biomasė ar durpės) |
| `othergaseousfuel` | `string` | — | `2` | `open` | — | Kito dujinio kuro rūšis | Kito dujinio kuro rūšis (išskyrus - gamtinės dujos) |
| `furtherdetails` | `string` | — | `2` | `open` | — | Papildoma informacija | Papildoma informacija - nespecifikuotas kuras |
| `energyinput` | `number` | `TJ` | `4` | `open` | — | Visas energijos kiekis | Energijos kiekis, teradžiauliais per ataskaitinius metus |
| `year` | `integer` | — | `2` | `open` | — | Ataskaitiniai metai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `fuelinput` | `"Biomass"` | — | — | Biomasė | — |
| `fuelinput` | `"Coal"` | — | — | Anglis | — |
| `fuelinput` | `"Lignite"` | — | — | Lignitas | — |
| `fuelinput` | `"LiquidFuels"` | — | — | Skystas kuras | — |
| `fuelinput` | `"NaturalGas"` | — | — | Gamtinės dujos | — |
| `fuelinput` | `"OtherGases"` | — | — | Kitas dujinis kuras | — |
| `fuelinput` | `"OtherSolidFuels"` | — | — | Kitas kietas kuras | — |
| `fuelinput` | `"Peat"` | — | — | Durpės | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `year` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L12 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L12)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai (https://data.gov.lt/datasets/665/)
