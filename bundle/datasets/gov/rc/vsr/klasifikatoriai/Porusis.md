---
type: Table
title: "Porusis — Sutarčių porūšių klasifikatorius"
description: "Spinta table datasets/gov/rc/vsr/klasifikatoriai/Porusis (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/klasifikatoriai/Porusis"
tags: [gov, rc, porusis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/klasifikatoriai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2157/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/vsr/klasifikatoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Porusis — Sutarčių porūšių klasifikatorius

- **Model:** `datasets/gov/rc/vsr/klasifikatoriai/Porusis`[^manifest]
- **Dataset:** [Vedybų sutarčių registro (VSR) klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/rc/vsr/klasifikatoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/vsr/klasifikatoriai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/klasifikatoriai/Porusis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `porusis`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `porusis` | `string` | — | `4` | `open` | — | Sutarties porūšio kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Sutarties porūšio pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/klasifikatoriai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/klasifikatoriai.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/vsr/klasifikatoriai (https://data.gov.lt/datasets/2157/)
