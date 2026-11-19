---
type: Table
title: "Fondas — Fondai"
description: "Šioje rinkinio lentelėje vienos eilutės objektas yra fondas – hierarchiškai aukščiausia numeruojama archyvinių dokumentų struktūra."
resource: "https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas/Fondas"
tags: [gov, lvat, fondas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3836/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lvat/elektroninis_archyvas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Fondas — Fondai

Šioje rinkinio lentelėje vienos eilutės objektas yra fondas – hierarchiškai aukščiausia numeruojama archyvinių dokumentų struktūra. Lentelėje atskirai pateikiamas fondo vidinis identifikatorius (stulpelyje „fondo_id“) ir fondo numeris archyve (stulpelyje „fondo_nr“). Fondo vidinis identifikatorius yra unikalus, per jį galima prijungti apyrašų lentelę, taip pat jį prirašius nuorodos <https://eais.archyvai.lt/repo-ext/view/> gale gaunamas adresas į fondo aprašą LVAT EAIS skaitmeninėje skaitykloje; o fondų numeriai gali kartotis, nes kiekvienas fondo saugotojas (archyvas) numeruoja savo fondus nepriklausomai.[^manifest]

- **Model:** `datasets/gov/lvat/elektroninis_archyvas/Fondas`[^manifest]
- **Dataset:** [Elektroninis archyvas](../elektroninis_archyvas.md) (`datasets/gov/lvat/elektroninis_archyvas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lvat/elektroninis_archyvas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lvat/elektroninis_archyvas/Fondas` (`deployed`)[^manifest]
- **Provider:** `lvat` — Lietuvos vyriausiojo archyvaro tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `fondo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lvat/elektroninis_archyvas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lvat/elektroninis_archyvas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lvat/elektroninis_archyvas (https://data.gov.lt/datasets/3836/)
