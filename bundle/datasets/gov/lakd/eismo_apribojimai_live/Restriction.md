---
type: Table
title: "Restriction"
description: "Spinta table datasets/gov/lakd/eismo_apribojimai_live/Restriction (4 columns)."
tags: [gov, lakd, restriction, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_apribojimai_live.csv#L40"
    title: "atviriduomenys/manifest — datasets/gov/lakd/eismo_apribojimai_live.csv#L40"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Restriction

- **Model:** `datasets/gov/lakd/eismo_apribojimai_live/Restriction`[^manifest]
- **Dataset:** [Eismo ribojimų duomenų katalogas](../eismo_apribojimai_live.md) (`datasets/gov/lakd/eismo_apribojimai_live`)[^manifest]
- **Manifest CSV:** [datasets/gov/lakd/eismo_apribojimai_live.csv#L40](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_apribojimai_live.csv#L40)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `lakd` — AB „Via Lietuva“ (buv. Lietuvos automobilių kelių direkcija) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `traffic_restriction_service` | `ref` | [TrafficRestrictionService](TrafficRestrictionService.md) (`level=4 UUID`: `traffic_restriction_service._id`) | `4` | `open` | — | — | — |
| `restriction_type` | `string` | — | `4` | `open` | — | Apribojimo tipas | — |
| `value` | `integer` | — | `3` | `open` | — | Apribojimo informacija | — |
| `transport_type` | `string` | — | `3` | `open` | — | Transporto tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `restriction_type` | `"heightLimit"` | — | — | Aukščio apribojimas | — |
| `restriction_type` | `"widthLimit"` | — | — | Pločio apribojimas | — |
| `restriction_type` | `"weightLimit"` | — | — | Svorio apribojimas | — |
| `restriction_type` | `"speedLimit"` | — | — | Greičio apribojimas | — |
| `restriction_type` | `"LD"` | — | — | — | — |
| `restriction_type` | `"roadClosed"` | — | — | Uždarytas kelias | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lakd/eismo_apribojimai_live.csv#L40 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lakd/eismo_apribojimai_live.csv#L40)
