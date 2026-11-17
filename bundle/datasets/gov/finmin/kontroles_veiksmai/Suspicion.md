---
type: Table
title: "Suspicion — Įtarimas"
description: "Spinta table datasets/gov/finmin/kontroles_veiksmai/Suspicion (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai/Suspicion"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L23"
    last_modified: "2026-11-11T14:39:20Z"
---

# Suspicion — Įtarimas

- **Model:** `datasets/gov/finmin/kontroles_veiksmai/Suspicion`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų kontrolės veiksmų duomenys](../kontroles_veiksmai.md) (`datasets/gov/finmin/kontroles_veiksmai`)
- **Manifest CSV:** [datasets/gov/finmin/kontroles_veiksmai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L23)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai/Suspicion`
- **Primary Key (`ref`):** `suspicion_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suspicion_id` | `string` | — | `4` | `open` | — | Įtarimo identifikatorius | — |
| `project_hash` | `ref` | [Revise[project_hash_id]](Revise.md) | `3` | `open` | — | Projekto pseudonimas | — |
| `number` | `string` | — | `4` | `open` | — | Įtarimo apie pažeidimą numeris | — |
| `created` | `date` | `D` | `4` | `open` | — | Įtarimo apie pažeidimą data | — |
| `violation_kind` | `string` | — | `3` | `open` | — | Pažeidimo pobūdis | — |
| `is_relate_purchase_contract` | `string` | — | `2` | `open` | — | Ar susijęs su pirkimo sutartimi? | — |
| `violated_eu_regul` | `string` | — | `4` | `open` | — | Pažeistos ES teisės aktų nuostatos | — |
| `violation_solution` | `string` | — | `3` | `open` | — | Sprendimas dėl pažeidimo | — |
| `violation_solved` | `date` | `D` | `4` | `open` | — | Sprendimo dėl įtariamo pažeidimo data | — |
| `ineligible_expense` | `number` | — | `2` | `open` | — | Nustatytos netinkamos finansuoti projekto išlaidos | — |
| `ineligible_expense_percent` | `number` | `%` | `4` | `open` | — | Nustatyta netinkamų finansuoti projekto išlaidų dalis | — |
| `repayment_amount` | `number` | — | `2` | `open` | — | Grąžintinos lėšos | — |
| `correct_by` | `date` | `D` | `4` | `open` | — | Pažeidimo ištaisymo terminas | — |
| `repaid` | `date` | `D` | `4` | `open` | — | Lėšų grąžinimo terminas | — |
| `state` | `string` | — | `3` | `open` | — | Įtarimo apie pažeidimą / pažeidimo būsena | — |
| `state_updated` | `datetime` | `L` | `4` | `open` | — | Įtarimo apie pažeidimą / pažeidimo būsenos data | — |
| `solution` | `string` | — | `2` | `open` | — | Priimtas įtarimo sprendimas | Sprendimai atskirti kabliataškiais |
| `type` | `string` | — | `2` | `open` | — | Įtariamų pažeidimų tipai | Tipai atskirti kabliataškiais |
| `subtype` | `string` | — | `2` | `open` | — | Įtariamų pažeidimų potipiai | Potipiai atskirti kabliataškiais |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ineligible_expense` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `repayment_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `solution` | `"update(property: ""solution[]"", type: ""array"", source: ""Solution"")"` | `property` | `4` | — | — | — | — |
| `type` | `"update(property: ""type[]"", type: ""array"", source: ""Type"")"` | `property` | `4` | — | — | — | — |
| `subtype` | `"update(property: ""subtype[]"", type: ""array"", source: ""Subtype"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv
