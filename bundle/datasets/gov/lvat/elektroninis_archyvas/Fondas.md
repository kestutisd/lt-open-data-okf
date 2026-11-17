---
type: Table
title: "Fondas — Fondai"
description: "Šioje rinkinio lentelėje vienos eilutės objektas yra fondas – hierarchiškai aukščiausia numeruojama archyvinių dokumentų struktūra."
resource: "https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas/Fondas"
tags: [gov, lvat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Fondas — Fondai

Šioje rinkinio lentelėje vienos eilutės objektas yra fondas – hierarchiškai aukščiausia numeruojama archyvinių dokumentų struktūra. Lentelėje atskirai pateikiamas fondo vidinis identifikatorius (stulpelyje „fondo_id“) ir fondo numeris archyve (stulpelyje „fondo_nr“). Fondo vidinis identifikatorius yra unikalus, per jį galima prijungti apyrašų lentelę, taip pat jį prirašius nuorodos <https://eais.archyvai.lt/repo-ext/view/> gale gaunamas adresas į fondo aprašą LVAT EAIS skaitmeninėje skaitykloje; o fondų numeriai gali kartotis, nes kiekvienas fondo saugotojas (archyvas) numeruoja savo fondus nepriklausomai.

- **Model:** `datasets/gov/lvat/elektroninis_archyvas/Fondas`[^manifest]
- **Dataset:** [Elektroninis archyvas](../elektroninis_archyvas.md) (`datasets/gov/lvat/elektroninis_archyvas`)
- **Manifest CSV:** [datasets/gov/lvat/elektroninis_archyvas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas/Fondas`
- **Primary Key (`ref`):** `fondo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fondo_id` | `string` | — | `4` | `open` | — | Fondo vidinis identifikatorius | — |
| `saugotojas` | `string` | — | `4` | `open` | — | Fondo saugotojo pilnas pavadinimas | — |
| `saugotojo_santrumpa` | `string` | — | `4` | `open` | — | Fondo saugotojo santrumpa | — |
| `fondo_nr` | `string` | — | `4` | `open` | — | Fondo numeris archyve | — |
| `fondo_pavadinimas` | `string` | — | `4` | `open` | — | Fondo pavadinimas | — |
| `chron_riba_nuo` | `date` | `D` | `4` | `open` | — | Chronologinės ribos pradžia | — |
| `chron_riba_iki` | `date` | `D` | `4` | `open` | — | Chronologinės ribos pabaiga | — |
| `chron_ribos` | `string` | — | `4` | `open` | — | Chronologinės ribos | — |
| `apyrasu_sk` | `integer` | — | `4` | `open` | — | Apyrašų skaičius fonde | — |
| `apskaitos_vnt_sk` | `integer` | — | `4` | `open` | — | Apskaitos vienetų skaičius fonde | — |
| `pasikeitimai` | `string` | — | `4` | `open` | — | Pasikeitimai | — |
| `sudarytojas` | `string` | — | `4` | `open` | — | Sudarytojo pavadinimas | — |
| `sudarytojo_istorija` | `string` | — | `4` | `open` | — | Sudarytojo administracinė istorija/biografija | — |
| `anotacija` | `string` | — | `4` | `open` | — | Anotacija | — |
| `ribojimai` | `integer` | — | `4` | `open` | — | Ar ribojamas priėjimas arba naudojimas (0–ne, 1–taip) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fondo_pavadinimas` | `update(property: "fondo_pavadinimas", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pasikeitimai` | `update(property: "pasikeitimai@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `sudarytojo_istorija` | `update(property: "sudarytojo_istorija", type: "text")` | `type` | `4` | `open` | — | — | — |
| `anotacija` | `update(property: "anotacija", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv
