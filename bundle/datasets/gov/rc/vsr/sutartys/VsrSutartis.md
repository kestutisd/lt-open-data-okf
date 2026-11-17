---
type: Table
title: "VsrSutartis — Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis"
description: "Spinta table datasets/gov/rc/vsr/sutartys/VsrSutartis (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/sutartys/VsrSutartis"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutartys.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# VsrSutartis — Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis

- **Model:** `datasets/gov/rc/vsr/sutartys/VsrSutartis`[^manifest]
- **Dataset:** [Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis](../sutartys.md) (`datasets/gov/rc/vsr/sutartys`)
- **Manifest CSV:** [datasets/gov/rc/vsr/sutartys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutartys.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/sutartys/VsrSutartis`
- **Primary Key (`ref`):** `dok_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `integer` | — | `4` | `open` | — | Dokumento identifikavimo kodas šiame rinkinyje | — |
| `porusis` | `ref` | [/datasets/gov/rc/vsr/klasifikatoriai/Porusis](../klasifikatoriai/Porusis.md) | `4` | `open` | — | Sutarties porūšis iš VRS sutarčių porūšių klasifikatoriaus | — |
| `statusas` | `ref` | [/datasets/gov/rc/vsr/klasifikatoriai/Statusas](../klasifikatoriai/Statusas.md) | `4` | `open` | — | Dokumento statusas iš VSR sutarčių statuso klasifikatoriaus | — |
| `sut_sud_metai` | `integer` | — | `2` | `open` | — | Sutarties patvirtinimo data (metai) | — |
| `sut_sud_ketvirtis` | `integer` | — | `2` | `open` | — | Sutarties patvirtinimo data (ketvirtis) | — |
| `reg_metai` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (metai) | — |
| `reg_ketvirtis` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (ketvirtis) | — |
| `teikejas` | `string` | — | `3` | `open` | — | Duomenų teikėjas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/sutartys.csv
