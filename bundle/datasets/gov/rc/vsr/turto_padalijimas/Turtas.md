---
type: Table
title: "Turtas — Vedybų sutarčių registro (VSR) duomenys - pranešimai apie turto padalijimo faktą"
description: "Spinta table datasets/gov/rc/vsr/turto_padalijimas/Turtas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/turto_padalijimas/Turtas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/turto_padalijimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/turto_padalijimas.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Turtas — Vedybų sutarčių registro (VSR) duomenys - pranešimai apie turto padalijimo faktą

- **Model:** `datasets/gov/rc/vsr/turto_padalijimas/Turtas`[^manifest]
- **Dataset:** [Vedybų sutarčių registro (VSR) duomenys - pranešimai apie turto padalijimo faktą](../turto_padalijimas.md) (`datasets/gov/rc/vsr/turto_padalijimas`)
- **Manifest CSV:** [datasets/gov/rc/vsr/turto_padalijimas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/turto_padalijimas.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/turto_padalijimas/Turtas`
- **Primary Key (`ref`):** `dok_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `integer` | — | `4` | `open` | — | Dokumento identifikavimo kodas šiame rinkinyje | — |
| `statusas` | `ref` | [/datasets/gov/rc/vsr/klasifikatoriai/Statusas](../klasifikatoriai/Statusas.md) | `4` | `open` | — | Dokumento statusas iš VSR sutarčių statuso klasifikatoriaus | — |
| `reg_metai` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (metai) | — |
| `reg_ketvirtis` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (ketvirtis) | — |
| `teikejas` | `string` | — | `3` | `open` | — | Duomenų teikėjas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/turto_padalijimas.csv
