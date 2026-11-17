---
type: Table
title: "IkeistasObjektas — HR archyviniai duomenys apie įkeistus objektus (HR įkeistus objektus (turto rūšį) apibūdinantys požymiai)"
description: "Spinta table datasets/gov/rc/hr/ikeisti_objektai/IkeistasObjektas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/hr/ikeisti_objektai/IkeistasObjektas"
tags: [gov, rc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/hr/ikeisti_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/ikeisti_objektai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# IkeistasObjektas — HR archyviniai duomenys apie įkeistus objektus (HR įkeistus objektus (turto rūšį) apibūdinantys požymiai)

- **Model:** `datasets/gov/rc/hr/ikeisti_objektai/IkeistasObjektas`[^manifest]
- **Dataset:** [Likviduoto hipotekos registro (HR) archyviniai duomenys apie įkeistus objektus](../ikeisti_objektai.md) (`datasets/gov/rc/hr/ikeisti_objektai`)
- **Manifest CSV:** [datasets/gov/rc/hr/ikeisti_objektai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/hr/ikeisti_objektai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/hr/ikeisti_objektai/IkeistasObjektas`
- **Primary Key (`ref`):** `sandorio_id`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sandorio_id` | `integer` | — | `2` | `open` | — | Sandorio identifikatorius dirbtinis | — |
| `turto_tipas` | `ref` | [/datasets/gov/rc/hr/tipu_klasifikatoriai/TurtoTipas](../tipu_klasifikatoriai/TurtoTipas.md) | `4` | `open` | — | Turto tipas | — |
| `sandorio_tipas` | `ref` | [/datasets/gov/rc/hr/tipu_klasifikatoriai/SandorioTipas](../tipu_klasifikatoriai/SandorioTipas.md) | `2` | `open` | — | Sandorio tipas | — |
| `sand_ireg_ketv` | `date` | `Q` | `2` | `open` | — | Sandorio įregistravimo metai - ketvirtis | — |
| `sand_isreg_ketv` | `date` | `Q` | `2` | `open` | — | Sandorio išregistravimo metai - ketvirtis | — |
| `iraso_priezastis` | `string` | — | `2` | `open` | — | Įrašo pagrindas | — |
| `sandorio_vieta` | `string` | — | `3` | `open` | — | Sandorio sudarymo vieta (sav. ; aps.) | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Sandorio sudarymo vietos savivaldybės kodas | — |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../ar/apskritis/Apskritis.md) | `4` | `open` | — | Sandorio sudarymo vietos apskrities kodas | — |
| `pri_dydis_rez` | `string` | — | `2` | `open` | — | Prievolės rėžių dydžiai | — |
| `objektu_verte_rez` | `string` | — | `2` | `open` | — | Bendras įkeičiamų daiktų įkainojimas (rėžiai, NULL - nėra duomenų) | — |
| `pri_terminas_metai` | `integer` | — | `2` | `open` | — | Prievolės įvykdymo terminas (metai, NULL - nėra duomenų) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pri_terminas_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/hr/ikeisti_objektai.csv
