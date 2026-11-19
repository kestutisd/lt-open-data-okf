---
type: Table
title: "PaslauguNustatymas"
description: "Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguNustatymas"
tags: [gov, vaspvt, paslaugunustatymas, deployed, level-3, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L143"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L143"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1623/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PaslauguNustatymas

**Dataset Context:** Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys[^manifest]

- **Model:** `datasets/gov/vaspvt/licencijos/PaslauguNustatymas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L143](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L143)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/PaslauguNustatymas` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `paslaugos_nustatymo_id`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugos_nustatymo_id` | `string` | — | `2` | `open` | — | Paslaugos nustatymo identifikatorius | — |
| `paslaugos_budas` | `string` | — | `2` | `open` | — | Paslaugos būdo identifikatorius | — |
| `paslaugos_id` | `string` | — | `2` | `open` | — | Paslaugos identifikatorius | — |
| `paslaugos_grupes_id` | `string` | — | `2` | `open` | — | Paslaugos grupės identifikatorius | — |
| `paslaugos_lygio_id` | `string` | — | `2` | `open` | — | Paslaugos lygio identifikatorius | — |
| `paslaugos_tipo_id` | `string` | — | `2` | `open` | — | Paslaugos tipo identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paslaugos_nustatymo_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `paslaugos_budas` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |
| `paslaugos_id` | `update(property: "paslauga", type: "ref", ref: "IstaigosPaslauga")` | `type` | `4` | `open` | — | — | — |
| `paslaugos_grupes_id` | `update(property: "paslaugu_grupe", type: "ref", ref: "PaslauguGrupe")` | `type` | `4` | `open` | — | — | — |
| `paslaugos_lygio_id` | `update(property: "paslaugu_lygis", type: "ref", ref: "PaslauguLygis")` | `type` | `4` | `open` | — | — | — |
| `paslaugos_tipo_id` | `update(ref: "enum")` | `ref` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L143 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L143)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos (https://data.gov.lt/datasets/1623/)
