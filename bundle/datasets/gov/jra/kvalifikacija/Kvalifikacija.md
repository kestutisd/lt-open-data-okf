---
type: Table
title: "Kvalifikacija — JRA jaunimo darbuotojų kvalifikacija"
description: "Jaunimo reikalų agentūros Jaunimo darbuotojų sistema kaupia duomenis apie JRA dirbančius darbuotojus."
resource: "https://get.data.gov.lt/datasets/gov/jra/kvalifikacija/Kvalifikacija"
tags: [gov, jra, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/jra/kvalifikacija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/kvalifikacija.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kvalifikacija — JRA jaunimo darbuotojų kvalifikacija

Jaunimo reikalų agentūros Jaunimo darbuotojų sistema kaupia duomenis apie JRA dirbančius darbuotojus. Teikiami duomenis kaupiami nuo 2018 m., numatyta atnaujinti kasdien. Duomenyse kaupiama darbuotojo šifruotas kodas, išsirinkti kursai, tuometiniai etatas, išsilavinimas ir darbovietė.

- **Model:** `datasets/gov/jra/kvalifikacija/Kvalifikacija`[^manifest]
- **Dataset:** [JRA jaunimo darbuotojų kvalifikacija](../kvalifikacija.md) (`datasets/gov/jra/kvalifikacija`)
- **Manifest CSV:** [datasets/gov/jra/kvalifikacija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/jra/kvalifikacija.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/jra/kvalifikacija/Kvalifikacija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `darbuotojas` | `string` | — | `4` | `open` | — | Darbuotojo šifruotas identifikatoirus | — |
| `kursai_lt` | `string` | — | `4` | `open` | — | Darbuotojo išsirinkti kursai | — |
| `etatas` | `string` | — | `4` | `open` | — | Darbuotojo etatas | — |
| `issilavinimas` | `string` | — | `4` | `open` | — | Darbuotojo išsilavinimas | — |
| `darboviete` | `string` | — | `4` | `open` | — | Darbuotojo darbo vieta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kursai_lt` | `update(property: "kursai_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/jra/kvalifikacija.csv
