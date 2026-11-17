---
type: Table
title: "ZalgirioKlinika — VU ligoninės „Žalgirio klinika“ pacientams atlikti radiologiniai tyrimai"
description: "Vilniaus universiteto ligoninės Žalgirio klinikos „MedDream“ IS kaupia duomenis apie pacientams vykdytus radiologinius tyrimus."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/ZalgirioKlinika"
tags: [gov, radiologija, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZalgirioKlinika — VU ligoninės „Žalgirio klinika“ pacientams atlikti radiologiniai tyrimai

Vilniaus universiteto ligoninės Žalgirio klinikos „MedDream“ IS kaupia duomenis apie pacientams vykdytus radiologinius tyrimus. Taikomas vienkartinis duomenų, kurie kaupiami nuo 2013 metų, teikimas. Duomenis papildomai numatoma atnaujinti priėmus sprendimą dėl informacinės sistemos jungimo prie VšĮ Vilniaus universiteto ligoninės Santaros klinikos ir pabaigus aktyviai eksploatuoti esamą sistemą. Duomenys apima pacientų informaciją: asmens kodus, gimimo metus bei lytį, tyrimų informaciją: modalumą, studijos ir serijos aprašymus, tirtą paciento kūno dalį, fotometrinę interpretaciją, paskyrusį gydytoją, atlikusį techniką, dozę decigrėjais kvadratiniame centimetre, apšvitą arksekundėmis.

- **Model:** `datasets/gov/radiologija/ZalgirioKlinika`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/ZalgirioKlinika`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Paciento asmens kodas | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `kuno_dalis` | `string` | — | `4` | `open` | — | Tirta kūno dalis | — |
| `tyrimo_modalumas` | `string` | — | `4` | `open` | — | Tyrimo modalumas | — |
| `tyrimo_studijos_aprasymas` | `string` | — | `4` | `open` | — | Tyrimo studijos aprašymas | — |
| `tyrimo_serijos_aprasymas` | `string` | — | `4` | `open` | — | Tyrimo serijos aprašymas | — |
| `atvaizdo_uuid` | `string` | — | `4` | `open` | — | Atvaizdo unikalus identifikatorius | — |
| `apsvita_as` | `number` | `″` | `4` | `open` | — | Apšvita arksekundėmis | — |
| `spinduliuote_dgy_cm2` | `number` | `dGy/cm^2` | `4` | `open` | — | Spinduliuotė decigrėjais kvadratiniame centimetre | — |
| `paskyres_gydytojas` | `string` | — | `4` | `open` | — | Tyrimą paskyręs gydytojas | — |
| `atlikes_technikas` | `string` | — | `4` | `open` | — | Tyrimą atlikęs technikas | — |
| `fotometrine_interpretacija` | `string` | — | `4` | `open` | — | Fotometrinė interpretacija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"vyras"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"moteris"` | `M` | — | Moteris | — |
| `paciento_lytis` | `"kita"` | `K` | — | Kita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv
