---
type: Table
title: "PaukscioZiedavimas — Paukščių ir šikšnosparnių žiedavimo duomenys"
description: "Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Lietuvoje atliktų paukščių ir šikšnosparnių žiedavimų duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioZiedavimas"
tags: [gov, ktizm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L28"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaukscioZiedavimas — Paukščių ir šikšnosparnių žiedavimo duomenys

Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Lietuvoje atliktų paukščių ir šikšnosparnių žiedavimų duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės. Duomenų atnaujinimas vykdomas kartą per metus.

- **Model:** `datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioZiedavimas`[^manifest]
- **Dataset:** [Paukščių ir šikšnosparnių aptikimų, žiedavimų ir biometriniai duomenys](../pauksciai_ir_siksnosparniai.md) (`datasets/gov/ktizm/pauksciai_ir_siksnosparniai`)
- **Manifest CSV:** [datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L28](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L28)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioZiedavimas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `ziedavimo_data` | `date` | `D` | `4` | `open` | — | Žiedavimo data | — |
| `p_rusis_lot` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio rūšies lotyniškas pavadinimas | — |
| `p_rusis_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio rūšies angliškas pavadinimas | — |
| `p_lytis_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio lytis | — |
| `p_amzius_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio amžiaus kategorija (anglų k.) | — |
| `p_amzius_lt` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio amžiaus kategorija (lietuvių k.) | — |
| `p_ziedo_schema` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedo schema | — |
| `p_ziedo_nr` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedo numeris | — |
| `ziedavimo_teritorija` | `string` | — | `4` | `open` | — | Žiedavimo teritorija | — |
| `ziedavimo_vietove` | `string` | — | `4` | `open` | — | Žiedavimo vietovė: rajonas, savivaldybė arba kita | — |
| `p_ziedavimo_centro_salis` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedavimo centro šalis | — |
| `p_ziedavimo_centras` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedavimo centras | — |
| `kas_ziedavo` | `string` | — | `4` | `open` | — | Žieduotojo kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv
