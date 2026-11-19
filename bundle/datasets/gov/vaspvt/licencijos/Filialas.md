---
type: Table
title: "Filialas — Sveikatos priežiūros įstaigų filialai"
description: "Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys"
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Filialas"
tags: [gov, vaspvt, filialas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L61"
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L61"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1623/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Filialas — Sveikatos priežiūros įstaigų filialai

**Dataset Context:** Valstybinės akreditavimo sveikatos priežiūrai veiklos tarnybos duomenys[^manifest]

- **Model:** `datasets/gov/vaspvt/licencijos/Filialas`[^manifest]
- **Dataset:** [Valstybinės akreditavimo sveikatos priežiūros veiklos tarnyba](../licencijos.md) (`datasets/gov/vaspvt/licencijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/licencijos.csv#L61](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L61)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/licencijos/Filialas` (`deployed`)[^manifest]
- **Provider:** `vaspvt` — Valstybinė akreditavimo sveikatos priežiūros veiklai tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `3` | `open` | — | Eilutės dirbtinis unikalus identifikatorius | — |
| `filialo_id` | `string` | — | `2` | `open` | — | Filialo identifikatorius | — |
| `istaiga` | `string` | — | `4` | `open` | — | Sveikatos priežiūros įstaiga | — |
| `juridinio_asmens_kodas` | `string` | — | `2` | `open` | — | Sveikatos priežiūros įstaigos juridinio asmens kodas | — |
| `filialo_pavadinimas` | `string` | — | `2` | `open` | — | Filialo pavadinimas | — |
| `adresas` | `string` | — | `1` | `open` | — | Buveinės adresas | — |
| `veiklos_adresas` | `string` | — | `1` | `open` | — | Veiklos adresas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `filialo_id` | `update(property: "id")` | `property` | `4` | `open` | — | — | — |
| `juridinio_asmens_kodas` | `update(property: "istaiga.ja_kodas", type: "")` | `property` | `4` | `open` | — | — | — |
| `filialo_pavadinimas` | `update(property: "pavadinimas")` | `property` | `4` | `open` | — | — | — |
| `filialo_pavadinimas` | `update(property: "pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `adresas` | `update(type: "ref", ref: "/datasets/gov/rc/ar/patalpa/Patalpa")` | `type` | `4` | `open` | — | — | — |
| `veiklos_adresas` | `update(type: "ref", ref: "/datasets/gov/rc/ar/patalpa/Patalpa")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/licencijos.csv#L61 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/licencijos.csv#L61)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vaspvt/licencijos (https://data.gov.lt/datasets/1623/)
