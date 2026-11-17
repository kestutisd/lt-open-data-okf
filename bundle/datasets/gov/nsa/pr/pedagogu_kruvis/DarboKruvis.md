---
type: Table
title: "DarboKruvis — Pedagogų darbo krūvis"
description: "Lentelėje pateikti Nacionalinės Švietimo agentūros (NŠA) pedagogų (bendrojo, ikimokyklinio ugdymo mokyklų, profesinio mokymo įstaigų, neformaliojo vaikų švietimo mokyklų ir formalųjį švietimą papildančio ugdymo mokyklų, mokslo ir..."
resource: "https://get.data.gov.lt/datasets/gov/nsa/pr/pedagogu_kruvis/DarboKruvis"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/pr/pedagogu_kruvis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/pr/pedagogu_kruvis.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# DarboKruvis — Pedagogų darbo krūvis

Lentelėje pateikti Nacionalinės Švietimo agentūros (NŠA) pedagogų (bendrojo, ikimokyklinio ugdymo mokyklų, profesinio mokymo įstaigų, neformaliojo vaikų švietimo mokyklų ir formalųjį švietimą papildančio ugdymo mokyklų, mokslo ir studijų institucijų pedagoginių darbuotojų ir/arba tyrėjų) pareigybių ir darbo krūvio duomenys iš pedagogų registro (PR). Duomenys kaupiami nuo 2010 m. Siekiant užtikrinti asmens duomenų apsaugą duomenys buvo triukšminti.

- **Model:** `datasets/gov/nsa/pr/pedagogu_kruvis/DarboKruvis`[^manifest]
- **Dataset:** [Pedagogų darbo krūvis](../pedagogu_kruvis.md) (`datasets/gov/nsa/pr/pedagogu_kruvis`)
- **Manifest CSV:** [datasets/gov/nsa/pr/pedagogu_kruvis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/pr/pedagogu_kruvis.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/pr/pedagogu_kruvis/DarboKruvis`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Pedagogo identifikatorius | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Pedagogo gimimo metai | — |
| `lytis` | `string` | — | `4` | `open` | — | Pedagogo lytis | — |
| `inst_id` | `string` | — | `4` | `open` | — | Institucijos identifikatorius | — |
| `institucija_grupes` | `string` | — | `4` | `open` | — | Institucijos grupė (-ės) | — |
| `institucija_tipai` | `string` | — | `4` | `open` | — | Institucijos tipas (-ai) | — |
| `pareigybe_pav_lt` | `string` | — | `3` | `open` | — | Pedagogo pareigybės pavadinimas | — |
| `pagrindine_pareigybe` | `boolean` | — | `4` | `open` | — | Požymis, ar pareigybė yra pagrindinė | — |
| `etat_kruvis` | `number` | — | `4` | `open` | — | Darbo krūvis (etato dydis) | — |
| `galioja_nuo` | `date` | `D` | `4` | `open` | — | Pareigybės galiojimo pradžios data | — |
| `galioja_iki` | `date` | `D` | `4` | `open` | — | Pareigybės galiojimo pabaigos data | — |
| `destomu_dalyku_sk` | `integer` | `U` | `4` | `open` | — | Pedagogo dėstomų dalykų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `institucija_grupes` | `update(property: "institucija_grupes[]", type: "array", source: "Institucija_grupes")` | `property` | `4` | — | — | — | — |
| `institucija_tipai` | `update(property: "institucija_tipai[]", type: "array", source: "Institucija_tipai")` | `property` | `4` | — | — | — | — |
| `pareigybe_pav_lt` | `update(property: "pareigybe_pav_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/pr/pedagogu_kruvis.csv
