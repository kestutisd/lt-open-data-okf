---
type: Table
title: "TmProjektas — Įgyvendintų tautinių mažumų kultūros projektų duomenys"
description: "Lentelėje - įgyvendintų tautinių mažumų kultūros projektų duomenys iš Tautinių mažumų departamento prie Lietuvos Respublikos Vyriausybės Elektroninės paraiškų ir ataskaitų valdymo sistemos (EPAVS)."
resource: "https://get.data.gov.lt/datasets/gov/tmd/tm_kulturos_projektai/TmProjektas"
tags: [gov, tmd, tmprojektas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tmd/tm_kulturos_projektai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/tmd/tm_kulturos_projektai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2866/"
    title: "data.gov.lt DCAT-AP — datasets/gov/tmd/tm_kulturos_projektai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# TmProjektas — Įgyvendintų tautinių mažumų kultūros projektų duomenys

Lentelėje - įgyvendintų tautinių mažumų kultūros projektų duomenys iš Tautinių mažumų departamento prie Lietuvos Respublikos Vyriausybės Elektroninės paraiškų ir ataskaitų valdymo sistemos (EPAVS). Pateikiami duomenys nuo jų rinkimo sistemoje pradžios (2020 m.) atnaujinant kas metus. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/tmd/tm_kulturos_projektai/TmProjektas`[^manifest]
- **Dataset:** [Įgyvendintų tautinių mažumų kultūros projektų duomenys](../tm_kulturos_projektai.md) (`datasets/gov/tmd/tm_kulturos_projektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/tmd/tm_kulturos_projektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tmd/tm_kulturos_projektai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tmd/tm_kulturos_projektai/TmProjektas` (`deployed`)[^manifest]
- **Provider:** `tmd` — Tautinių mažumų departamentas prie Lietuvos Respublikos Vyriausybės *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/tmd/tm_kulturos_projektai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tmd/tm_kulturos_projektai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/tmd/tm_kulturos_projektai (https://data.gov.lt/datasets/2866/)
