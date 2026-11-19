---
type: Table
title: "Tautybe — Gyventojų registro tautybių klasifikatorius"
description: "Spinta table datasets/gov/rc/gr/tautybes/Tautybe (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/gr/tautybes/Tautybe"
tags: [gov, rc, tautybe, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/tautybes.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/gr/tautybes.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1756/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/gr/tautybes"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Tautybe — Gyventojų registro tautybių klasifikatorius

- **Model:** `datasets/gov/rc/gr/tautybes/Tautybe`[^manifest]
- **Dataset:** [Gyventojų registro tautybių klasifikatorius](../tautybes.md) (`datasets/gov/rc/gr/tautybes`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/gr/tautybes.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/tautybes.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/gr/tautybes/Tautybe` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `mot_tautybe` | `string` | — | `3` | `open` | — | Tautybės pavadinimas (mot.) | — |
| `vyr_tautybe` | `string` | — | `3` | `open` | — | Tautybės pavadinimas (vyr.) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/gr/tautybes.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/gr/tautybes.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/gr/tautybes (https://data.gov.lt/datasets/1756/)
