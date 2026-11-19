---
type: Table
title: "Issilavinimas — Profesinių ligų atvejai pagal išsilavinimą"
description: "Spinta table datasets/gov/hi/profesines/Issilavinimas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/profesines/Issilavinimas"
tags: [gov, hi, issilavinimas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/hi/profesines.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2257/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/profesines"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Issilavinimas — Profesinių ligų atvejai pagal išsilavinimą

- **Model:** `datasets/gov/hi/profesines/Issilavinimas`[^manifest]
- **Dataset:** [Lietuvos Respublikos profesinių ligų valstybės registro duomenys](../profesines.md) (`datasets/gov/hi/profesines`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/profesines.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/profesines/Issilavinimas` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `atvejis_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atvejis_id` | `string` | — | `4` | `open` | — | Profesinės ligos atvejo identifikatorius | Lietuvos Respublikos profesinių ligų valstybės registro objekto įregistravimo data |
| `pagr_tlk_kodas` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[code]`: `pagr_tlk_kodas._id`) | `4` | `open` | — | Pagrindinės profesinės ligos kodas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `pagr_tlk_pav` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[name]`: `pagr_tlk_pav._id`) | `4` | `open` | — | Pagrindinės profesinės ligos pavadinimas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `lyties_kodas` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `lpk` | `string` | — | `4` | `open` | — | Paciento profesija | Pagal Lietuvos profesijų klasifikatorių |
| `evrk` | `ref` | [EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) (`level=4 UUID` via `EkonominesVeiklosRusis[kodas]`: `evrk._id`) | `4` | `open` | — | EVRK kodas | Ekonominės veiklos rūšies klasifikatoriaus kodas. Nurodo, kuriame sektoriuje pacientas dirba |
| `year` | `integer` | `yr` | `2` | `open` | — | Metai | Profesinės ligos užregistravimo metai |
| `quarter` | `integer` | `3mo` | `2` | `open` | — | Ketvirtis | Profesinės ligos užregistravimo ketvirtis |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lyties_kodas` | `'1'` | — | — | Vyras | — |
| `lyties_kodas` | `'2'` | — | — | Moteris | — |

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/profesines.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/profesines (https://data.gov.lt/datasets/2257/)
