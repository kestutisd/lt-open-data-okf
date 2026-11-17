---
type: Table
title: "Household2008 — Namų ūkio duomenys 2008m."
description: "Namų ūkio dydis, svoris įverčių skaičiavimui, vertinimo sritys (gyvenamoji vietovė, namų ūkio tipas, namų ūkio galvos socialinė-ekonominė grupė, amžius, išsilavinimas ir kt.)"
resource: "https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Household2008"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L263"
    last_modified: "2026-11-11T14:39:20Z"
---

# Household2008 — Namų ūkio duomenys 2008m.

Namų ūkio dydis, svoris įverčių skaičiavimui, vertinimo sritys (gyvenamoji vietovė, namų ūkio tipas, namų ūkio galvos socialinė-ekonominė grupė, amžius, išsilavinimas ir kt.)

- **Model:** `datasets/gov/lsd/namu_ukio_biudzetas/Household2008`[^manifest]
- **Dataset:** [datasets/gov/lsd/namu_ukio_biudzetas](../namu_ukio_biudzetas.md) (`datasets/gov/lsd/namu_ukio_biudzetas`)
- **Manifest CSV:** [datasets/gov/lsd/namu_ukio_biudzetas.csv#L263](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/namu_ukio_biudzetas.csv#L263)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/namu_ukio_biudzetas/Household2008`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `hh_ident` | `integer` | — | — | `open` | — | Namų ūkio ID | — |
| `month` | `integer` | — | — | `open` | — | Mėnuo | — |
| `hh_size` | `integer` | — | — | `open` | — | Namų ūkio dydis | — |
| `galut_sv` | `number` | — | — | `open` | — | Namų ūkio populiacijos svoris | — |
| `tipas` | `integer` | — | — | `open` | — | Namų ūkio tipas | — |
| `tipas2` | `integer` | — | — | `open` | — | Namų ūkiai su skirtingu vaikų skaičiumi | — |
| `tipas3` | `integer` | — | — | `open` | — | Namų ūkiai su vaikais ir be vaikų | — |
| `soc_ekon` | `integer` | — | — | `open` | — | Socialinė-ekonominė grupė, kuriai priklauso namų ūkio galva | — |
| `age_gr` | `integer` | — | — | `open` | — | Namų ūkio galvos amžius | — |
| `hh_educ2` | `integer` | — | — | `open` | — | Namų ūkio galvos išsilavinimas | — |
| `apskrit` | `integer` | — | — | `open` | — | Apskritis | — |
| `urb_rur` | `integer` | — | — | `open` | — | Miestas-Kaimas | — |
| `strata` | `integer` | — | — | `open` | — | Gyvenamoji vieta | — |
| `strata2` | `integer` | — | — | `open` | — | Gyvenamoji vieta2 | — |
| `dec_isl` | `integer` | — | — | `open` | — | Išlaidų decilinės grupės | — |
| `dec_urb` | `integer` | — | — | `open` | — | Miesto namų ūkių išlaidų decilinės grupės | — |
| `dec_rur` | `integer` | — | — | `open` | — | Kaimo namų ūkių išlaidų decilinės grupės | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `1` | — | — | Vienas gyvenantis asmuo | — |
| `tipas` | `2` | — | — | Vienas suaugęs asmuo su vaikais | — |
| `tipas` | `3` | — | — | Pora be vaikų | — |
| `tipas` | `4` | — | — | Pora su vaikais | — |
| `tipas` | `5` | — | — | Kiti namų ūkiai su vaikais | — |
| `tipas` | `6` | — | — | Kiti namų ūkiai be vaikų | — |
| `tipas2` | `1` | — | — | Namų ūkiai su 1 vaiku | — |
| `tipas2` | `2` | — | — | Namų ūkiai su 2 vaikais | — |
| `tipas2` | `3` | — | — | Namų ūkiai su 3 ir daugiau vaikų | — |
| `tipas2` | `4` | — | — | Namų ūkiai be vaikų | — |
| `tipas3` | `1` | — | — | Namų ūkiai su vaikais | — |
| `tipas3` | `2` | — | — | Namų ūkiai be vaikų | — |
| `soc_ekon` | `1` | — | — | Žemdirbiai | — |
| `soc_ekon` | `2` | — | — | Samdomieji darbuotojai | — |
| `soc_ekon` | `3` | — | — | Savarankiškai dirbantys asmenys | — |
| `soc_ekon` | `4` | — | — | Pensininkai | — |
| `soc_ekon` | `5` | — | — | Kiti | — |
| `age_gr` | `1` | — | — | iki 30 metų | — |
| `age_gr` | `2` | — | — | 30–39 metų | — |
| `age_gr` | `3` | — | — | 40–49 metų | — |
| `age_gr` | `4` | — | — | 50–59 metų | — |
| `age_gr` | `5` | — | — | 60 metų ir vyresni | — |
| `hh_educ2` | `1` | — | — | Pradinis, nebaigė pradinės mokyklos | — |
| `hh_educ2` | `2` | — | — | Pagrindinis | — |
| `hh_educ2` | `3` | — | — | Vidurinis | — |
| `hh_educ2` | `4` | — | — | Aukštesniojo ir aukštojo išsilavinimo nesuteikiantis povidurinis | — |
| `apskrit` | `1` | — | — | Alytaus | — |
| `apskrit` | `2` | — | — | Kauno | — |
| `apskrit` | `3` | — | — | Klaipėdos | — |
| `apskrit` | `4` | — | — | Marijampolės | — |
| `apskrit` | `5` | — | — | Panevėžio | — |
| `apskrit` | `6` | — | — | Šiaulių | — |
| `apskrit` | `7` | — | — | Tauragės | — |
| `apskrit` | `8` | — | — | Telšių | — |
| `apskrit` | `9` | — | — | Utenos | — |
| `apskrit` | `10` | — | — | Vilniaus | — |
| `urb_rur` | `1` | — | — | Miestas | — |
| `urb_rur` | `2` | — | — | Kaimas | — |
| `strata` | `1` | — | — | 5 Didieji miestai | — |
| `strata` | `2` | — | — | Kiti miestai | — |
| `strata` | `3` | — | — | Kaimas | — |
| `strata2` | `1` | — | — | Vilnius | — |
| `strata2` | `2` | — | — | Kaunas | — |
| `strata2` | `3` | — | — | Klaipėda | — |
| `strata2` | `4` | — | — | Šiauliai | — |
| `strata2` | `5` | — | — | Panevėžys | — |
| `strata2` | `6` | — | — | Kiti miestai | — |
| `strata2` | `7` | — | — | Kaimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/namu_ukio_biudzetas.csv
