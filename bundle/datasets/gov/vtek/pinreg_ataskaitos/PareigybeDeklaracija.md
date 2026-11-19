---
type: Table
title: "PareigybeDeklaracija — Privačių interesų deklaracijų statistika pagal pareigybės pobūdį"
description: "Į ataskaitą įtrauktos tik standartinio tipo pareigybės arba ekspertų ataskaitose nurodytų pareigybių pobūdis, kai asmuo teikia deklaraciją dėl einamųjų pareigų ir dėl dalyvavimo viešuosiuose pirkimuose bei turi deklaruoti pareigas."
resource: "https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/PareigybeDeklaracija"
tags: [gov, vtek, pareigybedeklaracija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L21"
    title: "atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv#L21"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3798/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vtek/pinreg_ataskaitos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PareigybeDeklaracija — Privačių interesų deklaracijų statistika pagal pareigybės pobūdį

Į ataskaitą įtrauktos tik standartinio tipo pareigybės arba ekspertų ataskaitose nurodytų pareigybių pobūdis, kai asmuo teikia deklaraciją dėl einamųjų pareigų ir dėl dalyvavimo viešuosiuose pirkimuose bei turi deklaruoti pareigas. Be to, jei asmuo užima vienodo pobūdžio pareigybes keliose darbovietėse, į statistiką įtraukiamos tik unikalios pobūdžių reikšmės. Ataskaitoje pateikiami nuo 2020 m. kaupiami duomenys pamėnesiui.[^manifest]

- **Model:** `datasets/gov/vtek/pinreg_ataskaitos/PareigybeDeklaracija`[^manifest]
- **Dataset:** [Privačių interesų registro ataskaitos](../pinreg_ataskaitos.md) (`datasets/gov/vtek/pinreg_ataskaitos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vtek/pinreg_ataskaitos.csv#L21](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L21)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/pinreg_ataskaitos/PareigybeDeklaracija` (`deployed`)[^manifest]
- **Provider:** `vtek` — Vyriausioji tarnybinės etikos komisija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `ataskaitos_data` | `date` | `D` | `4` | `open` | — | Ataskaitinė data | — |
| `pareigu_pobudis` | `string` | — | `4` | `open` | — | Pareigų pobūdžio kategorija | — |
| `pateikta_deklaraciju` | `integer` | — | `4` | `open` | — | Bendras paskelbtų deklaracijų skaičius per ataskaitinį laikotarpį | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/pinreg_ataskaitos.csv#L21 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/pinreg_ataskaitos.csv#L21)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vtek/pinreg_ataskaitos (https://data.gov.lt/datasets/3798/)
