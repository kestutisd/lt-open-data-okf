---
type: Table
title: "KazluRudosPSPC — Kazlų Rūdos pirminės sveikatos priežiūros centro pacientams atlikti radiologiniai tyrimai"
description: "Informacinėje sistemoje „JiveX“ kaupiami Kazlų Rūdos PSPC pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/KazluRudosPSPC"
tags: [gov, radiologija, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L624"
    last_modified: "2026-11-11T14:39:20Z"
---

# KazluRudosPSPC — Kazlų Rūdos pirminės sveikatos priežiūros centro pacientams atlikti radiologiniai tyrimai

Informacinėje sistemoje „JiveX“ kaupiami Kazlų Rūdos PSPC pacientams atliktų radiologinių tyrimų duomenys. Rinkinyje pateikti duomenys yra nuo 2020 m. kovo mėnesio ir atnaujinami kasdien. Vienas įrašas atitinka vieną tyrimo seriją (visų tyrimo serijų identifikatoriai unikalūs). Duomenų rinkinį sudaro: paciento pseudonimizuotas identifikatorius, lytis, gimimo metai, tyrimo studijos identifikatorius ir data, tyrimo serijos identifikatorius ir data, paciento kūno padėtis, tirta kūno dalis, tyrimo serijos modalumas ir protokolas. Pacientų gimimo metai paimti iš galiojančių asmens kodų, o tais atvejais, kai asmens kodai negaliojančių – iš gimimo datos stulpelio. Duomenų teikėjas – VšĮ Kazlų Rūdos pirminės sveikatos priežiūros centras.

- **Model:** `datasets/gov/radiologija/KazluRudosPSPC`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L624](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L624)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/KazluRudosPSPC`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento identifikatorius | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `tyrimo_studijos_id` | `string` | — | `4` | `open` | — | Tyrimo studijos identifikatorius | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `tyrimo_serijos_id` | `string` | — | `4` | `open` | — | Tyrimo serijos identifikatorius | — |
| `tyrimo_serijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo serijos data | — |
| `paciento_kuno_padetis` | `string` | — | `4` | `open` | — | Paciento kūno padėtis tyrimo metu | — |
| `tirta_paciento_kuno_dalis` | `string` | — | `4` | `open` | — | Tirta paciento kūno dalis | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_protokolas` | `string` | — | `4` | `open` | — | Tyrimo serijos protokolas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `paciento_lytis` | `"K"` | — | — | Kita | — |
| `tyrimo_serijos_modalumas` | `"DX"` | — | — | Skaitmeninė radiografija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv
