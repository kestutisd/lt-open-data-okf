---
type: Table
title: "Laivas — Į Klaipėdos uostą atplaukiantys arba iš jo išplaukiantys tarptautiniai laivai."
description: "Informacija apie registruojamus į Klaipėdos uostą atplaukiančius arba iš jo išplaukiančius tarptautinius laivus."
resource: "https://get.data.gov.lt/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras/Laivas"
tags: [gov, kvjud, laivas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2864/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Laivas — Į Klaipėdos uostą atplaukiantys arba iš jo išplaukiantys tarptautiniai laivai.

Informacija apie registruojamus į Klaipėdos uostą atplaukiančius arba iš jo išplaukiančius tarptautinius laivus.[^manifest]

- **Model:** `datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras/Laivas`[^manifest]
- **Dataset:** [Į Klaipėdos uostą atplaukiantys arba iš jo išplaukiantys tarptautiniai laivai.](../atvykstanciu_isvykstanciu_laivu_registras.md) (`datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras/Laivas` (`deployed`)[^manifest]
- **Provider:** `kvjud` — AB Klaipėdos valstybinio jūrų uosto direkcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `laivo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `laivo_id` | `string` | — | `4` | `open` | — | Plaukiančio laivo identifikatorius | — |
| `laivo_registracijos_numeris` | `string` | — | `4` | `open` | — | Laivo registracijos numeris | — |
| `numatomas_atvykimas_isvykimas` | `datetime` | — | `4` | `open` | — | Numatoma atvykimo ar išvykimo data ir laikas | — |
| `faktinis_atvykimas_isvykimas` | `datetime` | — | `4` | `open` | — | Realus atvykimo ar išvykimo data ir laikas | — |
| `laivo_pavadinimas` | `string` | — | `4` | `open` | — | Laivo pavadinimas | — |
| `laivo_saukinys` | `string` | — | `4` | `open` | — | Laivo šaukinys | — |
| `laivo_tipas` | `string` | — | `4` | `open` | — | Laivo tipo pavadinimas | — |
| `registracijos_valstybes_pavadinimas` | `string` | — | `4` | `open` | — | Šalis, po kuria plaukia laivas | — |
| `atvykimo_ar_isvykimo_uosto_pavadinimas` | `string` | — | `4` | `open` | — | Pradinio ar galutinio uosto pavadinimas (priklausomai nuo judėjimo krypties) | — |
| `atvykimo_ar_isvykimo_uosto_valstybes_pavadinimas` | `string` | — | `4` | `open` | — | Valstybė kuriai priklauso pradinis ar galutinis uostas | — |
| `laivo_ilgis` | `number` | — | `4` | `open` | — | Laivo ilgis metrais | — |
| `laivo_tonazas` | `number` | — | `4` | `open` | — | Bruto masė tonomis | — |
| `laivo_plaukimo_kryptis` | `string` | — | `4` | `open` | — | Laivo judėjimo kryptis | — |
| `agento_imone` | `string` | — | `4` | `open` | — | Agento įmonės pavadinimas | — |
| `stovejimo_vietos_tipas` | `string` | — | `4` | `open` | — | Laivo stovėjimo vietos tipas | — |
| `stovejimo_vieta` | `string` | — | `4` | `open` | — | Laivo stovėjimo vietos pavadinimas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `laivo_plaukimo_kryptis` | `"ATV"` | — | — | Atvykstantis laivas | — |
| `laivo_plaukimo_kryptis` | `"ISV"` | — | — | Išvykstantis laivas | — |
| `stovejimo_vietos_tipas` | `"KRANT"` | — | — | Krantinė | — |
| `stovejimo_vietos_tipas` | `"DOK"` | — | — | Dokas | — |
| `stovejimo_vietos_tipas` | `"VIDR"` | — | — | Vidurio linija | — |
| `stovejimo_vietos_tipas` | `"KITA"` | — | — | Kita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kvjud/atvykstanciu_isvykstanciu_laivu_registras (https://data.gov.lt/datasets/2864/)
