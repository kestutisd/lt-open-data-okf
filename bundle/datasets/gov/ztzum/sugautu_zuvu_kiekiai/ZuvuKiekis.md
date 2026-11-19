---
type: Table
title: "ZuvuKiekis — Informacija apie sugautų žuvų kiekius"
description: "Lentelėje pateikta informacija apie sugautų žuvų kiekius iš Žuvininkystės tarnybos prie Lietuvos Respublikos žemės ūkio ministerijos Žuvininkystės duomenų informacinės sistemos (ŽDIS)."
resource: "https://get.data.gov.lt/datasets/gov/ztzum/sugautu_zuvu_kiekiai/ZuvuKiekis"
tags: [gov, ztzum, zuvukiekis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ztzum/sugautu_zuvu_kiekiai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/ztzum/sugautu_zuvu_kiekiai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2877/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ztzum/sugautu_zuvu_kiekiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ZuvuKiekis — Informacija apie sugautų žuvų kiekius

Lentelėje pateikta informacija apie sugautų žuvų kiekius iš Žuvininkystės tarnybos prie Lietuvos Respublikos žemės ūkio ministerijos Žuvininkystės duomenų informacinės sistemos (ŽDIS). Pateikti duomenys nuo jų rinkimo sistemoje pradžios (2015 metų) atnaujinant kas pusę metų. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/ztzum/sugautu_zuvu_kiekiai/ZuvuKiekis`[^manifest]
- **Dataset:** [Informacija apie sugautų žuvų kiekius](../sugautu_zuvu_kiekiai.md) (`datasets/gov/ztzum/sugautu_zuvu_kiekiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/ztzum/sugautu_zuvu_kiekiai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ztzum/sugautu_zuvu_kiekiai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ztzum/sugautu_zuvu_kiekiai/ZuvuKiekis` (`deployed`)[^manifest]
- **Provider:** `ztzum` — Žuvininkystės tarnyba prie LR žemės ūkio ministerijos *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `sugauta_kiekis` | `integer` | — | `4` | `open` | — | Sugautų žuvų kiekis | — |
| `matavimo_vnt` | `string` | — | `4` | `open` | — | Sugautų žuvų kiekio matavimo vienetas | — |
| `zuvies_pav` | `string` | — | `4` | `open` | — | Žuvies pavadinimas | — |
| `zuvies_komercinis_pav` | `string` | — | `4` | `open` | — | Žuvies komercinis pavadinimas | — |
| `zuvies_pav_en` | `string` | — | `4` | `open` | — | Žuvies pavadinimas anglų kalba | — |
| `zuvies_mokslinis_pav` | `string` | — | `4` | `open` | — | Mokslinis žuvies pavadinimas | — |
| `seima` | `string` | — | `4` | `open` | — | Šeima | — |
| `zvejybos_pastangos_id` | `string` | — | `4` | `open` | — | Žvejybos pastangos identifikacinis numeris | — |
| `zvejybos_pastangos_pradzia` | `datetime` | `S` | `4` | `open` | — | Žvejybos pastangos pradžios data ir laikas | — |
| `zvejybos_pastangos_pabaiga` | `datetime` | `S` | `4` | `open` | — | Žvejybos pastangos pabaigos data ir laikas | — |
| `pastangos_trukme_val` | `integer` | — | `4` | `open` | — | Žvejybos pastangos trukmė (val.) | — |
| `ekonomines_zonos_kodas` | `string` | — | `4` | `open` | — | Ekonominės zonos kodas | — |
| `ekonomines_zonos_pav` | `string` | — | `4` | `open` | — | Ekonominės zonos pavadinimas | — |
| `fao_zonos_kodas` | `string` | — | `4` | `open` | — | FAO ("Food and Agriculture Organization") zonos kodas | — |
| `fao_zonos_pav` | `string` | — | `4` | `open` | — | FAO ("Food and Agriculture Organization") zonos pavadinimas | — |
| `laivo_registracijos_numeris` | `string` | — | `4` | `open` | — | Laivo registracijos numeris (šifruotas) | — |
| `kapitono_id` | `string` | — | `4` | `open` | — | Kapitono identifikacinis numeris (šifruotas) | — |
| `zvejybos_irankio_pav` | `string` | — | `4` | `open` | — | Žvejybos įrankio pavadinimas | — |
| `zvejybos_irankio_ilgis` | `number` | `m` | `4` | `open` | — | Žvejybos įrankio ilgis (metrais, m) | — |
| `zvejybos_irankio_tankumas` | `number` | `mm` | `4` | `open` | — | Žvejybos įrankio tankumas (milimetrais, mm) | — |
| `gylis` | `number` | `m` | `4` | `open` | — | Gylis (metrais, m), kuriame sugautos žuvys | — |
| `laivo_isvykimo_data_laikas` | `datetime` | `S` | `4` | `open` | — | Laivo išvykimo iš uosto data ir laikas | — |
| `laivo_isvykimo_uosto_pav` | `string` | — | `4` | `open` | — | Uosto, iš kurio išplaukė laivas, pavadinimas su šalies FAO kodu | — |
| `laivo_isvykimo_uosto_salis` | `string` | — | `4` | `open` | — | Uosto, iš kurio išplaukė laivas, šalis | — |
| `ar_isvykimo_uostas_eu` | `boolean` | — | `4` | `open` | — | Požymis, ar uostas, iš kurio išplaukė laivas, yra Europos Sąjungoje ("true" - taip, "false" - ne) | — |
| `laivo_grizimo_data_laikas` | `datetime` | `S` | `4` | `open` | — | Laivo grįžimo į uostą data ir laikas | — |
| `laivo_grizimo_uosto_pavadinimas` | `string` | — | `4` | `open` | — | Uosto, į kurį sugrįžo laivas, pavadinimas su šalies FAO kodu | — |
| `laivo_grizimo_uosto_salis` | `string` | — | `4` | `open` | — | Uosto, į kurį sugrįžo laivas, šalis | — |
| `ar_grizimo_uostas_eu` | `boolean` | — | `4` | `open` | — | Požymis, ar uostas, į kurį sugrįžo laivas, yra Europos Sąjungoje ("true" - taip, "false" - ne) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ztzum/sugautu_zuvu_kiekiai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ztzum/sugautu_zuvu_kiekiai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ztzum/sugautu_zuvu_kiekiai (https://data.gov.lt/datasets/2877/)
