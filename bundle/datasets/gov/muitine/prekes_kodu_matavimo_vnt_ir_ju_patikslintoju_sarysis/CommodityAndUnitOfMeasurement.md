---
type: Table
title: "CommodityAndUnitOfMeasurement — Prekės kodų, matavimo vienetų ir jų patikslintojų kodų sąryšis"
description: "Spinta table datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis/CommodityAndUnitOfMeasurement (8 columns)."
tags: [gov, muitine, commodityandunitofmeasurement, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# CommodityAndUnitOfMeasurement — Prekės kodų, matavimo vienetų ir jų patikslintojų kodų sąryšis

- **Model:** `datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis/CommodityAndUnitOfMeasurement`[^manifest]
- **Dataset:** [datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis](../prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.md) (`datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `commodity, unit, unit_qualifier, country`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `commodity` | `ref` | [Commodity](../prekiu_kodai/Commodity.md) (`level=4 UUID`: `commodity._id`) | `4` | `open` | — | Prekė | — |
| `unit` | `ref` | [UnitOfMeasurement](../matavimo_vienetai/UnitOfMeasurement.md) (`level=4 UUID`: `unit._id`) | `4` | `open` | — | Matavimo vienetas | — |
| `unit_qualifier` | `ref` | [SupplementaryUnitQualifier](../matavimo_vienetu_patikslintojai/SupplementaryUnitQualifier.md) (`level=4 UUID`: `unit_qualifier._id`) | `4` | `open` | — | Patikslintojo kodas | — |
| `country` | `string` | — | `2` | `open` | — | Šalis | 2 simbolių šalies kodas |
| `import` | `boolean` | — | `4` | `open` | — | Importo požymis | — |
| `export` | `boolean` | — | `4` | `open` | — | Eksporto požymis | — |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžios | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaigos | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `country` | `update(type: "ref", ref: "?")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/prekes_kodu_matavimo_vnt_ir_ju_patikslintoju_sarysis.csv#L6)
