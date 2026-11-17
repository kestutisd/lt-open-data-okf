---
type: Table
title: "SportoVieta — Šiaulių miesto savivaldybės sporto vietos"
description: "Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys."
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys/SportoVieta"
tags: [gov, siauliu_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# SportoVieta — Šiaulių miesto savivaldybės sporto vietos

Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. Rinkinyje pateikiami šiuo metu aktualios sporto vietų duomenys. Tarp sporto vietų duomenų pateikiami ir atsakingų asmenų kontaktai, kurių pagalba galima rezervuoti aikštę, salę ir kt.

Duomenų teikėjas – Šiaulių miesto savivaldybės administracija.

- **Model:** `datasets/gov/siauliu_m_sav/geografiniai_duomenys/SportoVieta`[^manifest]
- **Dataset:** [Šiaulių miesto savivaldybės geografiniai duomenys](../geografiniai_duomenys.md) (`datasets/gov/siauliu_m_sav/geografiniai_duomenys`)
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys/SportoVieta`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Tipas | — |
| `adresas` | `string` | — | `4` | `open` | — | Adresas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatė LKS94 koordinačių sistemoje | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatė LKS94 koordinačių sistemoje | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Platumos koordinatė WGS84 koordinačių sistemoje | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Ilgumos koordinatė WGS84 koordinačių sistemoje | — |
| `epastas` | `string` | — | `4` | `open` | — | El. paštas | — |
| `kontaktai` | `string` | — | `2` | `open` | — | Kontaktai | — |
| `svetaine` | `string` | — | `4` | `open` | — | Svetainės adresas | — |
| `kalendorius` | `string` | — | `4` | `open` | — | Kalendorius | — |
| `geometrija` | `geometry(point, 3346)` | — | `3` | `open` | — | Geometrija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv
