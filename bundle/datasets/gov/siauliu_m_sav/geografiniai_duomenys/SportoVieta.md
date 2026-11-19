---
type: Table
title: "SportoVieta — Šiaulių miesto savivaldybės sporto vietos"
description: "Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys."
resource: "https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys/SportoVieta"
tags: [gov, siauliu_m_sav, sportovieta, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2895/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/geografiniai_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# SportoVieta — Šiaulių miesto savivaldybės sporto vietos

Geografinėje informacinėje sistemoje ArcGis kaupiami geografiniai Šiaulių miesto savivaldybės duomenys. Rinkinyje pateikiami šiuo metu aktualios sporto vietų duomenys. Tarp sporto vietų duomenų pateikiami ir atsakingų asmenų kontaktai, kurių pagalba galima rezervuoti aikštę, salę ir kt. Duomenų teikėjas – Šiaulių miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/siauliu_m_sav/geografiniai_duomenys/SportoVieta`[^manifest]
- **Dataset:** [Šiaulių miesto savivaldybės geografiniai duomenys](../geografiniai_duomenys.md) (`datasets/gov/siauliu_m_sav/geografiniai_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_m_sav/geografiniai_duomenys/SportoVieta` (`deployed`)[^manifest]
- **Provider:** `siauliu_m_sav` — Šiaulių miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_m_sav/geografiniai_duomenys.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_m_sav/geografiniai_duomenys (https://data.gov.lt/datasets/2895/)
