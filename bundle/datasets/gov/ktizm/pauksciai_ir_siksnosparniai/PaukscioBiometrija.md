---
type: Table
title: "PaukscioBiometrija — Paukščių ir šikšnosparnių biometriniai duomenys (išmatuoti žieduojant)"
description: "Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Lietuvoje atliktų paukščių ir šikšnosparnių žiedavimų biometriniai duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės."
resource: "https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioBiometrija"
tags: [gov, ktizm, pauksciobiometrija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44"
    title: "atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2714/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ktizm/pauksciai_ir_siksnosparniai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PaukscioBiometrija — Paukščių ir šikšnosparnių biometriniai duomenys (išmatuoti žieduojant)

Lentelėje pateikti Kauno Tado Ivanausko zoologijos muziejaus Lietuvoje atliktų paukščių ir šikšnosparnių žiedavimų biometriniai duomenys iš Paukščių žiedavimo ir aptikimo duomenų bazės. Duomenų atnaujinimas vykdomas kartą per metus.[^manifest]

- **Model:** `datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioBiometrija`[^manifest]
- **Dataset:** [Paukščių ir šikšnosparnių aptikimų, žiedavimų ir biometriniai duomenys](../pauksciai_ir_siksnosparniai.md) (`datasets/gov/ktizm/pauksciai_ir_siksnosparniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ktizm/pauksciai_ir_siksnosparniai/PaukscioBiometrija` (`deployed`)[^manifest]
- **Provider:** `ktizm` — Kauno Tado Ivanausko zoologijos muziejus *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ktizm/pauksciai_ir_siksnosparniai.csv#L44)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ktizm/pauksciai_ir_siksnosparniai (https://data.gov.lt/datasets/2714/)
