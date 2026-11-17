---
type: Table
title: "ProductionInstallationPartReport — Gamybos įrengimų duomenys"
description: "Spinta table datasets/gov/aaa/isleid_perd_tersalai/ProductionInstallationPartReport (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/ProductionInstallationPartReport"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L76"
    last_modified: "2026-11-11T14:39:20Z"
---

# ProductionInstallationPartReport — Gamybos įrengimų duomenys

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/ProductionInstallationPartReport`[^manifest]
- **Dataset:** [datasets/gov/aaa/isleid_perd_tersalai](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L76](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L76)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/ProductionInstallationPartReport`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `localid` | `string` | — | `4` | `open` | — | Gamybos įrengimo Id | Gamybos įrengimo identifikacinis numeris |
| `namespace` | `string` | — | `2` | `open` | — | Duomenis teikianti šalis | LT. CAED – Lithuanian Competent Authority for Environmental Data |
| `category` | `string` | — | `4` | `open` | — | Kurą deginančio įrenginio kategorija | Kurą deginančio įrenginio kategorija |
| `operatinghours` | `integer` | `h` | `4` | `open` | — | Darbo valandos | Darbo valandų per metus skaičius |
| `withinrefinery` | `boolean` | — | `4` | `open` | — | Naftos perdirbimo gamykla | Kurą deginančio įrenginio priklausymas naftos perdirbimo gamyklai |
| `productionproportion` | `number` | — | `3` | `open` | — | Šilumos gamybos dalis tiekiama centralizuotam šildymui | Šilumos gamybos dalis tiekiama centralizuotam šildymui |
| `reportid` | `integer` | — | `4` | `open` | — | Ataskaitos Id | Ataskaitos identifikacinis numeris |
| `year` | `integer` | — | `2` | `open` | — | Ataskaitiniai metai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `category` | `"Boiler"` | — | — | Boileris | — |
| `category` | `"DieselEngine"` | — | — | Dyzelinis variklis | — |
| `category` | `"GasEngine"` | — | — | Dujinis variklis | — |
| `category` | `"GasTurbine"` | — | — | Dujinė turbina | — |
| `category` | `"Other"` | — | — | Kita | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `year` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv
