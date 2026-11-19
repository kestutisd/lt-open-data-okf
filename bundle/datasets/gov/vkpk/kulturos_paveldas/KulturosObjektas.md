---
type: Table
title: "KulturosObjektas — Lietuvai reikšmingas kultūros paveldas, esantis užsienyje"
description: "Duomenų rinkinyje pateikiamas kultūros paveldo objekto pavadinimas, aprašymas, kategorijos, laikotarpis, metai, miestas, šalis, WGS koordinatės, autoriai, susiję asmenys ir interneto svetainės adresas (URL)."
resource: "https://get.data.gov.lt/datasets/gov/vkpk/kulturos_paveldas/KulturosObjektas"
tags: [gov, vkpk, kulturosobjektas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkpk/kulturos_objektai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vkpk/kulturos_objektai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3814/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vkpk/kulturos_paveldas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KulturosObjektas — Lietuvai reikšmingas kultūros paveldas, esantis užsienyje

Duomenų rinkinyje pateikiamas kultūros paveldo objekto pavadinimas, aprašymas, kategorijos, laikotarpis, metai, miestas, šalis, WGS koordinatės, autoriai, susiję asmenys ir interneto svetainės adresas (URL).[^manifest]

- **Model:** `datasets/gov/vkpk/kulturos_paveldas/KulturosObjektas`[^manifest]
- **Dataset:** [Lietuvai reikšmingas kultūros paveldas, esantis užsienyje](../kulturos_paveldas.md) (`datasets/gov/vkpk/kulturos_paveldas`)[^manifest]
- **Manifest CSV:** [datasets/gov/vkpk/kulturos_objektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkpk/kulturos_objektai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vkpk/kulturos_paveldas/KulturosObjektas` (`deployed`)[^manifest]
- **Provider:** `vkpk` — Valstybinė kultūros paveldo komisija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vkpk/kulturos_objektai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vkpk/kulturos_objektai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vkpk/kulturos_paveldas (https://data.gov.lt/datasets/3814/)
