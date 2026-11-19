---
type: Table
title: "NaujosiosVilniosPoliklinika — Naujosios Vilnios poliklinikos pacientams atlikti radiologiniai tyrimai"
description: "Informacinėje sistemoje „MedDream“ nuo 2013 metų kaupiami Naujosios Vilnios poliklinikos pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/NaujosiosVilniosPoliklinika"
tags: [gov, radiologija, naujosiosvilniospoliklinika, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L117"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L117"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# NaujosiosVilniosPoliklinika — Naujosios Vilnios poliklinikos pacientams atlikti radiologiniai tyrimai

Informacinėje sistemoje „MedDream“ nuo 2013 metų kaupiami Naujosios Vilnios poliklinikos pacientams atliktų radiologinių tyrimų duomenys. Duomenų rinkinyje pateikiami nuo 2016 metų birželio mėn. kaupiami ir iki šiol atnaujinami duomenys. Vienas įrašas atitinka vieną tyrimo medicininį atvaizdą (visų tyrimo atvaizdų identifikatoriai unikalūs). Duomenų rinkinį sudaro: paciento pseudonimizuotas asmens kodas, tyrimo studijos identifikatorius, data, paciento gimimo metai, lytis, tyrimo serijos identifikatorius, tirta kūno dalis, serijos modalumas, aprašymas, tyrimo atvaizdo identifikatorius, apšvita, spinduliuotės dozė ir fotometrinė interpretacija. Duomenų teikėjas – VšĮ Naujosios Vilnios poliklinika. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/radiologija/NaujosiosVilniosPoliklinika`[^manifest]
- **Dataset:** [Pacientams atlikti radiologiniai tyrimai](../radiologija.md) (`datasets/gov/radiologija`)[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L117](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L117)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/NaujosiosVilniosPoliklinika` (`deployed`)[^manifest]
- **Provider:** `radiologija`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-26`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_asm_k` | `string` | — | `4` | `open` | — | Pseudonimizuotas paciento asmens kodas | — |
| `tyrimo_studijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo studijos identifikatorius | — |
| `tyrimo_studijos_data` | `date` | `D` | `4` | `open` | — | Tyrimo studijos data | — |
| `paciento_gimimo_metai` | `date` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `tyrimo_serijos_uuid` | `string` | — | `4` | `open` | — | Tyrimo serijos identifikatorius | — |
| `tirta_kuno_dalis` | `string` | — | `4` | `open` | — | Tirta paciento kūno dalis | — |
| `tyrimo_serijos_modalumas` | `string` | — | `4` | `open` | — | Tyrimo serijos modalumas | — |
| `tyrimo_serijos_aprasymas` | `string` | — | `4` | `open` | — | Tyrimo serijos aprašymas | — |
| `atvaizdo_uuid` | `string` | — | `4` | `open` | — | Atvaizdo unikalus identifikatorius | — |
| `apsvita` | `number` | `″` | `4` | `open` | — | Apšvita arksekundėmis | — |
| `doze` | `number` | `dGy/cm^2` | `4` | `open` | — | Spinduliuotės dozė decigrėjais kvadratiniame centimetre | — |
| `fotometrine_interpretacija` | `string` | — | `4` | `open` | — | Fotometrinė interpretacija | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"M"` | — | — | Moteris | — |
| `paciento_lytis` | `"K"` | — | — | Kita | — |
| `paciento_lytis` | `"V"` | — | — | Vyras | — |
| `tyrimo_serijos_modalumas` | `"DX"` | — | — | Skaitmeninė radiografija | — |
| `tyrimo_serijos_modalumas` | `"PX"` | — | — | Panoraminis rentgenas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L117 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L117)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)
