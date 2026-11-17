---
type: Table
title: "VidDarboUzmokestis"
description: "Spinta table datasets/gov/urm/vmdu/VidDarboUzmokestis (25 columns)."
tags: [gov, urm, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/urm/vmdu.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vmdu.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# VidDarboUzmokestis

- **Model:** `datasets/gov/urm/vmdu/VidDarboUzmokestis`[^manifest]
- **Dataset:** [Vidutinio mėnesio darbo užmokesčio duomenys](../vmdu.md) (`datasets/gov/urm/vmdu`)
- **Manifest CSV:** [datasets/gov/urm/vmdu.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/urm/vmdu.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `pareigybes_pavadinimas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pareigybes_pavadinimas` | `string` | — | `3` | `open` | — | Pareigybės pavadinimas | — |
| `darb_sk_sausis_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. sausio) | — |
| `vid_du_sausis_2021` | `integer` | — | `2` | `open` | — | 2021 m. sausio vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_vasaris_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m.vasario) | — |
| `vid_du_vasaris_2021` | `integer` | — | `2` | `open` | — | 2021 m. vasario vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_kovas_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. kovo) | — |
| `vid_du_kovas_2021` | `integer` | — | `2` | `open` | — | 2021 m. kovo vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_balandis_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. balandžio) | — |
| `vid_du_balandis_2021` | `integer` | — | `2` | `open` | — | 2021 m. balandžio vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_geguze_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. gegužės) | — |
| `vid_du_geguze_2021` | `integer` | — | `2` | `open` | — | 2021 m. gegužės vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_birzelis_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. birželio) | — |
| `vid_du_birzelis_2021` | `integer` | — | `2` | `open` | — | 2021 m. birželio vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_liepa_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. liepos) | — |
| `vid_du_liepa_2021` | `integer` | — | `2` | `open` | — | 2021 m. liepos vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_rugpjutis_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. rugpjūčio) | — |
| `vid_du_rugpjutis_2021` | `integer` | — | `2` | `open` | — | 2021 m. rugpjūčio vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_rugsejis_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. rugsėjo) | — |
| `vid_du_rugsejis_2021` | `integer` | — | `2` | `open` | — | 2021 m. rugsėjo vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_spalis_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. spalis) | — |
| `vid_du_spalis_2021` | `integer` | — | `2` | `open` | — | 2021 m. spalio vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_lapkritis_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. lapkričio) | — |
| `vid_du_lapkritis_2021` | `integer` | — | `2` | `open` | — | 2021m. lapkričio vidutinis apskaičiuotas darbo užmokestis (EUR) | — |
| `darb_sk_gruodis_2021` | `integer` | — | `4` | `open` | — | Darbuotojų skaičius (2021 m. gruodžio) | — |
| `vid_du_gruodis_2021` | `integer` | — | `2` | `open` | — | 2021 m. gruodžio vidutinis apskaičiuotas darbo užmokestis (EUR) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vid_du_sausis_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_vasaris_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_kovas_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_balandis_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_geguze_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_birzelis_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_liepa_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_rugpjutis_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_rugsejis_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_spalis_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_lapkritis_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `vid_du_gruodis_2021` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/urm/vmdu.csv
