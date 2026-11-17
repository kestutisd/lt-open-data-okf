---
type: Table
title: "Planinis — Metiniai planinių patikrinimų planai"
description: "Spinta table datasets/gov/ntakd/patikrinimo_planai/Planinis (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ntakd/patikrinimo_planai/Planinis"
tags: [gov, ntakd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ntakd/patikrinimo_planai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/patikrinimo_planai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Planinis — Metiniai planinių patikrinimų planai

- **Model:** `datasets/gov/ntakd/patikrinimo_planai/Planinis`[^manifest]
- **Dataset:** [Ūkio subjektų besiverčiančių alkoholio ir tabako gaminių didmenine ir mažmenine prekyba metiniai planinių patikrinimų planai](../patikrinimo_planai.md) (`datasets/gov/ntakd/patikrinimo_planai`)
- **Manifest CSV:** [datasets/gov/ntakd/patikrinimo_planai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ntakd/patikrinimo_planai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ntakd/patikrinimo_planai/Planinis`
- **Primary Key (`ref`):** `eil_nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `integer` | — | `4` | `open` | — | Eilės numeris | — |
| `ukio_subj_pav` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_pavadinimas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `2` | `open` | — | Ūkio subjekto pavadinimas | — |
| `ukio_subj_kodas` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_kodas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `3` | `open` | — | Ūkio subjekto kodas | — |
| `ukio_subj_adresas` | `string` | — | `2` | `open` | — | Ūkio subjekto adresas | — |
| `licencija` | `string` | — | `2` | `open` | — | Licencijos numeris | — |
| `veikla` | `string` | — | `3` | `open` | — | Ūkinės veiklos rūšis | — |
| `sandelio_prek_adresas` | `string` | — | `2` | `open` | — | Numatomo tikrinti sandėlio ar prekybos vietos adresas | — |
| `patikr_terminas` | `string` | — | `2` | `open` | — | Patikrinimo terminas ketvirčiais | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pastabos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ntakd/patikrinimo_planai.csv
