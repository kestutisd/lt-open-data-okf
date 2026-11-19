---
type: Table
title: "PazeidimoTyrimas — Pažeidimų tyrimų informacija įtariant pažeidimą"
description: "Duomenys pateikiami iš Informacinių projektų administravimo sistemų (EEENORIS, SPIS, LŠBP, CPVAIS), skirtų kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2007–2017 m...."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_dr/PazeidimoTyrimas"
tags: [gov, cpva, pazeidimotyrimas, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L11"
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L11"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2931/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys_dr"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PazeidimoTyrimas — Pažeidimų tyrimų informacija įtariant pažeidimą

Duomenys pateikiami iš Informacinių projektų administravimo sistemų (EEENORIS, SPIS, LŠBP, CPVAIS), skirtų kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2007–2017 m. fondų programų projektų įgyvendinimu. Rinkinyje pateikiamos dvi lentelės, kuriose galima rasti tokią informaciją: pažeidimų tyrimų informaciją įtariant pažeidimą (viena eilutė atitinka vieną įtariamą pažeidimą ir statusą, nurodantį, ar pažeidimas nustatytas). Projektai, kurie buvo vykdomi naudojantis šia sistema jau pasibaigę, todėl duomenys nebebus atnaujinami. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/cpva/paramu_duomenys_dr/PazeidimoTyrimas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros administruojamos ES fondų ir tarptautinių programų...](../paramu_duomenys_dr.md) (`datasets/gov/cpva/paramu_duomenys_dr`)[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L11)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_dr/PazeidimoTyrimas` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pazeidimo_tyr_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pazeidimo_tyr_id` | `string` | — | `4` | `open` | — | Pažeidimo tyrimo identifikacinis numeris | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `priemones_tipo_pavadinimas` | `string` | — | `4` | `open` | — | Finansavimo priemonės pavadinimas | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `pazeidimo_tyr_pradzia` | `date` | `D` | `4` | `open` | — | Pažeidimo tyrimo data | — |
| `pazeidimo_tyr_busenos_data` | `date` | `D` | `4` | `open` | — | Pažeidimo būsenos data | — |
| `pazeidimo_tyr_busena` | `string` | — | `4` | `open` | — | Pažeidimo tyrimo stausas | — |
| `pazeidimo_tipas` | `string` | — | `4` | `open` | — | Pažeidimo tipas | — |
| `pazeidimo_busena` | `string` | — | `4` | `open` | — | Pažeidimo būsena | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pazeidimo_tipas` | `"Įprastas pažeidimas"` | — | — | Įprastas pažeidimas | — |
| `pazeidimo_tipas` | `"Supaprastintas pažeidimas"` | — | — | Supaprastintas pažeidimas | — |
| `pazeidimo_busena` | `"Pažeidimas nustatytas"` | — | — | Pažeidimas nustatytas | — |
| `pazeidimo_busena` | `"Pažeidimas"` | — | — | Pažeidimas | — |
| `pazeidimo_busena` | `"Pažeidimas nenustatytas"` | — | — | Pažeidimas nenustatytas | — |
| `pazeidimo_busena` | `"Pažeidimas ir įtariama nusikalstama veikla"` | — | — | Pažeidimas ir įtariama nusikalstama veikla | — |
| `pazeidimo_busena` | `"Įtariama nusikalstama veikla"` | — | — | Įtariama nusikalstama veikla | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L11 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_drugeliai.csv#L11)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys_dr (https://data.gov.lt/datasets/2931/)
