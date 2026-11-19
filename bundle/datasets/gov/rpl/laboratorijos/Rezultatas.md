---
type: Table
title: "Rezultatas — Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė)"
description: "Spinta table datasets/gov/rpl/laboratorijos/Rezultatas (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rpl/laboratorijos/Rezultatas"
tags: [gov, rpl, rezultatas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/laboratorijos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rpl/laboratorijos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2723/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rpl/laboratorijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rezultatas — Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė)

- **Model:** `datasets/gov/rpl/laboratorijos/Rezultatas`[^manifest]
- **Dataset:** [Sveikatos priežiūros įstaigų laboratorijos rezultatų duomenys (Rokiškio psichiatrijos ligoninė)](../laboratorijos.md) (`datasets/gov/rpl/laboratorijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rpl/laboratorijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/laboratorijos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rpl/laboratorijos/Rezultatas` (`deployed`)[^manifest]
- **Provider:** `rpl` — Rokiškio psichiatrijos ligoninė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tyr_grupe` | `"KRAUJAS"` | — | — | Kraujas | — |
| `tyr_grupe` | `"BIOCHEMIJA"` | — | — | Biochemija | — |
| `tyr_grupe` | `"ŠLAPIMAS"` | — | — | Šlapimas | — |
| `tyr_grupe` | `"TPHA"` | — | — | TPHA | — |
| `tyr_grupe` | `"KOPROLOGIJA"` | — | — | Koprologija | — |
| `tyr_grupe` | `"SEROLOGIJA"` | — | — | Serologija | — |
| `tyr_grupe` | `"HORMONAI"` | — | — | Hormonai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rpl/laboratorijos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rpl/laboratorijos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rpl/laboratorijos (https://data.gov.lt/datasets/2723/)
