---
type: Table
title: "PaslauguLygis"
description: "Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguLygis"
tags: [gov, vaspvt, paslaugulygis, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L188"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L188"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1623/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PaslauguLygis

**Dataset Context:** Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys[^manifest]

- **Model:** `datasets/gov/vaspvt/licencijos/PaslauguLygis`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L188](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L188)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguLygis` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `paslaugu_lygio_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugu_lygio_id` | `string` | — | `2` | `open` | — | Paslaugos lygio identifikatorius | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Paslaugos lygio pavadinimas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugu_lygio_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `pavadinimas` | `update(property: "pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L188 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L188)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos (https://data.gov.lt/datasets/1623/)
