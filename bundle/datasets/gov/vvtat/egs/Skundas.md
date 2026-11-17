---
type: Table
title: "Skundas — VVTAT elektroninėje ginčų platformoje gauti skundai"
description: "Rinkinyje pateikiami Valstybinės vartotojų teisių apsaugos tarnyboje gautų skundų iš Elektroninės ginčų sprendimų platformos (EGS) sistemos duomenys nuo 2015m. iki šių dienų."
resource: "https://get.data.gov.lt/datasets/gov/vvtat/egs/Skundas"
tags: [gov, vvtat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvtat/egs.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/egs.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Skundas — VVTAT elektroninėje ginčų platformoje gauti skundai

Rinkinyje pateikiami Valstybinės vartotojų teisių apsaugos tarnyboje gautų skundų iš Elektroninės ginčų sprendimų platformos (EGS) sistemos duomenys nuo 2015m. iki šių dienų. Elektroninė ginčo sprendimo platforma buvo įkurta Europos Komisijos, siekiant užtikrinti lengvesnį ir greitesnį ginčų sprendimą. Platforma leidžia vartotojams patogiai pradėti neteisminio ginčo sprendimo procedūrą internetu. Vartotojas, įsigijęs prekes ar paslaugas internetu Lietuvoje, kitose ES šalyse, Islandijoje, Lichtenšteine ar Norvegijoje, dėl savo pažeistų teisių gynimo turi galimybę teikti skundus per šią platformą. Skundus gavusios įmonės nėra įpareigotos atsakyti į vartotojo kreipimus. Ateityje numatyta, jog EGS sistema bus likviduojama, tad skundų duomenys taps archyviniai.

- **Model:** `datasets/gov/vvtat/egs/Skundas`[^manifest]
- **Dataset:** [Elektroninėje ginčų platformoje gauti skundai](../egs.md) (`datasets/gov/vvtat/egs`)
- **Manifest CSV:** [datasets/gov/vvtat/egs.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvtat/egs.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvtat/egs/Skundas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros unikalus įrašo identifikatorius | — |
| `skundo_tipas` | `string` | — | `4` | `open` | — | Pateikto skundo tipas | — |
| `reikalavimas` | `string` | — | `4` | `open` | — | Vartotojo reikalavimas skunde | — |
| `isigijimas` | `date` | `D` | `4` | `open` | — | Prekės/paslaugos įsigijimo data | — |
| `skundas_pastu` | `date` | `D` | `4` | `open` | — | Skundo, siųsto paštu, gavimo data | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Skundo registracijos data | — |
| `institucija` | `string` | — | `4` | `open` | — | Skundą nagrinėjusi institucija | — |
| `isigyta_internetu` | `boolean` | — | `4` | `open` | — | Požymis, ar prekė/paslauga buvo įsigyta internetu | — |
| `atsiskaitymas` | `string` | — | `4` | `open` | — | Atsiskaitymo už įsigytą prekę ar paslaugą būdas | — |
| `vartotojo_salis` | `string` | — | `4` | `open` | — | Vartotojo kilmės šalis | — |
| `apskritis` | `string` | — | `4` | `open` | — | Vartotojo gyvenamosios vietos apskritis | — |
| `vieta` | `string` | — | `4` | `open` | — | Prekės/paslaugos įsigijimo vieta | — |
| `jar_kodas` | `string` | — | `2` | `open` | — | Prekės/paslaugos pardavėjo juridinio asmens kodas | — |
| `teikejas` | `string` | — | `1` | `open` | — | Prekės/paslaugos pardavėjas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `skundo_tipas` | `"update(property: ""skundo_tipas[]"", type: ""array"", source: ""Skundo_tipas"")"` | `property` | `4` | — | — | — | — |
| `reikalavimas` | `"update(property: ""reikalavimas[]"", type: ""array"", source: ""Reikalavimas"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvtat/egs.csv
