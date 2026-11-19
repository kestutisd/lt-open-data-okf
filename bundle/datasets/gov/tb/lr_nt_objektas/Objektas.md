---
type: Table
title: "Objektas — Lietuvos Respublikos nuosavybės teise valdomas turtas"
description: "\"Turto banke registruotas Lietuvos Respublikos nuosavybės teise valdomas turtas\""
resource: "https://get.data.gov.lt/datasets/gov/tb/lr_nt_objektas/Objektas"
tags: [gov, tb, objektas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tb/lr_nt_objektas.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/tb/lr_nt_objektas.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2882/"
    title: "data.gov.lt DCAT-AP — datasets/gov/tb/lr_nt_objektas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Objektas — Lietuvos Respublikos nuosavybės teise valdomas turtas

"Turto banke registruotas Lietuvos Respublikos nuosavybės teise valdomas turtas"[^manifest]

- **Model:** `datasets/gov/tb/lr_nt_objektas/Objektas`[^manifest]
- **Dataset:** [Lietuvos Respublikos nuosavybės teise valdomas turtas](../lr_nt_objektas.md) (`datasets/gov/tb/lr_nt_objektas`)[^manifest]
- **Manifest CSV:** [datasets/gov/tb/lr_nt_objektas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tb/lr_nt_objektas.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tb/lr_nt_objektas/Objektas` (`deployed`)[^manifest]
- **Provider:** `tb` — Turto Bankas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `obj_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `obj_id` | `string` | — | `4` | `open` | — | Unikalus objekto identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | Objekto kodas | — |
| `tipas` | `string` | — | `4` | `open` | — | "Objekto tipas: Pastatas, Inžinerija, Patalpa" | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `registro_nr` | `string` | — | `4` | `open` | — | Registro kodas RC | — |
| `unikalus_nr` | `string` | — | `4` | `open` | — | Unikalus objekto kodas RC | — |
| `paskirtis` | `string` | — | `4` | `open` | — | Pastato paskirtis | — |
| `paskirtis_1` | `string` | — | `4` | `open` | — | Detalesnė pastato paskirtis | — |
| `paskirtis_2` | `string` | — | `4` | `open` | — | Detalesnė pastato paskirtis 2 | — |
| `bendras_plotas` | `number` | — | `4` | `open` | — | Bendras plotas | — |
| `salis` | `string` | — | `4` | `open` | — | Šalis | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | — |
| `miestas` | `string` | — | `4` | `open` | — | Miestas | — |
| `gatve` | `string` | — | `4` | `open` | — | Gatvė | — |
| `namas` | `string` | — | `4` | `open` | — | Namas | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | X koordinatės LKS | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Y koordinatės LKS | — |
| `nuosavybe_nuo` | `date` | `D` | `4` | `open` | — | Lietuvos Respublikos nuosavybė nuo | — |
| `nuosavybe_iki` | `date` | `D` | `4` | `open` | — | Lietuvos Respublikos nuosavybė iki | — |
| `geometrija` | `geometry(3346)` | — | `4` | `open` | — | Geometrija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"Pastatas"` | — | — | Pastatas | — |
| `tipas` | `"Inžinerija"` | — | — | Inžinerija | — |
| `tipas` | `"Patalpa"` | — | — | Patalpa | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/tb/lr_nt_objektas.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tb/lr_nt_objektas.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/tb/lr_nt_objektas (https://data.gov.lt/datasets/2882/)
