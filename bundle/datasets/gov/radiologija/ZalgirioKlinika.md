---
type: Table
title: "ZalgirioKlinika — VU ligoninės „Žalgirio klinika“ pacientams atlikti radiologiniai tyrimai"
description: "Vilniaus universiteto ligoninės Žalgirio klinikos „MedDream“ IS kaupia duomenis apie pacientams vykdytus radiologinius tyrimus."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/ZalgirioKlinika"
tags: [gov, radiologija, zalgirioklinika, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# ZalgirioKlinika — VU ligoninės „Žalgirio klinika“ pacientams atlikti radiologiniai tyrimai

Vilniaus universiteto ligoninės Žalgirio klinikos „MedDream“ IS kaupia duomenis apie pacientams vykdytus radiologinius tyrimus. Taikomas vienkartinis duomenų, kurie kaupiami nuo 2013 metų, teikimas. Duomenis papildomai numatoma atnaujinti priėmus sprendimą dėl informacinės sistemos jungimo prie VšĮ Vilniaus universiteto ligoninės Santaros klinikos ir pabaigus aktyviai eksploatuoti esamą sistemą. Duomenys apima pacientų informaciją: asmens kodus, gimimo metus bei lytį, tyrimų informaciją: modalumą, studijos ir serijos aprašymus, tirtą paciento kūno dalį, fotometrinę interpretaciją, paskyrusį gydytoją, atlikusį techniką, dozę decigrėjais kvadratiniame centimetre, apšvitą arksekundėmis.[^manifest]

- **Model:** `datasets/gov/radiologija/ZalgirioKlinika`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/ZalgirioKlinika` (`deployed`)[^manifest]
- **Provider:** `radiologija`[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-26`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"vyras"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"moteris"` | `M` | — | Moteris | — |
| `paciento_lytis` | `"kita"` | `K` | — | Kita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)
