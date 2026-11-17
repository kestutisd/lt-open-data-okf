---
type: Table
title: "JivexRadiologija — Pacientams atlikti radiologiniai tyrimai"
description: "Ukmergės ligoninės JIVEX sistema kaupia žmonėms atliekamų radiologinių tyrimų duomenis nuo 2018 m., atnaujinamus kasdien."
resource: "https://get.data.gov.lt/datasets/gov/ukmlig/jivex/JivexRadiologija"
tags: [gov, ukmlig, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ukmlig/jivex.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ukmlig/jivex.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# JivexRadiologija — Pacientams atlikti radiologiniai tyrimai

Ukmergės ligoninės JIVEX sistema kaupia žmonėms atliekamų radiologinių tyrimų duomenis nuo 2018 m., atnaujinamus kasdien. Duomenys apima šifruotus pacientų vidinius sistemos identifikatorius, lytį, gimimo metus. Į duomenis taip pat patenka tyrimų užsakymai, vadinami studijomis: jų identifikatoriai, datos. Patenkantys tyrimų serijų duomenys yra identifikatoriai, datos, paciento kūno padėtis tyrimo metu, tirta kūno dalis, tyrimo serijos modalumas, nusakantis tyrimo pobūdį bei tyrimo serijos protokolas.

- **Model:** `datasets/gov/ukmlig/jivex/JivexRadiologija`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../jivex.md) (`datasets/gov/ukmlig/jivex`)
- **Manifest CSV:** [datasets/gov/ukmlig/jivex.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ukmlig/jivex.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ukmlig/jivex/JivexRadiologija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros unikalus identifikatorius | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento identifikatorius JIVEX sistemoje | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `tyrimo_studijos_id` | `string` | — | `4` | `open` | — | Tyrimo užsakymo (studijos) identifikatorius | — |
| `tyrimo_studijos_data` | `datetime` | `S` | `4` | `open` | — | Tyrimo studijos data ir laikas | — |
| `tyrimo_serijos_id` | `string` | — | `4` | `open` | — | Tyrimo serijos identifikatorius | — |
| `tyrimo_serijos_data` | `datetime` | `S` | `4` | `open` | — | Tyrimo sertijos data ir laikas | — |
| `paciento_kuno_padetis` | `string` | — | `4` | `open` | — | Paciento kūno padėtis tyrimo serijos metu | — |
| `tirta_paciento_kuno_dalis` | `string` | — | `4` | `open` | — | Tyrimo serijos metu tirta paciento kūno dalis | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo sertijos modalumas | — |
| `tyrimo_serijos_protokolas` | `string` | — | `3` | `open` | — | Tyrimo serijos protokolas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"vyras"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"moteris"` | `M` | — | Moteris | — |
| `paciento_lytis` | `"kita"` | `K` | — | Kita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ukmlig/jivex.csv
