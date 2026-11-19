---
type: Table
title: "RestrukturizavimoAtaskaitosFinansiniai"
description: "Spinta table datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai"
tags: [gov, avnt, restrukturizavimoataskaitosfinansiniai, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44"
    title: "atviriduomenys/manifest — datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1333/"
    title: "data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_restrukturizavimas"
    author: "team:vda"
    last_modified: "2026-02-25T00:00:00Z"
---

# RestrukturizavimoAtaskaitosFinansiniai

- **Model:** `datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai`[^manifest]
- **Dataset:** [Įmonių restruktūrizavimo ataskaitų duomenys](../imoniu_restrukturizavimas.md) (`datasets/gov/avnt/imoniu_restrukturizavimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/avnt/imoniu_restrukturizavimas/RestrukturizavimoAtaskaitosFinansiniai` (`deployed`)[^manifest]
- **Provider:** `avnt` — Audito, apskaitos, turto vertinimo ir nemokumo valdymo tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-02-25`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/avnt/imoniu_restrukturizavimas.csv#L44)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/avnt/imoniu_restrukturizavimas (https://data.gov.lt/datasets/1333/)
