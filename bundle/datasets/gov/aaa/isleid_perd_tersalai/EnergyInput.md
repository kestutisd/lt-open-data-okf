---
type: Table
title: "EnergyInput — Energijos sąnaudos"
description: "Spinta table datasets/gov/aaa/isleid_perd_tersalai/EnergyInput (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/EnergyInput"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L12"
    last_modified: "2026-11-11T14:39:20Z"
---

# EnergyInput — Energijos sąnaudos

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/EnergyInput`[^manifest]
- **Dataset:** [datasets/gov/aaa/isleid_perd_tersalai](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L12)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/EnergyInput`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv
