---
type: Table
title: "PatvirtintaAtlieka — Registruotos tvarkomos atliekos"
description: "Atliekų tvarkytojų patvirtintos registruotos tvarkomos atliekos"
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/PatvirtintaAtlieka"
tags: [gov, aaa, patvirtintaatlieka, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L43"
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L43"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3840/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PatvirtintaAtlieka — Registruotos tvarkomos atliekos

Atliekų tvarkytojų patvirtintos registruotos tvarkomos atliekos[^manifest]

- **Model:** `datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/PatvirtintaAtlieka`[^manifest]
- **Dataset:** [Atliekų tvarkytojų valstybės registro duomenys](../atlieku_tvarkytoju_valstybes_registras.md) (`datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L43](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L43)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/PatvirtintaAtlieka` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `patvirtintu_atlieku_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patvirtintu_atlieku_id` | `string` | — | `4` | `open` | — | Tvarkymo vietoje patvirtintų atliekų identifikatorius | — |
| `nuo_kada_atliekos_patvirtintos` | `date` | `D` | `4` | `open` | — | Data, nurodanti nuo kada tvarkomos atliekos | — |
| `iki_kada_atliekos_patvirtintos` | `date` | `D` | `4` | `open` | — | Data, nurodanti iki kada tvarkomos atliekos | — |
| `ar_tvarkomos_savo_atliekos` | `boolean` | — | `4` | `open` | — | Požymis, nurodantis, kad tvarkomos savos atliekos | — |
| `atlieku_tvarkymo_veiklos_kategorija` | `string` | — | `4` | `open` | — | Atliekų tvarkymo veiklos kategorija | — |
| `atlieku_tvarkymo_veiklos_kodas` | `string` | — | `4` | `open` | — | Atliekų tvarkymo veiklos kodas | — |
| `atlieku_tvarkymo_veikla` | `string` | — | `4` | `open` | — | Atliekų tvarkymo veikla | — |
| `atliekos_kodas` | `string` | — | `4` | `open` | — | Atliekos kodas | — |
| `atliekos_pavadinimas` | `string` | — | `4` | `open` | — | Atliekos pavadinimas | — |
| `ar_atlieka_pavojinga` | `boolean` | — | `4` | `open` | — | Požymis, ar atlieka pavojinga | — |
| `technologinio_srauto_identifikatorius` | `string` | — | `4` | `open` | — | Pavojingųjų atliekų technologinio srauto identifikatorius | — |
| `technologinio_srauto_pavadinimas` | `string` | — | `4` | `open` | — | Pavojingųjų atliekų technologinio srauto pavadinimas | — |
| `tvarkytojo_kodas_atvr_sistemoje` | `string` | — | `4` | `open` | — | Tvarkytojo kodas ATVR sistemoje | — |
| `tvarkytojo_juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo juridinio asmens kodas | — |
| `tvarkytojo_pavadinimas` | `string` | — | `4` | `open` | — | Tvarkytojo pavadinimas | — |
| `tvarkytojo_isregistravimo_data` | `date` | `D` | `4` | `open` | — | Tvarkytojo išregistravimo data | — |
| `tvarkytojo_adresas` | `string` | — | `4` | `open` | — | Tvarkytojo adresas | — |
| `tvarkymo_vietos_numeris_atvr_sistemoje` | `string` | — | `4` | `open` | — | Tvarkymo vietos numeris ATVR | — |
| `tvarkymo_vietos_pavadinimas` | `string` | — | `4` | `open` | — | Tvarkymo vietos pavadinimas | — |
| `tvarkymo_vietos_isregistravimo_data` | `date` | `D` | `4` | `open` | — | Tvarkymo vietos išregistravimo data | — |
| `tvarkymo_vietos_busena` | `string` | — | `4` | `open` | — | Tvarkymo vietos būsena | — |
| `tvarkymo_vietos_adresas` | `string` | — | `4` | `open` | — | Tvarkymo vietos adresas, sugeneruotas VDA pagal GPAIS duomenis | — |
| `tvarkymo_vietos_koordinates_lks` | `string` | — | `4` | `open` | — | Tvarkymo vietos koordinatės lks sistemoje | — |
| `tvarkymo_vietos_tikslumas_balais` | `number` | — | `4` | `open` | — | Tvarkymo vietos tikslumas balais | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tvarkymo_vietos_busena` | `"Patvirtinta"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Išregistruota"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Tikslinama"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Išregistruojama"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L43 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L43)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras (https://data.gov.lt/datasets/3840/)
