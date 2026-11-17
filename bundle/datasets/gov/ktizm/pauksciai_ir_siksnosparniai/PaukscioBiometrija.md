---
type: Table
title: "PaukscioBiometrija — Paukščių ir šikšnosparnių biometriniai duomenys (išmatuoti žieduojant)"
description: "Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Lietuvoje atliktų paukščių ir šikšnosparnių žiedavimų biometriniai duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioBiometrija"
tags: [gov, ktizm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaukscioBiometrija — Paukščių ir šikšnosparnių biometriniai duomenys (išmatuoti žieduojant)

Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Lietuvoje atliktų paukščių ir šikšnosparnių žiedavimų biometriniai duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės. Duomenų atnaujinimas vykdomas kartą per metus.

- **Model:** `datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioBiometrija`[^manifest]
- **Dataset:** [Paukščių ir šikšnosparnių aptikimų, žiedavimų ir biometriniai duomenys](../pauksciai_ir_siksnosparniai.md) (`datasets/gov/ktizm/pauksciai_ir_siksnosparniai`)
- **Manifest CSV:** [datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioBiometrija`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `matavimo_pav_en` | `string` | — | `4` | `open` | — | Matavimo pavadinimas (anglų k.) | — |
| `matavimo_pav_lt` | `string` | — | `4` | `open` | — | Matavimo pavadinimas (lietuvių k.) | — |
| `metodas` | `string` | — | `4` | `open` | — | Metodo kodas | — |
| `metodo_paaiskinimas_en` | `string` | — | `4` | `open` | — | Metodo paaiškinimas (anglų k.) | — |
| `matavimo_ivertis` | `number` | — | `4` | `open` | — | Matavimo skaitinis įvertis | — |
| `mato_vienetas` | `string` | — | `4` | `open` | — | Mato vienetas | — |
| `kategorinis_ivertis` | `string` | — | `4` | `open` | — | Kategorinio įverčio kodas | — |
| `kategorinio_ivercio_prasme` | `string` | — | `4` | `open` | — | Kategorinio įverčio prasmė | — |
| `p_rusis_lot` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio rūšies lotyniškas pavadinimas | — |
| `p_rusis_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio rūšies angliškas pavadinimas | — |
| `p_lytis_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio lytis | — |
| `p_amzius_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio amžiaus kategorija (anglų k.) | — |
| `p_amzius_lt` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio amžiaus kategorija (lietuvių k.) | — |
| `p_ziedo_schema` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedo schema | — |
| `p_ziedo_nr` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedo numeris | — |
| `matavimo_data` | `date` | `D` | `4` | `open` | — | Matavimo data | — |
| `kas_irase` | `string` | — | `4` | `open` | — | Asmens, įrašiusio duomenis į sistemą, kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv
