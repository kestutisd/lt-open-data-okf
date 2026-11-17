---
type: Table
title: "KilnojamasTurtas — Duomenys apie įkeitimo ir hipotekos sandorių objektus – turtą (kilnojamieji daiktai ir t.t.)"
description: "Spinta table datasets/gov/rc/stsr/kilnojamas_turtas/KilnojamasTurtas (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/stsr/kilnojamas_turtas/KilnojamasTurtas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/stsr/kilnojamas_turtas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/kilnojamas_turtas.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# KilnojamasTurtas — Duomenys apie įkeitimo ir hipotekos sandorių objektus – turtą (kilnojamieji daiktai ir t.t.)

- **Model:** `datasets/gov/rc/stsr/kilnojamas_turtas/KilnojamasTurtas`[^manifest]
- **Dataset:** [STSR duomenys apie įkeitimo ir hipotekos sandorių objektus – turtą (kilnojamieji daiktai ir t.t.)](../kilnojamas_turtas.md) (`datasets/gov/rc/stsr/kilnojamas_turtas`)
- **Manifest CSV:** [datasets/gov/rc/stsr/kilnojamas_turtas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/kilnojamas_turtas.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/stsr/kilnojamas_turtas/KilnojamasTurtas`
- **Primary Key (`ref`):** `turtoid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `st_nr` | `integer` | — | `2` | `open` | — | Hipotekos / įkeitimo dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `turtoid` | `integer` | — | `4` | `open` | — | Turto identifikatorius dirbtinis šiame duomenų rinkinyje | — |
| `turto_rusis` | `string` | — | `3` | `open` | — | Turto rūšis | — |
| `st_tipas` | `string` | — | `2` | `open` | — | Hipotekos / įkeitimo tipas šiame duomenų rinkinyje | — |
| `st_ireg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / įkeitimo įregistravimo data (metai - ketvirtis) | — |
| `st_isreg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / įkeitimo išregistravimo data (metai - ketvirtis) | — |
| `iraso_priezastis` | `string` | — | `2` | `open` | — | Hipotekos / įkeitimo paskutinio įregistruoto įrašo tipas Sutarčių ir teisių suvaržymų registre | — |
| `sudarymo_vieta` | `string` | — | `3` | `open` | — | Hipotekos / įkeitimo sudarymo vieta (sav.; apskr.) | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Hipotekos / įkeitimo sudarymo vietos savivaldybės kodas iš Adresų registro (tik didmiesčių savivaldybės) | — |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../ar/apskritis/Apskritis.md) | `4` | `open` | — | Hipotekos / įkeitimo sudarymo vietos apskrities kodas iš Adresų registro | — |
| `pri_dydis_rez` | `string` | — | `3` | `open` | — | Prievolės rėžių dydžiai | — |
| `objektu_verte_rez` | `string` | — | `3` | `open` | — | Bendras įkeičiamų daiktų įkainojimas (rėžiai) | — |
| `pri_terminas_metai` | `date` | `Y` | `4` | `open` | — | Prievolės įvykdymo terminas (metai) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/stsr/kilnojamas_turtas.csv
