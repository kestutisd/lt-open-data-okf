---
type: Table
title: "RegionineTelsiuLigonine — Regioninėje Telšių ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai"
description: "Regioninės Telšių ligoninės (RTL) OpenLIMS sistemoje kaupiami RTL pacientams atliktų laboratorinių tyrimų duomenys, atnaujinami iki šiol."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/RegionineTelsiuLigonine"
tags: [gov, lab_tyrimai, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L224"
    last_modified: "2026-11-11T14:39:20Z"
---

# RegionineTelsiuLigonine — Regioninėje Telšių ligoninėje pacientams atliktų laboratorinių tyrimų rezultatai

Regioninės Telšių ligoninės (RTL) OpenLIMS sistemoje kaupiami RTL pacientams atliktų laboratorinių tyrimų duomenys, atnaujinami iki šiol. Duomenų rinkinys apima įstaigos pavadinimą, paciento šifruotą identifikatorių, lytį, gimimo metus, tyrimų grupę, tyrimo datą, tyrimo mėginio / ėminio tipą, tyrimo analitės pavadinimą, analitės LOINC kodą, analitės rezultatą bei normalių rezultato reikšmių rėžius, suapvalintus 5 skaitmenų tikslumu, rezultato matavimo vienetus, paciento pagrindinės diagnozės TLK-10-AM kodą ir pavadinimą. Vienas įrašas atitinka vieną tyrimo-analitės kombinaciją. OpenLIMS sistemoje yra saugomi analičių, tačiau ne jų sudaromų tyrimų pavadinimai.

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/RegionineTelsiuLigonine`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L224](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L224)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/RegionineTelsiuLigonine`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `istaigos_pav` | `string` | — | `4` | `open` | — | Tyrimą atlikusios įstaigos pavadinimas | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento šifruotas identifikatorius | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `tyrimo_grupe` | `string` | — | `4` | `open` | — | Tyrimo grupė | — |
| `tyrimo_data` | `date` | `D` | `4` | `open` | — | Tyrimo data dienos tikslumu | — |
| `tyrimo_meginio_tipas` | `string` | — | `3` | `open` | — | Tyrimo mėginio tipas | — |
| `tyrimo_analite` | `string` | — | `4` | `open` | — | Tyrimo analitės pavadinimas | — |
| `analites_loinc_kodas` | `string` | — | `4` | `open` | — | Tyrimo analitės LOINC kodas | — |
| `analites_rezultatas` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultatas | — |
| `analites_norma_nuo` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultato minimali norma | — |
| `analites_norma_iki` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultato maksimali norma | — |
| `matavimo_vienetas` | `string` | — | `4` | `open` | — | Tyrimo analitės matavimo vienetas | — |
| `paciento_diagnozes_tlk_10_am_kodas` | `string` | — | `4` | `open` | — | Paciento pagrindinės diagnozės TLK-10-AM kodas | — |
| `paciento_diagnoze` | `string` | — | `4` | `open` | — | Paciento pagrindinės diagnozės pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `paciento_lytis` | `"N"` | — | — | Nežinoma | — |
| `tyrimo_grupe` | `"Hematologija"` | — | — | Hematologija | — |
| `tyrimo_grupe` | `"Biochemija"` | — | — | Biochemija | — |
| `tyrimo_grupe` | `"Šlapimas"` | — | — | Šlapimas | — |
| `tyrimo_grupe` | `"Imunologija"` | — | — | Imunologija | — |
| `tyrimo_grupe` | `"Angliavandeniai"` | — | — | Angliavandeniai | — |
| `tyrimo_grupe` | `"Koprologija"` | — | — | Koprologija | — |
| `tyrimo_grupe` | `"Punktatai, CSF, nosis"` | — | — | Punktatai, CSF, nosis | — |
| `tyrimo_grupe` | `"Šarmų-rūgščių balansas"` | — | — | Šarmų-rūgščių balansas | — |
| `tyrimo_grupe` | `"Lytiniai organai"` | — | — | Lytiniai organai | — |
| `tyrimo_meginio_tipas` | `"Kraujas"` | — | — | Kraujas | — |
| `tyrimo_meginio_tipas` | `"Serumas"` | — | — | Serumas | — |
| `tyrimo_meginio_tipas` | `"Šlapimas"` | — | — | Šlapimas | — |
| `tyrimo_meginio_tipas` | `"Plazma"` | — | — | Plazma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv
