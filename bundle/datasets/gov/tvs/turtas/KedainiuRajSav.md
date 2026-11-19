---
type: Table
title: "KedainiuRajSav"
description: "Rinkinys pateikia informaciją apie savivaldybių valdomą nekilnojamąjį turtą."
resource: "https://get.data.gov.lt/datasets/gov/tvs/turtas/KedainiuRajSav"
tags: [gov, tvs, kedainiurajsav, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L22"
    title: "atviriduomenys/manifest — datasets/gov/tvs/turtas.csv#L22"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3825/"
    title: "data.gov.lt DCAT-AP — datasets/gov/tvs/turtas"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# KedainiuRajSav

**Dataset Context:** Rinkinys pateikia informaciją apie savivaldybių valdomą nekilnojamąjį turtą. Duomenyse nurodomas turto identifikatorius, NT registro kodas, objekto pavadinimas, statybos pabaigos metai, objekto paskirtis, plotas kvadratiniais metrais, bei geografinė vieta. Geografinė informacija pateikiama tiek geografinių koordinačių, tiek LKS-94 plokštuminių koordinačių formatais. Taip pat įtrauktas objekto adreso informacijos aktualumas bei geografinio koordinavimo patikimumo procentas. Duomenų teikėjas: Savivaldybių administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/tvs/turtas/KedainiuRajSav`[^manifest]
- **Dataset:** [Duomenys apie savyvaldybės turtą](../turtas.md) (`datasets/gov/tvs/turtas`)[^manifest]
- **Manifest CSV:** [datasets/gov/tvs/turtas.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L22)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tvs/turtas/KedainiuRajSav` (`deployed`)[^manifest]
- **Provider:** `tvs` — Savivaldybių turto valdymo duomenų rinkinys *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `ntr_reg_kodas` | `string` | — | `4` | `open` | — | NT registro kodas | — |
| `statybos_pabaigos_metai` | `integer` | — | `4` | `open` | — | Objekto statybos pabaigos metai | — |
| `plotas_kv_metrais` | `number` | — | `4` | `open` | — | Objekto plotas kvadratiniais metrais | — |
| `ntr_paskirtis` | `string` | — | `4` | `open` | — | Objekto paskirtis | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Geografinės koordinatės | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Geografinės koordinatės | — |
| `lks_x` | `number` | — | `4` | `open` | — | Stačiakampės plokštuminės LKS-94 koordinatės | — |
| `lks_y` | `number` | — | `4` | `open` | — | Stačiakampės plokštuminės LKS-94 koordinatės | — |
| `geometrija` | `string` | — | `4` | `open` | — | Geografinės koordinatės | — |
| `tipas` | `string` | — | `4` | `open` | — | Objekto adreso informacijos aktualumas | — |
| `patikimumas` | `number` | — | `4` | `open` | — | Geografinių koordinačių patikimumas (procentais) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/tvs/turtas.csv#L22 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/turtas.csv#L22)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/tvs/turtas (https://data.gov.lt/datasets/3825/)
