---
type: Table
title: "IkeistasObjektas — HR archyviniai duomenys apie įkeistus objektus (HR įkeistus objektus (turto rūšį) apibūdinantys požymiai)"
description: "Spinta table datasets/gov/rc/hr/ikeisti_objektai/IkeistasObjektas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/hr/ikeisti_objektai/IkeistasObjektas"
tags: [gov, rc, ikeistasobjektas, deployed, level-2, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/ikeisti_objektai.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/hr/ikeisti_objektai.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1995/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/hr/ikeisti_objektai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# IkeistasObjektas — HR archyviniai duomenys apie įkeistus objektus (HR įkeistus objektus (turto rūšį) apibūdinantys požymiai)

- **Model:** `datasets/gov/rc/hr/ikeisti_objektai/IkeistasObjektas`[^manifest]
- **Dataset:** [Likviduoto hipotekos registro (HR) archyviniai duomenys apie įkeistus objektus](../ikeisti_objektai.md) (`datasets/gov/rc/hr/ikeisti_objektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/hr/ikeisti_objektai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/ikeisti_objektai.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/hr/ikeisti_objektai/IkeistasObjektas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `sandorio_id`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sandorio_id` | `integer` | — | `2` | `open` | — | Sandorio identifikatorius dirbtinis | — |
| `turto_tipas` | `ref` | [TurtoTipas](../tipu_klasifikatoriai/TurtoTipas.md) (`level=4 UUID`: `turto_tipas._id`) | `4` | `open` | — | Turto tipas | — |
| `sandorio_tipas` | `ref` | [SandorioTipas](../tipu_klasifikatoriai/SandorioTipas.md) (`level=2` scalar) | `2` | `open` | — | Sandorio tipas | — |
| `sand_ireg_ketv` | `date` | `Q` | `2` | `open` | — | Sandorio įregistravimo metai - ketvirtis | — |
| `sand_isreg_ketv` | `date` | `Q` | `2` | `open` | — | Sandorio išregistravimo metai - ketvirtis | — |
| `iraso_priezastis` | `string` | — | `2` | `open` | — | Įrašo pagrindas | — |
| `sandorio_vieta` | `string` | — | `3` | `open` | — | Sandorio sudarymo vieta (sav. ; aps.) | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Sandorio sudarymo vietos savivaldybės kodas | — |
| `apskritis` | `ref` | [Apskritis](../../ar/apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Sandorio sudarymo vietos apskrities kodas | — |
| `pri_dydis_rez` | `string` | — | `2` | `open` | — | Prievolės rėžių dydžiai | — |
| `objektu_verte_rez` | `string` | — | `2` | `open` | — | Bendras įkeičiamų daiktų įkainojimas (rėžiai, NULL - nėra duomenų) | — |
| `pri_terminas_metai` | `integer` | — | `2` | `open` | — | Prievolės įvykdymo terminas (metai, NULL - nėra duomenų) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pri_terminas_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/hr/ikeisti_objektai.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/ikeisti_objektai.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/hr/ikeisti_objektai (https://data.gov.lt/datasets/1995/)
