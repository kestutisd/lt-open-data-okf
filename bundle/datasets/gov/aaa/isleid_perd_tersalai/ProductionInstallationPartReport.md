---
type: Table
title: "ProductionInstallationPartReport — Gamybos įrengimų duomenys"
description: "Spinta table datasets/gov/aaa/isleid_perd_tersalai/ProductionInstallationPartReport (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/ProductionInstallationPartReport"
tags: [gov, aaa, productioninstallationpartreport, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L76"
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L76"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/665/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# ProductionInstallationPartReport — Gamybos įrengimų duomenys

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/ProductionInstallationPartReport`[^manifest]
- **Dataset:** [Išleidžiamų ir perduodamų teršalų duomenys](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L76](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L76)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/ProductionInstallationPartReport` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `localid` | `string` | — | `4` | `open` | — | Gamybos įrengimo Id | Gamybos įrengimo identifikacinis numeris |
| `namespace` | `string` | — | `2` | `open` | — | Duomenis teikianti šalis | LT.CAED – Lithuanian Competent Authority for Environmental Data |
| `category` | `string` | — | `4` | `open` | — | Kurą deginančio įrenginio kategorija | Kurą deginančio įrenginio kategorija |
| `operatinghours` | `integer` | `h` | `4` | `open` | — | Darbo valandos | Darbo valandų per metus skaičius |
| `withinrefinery` | `boolean` | — | `4` | `open` | — | Naftos perdirbimo gamykla | Kurą deginančio įrenginio priklausymas naftos perdirbimo gamyklai |
| `productionproportion` | `number` | — | `3` | `open` | — | Šilumos gamybos dalis tiekiama centralizuotam šildymui | Šilumos gamybos dalis tiekiama centralizuotam šildymui |
| `reportid` | `integer` | — | `4` | `open` | — | Ataskaitos Id | Ataskaitos identifikacinis numeris |
| `year` | `integer` | — | `2` | `open` | — | Ataskaitiniai metai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L76 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L76)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai (https://data.gov.lt/datasets/665/)
