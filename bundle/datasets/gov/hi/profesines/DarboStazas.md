---
type: Table
title: "DarboStazas — Profesinių ligų atvejai pagal darbo stažą"
description: "Spinta table datasets/gov/hi/profesines/DarboStazas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/profesines/DarboStazas"
tags: [gov, hi, darbostazas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L16"
    title: "atviriduomenys/manifest — datasets/gov/hi/profesines.csv#L16"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2257/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/profesines"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# DarboStazas — Profesinių ligų atvejai pagal darbo stažą

- **Model:** `datasets/gov/hi/profesines/DarboStazas`[^manifest]
- **Dataset:** [Lietuvos Respublikos profesinių ligų valstybės registro duomenys](../profesines.md) (`datasets/gov/hi/profesines`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/profesines.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L16)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/profesines/DarboStazas` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `atvejis_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atvejis_id` | `string` | — | `4` | `open` | — | Profesinės ligos atvejo identifikatorius | — |
| `pagr_tlk_kodas` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[code]`: `pagr_tlk_kodas._id`) | `4` | `open` | — | Pagrindinės profesinės ligos kodas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `pagr_tlk_pav` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[name]`: `pagr_tlk_pav._id`) | `4` | `open` | — | Pagrindinės profesinės ligos pavadinimas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `lpk` | `string` | — | `4` | `open` | — | Paciento profesija | Pagal Lietuvos profesijų klasifikatorių |
| `evrk` | `string` | — | `4` | `open` | — | EVRK kodas | Ekonominės veiklos rūšies klasifikatoriaus kodas. Nurodo, kuriame sektoriuje pacientas dirba |
| `stazas` | `string` | — | `4` | `open` | — | Darbo stažo grupės | Metais |
| `year` | `integer` | `yr` | `2` | `open` | — | Metai | Profesinės ligos užregistravimo metai |
| `quarter` | `integer` | `3mo` | `2` | `open` | — | Ketvirtis | Profesinės ligos užregistravimo ketvirtis |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `stazas` | `'50+'` | — | — | 50+ | — |
| `stazas` | `'45-49'` | — | — | 45-49 | — |
| `stazas` | `'40-44'` | — | — | 40-44 | — |
| `stazas` | `'35-39'` | — | — | 35-39 | — |
| `stazas` | `'30-34'` | — | — | 30-34 | — |
| `stazas` | `'25-29'` | — | — | 25-29 | — |
| `stazas` | `'20-24'` | — | — | 20-24 | — |
| `stazas` | `'15-19'` | — | — | 15-19 | — |
| `stazas` | `'10-14'` | — | — | 10-14 | — |
| `stazas` | `'5-9'` | — | — | 5-9 | — |
| `stazas` | `'0-4'` | — | — | 0-4 | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/profesines.csv#L16 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L16)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/profesines (https://data.gov.lt/datasets/2257/)
