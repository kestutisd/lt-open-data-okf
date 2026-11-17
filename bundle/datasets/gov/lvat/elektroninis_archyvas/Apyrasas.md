---
type: Table
title: "Apyrasas — Apyrašai"
description: "Šioje rinkinio lentelėje vienos eilutės objektas yra bylos apyrašas – hierarchiškai žemesnė numeruojama archyvinių dokumentų struktūra nei fondas, bet aukštesnė nei apskaitos vienetas (byla)."
resource: "https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas/Apyrasas"
tags: [gov, lvat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L26"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apyrasas — Apyrašai

Šioje rinkinio lentelėje vienos eilutės objektas yra bylos apyrašas – hierarchiškai žemesnė numeruojama archyvinių dokumentų struktūra nei fondas, bet aukštesnė nei apskaitos vienetas (byla). Lentelėje atskirai pateikiamas apyrašo vidinis identifikatorius (stulpelyje „apyraso_id“) ir apyrašo numeris fonde (stulpelyje „apyraso_nr“). Apyrašo vidinis identifikatorius yra unikalus, jį prirašius nuorodos <https://eais.archyvai.lt/repo-ext/view/> gale gaunamas adresas į apyrašo aprašą LVAT EAIS skaitmeninėje skaitykloje, kur rasite apyrašui priklausančius apskaitos vienetus (bylas); o apyrašų numeriai gali kartotis, nes kiekvienas fondas numeruoja savo apyrašus nepriklausomai. Per fondo vidinį identifikatorių (stulpelį „fondo_id“) šią apyrašų lentelę galite sujungti su fondų lentele.

- **Model:** `datasets/gov/lvat/elektroninis_archyvas/Apyrasas`[^manifest]
- **Dataset:** [Elektroninis archyvas](../elektroninis_archyvas.md) (`datasets/gov/lvat/elektroninis_archyvas`)
- **Manifest CSV:** [datasets/gov/lvat/elektroninis_archyvas.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L26)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas/Apyrasas`
- **Primary Key (`ref`):** `apyraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apyraso_id` | `string` | — | `4` | `open` | — | Apyrašo vidinis identifikatorius | — |
| `fondo_id` | `string` | — | `4` | `open` | — | Fondo vidinis identifikatorius | — |
| `apyraso_nr` | `string` | — | `4` | `open` | — | Apyrašo numeris fonde | — |
| `apyraso_pavadinimas` | `string` | — | `4` | `open` | — | Apyrašo pavadinimas | — |
| `chron_riba_nuo` | `date` | `D` | `4` | `open` | — | Chronologinės ribos pradžia | — |
| `chron_riba_iki` | `date` | `D` | `4` | `open` | — | Chronologinės ribos pabaiga | — |
| `chron_ribos` | `string` | — | `4` | `open` | — | Chronologinės ribos | — |
| `apskaitos_vnt_sk` | `integer` | — | `4` | `open` | — | Apskaitos vienetų skaičius apyraše | — |
| `pasikeitimai` | `string` | — | `4` | `open` | — | Pasikeitimai | — |
| `anotacija` | `string` | — | `4` | `open` | — | Anotacija | — |
| `ribojimai` | `integer` | — | `4` | `open` | — | Ar ribojamas priėjimas arba naudojimas (0–ne, 1–taip) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apyraso_pavadinimas` | `update(property: "apyraso_pavadinimas", type: "text")` | `type` | `4` | `open` | — | — | — |
| `pasikeitimai` | `update(property: "pasikeitimai@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `anotacija` | `update(property: "anotacija", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv
