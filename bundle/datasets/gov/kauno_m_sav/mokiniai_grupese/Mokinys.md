---
type: Table
title: "Mokinys — Neformalaus ugdymo grupių mokiniai"
description: "\"Rinkinyje pateikiama Kauno m. savivaldybės neformalaus ugdymo grupių užimtumo informacija nuo 2021 m. rugsėjo mėn.\""
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/mokiniai_grupese/Mokinys"
tags: [gov, kauno_m_sav, mokinys, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/mokiniai_grupese.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/mokiniai_grupese.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2943/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/mokiniai_grupese"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Mokinys — Neformalaus ugdymo grupių mokiniai

"Rinkinyje pateikiama Kauno m. savivaldybės neformalaus ugdymo grupių užimtumo informacija nuo 2021 m. rugsėjo mėn."[^manifest]

- **Model:** `datasets/gov/kauno_m_sav/mokiniai_grupese/Mokinys`[^manifest]
- **Dataset:** [Neformalaus ugdymo grupių mokiniai](../mokiniai_grupese.md) (`datasets/gov/kauno_m_sav/mokiniai_grupese`)[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/mokiniai_grupese.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/mokiniai_grupese.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/mokiniai_grupese/Mokinys` (`deployed`)[^manifest]
- **Provider:** `kauno_m_sav` — Kauno miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `mokinio_id` | `string` | — | `4` | `open` | — | Unikalus mokinio id | — |
| `grupes_id` | `string` | — | `4` | `open` | — | Unikalus grupės id | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Mokinio gmimo metai sistemoje | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Mokinio asmens kodas | — |
| `asmens_kodas_validus` | `string` | — | `4` | `open` | — | Požymis ar asmens kodas validus | — |
| `gim_metai_ak` | `date` | `Y` | `4` | `open` | — | Gimimo metai iš asmens kodo | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Lytis iš asmens kodo | — |
| `deklaruotas_kaune` | `boolean` | — | `4` | `open` | — | Požymis ar deklaruotas Kaune | — |
| `grupe_lanko_nuo` | `date` | `D` | `4` | `open` | — | Grupę lanko nuo | — |
| `grupe_lanko_iki` | `date` | `D` | `4` | `open` | — | Grupę lanko iki | — |
| `grupes_veikla` | `string` | — | `4` | `open` | — | Grupės veikla | — |
| `grupes_veiklos_tipas` | `string` | — | `4` | `open` | — | Grupės veiklos tipas | — |
| `max_grupeje_asm` | `integer` | — | `4` | `open` | — | Didžiausias kiekis asmenų grupėje | — |
| `indiv_iduali_grupe` | `boolean` | — | `4` | `open` | — | Požymis ar individuali grupė | — |
| `mokyklos_kodas` | `string` | — | `4` | `open` | — | Mokyklos kodas | — |
| `mokyklos_pavadinimas` | `string` | — | `4` | `open` | — | Mokyklos pavadinimas | — |
| `mokyklos_adresas` | `string` | — | `4` | `open` | — | Mokyklos adresas | — |
| `lat_wgs` | `number` | — | `4` | `open` | — | Mokyklos WGS koordinatės platuma | — |
| `lon_wgs` | `number` | — | `4` | `open` | — | Mokyklos WGS koordinatės ilguma | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_ak` | `"Moteris"` | — | — | Moteris | — |
| `lytis_ak` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/mokiniai_grupese.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/mokiniai_grupese.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kauno_m_sav/mokiniai_grupese (https://data.gov.lt/datasets/2943/)
