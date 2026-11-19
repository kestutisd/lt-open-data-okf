---
type: Table
title: "VeiklosAdresoPaslauga — Veiklos adresų paslaugos"
description: "Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/VeiklosAdresoPaslauga"
tags: [gov, vaspvt, veiklosadresopaslauga, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L118"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L118"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1623/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# VeiklosAdresoPaslauga — Veiklos adresų paslaugos

**Dataset Context:** Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys[^manifest]

- **Model:** `datasets/gov/vaspvt/licencijos/VeiklosAdresoPaslauga`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L118](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L118)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/VeiklosAdresoPaslauga` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `veiklos_adreso_paslaugos_id`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veiklos_adreso_paslaugos_id` | `string` | — | `2` | `open` | — | Veiklos adreso paslaugos identifikatorius | — |
| `paslauga` | `string` | — | `4` | `open` | — | Paslaugos identifikatorius | — |
| `paslaugos_lygis` | `string` | — | `4` | `open` | — | Paslaugos lygio identifikatorius | — |
| `paslaugos_budo_id` | `string` | — | `2` | `open` | — | Paslaugos būdo identifikatorius | — |
| `paslaugos_grupe` | `string` | — | `4` | `open` | — | Paslaugos grupės identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(ref: "veiklos_adreso_paslaugos_id")` | `ref` | `4` | `open` | — | — | — |
| `veiklos_adreso_paslaugos_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `paslaugos_budo_id` | `update(property: "paslaugu_lygis")` | `property` | `4` | `open` | — | — | — |
| `paslaugos_budo_id` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L118 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L118)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos (https://data.gov.lt/datasets/1623/)
