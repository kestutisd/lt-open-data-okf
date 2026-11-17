---
type: Table
title: "Receptas — Elektroninių receptų duomenys"
description: "Pacientams išrašyti elektroniniai receptai, jų išrašymo data (mėnesio tikslumu), recepto skyrimo diagnozės kodas ir pavadinimas, vaisto ATC kodai, bendriniai pavadinimai ir stiprumas."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/Receptas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L75"
    last_modified: "2026-11-11T14:39:20Z"
---

# Receptas — Elektroninių receptų duomenys

Pacientams išrašyti elektroniniai receptai, jų išrašymo data (mėnesio tikslumu), recepto skyrimo diagnozės kodas ir pavadinimas, vaisto ATC kodai, bendriniai pavadinimai ir stiprumas. Filtruoti tik su inkstų patologija susiję elektroniniai receptai pagal ATC kodus, t. y. renino angiotenzino sistemą veikiantys vaistai, beta adrenoblokatoriai, kalcio kanalų blokatoriai, diuretikai, ne geležies antianeminiai preparatai, geležies preparatai, imunosupresantai, sistemiškai veikiantys kortikosteroidai.

- **Model:** `datasets/gov/lsd/sveikata/inkstu_biopsijos/Receptas`[^manifest]
- **Dataset:** [Pacientų, kuriems atlikta inkstų biopsija, duomenys](../inkstu_biopsijos.md) (`datasets/gov/lsd/sveikata/inkstu_biopsijos`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L75](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L75)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/Receptas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `israsymo_data` | `date` | `M` | `4` | `open` | — | Recepto išrašymo data (mėnesio tikslumu) | — |
| `diagnoz_kodas` | `string` | — | `4` | `open` | — | Diagnozės kodas | Diagnozės, dėl kurios skririamas vaistas, TLK-10-AM kodas |
| `diagnoz_pav` | `string` | — | `4` | `open` | — | Diagnozės pavadinimas | Diagnozės, dėl kurios skririamas vaistas, pavadinimas |
| `vaisto_atc_kodas` | `string` | — | `4` | `open` | — | Vaisto ATC kodas | — |
| `vaisto_bendr_pav` | `string` | — | `4` | `open` | — | Bendrinis pavadinimas (veikliosios medžiagos) | — |
| `vaisto_stiprumas` | `string` | — | `3` | `open` | — | Vaisto stiprumas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv
