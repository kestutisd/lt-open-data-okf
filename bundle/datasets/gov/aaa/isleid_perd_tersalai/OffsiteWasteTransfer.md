---
type: Table
title: "OffsiteWasteTransfer — Atliekų perdavimas už objekto ribų"
description: "Spinta table datasets/gov/aaa/isleid_perd_tersalai/OffsiteWasteTransfer (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/OffsiteWasteTransfer"
tags: [gov, aaa, offsitewastetransfer, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L41"
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L41"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/665/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# OffsiteWasteTransfer — Atliekų perdavimas už objekto ribų

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/OffsiteWasteTransfer`[^manifest]
- **Dataset:** [Išleidžiamų ir perduodamų teršalų duomenys](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L41)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/OffsiteWasteTransfer` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Perduodamų atliekų Id | Perduodamų atliekų identifikacinis numeris (Eil. Nr.) |
| `localid` | `string` | — | `4` | `open` | — | Gamybos įrengimų komplekso Id | Gamybos įrengimų komplekso identifikacinis numeris |
| `wasteclassification` | `string` | — | `4` | `open` | — | Atliekų klasifikacija | Atliekų klasifikacija |
| `wastetreatment` | `string` | — | `4` | `open` | — | Atliekų naudojimas | Atliekų pašalinimas/perdirbimas |
| `quantity` | `number` | `t` | `4` | `open` | — | Visos atliekos | Visų atliekų kiekis, tonomis per ataskaitinius metus |
| `methodcode` | `string` | — | `2` | `open` | — | Metodo kodas | Metodo kodas (apskaičiuota/išmatuota reikšmė) |
| `methodclassification` | `string` | — | `2` | `open` | — | Metodo klasifikacija | Metodo klasifikacija |
| `nameofreceiver` | `string` | — | `1` | `open` | — | Gavėjo pavadinimas | Atliekų gavėjo pavadinimas |
| `countrycode` | `string` | — | `4` | `open` | — | Gavėjo šalies kodas | Pagal https://dd.eionet.europa.eu/vocabulary/EPRTRandLCP/CountryCodeValue/view |
| `year` | `integer` | — | `2` | `open` | — | Ataskaitiniai metai | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `wasteclassification` | `"HW"` | — | — | Pavojingosios atliekos | — |
| `wasteclassification` | `"NONHW"` | — | — | Nepavojingosios atliekos | — |
| `wastetreatment` | `"D"` | — | — | Šalinimas | — |
| `wastetreatment` | `"R"` | — | — | Perdirbimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `year` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv#L41 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L41)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/isleid_perd_tersalai (https://data.gov.lt/datasets/665/)
