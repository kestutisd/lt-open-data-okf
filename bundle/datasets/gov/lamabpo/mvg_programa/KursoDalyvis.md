---
type: Table
title: "KursoDalyvis — MVG dalyvių duomenys"
description: "Lentelėje pateikiami MVG programoje dalyvaujančių ar praeityje dalyvavusių dalyvių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa/KursoDalyvis"
tags: [gov, lamabpo, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/mvg_programa.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# KursoDalyvis — MVG dalyvių duomenys

Lentelėje pateikiami MVG programoje dalyvaujančių ar praeityje dalyvavusių dalyvių duomenys. Vienoje eilutėje pateikiama informacija apie vieną mokinį, priskirtą atitinkamai MVG kursų grupei. Eilutės duomenys apima: unikalų eilutės identifikatorių, mokinio identifikacinį numerį, grupės identifikacinį numerį, gimimo metus, lytį, gyvenamąją apskritį, datą, kada mokinys užsiregistravo į mokymus, bei požymį, nurodantį, ar mokinys įgijo kurso baigimo pažymėjimą ir kursų kainos dalis, kurias finansavo pats mokinys ir valstybė. Kiekvienas mokinys priskiriamas kursų grupei pagal grupės identifikacinį kodą.

- **Model:** `datasets/gov/lamabpo/mvg_programa/KursoDalyvis`[^manifest]
- **Dataset:** [Projekto „Mokykis visą gyvenimą!“ dalyvių ir kursų duomenys](../mvg_programa.md) (`datasets/gov/lamabpo/mvg_programa`)
- **Manifest CSV:** [datasets/gov/lamabpo/mvg_programa.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/mvg_programa.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/mvg_programa/KursoDalyvis`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Eilutės identifikacinis numeris | Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius |
| `mokinio_id` | `string` | — | `4` | `open` | — | Mokinio identifikacinis numeris | Programos "Mokykis visą gyvenimą" mokinio identifikacinis numeris |
| `grupes_id_numeris` | `string` | — | `4` | `open` | — | Kursų grupės identifikacinis numeris | Kursų grupės identifikacinis numeris |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Mokinio gimimo metai | Gimimo metai gauti iš mokinio asmens kodo ir suapvalinti iki metų |
| `lytis` | `string` | — | `4` | `open` | — | Mokinio lytis | Lytis gauta iš mokinio asmens kodo |
| `vietove` | `string` | — | `4` | `open` | — | Mokinio gyvenamoji vietovė | — |
| `registracijos_data` | `date` | `D` | `4` | `open` | — | Registracijos data | Data, kada mokinys užsiregistravo į kursus |
| `pazymejimas` | `boolean` | — | `4` | `open` | — | Pažymėjimo statusas | Požymis, nurodantis ar mokinys įgijo programos pažymėjimą |
| `finansavimas_valst` | `integer` | — | `4` | `open` | — | Valstybės finansavimas | Valstybės finansuojama suma eurais už kursus |
| `finansavimas_mok` | `integer` | — | `4` | `open` | — | Mokinio finansavimas | Mokinio finansuojama suma eurais už kursus |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | — | `"V"` | — | Vyras | — |
| `lytis` | — | `"M"` | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/mvg_programa.csv
