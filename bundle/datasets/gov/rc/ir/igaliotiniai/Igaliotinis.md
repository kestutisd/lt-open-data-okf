---
type: Table
title: "Igaliotinis — Įgaliotinių duomenys"
description: "Spinta table datasets/gov/rc/ir/igaliotiniai/Igaliotinis (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/igaliotiniai/Igaliotinis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/igaliotiniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/igaliotiniai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Igaliotinis — Įgaliotinių duomenys

- **Model:** `datasets/gov/rc/ir/igaliotiniai/Igaliotinis`[^manifest]
- **Dataset:** [Įgaliojimų registro (ĮR) įgaliotinių duomenys](../igaliotiniai.md) (`datasets/gov/rc/ir/igaliotiniai`)
- **Manifest CSV:** [datasets/gov/rc/ir/igaliotiniai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/igaliotiniai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/igaliotiniai/Igaliotinis`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `tipas` | `string` | — | `3` | `open` | — | Įgalioto asmens tipas (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo) | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės, kurioje deklaruota įgalioto (fizinio asmens) gyvenamoji vieta arba registruota įgalioto (juridinio asmens) buveinė, kodas iš Adresų registro (kai gyvenamoji vieta arba buveinė nenurodyta - -1) | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Įgalioto asmens amžiaus grupė įgaliojimo sudarymo metu (0-24 - kai amžius nuo 0 iki 24 metų, 25-34 - kai amžius nuo 25 iki 34 metų, 35-44 - kai amžius nuo 35 iki 44 metų, 45-54 - kai amžius nuo 45 iki 54 metų, 55-64 - kai amžius nuo 55 iki 64 metų, 65-84 - kai amžius nuo 65 iki 84 metų, 85+ - kai amžius nuo 85 metų, Nenustatyta - kai amžius nenurodytas) | — |
| `asmenu_kiekis` | `string` | — | `3` | `open` | — | Įgaliotų asmenų kiekis (sugrupuota pagal tipą, savivaldybę ir amžiaus grupę) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/igaliotiniai.csv
