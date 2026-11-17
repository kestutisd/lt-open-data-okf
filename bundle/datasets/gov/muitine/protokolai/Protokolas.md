---
type: Table
title: "Protokolas — Muitinės sulaikytų prekių protokolų duomenys"
description: "Rinkinyje pateikiami Muitinės departamento prekių sulaikymo protokolų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/muitine/protokolai/Protokolas"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/protokolai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/protokolai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Protokolas — Muitinės sulaikytų prekių protokolų duomenys

Rinkinyje pateikiami Muitinės departamento prekių sulaikymo protokolų duomenys. Muitinei sulaikius prekes surašomas Prekių sulaikymo protokolas. Tai yra pirminės būsenos dokumentas, kurio duomenys vaizduojami atveriamame rinkinyje. Nustačius Lietuvos Respublikos administracinių teisės pažeidimų arba pareiškus įtarimus dėl baudžiamojo kodekso pažeidimų, atitinkamai gali būti pildomas administracinio teisės pažeidimo protokolas arba pradedamas ikiteisminis tyrimas. Kitu atveju, įsigaliojus sprendimui dėl sulaikytų prekių išdavimo arba prekių grąžinimo savininkams ar kitiems asmenims yra pildomas nutarimas prekes grąžinti. Pažymėtina, jog šie duomenys negali būti naudojami oficialiajai statistikai skaičiuoti. Rinkinyje skelbiami nuo 2008 m. iki šių dienų kaupiami duomenys, surašyti Lietuvos Respublikos kelio, geležinkelio, krovinių, pašto, oro ar mobiliųjų grupių postuose. Duomenų teikėjas – Muitinės departamentas prie Lietuvos Respublikos finansų ministerijos.

- **Model:** `datasets/gov/muitine/protokolai/Protokolas`[^manifest]
- **Dataset:** [Muitinės sulaikytų prekių protokolų duomenys](../protokolai.md) (`datasets/gov/muitine/protokolai`)
- **Manifest CSV:** [datasets/gov/muitine/protokolai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/protokolai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/protokolai/Protokolas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agenūros įrašo unikalus identifikatorius | — |
| `protokolo_id` | `string` | — | `4` | `open` | — | Protokolo identifikatorius | — |
| `protokolo_data` | `date` | `D` | `4` | `open` | — | Protokolo surašymo data | — |
| `pasienio_ruozas` | `string` | — | `4` | `open` | — | Pasienio ruožas, kuriame prekės buvo sulaikytos | — |
| `surasymo_vieta_lt` | `string` | — | `2` | `open` | — | Prekių sulaikymo protokolo surašyma vieta | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `surasymo_vieta_lt` | `update(property: "surasymo_vieta_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/protokolai.csv
