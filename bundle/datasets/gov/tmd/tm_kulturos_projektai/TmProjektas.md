---
type: Table
title: "TmProjektas — Įgyvendintų tautinių mažumų kultūros projektų duomenys"
description: "Lentelėje - įgyvendintų tautinių mažumų kultūros projektų duomenys iš Tautinių mažumų departamento prie Lietuvos Respublikos Vyriausybės Elektroninės paraiškų ir ataskaitų valdymo sistemos (EPAVS)."
resource: "https://get.data.gov.lt/datasets/gov/tmd/tm_kulturos_projektai/TmProjektas"
tags: [gov, tmd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/tmd/tm_kulturos_projektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tmd/tm_kulturos_projektai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# TmProjektas — Įgyvendintų tautinių mažumų kultūros projektų duomenys

Lentelėje - įgyvendintų tautinių mažumų kultūros projektų duomenys iš Tautinių mažumų departamento prie Lietuvos Respublikos Vyriausybės Elektroninės paraiškų ir ataskaitų valdymo sistemos (EPAVS). Pateikiami duomenys nuo jų rinkimo sistemoje pradžios (2020 m.) atnaujinant kas metus.

- **Model:** `datasets/gov/tmd/tm_kulturos_projektai/TmProjektas`[^manifest]
- **Dataset:** [Įgyvendintų tautinių mažumų kultūros projektų duomenys](../tm_kulturos_projektai.md) (`datasets/gov/tmd/tm_kulturos_projektai`)
- **Manifest CSV:** [datasets/gov/tmd/tm_kulturos_projektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tmd/tm_kulturos_projektai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tmd/tm_kulturos_projektai/TmProjektas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `projekto_pateikimo_data` | `date` | `D` | `4` | `open` | — | Projekto pateikimo data | — |
| `projekto_reg_nr` | `string` | — | `4` | `open` | — | Projekto registracijos numeris | — |
| `konkurso_pavadinimas` | `string` | — | `4` | `open` | — | Konkurso pavadinimas | — |
| `sutarties_data` | `date` | `D` | `4` | `open` | — | Sutarties data | — |
| `sutarties_numeris` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `projekto_pavadinimas` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `projekto_planuojamas_terminas` | `date` | `D` | `4` | `open` | — | Planuojamas (preliminarus) projekto įgyvendinimo terminas | — |
| `ar_tesiamas_ateity` | `boolean` | — | `4` | `open` | — | Požymis, ar projektas bus tęsiamas ateityje ("true" - taip, "false" - ne) | — |
| `projekto_pareiskejo_instkodas` | `string` | — | `4` | `open` | — | Projekto pareiškėjo juridinio asmens kodas | — |
| `projekto_pareiskejo_instpav` | `string` | — | `4` | `open` | — | Projekto pareiškėjo pavadinimas | — |
| `viso_suplanuotos_islaidos` | `number` | — | `4` | `open` | — | Planuojamos projekto bendros išlaidos (EUR) | — |
| `suplanuotos_dep_islaidos` | `number` | — | `4` | `open` | — | Planuojamos projekto išlaidos (EUR), kurias finansuotų Tautinių mažumų departamentas | — |
| `suplanuotos_rem_islaidos` | `number` | — | `4` | `open` | — | Planuojamos projekto išlaidos (EUR), kurias finansuotų projekto remėjai | — |
| `ataskaitos_dep_islaidos` | `number` | — | `4` | `open` | — | Tautinių mažumų departamento skirtas finansavimas (EUR) iš projekto įgyvendinimo ataskaitos | — |
| `ataskaitos_busena` | `string` | — | `4` | `open` | — | Projekto įgyvendinimo ataskaitos būsena | — |
| `ataskaitos_data` | `date` | `D` | `4` | `open` | — | Projekto įgyvendinimo ataskaitos data | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `viso_suplanuotos_islaidos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `suplanuotos_dep_islaidos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `suplanuotos_rem_islaidos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `ataskaitos_dep_islaidos` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/tmd/tm_kulturos_projektai.csv
