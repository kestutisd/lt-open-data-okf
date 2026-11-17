---
type: Table
title: "PareigybeDeklaracija — Privačių interesų deklaracijų statistika pagal pareigybės pobūdį"
description: "Į ataskaitą įtrauktos tik standartinio tipo pareigybės arba ekspertų ataskaitose nurodytų pareigybių pobūdis, kai asmuo teikia deklaraciją dėl einamųjų pareigų ir dėl dalyvavimo viešuosiuose pirkimuose bei turi deklaruoti pareigas."
resource: "https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/PareigybeDeklaracija"
tags: [gov, vtek, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L21"
    last_modified: "2026-11-11T14:39:20Z"
---

# PareigybeDeklaracija — Privačių interesų deklaracijų statistika pagal pareigybės pobūdį

Į ataskaitą įtrauktos tik standartinio tipo pareigybės arba ekspertų ataskaitose nurodytų pareigybių pobūdis, kai asmuo teikia deklaraciją dėl einamųjų pareigų ir dėl dalyvavimo viešuosiuose pirkimuose bei turi deklaruoti pareigas. Be to, jei asmuo užima vienodo pobūdžio pareigybes keliose darbovietėse, į statistiką įtraukiamos tik unikalios pobūdžių reikšmės. Ataskaitoje pateikiami nuo 2020 m. kaupiami duomenys pamėnesiui.

- **Model:** `datasets/gov/vtek/pinreg_ataskaitos/PareigybeDeklaracija`[^manifest]
- **Dataset:** [Privačių interesų registro ataskaitos](../pinreg_ataskaitos.md) (`datasets/gov/vtek/pinreg_ataskaitos`)
- **Manifest CSV:** [datasets/gov/vtek/pinreg_ataskaitos.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L21)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/PareigybeDeklaracija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `ataskaitos_data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `pareigu_pobudis` | `string` | — | `4` | `open` | — | Pareigų pobūdžio kategorija | — |
| `pateikta_deklaraciju` | `integer` | — | `4` | `open` | — | Bendras paskelbtų deklaracijų skaičius per ataskaitinį laikotarpį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv
