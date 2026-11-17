---
type: Table
title: "OffSitePollutantTransfer — Teršalų perdavimas už objekto ribų"
description: "Spinta table datasets/gov/aaa/isleid_perd_tersalai/OffSitePollutantTransfer (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/OffSitePollutantTransfer"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L31"
    last_modified: "2026-11-11T14:39:20Z"
---

# OffSitePollutantTransfer — Teršalų perdavimas už objekto ribų

- **Model:** `datasets/gov/aaa/isleid_perd_tersalai/OffSitePollutantTransfer`[^manifest]
- **Dataset:** [datasets/gov/aaa/isleid_perd_tersalai](../isleid_perd_tersalai.md) (`datasets/gov/aaa/isleid_perd_tersalai`)
- **Manifest CSV:** [datasets/gov/aaa/isleid_perd_tersalai.csv#L31](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/isleid_perd_tersalai.csv#L31)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/isleid_perd_tersalai/OffSitePollutantTransfer`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Perduodamų teršalų Id | Perduodamų teršalų identifikacinis numeris (Eil. Nr.) |
| `localid` | `string` | — | `4` | `open` | — | Gamybos įrengimų komplekso Id | Gamybos įrengimų komplekso identifikacinis numeris |
| `pollutant` | `string` | — | `2` | `open` | — | Teršalas | Teršalo kodas pagal https://dd.eionet.europa.eu/vocabulary/EPRTRandLCP/EPRTRPollutantCodeValue/view |
| `quantity` | `number` | `kg` | `4` | `open` | — | Visas teršalo kiekis | Teršalo kiekis, esantis nuotekose prieš jų valymą |
| `methodcode` | `string` | — | `2` | `open` | — | Metodo kodas | Metodo kodas (apskaičiuota/išmatuota reikšmė) |
| `methodclassification` | `string` | — | `2` | `open` | — | Metodo klasifikacija | Metodo klasifikacija, pateikta aktyvia nuoroda: https://dd.eionet.europa.eu/vocabulary/EPRTRandLCP/MethodClassificationValue/view |
| `year` | `integer` | — | `2` | `open` | — | Ataskaitiniai metai | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `year` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/isleid_perd_tersalai.csv
