---
type: Table
title: "Dokumentas — Atestatai ir teisės pripažinimo dokumentai"
description: "Spinta table datasets/gov/ssva/rangovu_atestatai/Dokumentas (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/rangovu_atestatai/Dokumentas"
tags: [gov, ssva, dokumentas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1314/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/rangovu_atestatai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Dokumentas — Atestatai ir teisės pripažinimo dokumentai

- **Model:** `datasets/gov/ssva/rangovu_atestatai/Dokumentas`[^manifest]
- **Dataset:** [Duomenys apie statinio statybos ir ekspertizės rangovų atestatus, apie statinio statybos...](../rangovu_atestatai.md) (`datasets/gov/ssva/rangovu_atestatai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/rangovu_atestatai/Dokumentas` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc-nd/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Teisės dokumento ID | — |
| `nr` | `integer` | — | `4` | `open` | — | Teisės dokumento numeris | — |
| `isdavimas` | `date` | `D` | `4` | `open` | — | Teisės dokumento išdavimo data | — |
| `galiojimas` | `date` | `D` | `4` | `open` | — | Teisės dokumento galiojimo pabaiga | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Pirmoji teisės dokumento išdavimo data | — |
| `dokumentas` | `string` | — | `4` | `open` | — | Teisės dokumento tekstas | — |
| `rangovo_pav` | `string` | — | `2` | `open` | — | Rangovo pavadinimas | — |
| `rangovo_kod` | `string` | — | `2` | `open` | — | Rangovo juridinio asmens kodas | — |
| `rangovo_adr` | `string` | — | `2` | `open` | — | Rangovo adresas | — |
| `tipas` | `string` | — | `4` | `open` | — | Teisės dokumento tipas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Pripažinas teisės dokumentas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"KA"` | — | — | Kvalifikacijos atestatas | — |
| `tipas` | `"TPD"` | — | — | Teisės pripažinimo dokumentas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rangovo_pav` | `"update(property: ""rangovas@lt"", type: ""text"")"` | `property` | `4` | — | — | — | — |
| `rangovo_kod` | `"update(type: ""ref"", ref: ""/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/rangovu_atestatai (https://data.gov.lt/datasets/1314/)
