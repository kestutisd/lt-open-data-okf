---
type: Table
title: "NekilnojamasTurtas — Duomenys apie įkeitimo ir hipotekos sandorių objektus (turtą) - nekilnojamuosius daiktus"
description: "Spinta table datasets/gov/rc/stsr/nekilnojamas_turtas/NekilnojamasTurtas (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/stsr/nekilnojamas_turtas/NekilnojamasTurtas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/stsr/nekilnojamas_turtas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/nekilnojamas_turtas.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# NekilnojamasTurtas — Duomenys apie įkeitimo ir hipotekos sandorių objektus (turtą) - nekilnojamuosius daiktus

- **Model:** `datasets/gov/rc/stsr/nekilnojamas_turtas/NekilnojamasTurtas`[^manifest]
- **Dataset:** [STSR duomenys apie įkeitimo ir hipotekos sandorių objektus (turtą) - nekilnojamuosius daiktus](../nekilnojamas_turtas.md) (`datasets/gov/rc/stsr/nekilnojamas_turtas`)
- **Manifest CSV:** [datasets/gov/rc/stsr/nekilnojamas_turtas.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/stsr/nekilnojamas_turtas.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/stsr/nekilnojamas_turtas/NekilnojamasTurtas`
- **Primary Key (`ref`):** `turtoid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `st_nr` | `integer` | — | `2` | `open` | — | Hipotekos / Įkeitimo dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `turtoid` | `integer` | — | `4` | `open` | — | Turto dirbtinis identifikatorius šiame duomenų rinkinyje | — |
| `objekto_tipas` | `ref` | [/datasets/gov/rc/ntr/ntr_objektai/NtrObjektoTipas](../../ntr/ntr_objektai/NtrObjektoTipas.md) | `4` | `open` | — | Nekilnojamojo turto objekto tipas Nekilnojamojo turto registre | — |
| `ntr_paskirties_tipas` | `ref` | [/datasets/gov/rc/ntr/ntr_paskirtys/NtrPaskirtiesTipas](../../ntr/ntr_paskirtys/NtrPaskirtiesTipas.md) | `4` | `open` | — | Nekilnojamojo turto objekto paskirties tipas Nekilnojamojo turto registre | — |
| `nt_sav_aps_pav` | `string` | — | `3` | `open` | — | Turto buvimo vietos savivaldybės / apskrities pavadinimas | — |
| `turto_savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Turto buvimo vietos savivaldybės kodas iš Adresų registro (Tik didmiesčių savivaldybės) | — |
| `turto_apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../ar/apskritis/Apskritis.md) | `4` | `open` | — | Turto buvimo vietos apskrities kodas iš Adresų registro | — |
| `st_tipas` | `string` | — | `2` | `open` | — | Hipotekos / Įkeitimo tipas šiame duomenų rinkinyje | — |
| `st_ireg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / Įkeitimo įregistravimo data (metai - ketvirtis) | — |
| `st_isreg_ketv` | `date` | `Q` | `4` | `open` | — | Hipotekos / Įkeitimo išregistravimo data (metai - ketvirtis) | — |
| `iraso_priezastis` | `string` | — | `2` | `open` | — | Hipotekos / Įkeitimo paskutinio įregistruoto įrašo tipas Sutarčių ir teisių suvaržymų registre | — |
| `sudarymo_vieta` | `string` | — | `3` | `open` | — | Hipotekos / Įkeitimo sudarymo vieta (sav.; apskr.) | — |
| `hipotekos_savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Hipotekos / Įkeitimo sudarymo vietos savivaldybės kodas iš Adresų registro (tik didmiesčių savivaldybės) | — |
| `hipotekos_apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../ar/apskritis/Apskritis.md) | `4` | `open` | — | Hipotekos / Įkeitimo sudarymo vietos apskrities kodas iš Adresų registro | — |
| `pri_dydis_rez` | `string` | — | `3` | `open` | — | Prievolės rėžių dydžiai | — |
| `objektu_verte_rez` | `string` | — | `3` | `open` | — | Bendras įkeičiamų daiktų įkainojimas (rėžiai) | — |
| `pri_terminas_metai` | `date` | `Y` | `4` | `open` | — | Prievolės įvykdymo terminas (metai) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/stsr/nekilnojamas_turtas.csv
