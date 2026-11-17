---
type: Table
title: "Sprendimas — Mokestinių patikrinimų metu juridiniams asmenims priskaičiuotos sumos"
description: "Spinta table datasets/gov/vmi/sprendimai/Sprendimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/sprendimai/Sprendimas"
tags: [gov, vmi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/mokestiniai_patikrinimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sprendimas — Mokestinių patikrinimų metu juridiniams asmenims priskaičiuotos sumos

- **Model:** `datasets/gov/vmi/sprendimai/Sprendimas`[^manifest]
- **Dataset:** [Mokestinių patikrinimų metu juridiniams asmenims priskaičiuotos sumos](../sprendimai.md) (`datasets/gov/vmi/sprendimai`)
- **Manifest CSV:** [datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/sprendimai/Sprendimas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `evrk` | `ref` | [/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) | `4` | `open` | — | Ekonominės veiklos rūšies kodas | — |
| `metai` | `integer` | — | `4` | `open` | — | Patikrinimo metai | — |
| `mm_skaicius` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |
| `suma_akc` | `number` | — | `4` | `open` | — | Akcizo suma | Sprendimo dėl akcizo mokesčio suma,įskaitant delspinigius ir baudas |
| `suma_pln` | `number` | — | `4` | `open` | — | Pelno mokesčio suma | Sprendimo dėl pelno mokesčio suma,įskaitant delspinigius ir baudas |
| `suma_pvm` | `number` | — | `4` | `open` | — | Pridėtinės vertės mokesčio suma | Sprendimo dėl pridėtinės vertės mokesčio suma,įskaitant delspinigius ir baudas |
| `suma_gpm` | `number` | — | `4` | `open` | — | Gyventojų pajamų mokesčio suma | Sprendimo dėl gyventojų pajamų mokesčio suma,įskaitant delspinigius ir baudas |
| `suma_kiti` | `number` | — | `4` | `open` | — | Kitų mokesčių suma | Sprendimo dėl kitų mokesčių suma,įskaitant delspinigius ir baudas |
| `suma_viso` | `number` | — | `4` | `open` | — | Sprendimo suma | Sprendimo suma iš viso,įskaitant delspinigius ir baudas |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `suma_akc` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_pln` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_pvm` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_gpm` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_kiti` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `suma_viso` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/mokestiniai_patikrinimai.csv
