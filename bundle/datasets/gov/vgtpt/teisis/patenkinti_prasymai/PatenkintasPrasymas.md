---
type: Table
title: "PatenkintasPrasymas — Prašymų suteikti antrinę teisinę pagalbą patenkinimo duomenys"
description: "Spinta table datasets/gov/vgtpt/teisis/patenkinti_prasymai/PatenkintasPrasymas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/patenkinti_prasymai/PatenkintasPrasymas"
tags: [gov, vgtpt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# PatenkintasPrasymas — Prašymų suteikti antrinę teisinę pagalbą patenkinimo duomenys

- **Model:** `datasets/gov/vgtpt/teisis/patenkinti_prasymai/PatenkintasPrasymas`[^manifest]
- **Dataset:** [Prašymų suteikti antrinę teisinę pagalbą patenkinimo duomenys](../patenkinti_prasymai.md) (`datasets/gov/vgtpt/teisis/patenkinti_prasymai`)
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/patenkinti_prasymai/PatenkintasPrasymas`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `gauta_metai` | `integer` | — | `2` | `open` | — | Metai, kada gautas prašymas suteikti antrinę teisinę pagalbą | — |
| `gauta_ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis, kada gautas prašymas suteikti antrinę teisinę pagalbą | — |
| `priimta_metai` | `integer` | — | `4` | `open` | — | Metai, kada priimtas sprendimas suteikti antrinę teisinę pagalbą | — |
| `priimta_ketvirtis` | `integer` | — | `2` | `open` | — | Ketvirtis, kada priimtas sprendimas suteikti antrinę teisinę pagalbą | — |
| `teritorijos_kodas` | `ref` | [/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija](../klasifikatoriai/Teritorija.md) | `4` | — | — | Antrinę teisinę pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | Iš TEISIS teritorijos klasifikatoriaus |
| `gauti_prasymai` | `integer` | `U` | `4` | `open` | — | Teritoriniame padalinyje gautų prašymų suteikti antrinę teisinę pagalbą skaičius | — |
| `patenkinti_prasymai` | `integer` | `U` | `4` | `open` | — | Teritoriniame padalinyje patenkintų prašymų suteikti antrinę teisinę pagalbą skaičius | — |
| `patenkinti_prasymai_dalis` | `integer` | `%` | `4` | `open` | — | Patenkintų prašymų suteikti antrinę teisinę pagalbą skaičius procentais | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gauta_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |
| `priimta_metai` | `update(type: "date", ref: "Q")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/patenkinti_prasymai.csv
