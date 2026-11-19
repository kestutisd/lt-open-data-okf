---
type: Table
title: "Sutartis — Pateiktos paraiškos bei pasirašytos finansuoti sutartys"
description: "Duomenys pateikiami iš Informacinių projektų administravimo sistemų (EEENORIS, SPIS, LŠBP, CPVAIS), skirtų kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2007–2017 m...."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_dr/Sutartis"
tags: [gov, cpva, sutartis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L33"
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L33"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2931/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys_dr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sutartis — Pateiktos paraiškos bei pasirašytos finansuoti sutartys

Duomenys pateikiami iš Informacinių projektų administravimo sistemų (EEENORIS, SPIS, LŠBP, CPVAIS), skirtų kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2007–2017 m. fondų programų projektų įgyvendinimu. Rinkinyje pateikiamos dvi lentelės, kuriose galima rasti tokią informaciją: pateiktas paraiškas ir pasirašytas finansuoti sutartis (viena eilutė atitinka atitinkamą paraišką, pasirašytos sutarties statusų pasikeitimų eigą). Projektai, kurie buvo vykdomi naudojantis šia sistema jau pasibaigę, todėl duomenys nebebus atnaujinami. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/cpva/paramu_duomenys_dr/Sutartis`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros administruojamos ES fondų ir tarptautinių programų...](../paramu_duomenys_dr.md) (`datasets/gov/cpva/paramu_duomenys_dr`)[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L33](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L33)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_dr/Sutartis` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | identifikacinis numeris | — |
| `istaigos_jar_kodas` | `string` | — | `4` | `open` | — | Įstaigos JAR kodas | — |
| `istaigos_reg_savivaldybe` | `string` | — | `4` | `open` | — | Įstaigos registracijos savivaldybė | — |
| `paraiskos_id` | `string` | — | `4` | `open` | — | Paraiškos identifikacinis numeris | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `sutarties_pavadinimas` | `string` | — | `2` | `open` | — | Sutarties pavadinimas | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `finansuojama_suma` | `number` | — | `4` | `open` | — | Sutarties finansuojama suma | — |
| `ismoketa_suma` | `number` | — | `4` | `open` | — | Išmokėta suma | — |
| `sutarties_isigaliojimo_data` | `date` | `D` | `4` | `open` | — | Sutarties įsigaliojimo data | — |
| `sutarties_pabaigos_data` | `date` | `D` | `4` | `open` | — | Sutarties pabaigos data | — |
| `projekto_veiklu_pradzia` | `date` | `D` | `4` | `open` | — | Projekto veiklų pradžios data | — |
| `projekto_veiklu_pabaiga` | `date` | `D` | `4` | `open` | — | Projekto veiklų pabaigos data | — |
| `turi_partneriu` | `boolean` | — | `4` | `open` | — | Ar turi partnerių? | — |
| `sutarties_busena` | `string` | — | `4` | `open` | — | Sutarties būsena | — |
| `priemones_tipo_id` | `string` | — | `4` | `open` | — | Finansavimo priemonės identifikacinis numeris | — |
| `priemones_tipo_kodas` | `string` | — | `4` | `open` | — | Finansavimo priemonės kodas | — |
| `priemones_tipo_pavadinimas` | `string` | — | `4` | `open` | — | Finansavimo priemonės pavadinimas | — |
| `atsakinga_institucija` | `string` | — | `4` | `open` | — | Atsakinga instituciją už finansavimo priemonę | — |
| `apskritis` | `string` | — | `4` | `open` | — | Apskritis kam skirta finansavimo priemonės parama | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sutarties_busena` | `"Baigtas"` | — | — | Baigtas | — |
| `sutarties_busena` | `"Nutraukta sutartis"` | — | — | Nutraukta sutartis | — |
| `sutarties_busena` | `"Atsisakė pasirašyti"` | — | — | Atsisakė pasirašyti | — |
| `sutarties_busena` | `"Ruošiama sutartis"` | — | — | Ruošiama sutartis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L33 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L33)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys_dr (https://data.gov.lt/datasets/2931/)
