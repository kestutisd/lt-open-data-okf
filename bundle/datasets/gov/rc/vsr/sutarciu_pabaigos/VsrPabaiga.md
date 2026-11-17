---
type: Table
title: "VsrPabaiga — Vedybų sutarčių registro (VSR) duomenys - pranešimai apie vedybų sutarčių pabaigą"
description: "Spinta table datasets/gov/rc/vsr/sutarciu_pabaigos/VsrPabaiga (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/sutarciu_pabaigos/VsrPabaiga"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/sutarciu_pabaigos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# VsrPabaiga — Vedybų sutarčių registro (VSR) duomenys - pranešimai apie vedybų sutarčių pabaigą

- **Model:** `datasets/gov/rc/vsr/sutarciu_pabaigos/VsrPabaiga`[^manifest]
- **Dataset:** [Vedybų sutarčių registro (VSR) duomenys - pranešimai apie vedybų sutarčių pabaigą](../sutarciu_pabaigos.md) (`datasets/gov/rc/vsr/sutarciu_pabaigos`)
- **Manifest CSV:** [datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/sutarciu_pabaigos/VsrPabaiga`
- **Primary Key (`ref`):** `dok_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `integer` | — | `4` | `open` | — | Dokumento identifikavimo kodas šiame rinkinyje | — |
| `porusis` | `ref` | [/datasets/gov/rc/vsr/klasifikatoriai/Porusis](../klasifikatoriai/Porusis.md) | `4` | `open` | — | Sutarties porūšis iš VRS sutarčių porūšių klasifikatoriaus | — |
| `statusas` | `ref` | [/datasets/gov/rc/vsr/klasifikatoriai/Statusas](../klasifikatoriai/Statusas.md) | `4` | `open` | — | Sutarties statusas iš VRS sutarčių statusų klasifikatoriaus | — |
| `reg_metai` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (metai) | — |
| `reg_ketvirtis` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (ketvirtis) | — |
| `teikejas` | `string` | — | `3` | `open` | — | Duomenų teikėjas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/sutarciu_pabaigos.csv
