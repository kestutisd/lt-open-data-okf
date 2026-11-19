---
type: Table
title: "Statusas — Sutarčių statuso klasifikatorius"
description: "Spinta table datasets/gov/rc/vsr/klasifikatoriai/Statusas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/klasifikatoriai/Statusas"
tags: [gov, rc, statusas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/klasifikatoriai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2157/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/vsr/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Statusas — Sutarčių statuso klasifikatorius

- **Model:** `datasets/gov/rc/vsr/klasifikatoriai/Statusas`[^manifest]
- **Dataset:** [Vedybų sutarčių registro (VSR) klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/vsr/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/vsr/klasifikatoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/klasifikatoriai/Statusas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `statusas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `statusas` | `string` | — | `4` | `open` | — | Dokumento statusas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Dokumento statuso pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/klasifikatoriai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/vsr/klasifikatoriai (https://data.gov.lt/datasets/2157/)
