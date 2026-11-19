---
type: Table
title: "Suspicion — Įtarimas"
description: "Spinta table datasets/gov/finmin/kontroles_veiksmai/Suspicion (19 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai/Suspicion"
tags: [gov, finmin, suspicion, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L23"
    title: "atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv#L23"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2162/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/kontroles_veiksmai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Suspicion — Įtarimas

- **Model:** `datasets/gov/finmin/kontroles_veiksmai/Suspicion`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų kontrolės veiksmų duomenys](../kontroles_veiksmai.md) (`datasets/gov/finmin/kontroles_veiksmai`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kontroles_veiksmai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L23)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai/Suspicion` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `suspicion_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suspicion_id` | `string` | — | `4` | `open` | — | Įtarimo identifikatorius | — |
| `project_hash` | `ref` | [Revise](Revise.md) (`level=3`: `project_hash.project_hash_id`) | `3` | `open` | — | Projekto pseudonimas | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv#L23 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L23)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/kontroles_veiksmai (https://data.gov.lt/datasets/2162/)
