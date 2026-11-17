---
type: Table
title: "Pazeidimas — Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste"
description: "Rinkinyje skelbiami Vilniaus mieste fiksuoti parkavimo bei kiti kelių eismo taisyklių pažeidimai iš Administracinių nusižengimų administracinio modulio."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/nusizengimai/Pazeidimas"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/nusizengimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pazeidimas — Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste

Rinkinyje skelbiami Vilniaus mieste fiksuoti parkavimo bei kiti kelių eismo taisyklių pažeidimai iš Administracinių nusižengimų administracinio modulio. Viena eilutė yra vienas nusižengimas. Duomenys skelbiami nuo 2018 m. Pateikiama informacija apie nusižengimą atlikusio asmens automobilį (valstybinio numerio žymėjimas, registracijos valstybė, elektromobilio ar automobilio nutempimo požymiai) ir pažeidimą (laikas, vietos koordinatės bei duomenys apie pažeistą teisės aktą).

Duomenų teikėjas – Vilniaus miesto savivaldybės administracija.

- **Model:** `datasets/gov/vilniaus_m_sav/nusizengimai/Pazeidimas`[^manifest]
- **Dataset:** [Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste](../nusizengimai.md) (`datasets/gov/vilniaus_m_sav/nusizengimai`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/nusizengimai/Pazeidimas`
- **Primary Key (`ref`):** `pazeidimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pazeidimo_id` | `string` | — | `4` | `open` | — | Pažeidimo identifikacinis numeris | — |
| `laikas` | `datetime` | `S` | `4` | `open` | — | Pažeidimo užfiksavimo laiko žyma | — |
| `ar_elektromobilis` | `boolean` | — | `4` | `open` | — | Požymis, ar automobilis yra varomas elektriniu varikliu | — |
| `valst_nr_zym` | `string` | — | `4` | `open` | — | Transporto priemonės valstybinio numerio žymėjimas nurodant raidžių ir skaitmenų pozicijas | — |
| `kilmes_valst` | `string` | — | `4` | `open` | — | Transporto priemonės registracijos valstybė | — |
| `ar_nutempta` | `boolean` | — | `4` | `open` | — | Požymis, ar transporto priemonė po pažeidimo buvo nutempta | — |
| `geometrija_adp` | `geometry(4326)` | — | `4` | `open` | — | Pažeidimo vietos koordinatės (WGS) | — |
| `pazeidimas` | `string` | — | `4` | `open` | — | Administracinis pažeidimas | — |
| `aplinkybes` | `string` | — | `4` | `open` | — | Pažeidimo aplinkybės | — |
| `pazeistas_aktas` | `string` | — | `4` | `open` | — | Pažeistas teisės aktas | — |
| `akto_str` | `string` | — | `4` | `open` | — | Pažeisto teisės akto straipsnio numeris | — |
| `ank_nusizengimas` | `string` | — | `4` | `open` | — | Konstatuotas administracinis nusižengimas pagal Administracinių nusižengimų kodeksą (ANK) | — |
| `straipsnis` | `string` | — | `4` | `open` | — | Administracinių nusižengimų kodekso straipsnis | — |
| `dalis` | `string` | — | `4` | `open` | — | Administracinių nusižengimų kodekso straipsnio dalis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pazeistas_aktas` | `"Lietuvos Respublikos Vyriausybės,Kelių eismo taisyklių,2002-12-11,SAVAD,1950"` | — | — | — | — |
| `pazeistas_aktas` | `"Vilniaus miesto savivaldybės tarybos,Vietinės rinkliavos už naudojimąsi Tarybos nustatytomis mokamomis vietomis automobiliams statyti nuostatų,SAVAD,1-127,2011-07-13"` | — | — | — | — |
| `pazeistas_aktas` | `"Lietuvos Respublikos Saugaus eismo automobilių keliais įstatymo,SAVAD"` | — | — | — | — |
| `pazeistas_aktas` | `"Lietuvos Respublikos saugaus eismo automobilių keliais įstatymo,SAVAD"` | — | — | — | — |
| `straipsnis` | `"414"` | — | — | — | — |
| `straipsnis` | `"417"` | — | — | — | — |
| `straipsnis` | `"418"` | — | — | — | — |
| `straipsnis` | `"431"` | — | — | — | — |
| `dalis` | `"1"` | — | — | — | — |
| `dalis` | `"2"` | — | — | — | — |
| `dalis` | `"2(1)"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/nusizengimai.csv
