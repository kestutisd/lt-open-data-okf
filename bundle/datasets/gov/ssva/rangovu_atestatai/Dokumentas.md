---
type: Table
title: "Dokumentas — Atestatai ir teisės pripažinimo dokumentai"
description: "Spinta table datasets/gov/ssva/rangovu_atestatai/Dokumentas (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ssva/rangovu_atestatai/Dokumentas"
tags: [gov, ssva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dokumentas — Atestatai ir teisės pripažinimo dokumentai

- **Model:** `datasets/gov/ssva/rangovu_atestatai/Dokumentas`[^manifest]
- **Dataset:** [Duomenys apie statinio statybos ir ekspertizės rangovų atestatus, apie statinio statybos, ekspertizės rangovų ir projektuotojų teisės pripažinimo dokumentus (juridiniai asmenys)](../rangovu_atestatai.md) (`datasets/gov/ssva/rangovu_atestatai`)
- **Manifest CSV:** [datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/rangovu_atestatai/Dokumentas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"KA"` | — | — | Kvalifikacijos atestatas | — |
| `tipas` | `"TPD"` | — | — | Teisės pripažinimo dokumentas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rangovo_pav` | `"update(property: ""rangovas@lt"", type: ""text"")"` | `property` | `4` | — | — | — | — |
| `rangovo_kod` | `"update(type: ""ref"", ref: ""/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/atestatai_teses_pripazinimo_dok.csv
