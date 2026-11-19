---
type: Table
title: "Audit — Projekto audito pastebėjimai"
description: "Spinta table datasets/gov/finmin/kontroles_veiksmai/Audit (18 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai/Audit"
tags: [gov, finmin, audit, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L49"
    title: "atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv#L49"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2162/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/kontroles_veiksmai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Audit — Projekto audito pastebėjimai

- **Model:** `datasets/gov/finmin/kontroles_veiksmai/Audit`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų kontrolės veiksmų duomenys](../kontroles_veiksmai.md) (`datasets/gov/finmin/kontroles_veiksmai`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kontroles_veiksmai.csv#L49](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L49)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai/Audit` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `audit_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_id` | `string` | — | `4` | `open` | — | Audito pastebėjimo identifikatorius | — |
| `project_hash` | `ref` | [Revise](Revise.md) (`level=3`: `project_hash.project_hash_id`) | `3` | `open` | — | Projekto pseudonimas | — |
| `number` | `string` | — | `4` | `open` | — | Audito pastebėjimo numeris | — |
| `sfmis_number` | `string` | — | `4` | `open` | — | Audito pastebėjimo SFMIS numeris | — |
| `state` | `string` | — | `3` | `open` | — | Audito pastebėjimo būsena | — |
| `state_updated` | `date` | `D` | `4` | `open` | — | Audito pastebėjimo būsenos data | — |
| `audit_type` | `string` | — | `3` | `open` | — | Audito ar patikrinimo ataskaitos tipas | — |
| `ref_period` | `string` | — | `2` | `open` | — | Ataskaitinis laikotarpis | — |
| `importance` | `string` | — | `3` | `open` | — | Audito pastebėjimo svarba | — |
| `sign` | `string` | — | `3` | `open` | — | Audito pastebėjimo požymis | — |
| `fin_impact` | `string` | — | `2` | `open` | — | Ar yra finansinis poveikis | — |
| `submit_inst` | `string` | — | `3` | `open` | — | Pastebėjimą pateikusi institucija | — |
| `receive_inst` | `string` | — | `2` | `open` | — | Pastebėjimą gavusi institucija | — |
| `max_amount_ineligible` | `number` | — | `2` | `open` | — | Preliminari pastebėjime nurodyta klaida arba institucijos įvertinta maksimali galimai netinkamų finansuoti išlaidų suma | — |
| `is_rec` | `string` | — | `2` | `open` | — | Ar yra rekomendacija | — |
| `rec_impl_term` | `date` | `D` | `4` | `open` | — | Rekomendacijos įgyvendinimo terminas | — |
| `inst_acted` | `date` | `D` | `4` | `open` | — | Institucijos atliktų veiksmų data | — |
| `rating_received` | `date` | `D` | `4` | `open` | — | Įvertinimo gavimo data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `max_amount_ineligible` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv#L49 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L49)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/kontroles_veiksmai (https://data.gov.lt/datasets/2162/)
