---
type: Table
title: "VsrPabaiga — Vedybų sutarčių registro (VSR) duomenys - pranešimai apie vedybų sutarčių pabaigą"
description: "Spinta table datasets/gov/rc/vsr/sutarciu_pabaigos/VsrPabaiga (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/sutarciu_pabaigos/VsrPabaiga"
tags: [gov, rc, vsrpabaiga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2154/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/vsr/sutarciu_pabaigos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VsrPabaiga — Vedybų sutarčių registro (VSR) duomenys - pranešimai apie vedybų sutarčių pabaigą

- **Model:** `datasets/gov/rc/vsr/sutarciu_pabaigos/VsrPabaiga`[^manifest]
- **Dataset:** [Vedybų sutarčių registro (VSR) duomenys - pranešimai apie vedybų sutarčių pabaigą](../sutarciu_pabaigos.md) (`datasets/gov/rc/vsr/sutarciu_pabaigos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/sutarciu_pabaigos/VsrPabaiga` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `dok_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `integer` | — | `4` | `open` | — | Dokumento identifikavimo kodas šiame rinkinyje | — |
| `porusis` | `ref` | [Porusis](../klasifikatoriai/Porusis.md) (`level=4 UUID`: `porusis._id`) | `4` | `open` | — | Sutarties porūšis iš VRS sutarčių porūšių klasifikatoriaus | — |
| `statusas` | `ref` | [Statusas](../klasifikatoriai/Statusas.md) (`level=4 UUID`: `statusas._id`) | `4` | `open` | — | Sutarties statusas iš VRS sutarčių statusų klasifikatoriaus | — |
| `reg_metai` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (metai) | — |
| `reg_ketvirtis` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (ketvirtis) | — |
| `teikejas` | `string` | — | `3` | `open` | — | Duomenų teikėjas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutarciu_pabaigos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/vsr/sutarciu_pabaigos (https://data.gov.lt/datasets/2154/)
