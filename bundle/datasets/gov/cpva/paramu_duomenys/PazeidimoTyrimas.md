---
type: Table
title: "PazeidimoTyrimas — Pažeidimų tyrimų informacija įtariant pažeidimą"
description: "Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2014–2020 m. struktūrinių fondų..."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys/PazeidimoTyrimas"
tags: [gov, cpva, pazeidimotyrimas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L29"
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv#L29"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2904/"
    title: "data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PazeidimoTyrimas — Pažeidimų tyrimų informacija įtariant pažeidimą

Duomenys pateikiami iš Informacinės projektų administravimo sistemos (IPAS) skirtos kaupti, apdoroti ir saugoti statistinius ir finansinius duomenis, susijusius su VšĮ Centrinės projektų valdymo agentūros administruojamų Europos Sąjungos 2014–2020 m. struktūrinių fondų programos projektų įgyvendinimu. Lentelėje galima rasti tokią informaciją: pažeidimų tyrimų informacija įtariant pažeidimą (viena eilutė atitinka vieną įtariamą pažeidimą ir statusą, nurodantį, ar pažeidimas nustatytas). Projektai, kurie buvo vykdomi naudojantis šia sistema jau pasibaigę, bet sistemos duomenys retais atvejais vis dar atnaujinami. Tokiu atveju, duomenų atnaujinimas numatomas kas 6 mėn. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/cpva/paramu_duomenys/PazeidimoTyrimas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros teikiamų paramų sutartys ir finansavimas](../paramu_duomenys.md) (`datasets/gov/cpva/paramu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L29)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys/PazeidimoTyrimas` (`deployed`)[^manifest]
- **Provider:** `cpva` — VšĮ Centrinė projektų valdymo agentūra *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pazeidimo_tyr_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pazeidimo_tyr_id` | `string` | — | `4` | `open` | — | Pažeidimo tyrimo identifikacinis numeris | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Sutarties numeris | — |
| `pazeidimo_tikrinimo_data` | `date` | `D` | `4` | `open` | — | Pažeidimo tikrinimo data | — |
| `pazeidimo_statuso_data` | `date` | `D` | `4` | `open` | — | Pažeidimo statuso data | — |
| `pazeidimo_tyr_statusas` | `string` | — | `4` | `open` | — | Pažeidimo tyrimo stausas | — |
| `pazeidimo_rusis` | `string` | — | `4` | `open` | — | Pažeidimo rūšis | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pazeidimo_tyr_statusas` | `"Baigtas"` | — | — | Baigtas | — |
| `pazeidimo_tyr_statusas` | `"Patvirtintas"` | — | — | Patvirtintas | — |
| `pazeidimo_tyr_statusas` | `"Anuliuotas"` | — | — | Anuliuotas | — |
| `pazeidimo_tyr_statusas` | `"Papildymas"` | — | — | Papildymas | — |
| `pazeidimo_tyr_statusas` | `"Pradėtas tyrimas"` | — | — | Pradėtas tyrimas | — |
| `pazeidimo_tyr_statusas` | `"Atnaujintas tyrimas"` | — | — | Atnaujintas tyrimas | — |
| `pazeidimo_tyr_statusas` | `"Užregistruotas"` | — | — | Užregistruotas | — |
| `pazeidimo_rusis` | `"IRQ 2 - Pažeidimas"` | — | — | Pažeidimas | — |
| `pazeidimo_rusis` | `"IRQ 0 - Pažeidimas nenustatytas"` | — | — | Pažeidimas nenustatytas | — |
| `pazeidimo_rusis` | `"IRQ 3 - Įtarimas sukčiavimu"` | — | — | Įtarimas sukčiavimu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys.csv#L29 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys.csv#L29)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/cpva/paramu_duomenys (https://data.gov.lt/datasets/2904/)
