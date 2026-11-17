---
type: Table
title: "PaukscioAptikimas — Paukščių ir šikšnosparnių aptikimų duomenys"
description: "Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Paukščių ir šikšnosparnių, žieduotų Lietuvoje, aptikimų duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioAptikimas"
tags: [gov, ktizm, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PaukscioAptikimas — Paukščių ir šikšnosparnių aptikimų duomenys

Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Paukščių ir šikšnosparnių, žieduotų Lietuvoje, aptikimų duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės. Duomenų atnaujinimas vykdomas kartą per metus.

- **Model:** `datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioAptikimas`[^manifest]
- **Dataset:** [Paukščių ir šikšnosparnių aptikimų, žiedavimų ir biometriniai duomenys](../pauksciai_ir_siksnosparniai.md) (`datasets/gov/ktizm/pauksciai_ir_siksnosparniai`)
- **Manifest CSV:** [datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioAptikimas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `aptikimo_data` | `date` | `D` | `4` | `open` | — | Aptikimo data | — |
| `aptikimo_teritorija` | `string` | — | `4` | `open` | — | Aptikimo teritorija | — |
| `aptikimo_vietove` | `string` | — | `4` | `open` | — | Aptikimo vietovė: rajonas, savivaldybė arba kita | — |
| `p_rusis_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio rūšies angliškas pavadinimas | — |
| `p_rusis_lot` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio rūšies lotyniškas pavadinimas | — |
| `p_amzius_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio amžiaus kategorija (anglų k.) | — |
| `p_amzius_lt` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio amžiaus kategorija (lietuvių k.) | — |
| `p_lytis_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio lytis | — |
| `p_ziedo_schema` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedo schema | — |
| `p_ziedo_nr` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedo numeris | — |
| `p_spalvzied_kodas` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio spalvinio žiedo kodas | — |
| `p_ziedavimo_salis` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedavimo centro šalis | — |
| `p_ziedavimo_centras` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio žiedavimo centras | — |
| `bukle_en` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio būklė aptikimo metu (anglų k.) | — |
| `bukle_lt` | `string` | — | `4` | `open` | — | Paukščio arba šikšnosparnio būklė aptikimo metu (lietuvių k.) | — |
| `aplinkybes_en` | `string` | — | `4` | `open` | — | Aptikimo aplinkybės (anglų k.) | — |
| `aplinkybes_lt` | `string` | — | `4` | `open` | — | Aptikimo aplinkybės (lietuvių k.) | — |
| `aplinkybes_spejamos` | `boolean` | — | `4` | `open` | — | Požymis, ar aptikimo aplinkybės yra spėjamos | — |
| `aptikimo_pranesejas` | `string` | — | `4` | `open` | — | Aptikimo pranešėjo kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv
