---
type: Table
title: "SirvintuRajonoSavivaldybesSC — Širvintų savivaldybes rajono sveikatos centro pacientams atliktų laboratorinių tyrimų duomenys"
description: "Širvintų rajono savivaldybės sveikatos centro OpenLIMS sistemoje nuo 2017 m. kaupiami ir iki šiol atnaujinami pacientams atliktų laboratorinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/SirvintuRajonoSavivaldybesSC"
tags: [gov, lab_tyrimai, sirvinturajonosavivaldybessc, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L126"
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L126"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2700/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-02-23T00:00:00Z"
---

# SirvintuRajonoSavivaldybesSC — Širvintų savivaldybes rajono sveikatos centro pacientams atliktų laboratorinių tyrimų duomenys

Širvintų rajono savivaldybės sveikatos centro OpenLIMS sistemoje nuo 2017 m. kaupiami ir iki šiol atnaujinami pacientams atliktų laboratorinių tyrimų duomenys. Duomenų rinkinį sudaro:įstaigos pavadinimas, paciento šifruotas identifikatorius, lytis, gimimo metai, tyrimo data dienos tikslumu, rezultato interpretacijos stulpelis, tiek su skaitiniais rezultatais, tiek su semantiniais vertinimais, atskiras, 5 skaitmenų tikslumu suapvalintas skaitinių rezultatų stulpelis, tyrimo metodo pavadinimas, rezultato reikšmių normų rėžiai, suapvalinti 5 skaitmenų tikslumu, rezultato matavimo vienetai bei paciento pagrindinės diagnozės TLK-10-AM kodas ir pavadinimas. Vienas įrašas atitinka vienam pacientui atliktą vieną tyrimą. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/SirvintuRajonoSavivaldybesSC`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L126](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L126)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/SirvintuRajonoSavivaldybesSC` (`deployed`)[^manifest]
- **Provider:** `lab_tyrimai`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-02-23`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `istaigos_pav` | `string` | — | `4` | `open` | — | Tyrimą atlikusios įstaigos pavadinimas | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento šifruotas identifikatorius | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `tyrimo_data` | `date` | `D` | `4` | `open` | — | Tyrimo data dienos tikslumu | — |
| `tyrimo_rezultato_interpretacija` | `string` | — | `4` | `open` | — | Tyrimo rezultatų semantiniai vertinimai ir skaitiniai rezultatai | — |
| `tyrimo_skaitinis_rezultatas` | `number` | — | `4` | `open` | — | Tyrimo skaitinis rezultatas | — |
| `tyrimo_metodo_pavadinimas` | `string` | — | `4` | `open` | — | Tyrimo metodo pavadinimas | — |
| `tyrimo_rezultato_norma_nuo` | `number` | — | `4` | `open` | — | Tyrimo rezultato mažiausia normali reikšmė pagal metodą | — |
| `tyrimo_rezultato_norma_iki` | `number` | — | `4` | `open` | — | Tyrimo rezultato didžiausia normali reikšmė pagal metodą | — |
| `matavimo_vienetas` | `string` | — | `4` | `open` | — | Tyrimo rezultato matavimo vienetas | — |
| `paciento_diagnozes_tlk_10_am_kodas` | `string` | — | `4` | `open` | — | Paciento pagrindinės diagnozės TLK-10-AM kodas | — |
| `paciento_diagnoze` | `string` | — | `4` | `open` | — | Paciento pagrindinės diagnozės pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"Vyras"` | — | — | Vyras | — |
| `paciento_lytis` | `"Moteris"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L126 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L126)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai (https://data.gov.lt/datasets/2700/)
