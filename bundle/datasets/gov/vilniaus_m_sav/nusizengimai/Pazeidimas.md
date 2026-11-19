---
type: Table
title: "Pazeidimas — Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste"
description: "Rinkinyje skelbiami Vilniaus mieste fiksuoti parkavimo bei kiti kelių eismo taisyklių pažeidimai iš Administracinių nusižengimų administracinio modulio."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/nusizengimai/Pazeidimas"
tags: [gov, vilniaus_m_sav, pazeidimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3874/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/nusizengimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pazeidimas — Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste

Rinkinyje skelbiami Vilniaus mieste fiksuoti parkavimo bei kiti kelių eismo taisyklių pažeidimai iš Administracinių nusižengimų administracinio modulio. Viena eilutė yra vienas nusižengimas. Duomenys skelbiami nuo 2018 m. Pateikiama informacija apie nusižengimą atlikusio asmens automobilį (valstybinio numerio žymėjimas, registracijos valstybė, elektromobilio ar automobilio nutempimo požymiai) ir pažeidimą (laikas, vietos koordinatės bei duomenys apie pažeistą teisės aktą). Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vilniaus_m_sav/nusizengimai/Pazeidimas`[^manifest]
- **Dataset:** [Parkavimo ir kelių eismo taisyklių pažeidimai Vilniaus mieste](../nusizengimai.md) (`datasets/gov/vilniaus_m_sav/nusizengimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/nusizengimai/Pazeidimas` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pazeidimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/nusizengimai.csv#L10)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/nusizengimai (https://data.gov.lt/datasets/3874/)
