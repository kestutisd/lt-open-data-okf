---
type: Table
title: "KulturosObjektas — Lietuvai reikšmingas kultūros paveldas, esantis užsienyje"
description: "Duomenų rinkinyje pateikiamas kultūros paveldo objekto pavadinimas, aprašymas, kategorijos, laikotarpis, metai, miestas, šalis, WGS koordinatės, autoriai, susiję asmenys ir interneto svetainės adresas (URL)."
resource: "https://get.data.gov.lt/datasets/gov/vkpk/kulturos_paveldas/KulturosObjektas"
tags: [gov, vkpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vkpk/kulturos_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkpk/kulturos_objektai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# KulturosObjektas — Lietuvai reikšmingas kultūros paveldas, esantis užsienyje

Duomenų rinkinyje pateikiamas kultūros paveldo objekto pavadinimas, aprašymas, kategorijos, laikotarpis, metai, miestas, šalis, WGS koordinatės, autoriai, susiję asmenys ir interneto svetainės adresas (URL).

- **Model:** `datasets/gov/vkpk/kulturos_paveldas/KulturosObjektas`[^manifest]
- **Dataset:** [Lietuvai reikšmingas kultūros paveldas, esantis užsienyje](../kulturos_paveldas.md) (`datasets/gov/vkpk/kulturos_paveldas`)
- **Manifest CSV:** [datasets/gov/vkpk/kulturos_objektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkpk/kulturos_objektai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkpk/kulturos_paveldas/KulturosObjektas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įrašo identifikatorius | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Paveldo objekto pavadinimas | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Išsamus objekto aprašymas | — |
| `kategorija` | `string` | — | `4` | `open` | — | Objekto kategorija | — |
| `laikotarpis` | `string` | — | `4` | `open` | — | Istorinis laikotarpis | — |
| `metai` | `string` | — | `4` | `open` | — | Statybiniai metai | — |
| `miestas` | `string` | — | `4` | `open` | — | Miestas | — |
| `salis` | `string` | — | `4` | `open` | — | Šalis | — |
| `lat_wgs` | `number` | — | `4` | `open` | — | Geografinė platuma (WGS84) | — |
| `lng_wgs` | `number` | — | `4` | `open` | — | Geografinė ilguma (WGS84) | — |
| `autoriai` | `string` | — | `4` | `open` | — | Autorių informacija | — |
| `susijusios_asmenybes` | `string` | — | `4` | `open` | — | Susijusių asmenybių informacija | — |
| `url` | `string` | — | `4` | `open` | — | Išorinis URL nuoroda | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vkpk/kulturos_objektai.csv
