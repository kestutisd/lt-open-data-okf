---
type: Table
title: "OffsiteWasteTransfer — Atliekų perdavimas už objekto ribų"
description: "Spinta table datasets/gov/aaa/isleid_perd_tersalai/OffsiteWasteTransfer (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/OffsiteWasteTransfer"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L41"
    last_modified: "2026-11-11T14:39:20Z"
---

# OffsiteWasteTransfer — Atliekų perdavimas už objekto ribų

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/OffsiteWasteTransfer`[^manifest]
- **Dataset:** [datasets/gov/aaa/isleid_perd_tersalai](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L41)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/OffsiteWasteTransfer`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `wasteclassification` | `"HW"` | — | — | Pavojingosios atliekos | — |
| `wasteclassification` | `"NONHW"` | — | — | Nepavojingosios atliekos | — |
| `wastetreatment` | `"D"` | — | — | Šalinimas | — |
| `wastetreatment` | `"R"` | — | — | Perdirbimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `year` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv
