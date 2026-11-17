---
type: Table
title: "CommodityAndUnitOfMeasurement — Prekės kodų, matavimo vienetų ir jų patikslintojų kodų sąryšis"
description: "Spinta table datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis/CommodityAndUnitOfMeasurement (8 columns)."
tags: [gov, muitine, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# CommodityAndUnitOfMeasurement — Prekės kodų, matavimo vienetų ir jų patikslintojų kodų sąryšis

- **Model:** `datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis/CommodityAndUnitOfMeasurement`[^manifest]
- **Dataset:** [datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis](../prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.md) (`datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis`)
- **Manifest CSV:** [datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `commodity, unit, unit_qualifier, country`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `commodity` | `ref` | [/datasets/gov/muitine/prekiu_kodai/Commodity](../prekiu_kodai/Commodity.md) | `4` | `open` | — | Prekė | — |
| `unit` | `ref` | [/datasets/gov/muitine/matavimo_vienetai/UnitOfMeasurement](../matavimo_vienetai/UnitOfMeasurement.md) | `4` | `open` | — | Matavimo vienetas | — |
| `unit_qualifier` | `ref` | [/datasets/gov/muitine/matavimo_vienetu_patikslintojai/SupplementaryUnitQualifier](../matavimo_vienetu_patikslintojai/SupplementaryUnitQualifier.md) | `4` | `open` | — | Patikslintojo kodas | — |
| `country` | `string` | — | `2` | `open` | — | Šalis | 2 simbolių šalies kodas |
| `import` | `boolean` | — | `4` | `open` | — | Importo požymis | — |
| `export` | `boolean` | — | `4` | `open` | — | Eksporto požymis | — |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžios | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaigos | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `country` | `update(type: "ref", ref: "?")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv
