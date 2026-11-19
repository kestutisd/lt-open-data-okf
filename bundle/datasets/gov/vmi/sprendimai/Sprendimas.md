---
type: Table
title: "Sprendimas — Mokestinių patikrinimų metu juridiniams asmenims priskaičiuotos sumos"
description: "Spinta table datasets/gov/vmi/sprendimai/Sprendimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vmi/sprendimai/Sprendimas"
tags: [gov, vmi, sprendimas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/444/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmi/sprendimai"
    author: "team:vda"
    last_modified: "2026-03-09T00:00:00Z"
---

# Sprendimas — Mokestinių patikrinimų metu juridiniams asmenims priskaičiuotos sumos

- **Model:** `datasets/gov/vmi/sprendimai/Sprendimas`[^manifest]
- **Dataset:** [Mokestinių patikrinimų metu juridiniams asmenims priskaičiuotos sumos](../sprendimai.md) (`datasets/gov/vmi/sprendimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/sprendimai/Sprendimas` (`deployed`)[^manifest]
- **Provider:** `vmi` — Valstybinė mokesčių inspekcija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-03-09`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `evrk` | `ref` | [EkonominesVeiklosRusis](../../lsd/cl/evrk/EkonominesVeiklosRusis.md) (`level=4 UUID`: `evrk._id`) | `4` | `open` | — | Ekonominės veiklos rūšies kodas | — |
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

# Related References

- [EVRK 2 / NACE Rev. 2 & 2025-01-01 EVRK 2.1 Reference](../../../../references/evrk-nace-sekcijos.md) — 21 NACE sections, 88 divisions, and the 2025-01-01 section letter shift & Division 45 split.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/mokestiniai_patikrinimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmi/sprendimai (https://data.gov.lt/datasets/444/)
