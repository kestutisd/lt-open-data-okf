---
type: Table
title: "Kaina — Ugdymo įstaigų maitinimo sutartyse nurodytų patiekalų kainoraštis"
description: "Pateikiami ugdymo įstaigų maitinimo sutarčių kainos ir kiti maitinimo požymiai, dirbtinio intelekto (DI) modelio pagalba surinktos iš sutarčių tekstų"
resource: "https://get.data.gov.lt/datasets/gov/lsd/vpt/maitinimo_sutartys/Kaina"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/vpt/maitinimo_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L46"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kaina — Ugdymo įstaigų maitinimo sutartyse nurodytų patiekalų kainoraštis

Pateikiami ugdymo įstaigų maitinimo sutarčių kainos ir kiti maitinimo požymiai, dirbtinio intelekto (DI) modelio pagalba surinktos iš sutarčių tekstų

- **Model:** `datasets/gov/lsd/vpt/maitinimo_sutartys/Kaina`[^manifest]
- **Dataset:** [Ugdymo įstaigų maitinimo sutarčių duomenys](../maitinimo_sutartys.md) (`datasets/gov/lsd/vpt/maitinimo_sutartys`)
- **Manifest CSV:** [datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L46](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/vpt/maitinimo_sutartys.csv#L46)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/vpt/maitinimo_sutartys/Kaina`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris (jungiasi su Sutartis) | — |
| `mokykla` | `string` | — | `4` | `open` | — | Mokyklos pavadinimas | — |
| `mokyklos_jar` | `string` | — | `4` | `open` | — | Mokyklos juridinio asmens kodas | — |
| `mokyklos_ireg_data` | `date` | `D` | `4` | `open` | — | Mokyklos įregistravimo data | — |
| `ar_padalinys` | `boolean` | — | `4` | `open` | — | Požymis, ar mokykla yra padalinys | — |
| `mokyklos_tipas` | `string` | — | `4` | `open` | — | Mokyklos tipas | — |
| `paskirciu_grupe` | `string` | — | `4` | `open` | — | Mokyklos paskirties grupė | — |
| `vietoves_tipas` | `string` | — | `4` | `open` | — | Mokyklos vietovės tipas | — |
| `adresas` | `string` | — | `4` | `open` | — | Mokyklos adresas | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Mokyklos savivaldybės kodas | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Mokyklos savivaldybės pavadinimas | — |
| `mokyklos_geometrija` | `geometry(3346)` | — | `4` | `open` | — | Mokyklos koordinatės (LKS) | — |
| `viso_mokiniu` | `integer` | `U` | `4` | `open` | — | Ugdymo įstaigoje besimokančių mokinių skaičius duomenų atnaujinimo dieną | — |
| `mok_duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Mokinių skaičiaus duomenų atnaujinimo data | — |
| `sutarties_nr` | `string` | — | `4` | `open` | — | Mokyklos maitinimo sutarties numeris | — |
| `sutarties_data` | `date` | `D` | `4` | `open` | — | Maitinimo sutarties pasirašymo data | — |
| `sutarties_verte_eur` | `number` | — | `4` | `open` | — | DI modelio identifikuota maitinimo sutarties vertė | — |
| `ar_ekologiskas` | `boolean` | — | `4` | `open` | — | DI modelio identifikuotas požymis, nurodantis, ar mokykloje organizuojamas ekologiškas maitinimas | — |
| `ar_savitarna` | `boolean` | — | `4` | `open` | — | DI modelio identifikuotas požymis, nurodantis, ar maitinimas mokykloje organizuojamas savitarnos (švediško stalo) principu | — |
| `ar_emuas` | `boolean` | — | `4` | `open` | — | DI modelio identifikuotas požymis, nurodantis, ar maitinimą galima užsisakyti ir už jį atsiskaityti per elektroninę maitinimo užsakymų ir atsiskaitymų sistemą (EMUAS) | — |
| `patiekalas` | `string` | — | `4` | `open` | — | Maitinimui tiekiamo patiekalo pavadinimas | — |
| `maitinimo_laikas` | `string` | — | `4` | `open` | — | DI modelio identifikuotas patiekalo tiekimo laikas (pusryčiai, pietūs, vakarienė, kt.) | — |
| `amzius` | `string` | — | `4` | `open` | — | DI modelio identifikuota mokinių amžiaus grupė, kuriai skirtas nurodytas patiekalas | — |
| `kaina_eur` | `number` | — | `4` | `open` | — | DI modelio identifikuota patiekalo porcijos kaina, nurodyta eurais | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mokyklos_tipas` | `"Gimnazija"` | — | — | — | — |
| `mokyklos_tipas` | `"Progimnazija"` | — | — | — | — |
| `mokyklos_tipas` | `"Pagrindinė mokykla"` | — | — | — | — |
| `mokyklos_tipas` | `"Pradinė mokykla"` | — | — | — | — |
| `mokyklos_tipas` | `"Ikimokyklinio ugdymo mokykla"` | — | — | — | — |
| `vietoves_tipas` | `"Miestas"` | — | — | — | — |
| `vietoves_tipas` | `"Kaimas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/vpt/maitinimo_sutartys.csv
