---
type: Table
title: "Igaliotojas — Įgaliotojų duomenys"
description: "Spinta table datasets/gov/rc/ir/igaliotojai/Igaliotojas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ir/igaliotojai/Igaliotojas"
tags: [gov, rc, igaliotojas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/igaliotojai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/ir/igaliotojai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2164/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/ir/igaliotojai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Igaliotojas — Įgaliotojų duomenys

- **Model:** `datasets/gov/rc/ir/igaliotojai/Igaliotojas`[^manifest]
- **Dataset:** [Įgaliojimų registro (ĮR) įgaliotojų duomenys](../igaliotojai.md) (`datasets/gov/rc/ir/igaliotojai`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ir/igaliotojai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/igaliotojai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ir/igaliotojai/Igaliotojas` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `tipas` | `string` | — | `3` | `open` | — | Įgaliojančio asmens tipas (Fizinis asmuo - kai fizinis asmuo; Juridinis asmuo pats iš savęs (lot. Per se); LR juridinis asmuo; Užsienio juridinis asmuo - kai juridinis asmuo) | — |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės, kurioje deklaruota įgaliojančio (fizinio asmens) gyvenamoji vieta arba registruota įgaliojančio (juridinio asmens) buveinė, kodas iš Adresų registro (kai gyvenamoji vieta arba buveinė nenurodyta - -1) | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Įgaliojančio asmens amžiaus grupė įgaliojimo sudarymo metu (0-24 - kai amžius nuo 0 iki 24 metų, 25-34 - kai amžius nuo 25 iki 34 metų, 35-44 - kai amžius nuo 35 iki 44 metų, 45-54 - kai amžius nuo 45 iki 54 metų, 55-64 - kai amžius nuo 55 iki 64 metų, 65-84 - kai amžius nuo 65 iki 84 metų, 85+ - kai amžius nuo 85 metų, Nenustatyta - kai amžius nenurodytas). | — |
| `asmenu_kiekis` | `integer` | — | `3` | `open` | — | Įgaliojančių asmenų kiekis (sugrupuota pagal tipą, savivaldybę ir amžiaus grupę) | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ir/igaliotojai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ir/igaliotojai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/ir/igaliotojai (https://data.gov.lt/datasets/2164/)
