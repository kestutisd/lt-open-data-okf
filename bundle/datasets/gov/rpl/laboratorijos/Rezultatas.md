---
type: Table
title: "Rezultatas — Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė)"
description: "Spinta table datasets/gov/rpl/laboratorijos/Rezultatas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rpl/laboratorijos/Rezultatas"
tags: [gov, rpl, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rpl/laboratorijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/laboratorijos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Rezultatas — Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė)

- **Model:** `datasets/gov/rpl/laboratorijos/Rezultatas`[^manifest]
- **Dataset:** [Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė)](../laboratorijos.md) (`datasets/gov/rpl/laboratorijos`)
- **Manifest CSV:** [datasets/gov/rpl/laboratorijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/laboratorijos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rpl/laboratorijos/Rezultatas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `tyr_id` | `string` | — | `4` | `open` | — | Tyrimo identifikatorius | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento identifikatorius | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `tyr_data` | `date` | `D` | `4` | `open` | — | Tyrimo užsakymo ir atlikimo data | — |
| `paemimo_laikas` | `string` | — | `4` | `open` | — | Tyrimo mėginio paėmimo laikas | — |
| `atnesimo_laikas` | `string` | — | `4` | `open` | — | Tyrimo mėginio atnešimo laikas | — |
| `atlikimo_laikas` | `string` | — | `4` | `open` | — | Tyrimo atlikimo laikas | — |
| `tyr_grupe` | `string` | — | `4` | `open` | — | Tyrimo grupė | — |
| `tyr_analite_id` | `string` | — | `4` | `open` | — | Tyrimo numeris | — |
| `tyr_analite` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas | — |
| `norma_nuo` | `string` | — | `4` | `open` | — | Mažiausia norminio dydžio riba | — |
| `norma_iki` | `string` | — | `4` | `open` | — | Didžiausia norminio dydžio riba | — |
| `rez_tx` | `string` | — | `4` | `open` | — | Rezultato tekstinė reikšmė | — |
| `rezult` | `number` | — | `4` | `open` | — | Rezultato skaitinė reikšmė | — |
| `mat_vnt` | `string` | — | `4` | `open` | — | Matavimo vienetai | — |
| `skyr_pav` | `string` | — | `4` | `open` | — | Gydymo įstaigos padalinio pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tyr_grupe` | `"KRAUJAS"` | — | — | Kraujas | — |
| `tyr_grupe` | `"BIOCHEMIJA"` | — | — | Biochemija | — |
| `tyr_grupe` | `"ŠLAPIMAS"` | — | — | Šlapimas | — |
| `tyr_grupe` | `"TPHA"` | — | — | TPHA | — |
| `tyr_grupe` | `"KOPROLOGIJA"` | — | — | Koprologija | — |
| `tyr_grupe` | `"SEROLOGIJA"` | — | — | Serologija | — |
| `tyr_grupe` | `"HORMONAI"` | — | — | Hormonai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rpl/laboratorijos.csv
