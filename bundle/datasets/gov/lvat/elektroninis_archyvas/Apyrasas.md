---
type: Table
title: "Apyrasas — Apyrašai"
description: "Šioje rinkinio lentelėje vienos eilutės objektas yra bylos apyrašas – hierarchiškai žemesnė numeruojama archyvinių dokumentų struktūra nei fondas, bet aukštesnė nei apskaitos vienetas (byla)."
resource: "https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas/Apyrasas"
tags: [gov, lvat, apyrasas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L26"
    title: "atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv#L26"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3836/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lvat/elektroninis_archyvas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Apyrasas — Apyrašai

Šioje rinkinio lentelėje vienos eilutės objektas yra bylos apyrašas – hierarchiškai žemesnė numeruojama archyvinių dokumentų struktūra nei fondas, bet aukštesnė nei apskaitos vienetas (byla). Lentelėje atskirai pateikiamas apyrašo vidinis identifikatorius (stulpelyje „apyraso_id“) ir apyrašo numeris fonde (stulpelyje „apyraso_nr“). Apyrašo vidinis identifikatorius yra unikalus, jį prirašius nuorodos <https://eais.archyvai.lt/repo-ext/view/> gale gaunamas adresas į apyrašo aprašą LVAT EAIS skaitmeninėje skaitykloje, kur rasite apyrašui priklausančius apskaitos vienetus (bylas); o apyrašų numeriai gali kartotis, nes kiekvienas fondas numeruoja savo apyrašus nepriklausomai. Per fondo vidinį identifikatorių (stulpelį „fondo_id“) šią apyrašų lentelę galite sujungti su fondų lentele.[^manifest]

- **Model:** `datasets/gov/lvat/elektroninis_archyvas/Apyrasas`[^manifest]
- **Dataset:** [Elektroninis archyvas](../elektroninis_archyvas.md) (`datasets/gov/lvat/elektroninis_archyvas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lvat/elektroninis_archyvas.csv#L26](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L26)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas/Apyrasas` (`deployed`)[^manifest]
- **Provider:** `lvat` — Lietuvos vyriausiojo archyvaro tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `apyraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv#L26 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L26)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lvat/elektroninis_archyvas (https://data.gov.lt/datasets/3836/)
