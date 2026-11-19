---
type: Table
title: "RespublikineSiauliuLigonine — Respublikinės Šiaulių ligoninės pacientams atlikti laboratoriniai tyrimai"
description: "Duomenų rinkinyje pateikiami nuo 2020 metų informacinėje sistemoje „PanelLIMS“ kaupiami ir iki šiol atnaujinami Respublikinės Šiaulių ligoninės atliktų laboratorinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/RespublikineSiauliuLigonine"
tags: [gov, lab_tyrimai, respublikinesiauliuligonine, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L814"
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L814"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2700/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai"
    author: "team:vda"
    last_modified: "2026-02-23T00:00:00Z"
---

# RespublikineSiauliuLigonine — Respublikinės Šiaulių ligoninės pacientams atlikti laboratoriniai tyrimai

Duomenų rinkinyje pateikiami nuo 2020 metų informacinėje sistemoje „PanelLIMS“ kaupiami ir iki šiol atnaujinami Respublikinės Šiaulių ligoninės atliktų laboratorinių tyrimų duomenys. Vienas įrašas atitinka vieną užsakymo kodo, tyrimo analitės ir jos reikšmių normų rėžio kombinaciją. Duomenų rinkinį sudaro: užsakymo kodas ir data, paciento identifikatorius, asmens kodas, gimimo metai ir lytis iš atitinkamų stulpelių ir galiojančių asmens kodų, tyrimo grupė, pogrupis, analitės kodas, pavadinimas, tekstinis bei skaitinis rezultatai, analitės matavimo vienetas, normos rėžiai, tyrimo analitės rezultato data ir laikas. Tekstinių rezultatų reikšmės gali būti klaidingos, nes yra išgaunamos iš stulpelio, saugančio tiek tekstines, tiek skaitines reikšmes. Duomenų teikėjas – VšĮ Respublikinės Šiaulių ligoninė. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/RespublikineSiauliuLigonine`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L814](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L814)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/RespublikineSiauliuLigonine` (`deployed`)[^manifest]
- **Provider:** `lab_tyrimai`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-02-23`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `uzsakymo_kodas` | `string` | — | `4` | `open` | — | Tyrimo užsakymo kodas | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento šifruotas identifikatorius | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `vda_paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai iš asmens kodo | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `vda_paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis iš asmens kodo | — |
| `tyrimo_grupe` | `string` | — | `4` | `open` | — | Tyrimo grupė | — |
| `tyrimo_pogrupis` | `string` | — | `4` | `open` | — | Tyrimo pogrupis | — |
| `analites_kodas` | `string` | — | `4` | `open` | — | Tyrimo analitės kodas | — |
| `analites_pavadinimas` | `string` | — | `4` | `open` | — | Tyrimo analitės pavadinimas | — |
| `tekstinis_rezultatas` | `string` | — | `3` | `open` | — | Analitės tekstinis rezultatas | — |
| `skaitinis_rezultatas` | `number` | — | `4` | `open` | — | Analitės skaitinis rezultatas | — |
| `matavimo_vienetai` | `string` | — | `4` | `open` | — | Analitės matavimo vienetas | — |
| `norma_nuo` | `string` | — | `4` | `open` | — | Analitės apatinė norma | — |
| `norma_iki` | `string` | — | `4` | `open` | — | Analitės viršutinė norma | — |
| `rezultato_data` | `date` | `D` | `4` | `open` | — | Analitės rezultato data su laiku | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"Vyras"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"Moteris"` | `M` | — | Moteris | — |
| `vda_paciento_lytis` | `"Vyras"` | `V` | — | Vyras | — |
| `vda_paciento_lytis` | `"Moteris"` | `M` | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv#L814 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L814)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lab_tyrimai/lab_tyrimai (https://data.gov.lt/datasets/2700/)
