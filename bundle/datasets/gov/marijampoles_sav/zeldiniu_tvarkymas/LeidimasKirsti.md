---
type: Table
title: "LeidimasKirsti — Marijampolės savivaldybės išduoti leidimai kirsti, genėti ar pertvarkyti saugotinus želdinius"
description: "Pateikiama informacija apie Marijampolės savivaldybės išduotus leidimus kirsti, genėti ar pertvarkyti želdinius."
resource: "https://get.data.gov.lt/datasets/gov/marijampoles_sav/zeldiniu_tvarkymas/LeidimasKirsti"
tags: [gov, marijampoles_sav, leidimaskirsti, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/zeldiniu_tvarkymas.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/marijampoles_sav/zeldiniu_tvarkymas.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2657/"
    title: "data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/zeldiniu_tvarkymas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LeidimasKirsti — Marijampolės savivaldybės išduoti leidimai kirsti, genėti ar pertvarkyti saugotinus želdinius

Pateikiama informacija apie Marijampolės savivaldybės išduotus leidimus kirsti, genėti ar pertvarkyti želdinius. Informacija pateikiama nuo 2008 metų.[^manifest]

- **Model:** `datasets/gov/marijampoles_sav/zeldiniu_tvarkymas/LeidimasKirsti`[^manifest]
- **Dataset:** [Išduoti leidimai kirsti, genėti ar pertvarkyti saugotinus želdinius](../zeldiniu_tvarkymas.md) (`datasets/gov/marijampoles_sav/zeldiniu_tvarkymas`)[^manifest]
- **Manifest CSV:** [datasets/gov/marijampoles_sav/zeldiniu_tvarkymas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/zeldiniu_tvarkymas.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/marijampoles_sav/zeldiniu_tvarkymas/LeidimasKirsti` (`deployed`)[^manifest]
- **Provider:** `marijampoles_sav` — Marijampolės savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `prasymo_data` | `date` | `D` | `4` | `open` | — | Prašymo pateikimo data | Leidimo prašymo pateikimo data |
| `leidimo_id` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `leidimo_isdavimo_data` | `date` | `D` | `4` | `open` | — | Leidimo išdavimo data | — |
| `leidimas_galioja_iki` | `date` | `D` | `4` | `open` | — | Leidimas galioja iki | — |
| `seniunijos_pavadinimas` | `string` | — | `4` | `open` | — | Seniūnijos pavadinimas | — |
| `gatves_pavadinimas` | `string` | — | `4` | `open` | — | Gatvės pavadinimas | — |
| `adresas_tarp_namu` | `string` | — | `2` | `open` | — | Adresas tarp namų | — |
| `saugotinu_zeld_rusis` | `string` | — | `2` | `open` | — | Saugotinų želdinių rūšis | — |
| `kertami_medziai` | `string` | — | `2` | `open` | — | Kertami medziai | Kertami, genėjami, pertvarkomi želdiniai |
| `kompensacijos_dydis` | `number` | — | `3` | `open` | — | Kompensacijos dydis | Želdinių atkuriamosios vertės kompensacijos dydis |
| `valiuta` | `string` | — | `4` | `open` | — | Valiuta | — |
| `prasancio_asmens_kodas` | `string` | — | `4` | `open` | — | Prašančio asmens kodas | — |
| `ask_validus` | `string` | — | `4` | `open` | — | Asmens kodo validacija | — |
| `parasancio_jar_kodas` | `string` | — | `4` | `open` | — | Prašančios įstaigos juridinio asmens kodas | — |
| `jar_validus` | `boolean` | — | `4` | `open` | — | Juridinio asmens kodo validacija | — |
| `specialistas` | `string` | — | `4` | `open` | — | Specialistas | Darbuotojas išdavęs/suformavęs leidimą kirsti/genėti |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `saugotinu_zeld_rusis` | `update(property: "saugotinu_zeld_rusis", type: "text")` | `type` | `4` | `open` | — | — | — |
| `kertami_medziai` | `update(property: "kertami_medziai", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/marijampoles_sav/zeldiniu_tvarkymas.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/marijampoles_sav/zeldiniu_tvarkymas.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/marijampoles_sav/zeldiniu_tvarkymas (https://data.gov.lt/datasets/2657/)
