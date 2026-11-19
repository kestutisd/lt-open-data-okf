---
type: Table
title: "Sandoris — HR archyviniai duomenys apie sandorius (pagal hipotekos sandorių rūšis, vertė ir kt.)"
description: "Spinta table datasets/gov/rc/hr/sandoriai/Sandoris (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/hr/sandoriai/Sandoris"
tags: [gov, rc, sandoris, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/sandoriai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/hr/sandoriai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1996/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/hr/sandoriai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Sandoris — HR archyviniai duomenys apie sandorius (pagal hipotekos sandorių rūšis, vertė ir kt.)

- **Model:** `datasets/gov/rc/hr/sandoriai/Sandoris`[^manifest]
- **Dataset:** [Likviduoto hipotekos registro (HR) archyviniai duomenys apie sandorius](../sandoriai.md) (`datasets/gov/rc/hr/sandoriai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/hr/sandoriai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/sandoriai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/hr/sandoriai/Sandoris` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Sandorio identifikatorius dirbtinis | — |
| `sandorio_tipas` | `ref` | [SandorioTipas](../tipu_klasifikatoriai/SandorioTipas.md) (`level=4 UUID`: `sandorio_tipas._id`) | `4` | `open` | — | Sandorio tipas | — |
| `ireg_ketv` | `date` | `Q` | `4` | `open` | — | Sandorio įregistravimo metai - ketvirtis | — |
| `isreg_ketv` | `date` | `Q` | `4` | `open` | — | Sandorio išregistravimo metai - ketvirtis | — |
| `iraso_priezastis` | `string` | — | `3` | `open` | — | Įrašo pagrindas | — |
| `sandorio_vieta` | `string` | — | `3` | `open` | — | Sandorio sudarymo vieta (sav. ; aps.) | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Sandorio sudarymo vietos savivaldybės kodas | — |
| `apskritis` | `ref` | [Apskritis](../../ar/apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Sandorio sudarymo vietos apskrities kodas | — |
| `pri_dydis_rez` | `string` | — | `3` | `open` | — | Prievolės rėžių dydžiai | — |
| `objektu_verte_rez` | `string` | — | `3` | `open` | — | Bendras įkeičiamų daiktų įkainojimas (rėžiai) | — |
| `pri_terminas_metai` | `string` | — | `3` | `open` | — | Prievolės įvykdymo terminas (metai) | — |
| `maksimalus` | `integer` | — | `4` | `open` | — | Ar maksimalioji hipoteka (1 - taip; 0 - ne) | — |
| `paprastas` | `integer` | — | `4` | `open` | — | Ar paprastoji hipoteka (1 - taip; 0 - ne) | — |
| `jungtinis` | `integer` | — | `4` | `open` | — | Ar jungtinė hipoteka (1 - taip; 0 - ne) | — |
| `svetimas` | `integer` | — | `4` | `open` | — | Ar svetimo turto hipoteka (1 - taip; 0 - ne) | — |
| `bendras` | `integer` | — | `4` | `open` | — | Ar bendroji hipoteka (1 - taip; 0 - ne) | — |
| `salyginis` | `integer` | — | `4` | `open` | — | Ar sąlyginė hipoteka (1 - taip; 0 - ne) | — |
| `pareikstinis` | `integer` | — | `4` | `open` | — | Ar pareikštinė (1 - taip; 0 - ne) | — |
| `imones` | `integer` | — | `4` | `open` | — | Ar įmonės hipoteka (1 - taip; 0 - ne) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `maksimalus` | `0` | — | — | Ne | — |
| `maksimalus` | `1` | — | — | Taip | — |
| `paprastas` | `0` | — | — | Ne | — |
| `paprastas` | `1` | — | — | Taip | — |
| `jungtinis` | `0` | — | — | Ne | — |
| `jungtinis` | `1` | — | — | Taip | — |
| `svetimas` | `0` | — | — | Ne | — |
| `svetimas` | `1` | — | — | Taip | — |
| `bendras` | `0` | — | — | Ne | — |
| `bendras` | `1` | — | — | Taip | — |
| `salyginis` | `0` | — | — | Ne | — |
| `salyginis` | `1` | — | — | Taip | — |
| `pareikstinis` | `0` | — | — | Ne | — |
| `pareikstinis` | `1` | — | — | Taip | — |
| `imones` | `0` | — | — | Ne | — |
| `imones` | `1` | — | — | Taip | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pri_terminas_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/hr/sandoriai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/sandoriai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/hr/sandoriai (https://data.gov.lt/datasets/1996/)
