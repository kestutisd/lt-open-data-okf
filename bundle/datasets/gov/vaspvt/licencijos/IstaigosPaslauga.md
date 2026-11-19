---
type: Table
title: "IstaigosPaslauga — Sveikatos priežiūros įstaigų paslaugos"
description: "Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosPaslauga"
tags: [gov, vaspvt, istaigospaslauga, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L86"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L86"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1623/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IstaigosPaslauga — Sveikatos priežiūros įstaigų paslaugos

**Dataset Context:** Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys[^manifest]

- **Model:** `datasets/gov/vaspvt/licencijos/IstaigosPaslauga`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L86](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L86)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/IstaigosPaslauga` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `istaigos_paslaugos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaigos_paslaugos_id` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos paslaugos identifikatorius | — |
| `nustatymas` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaigos paslaugos nustatymo identifikatorius | — |
| `licenzija` | `string` | — | `4` | `open` | — | Licencija | — |
| `istaiga` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaiga | — |
| `filialo_id` | `string` | — | `2` | `open` | — | Filialo identifikatorius | — |
| `veiklos_adresas` | `string` | — | `4` | `open` | — | Veiklos adreso identifikatorius | — |
| `patikslinta` | `boolean` | — | `3` | `open` | — | Patikslinimo būsena | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istaigos_paslaugos_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `filialo_id` | `update(property: "filialas")` | `property` | `4` | `open` | — | — | — |
| `filialo_id` | `update(type: "ref", ref: "Istaiga")` | `type` | `4` | `open` | — | — | — |
| `patikslinta` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L86 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L86)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos (https://data.gov.lt/datasets/1623/)
