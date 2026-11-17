---
type: Table
title: "ViesojoSektoriausFbPaskyruSekejai — Viešojo sektoriaus Facebook paskyrų stebėsena"
description: "Lentelėje pateikiami valstybinių institucijų, įstaigų, tarnybų, agentūrų Facebook paskyrų sekėjų skačiaus stebėsenos rezultatai."
resource: "https://get.data.gov.lt/datasets/gov/lsd/socialiniu_mediju_stebesena/ViesojoSektoriausFbPaskyruSekejai"
tags: [gov, lsd, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/soc_erdves_stebesena.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/soc_erdves_stebesena.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# ViesojoSektoriausFbPaskyruSekejai — Viešojo sektoriaus Facebook paskyrų stebėsena

Lentelėje pateikiami valstybinių institucijų, įstaigų, tarnybų, agentūrų Facebook paskyrų sekėjų skačiaus stebėsenos rezultatai. Stebėsena vykdyta 2022-07-11, atnaujinimo data šiuo metu nenumatyta. Įtrauktos 99 paskyros. Stebėsena yra skirta viešojo sektoriaus bendravimui su visuomene skatinti, taip pat visuomenės informavimui apie šių paskyrų egzistavimą bei naudą.

Pastabos: Ne visos įstaigos turi socialinių medijų paskyras (pvz., Valstybinė lietuvių kalbos komisija). Įstagos gali turėti kelias paskyras (pvz., Lietuvos statistikos departamentas ir Valstybės duomenų analitika). Facebook paskyra gali nepriklausyti vienai konkrečiai įstaigai (pvz., Lietuvos teismai) arba priklausyti nebeegzistuojančiai įstaigai (Valstybinė energetikos inspekcija).

- **Model:** `datasets/gov/lsd/socialiniu_mediju_stebesena/ViesojoSektoriausFbPaskyruSekejai`[^manifest]
- **Dataset:** [Socialinių medijų stebėsena](../socialiniu_mediju_stebesena.md) (`datasets/gov/lsd/socialiniu_mediju_stebesena`)
- **Manifest CSV:** [datasets/gov/lsd/soc_erdves_stebesena.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/soc_erdves_stebesena.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/socialiniu_mediju_stebesena/ViesojoSektoriausFbPaskyruSekejai`
- **Primary Key (`ref`):** `url`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `data` | `date` | `D` | `4` | `open` | — | Data | Data, kuomet vykdyta paskyrų stebėsena |
| `jar_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `pavadinimas` | `string` | — | `2` | `open` | — | Valstybinės institucijos, įstaigos, tarnybos, agentūros pavadinimas | — |
| `sekeju_sk` | `integer` | — | `4` | `open` | — | Stebimos Facebook paskyros sekėjų ('followers') skaičius | — |
| `url` | `url` | — | `4` | `open` | — | URL adresas | Stebimos Facebook paskyros URL adresas |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar_kodas` | `update(property: "ja_kodas", type: "")` | `type` | `4` | `open` | — | — | — |
| `pavadinimas` | `update(property: "ja_pavadinimas", type: "")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/soc_erdves_stebesena.csv
