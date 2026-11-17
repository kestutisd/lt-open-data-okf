---
type: Table
title: "RestrukturizavimoAtaskaitosFinansiniai"
description: "Spinta table datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai"
tags: [gov, avnt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/avnt/imoniu_restrukturizavimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44"
    last_modified: "2026-11-11T14:39:20Z"
---

# RestrukturizavimoAtaskaitosFinansiniai

- **Model:** `datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai`[^manifest]
- **Dataset:** [Įmonių restruktūrizavimo ataskaitų duomenys](../imoniu_restrukturizavimas.md) (`datasets/gov/avnt/imoniu_restrukturizavimas`)
- **Manifest CSV:** [datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilutės numeris | — |
| `restrukt_metai` | `integer` | — | `4` | `open` | — | Restruktūrizavimo bylos iškėlimo metai | — |
| `turtas_proceso_pradzioje` | `number` | — | `4` | `open` | — | Turtas proceso pradžioje | — |
| `turtas_laikotarpio_pabaigoje` | `number` | — | `4` | `open` | — | Turtas ataskaitinio laikotarpio pabaigoje | — |
| `visi_kreditoriu_reikalavimai` | `number` | — | `4` | `open` | — | Teismo patvirtini visi kreditorių reikalavimai | — |
| `plane_numatyta_patenkinti` | `number` | — | `4` | `open` | — | Patenkinti kreditorių reikalavimai (numatyta plane) | — |
| `plane_numatyta_atsisakyti` | `number` | — | `4` | `open` | — | Atsisakyti kreditorių reikalavimai (numatyta plane) | — |
| `plane_numatyta_atideti` | `number` | — | `4` | `open` | — | Atidėti kreditorių reikalavimai (numatyta plane) | — |
| `patenkinti_reikalavimai` | `number` | — | `4` | `open` | — | Patenkinti kreditorių reikalavimai (įvykdyta) | — |
| `atsisakyti_reikalavimai` | `number` | — | `4` | `open` | — | Atsisakyti kreditorių reikalavimai (įvykdyta) | — |
| `atideti_reikalavimai` | `number` | — | `4` | `open` | — | Atidėti kreditorių reikalavimai (įvykdyta) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `update(base: "/datasets/gov/avnt/imoniu_bankrotas/BankrotoAtaskaitosFinansai")` | `base` | `4` | `open` | — | — | — |
| `(model)` | `update(ref: "eil_nr")` | `ref` | `4` | `open` | — | — | — |
| `eil_nr` | `update(type: "")` | `type` | `4` | `open` | — | — | — |
| `restrukt_metai` | `update(property: "metai", type: "")` | `type` | `4` | `open` | — | — | — |
| `restrukt_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `turtas_proceso_pradzioje` | `update(type: "")` | `type` | `4` | `open` | — | — | — |
| `turtas_proceso_pradzioje` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `turtas_laikotarpio_pabaigoje` | `update(type: "")` | `type` | `4` | `open` | — | — | — |
| `turtas_laikotarpio_pabaigoje` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `visi_kreditoriu_reikalavimai` | `update(type: "")` | `type` | `4` | `open` | — | — | — |
| `visi_kreditoriu_reikalavimai` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `plane_numatyta_patenkinti` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `plane_numatyta_atsisakyti` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `plane_numatyta_atideti` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `patenkinti_reikalavimai` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `atsisakyti_reikalavimai` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `atideti_reikalavimai` | `update(type: "currency", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/imoniu_restrukturizavimas.csv
