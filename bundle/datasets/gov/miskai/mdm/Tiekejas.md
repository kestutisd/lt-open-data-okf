---
type: Table
title: "Tiekejas"
description: "Spinta table datasets/gov/miskai/mdm/Tiekejas (8 columns)."
tags: [gov, miskai, tiekejas, undeployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/mdm.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/miskai/mdm.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tiekejas

- **Model:** `datasets/gov/miskai/mdm/Tiekejas`[^manifest]
- **Dataset:** [datasets/gov/miskai/mdm](../mdm.md) (`datasets/gov/miskai/mdm`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/mdm.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/mdm.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilės nr. | — |
| `tiekejas` | `string` | — | `3` | `open` | — | MDM tiekėjas | Miško dauginamosios medžiagos tiekėjas |
| `buveine` | `string` | — | `3` | `open` | — | Buveinė, gyvenamosios vietos adresas | — |
| `tel` | `string` | — | `2` | `open` | — | Telefono nr. | — |
| `mob_tel` | `string` | — | `3` | `open` | — | Mobilaus telefono nr. | — |
| `faksas` | `string` | — | `3` | `open` | — | Faksas | — |
| `el_pastas` | `string` | — | `2` | `open` | — | El. paštas | — |
| `papildoma_informacija` | `string` | — | `2` | `open` | — | Papildoma informacija | Pvz. kur siųsti korespondenciją |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/mdm.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/mdm.csv#L4)
