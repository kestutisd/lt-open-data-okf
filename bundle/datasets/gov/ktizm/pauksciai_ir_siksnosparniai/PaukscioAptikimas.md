---
type: Table
title: "PaukscioAptikimas — Paukščių ir šikšnosparnių aptikimų duomenys"
description: "Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Paukščių ir šikšnosparnių, žieduotų Lietuvoje, aptikimų duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioAptikimas"
tags: [gov, ktizm, paukscioaptikimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2714/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ktizm/pauksciai_ir_siksnosparniai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PaukscioAptikimas — Paukščių ir šikšnosparnių aptikimų duomenys

Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Paukščių ir šikšnosparnių, žieduotų Lietuvoje, aptikimų duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės. Duomenų atnaujinimas vykdomas kartą per metus.[^manifest]

- **Model:** `datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioAptikimas`[^manifest]
- **Dataset:** [Paukščių ir šikšnosparnių aptikimų, žiedavimų ir biometriniai duomenys](../pauksciai_ir_siksnosparniai.md) (`datasets/gov/ktizm/pauksciai_ir_siksnosparniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioAptikimas` (`deployed`)[^manifest]
- **Provider:** `ktizm` — Kauno Tado Ivanausko zoologijos muziejus *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ktizm/pauksciai_ir_siksnosparniai (https://data.gov.lt/datasets/2714/)
