---
type: Table
title: "Asmuo — Profesinių ligų įvykių pagrindiniai duomenys"
description: "Spinta table datasets/gov/hi/profesines/Asmuo (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo"
tags: [gov, hi, asmuo, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L37"
    title: "atviriduomenys/manifest — datasets/gov/hi/profesines.csv#L37"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2257/"
    title: "data.gov.lt DCAT-AP — datasets/gov/hi/profesines"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Asmuo — Profesinių ligų įvykių pagrindiniai duomenys

- **Model:** `datasets/gov/hi/profesines/Asmuo`[^manifest]
- **Dataset:** [Lietuvos Respublikos profesinių ligų valstybės registro duomenys](../profesines.md) (`datasets/gov/hi/profesines`)[^manifest]
- **Manifest CSV:** [datasets/gov/hi/profesines.csv#L37](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L37)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/profesines/Asmuo` (`deployed`)[^manifest]
- **Provider:** `hi` — Higienos institutas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `m_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m_id` | `string` | — | `4` | `open` | — | Paciento ID | — |
| `pagr_tlk_kodas` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[code]`: `pagr_tlk_kodas._id`) | `4` | `open` | — | Pagrindinės profesinės ligos kodas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `pagr_tlk_pav` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[name]`: `pagr_tlk_pav._id`) | `4` | `open` | — | Pagrindinės profesinės ligos pavadinimas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `papild_tlk_kodas` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[code]`: `papild_tlk_kodas._id`) | `4` | `open` | — | Papildomas profesinės ligos kodas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `papild_tlk_pav` | `ref` | [Tlk10am](../../vlk/tlk10am/Tlk10am.md) (`level=4 UUID` via `Tlk10am[name]`: `papild_tlk_pav._id`) | `4` | `open` | — | Papildomas profesinės ligos pavadinimas | Ligos nurodomos pagal TLK-10-AM sisteminį ligų sąrašą |
| `ligos_eiga` | `string` | — | `4` | `open` | — | Ligos eiga | — |
| `itarta_pav` | `string` | — | `4` | `open` | — | Profesinės ligos įtarimo pavadinimas | — |
| `itarta_kodas` | `string` | — | `4` | `open` | — | Profesinės ligos įtarimo kodas | — |
| `priezasties_kodas` | `string` | — | `4` | `open` | — | Profesinės ligos priežasties kodas | — |
| `priezasties_pav` | `string` | — | `4` | `open` | — | Profesinės ligos priežasties pavadinimas | — |
| `lyties_kodas` | `string` | — | `4` | `open` | — | Paciento lyties kodas | — |
| `lyties_pavadinimas` | `string` | — | `4` | `open` | — | Paciento lyties pavadinimas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybė | Užregistruota profesinė liga |
| `year` | `integer` | `yr` | `2` | `open` | — | Metai | Profesinės ligos užregistravimo metai |
| `quarter` | `integer` | `3mo` | `2` | `open` | — | Ketvirtis | Profesinės ligos užregistravimo ketvirtis |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/profesines.csv#L37 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L37)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/hi/profesines (https://data.gov.lt/datasets/2257/)
