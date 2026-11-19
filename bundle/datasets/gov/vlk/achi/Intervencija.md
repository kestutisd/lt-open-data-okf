---
type: Table
title: "Intervencija — Medicininių intervencijų sąrašas"
description: "Informacija apie medicinines intervencijas."
resource: "https://get.data.gov.lt/datasets/gov/vlk/achi/Intervencija"
tags: [gov, vlk, intervencija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/vlk/achi.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1383/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/achi"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Intervencija — Medicininių intervencijų sąrašas

Informacija apie medicinines intervencijas. ACHI – tai Australijos medicininių intervencijų klasifikacija. Jos devintasis leidimas pakeičia aštuntąjį, išleistą 2013 metais.[^manifest]

- **Model:** `datasets/gov/vlk/achi/Intervencija`[^manifest]
- **Dataset:** [Medicininių intervencijų sąrašas (ACHI)](../achi.md) (`datasets/gov/vlk/achi`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/achi.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/achi/Intervencija` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `achi_kodas` | `string` | — | `4` | `open` | — | ACHI kodas | Procedūros (ACHI) kodas pagal Australijos medicininių intervencijų klasifikaciją |
| `achi_pavadinimas` | `string` | — | `4` | `open` | — | ACHI pavadinimas | Procedūros (ACHI) pavadinimas pagal Australijos medicininių intervencijų klasifikaciją |
| `bloko_nr` | `integer` | — | `2` | `open` | — | Bloko numeris | Bloko, kurį sudaro susijusios pagal tam tikrus požymius (anatominę sritį ir procedūros tipą) procedūros, numeris |
| `bloko_pavadinimas` | `string` | — | `2` | `open` | — | Bloko pavadinimas | Bloko, kurį sudaro susijusios pagal tam tikrus požymius (anatominę sritį ir procedūros tipą) procedūros, pavadinimas |
| `proceduros_tipo_nr` | `integer` | — | `2` | `open` | — | Procedūros tipo eil. nr. | Medicininių intervencijų klasifikacijos procedūros tipo eilės numerį skyriuje |
| `proceduros_tipo_pav` | `string` | — | `2` | `open` | — | Procedūros tipo pavadinimas | Medicininių intervencijų klasifikacijos procedūros tipo pavadinimas (tyrimai, uždėjimas, įterpimas, šalinimas, incizija ir pan.) |
| `poskyrio_nr` | `integer` | — | `2` | `open` | — | Poskyrio eil. nr. | Medicininių intervencijų klasifikacijos poskyrio numeris skyriuje |
| `poskyrio_pavadinimas` | `string` | — | `2` | `open` | — | Poskyrio pavadinimas | Medicininių intervencijų klasifikacijos poskyrio pavadinimas (pagal anatomines sritis - organus) |
| `skyriaus_nr` | `integer` | — | `2` | `open` | — | Skyriaus nr. | Medicininių intervencijų klasifikacijos skyriaus numeris |
| `bloku_grupe` | `string` | — | `2` | `open` | — | Blokų grupė | Medicininių intervencijų klasifikacijos skyriui priklausanti blokų grupė |
| `skyriaus_pavadinimas` | `string` | — | `2` | `open` | — | Skyriaus pavadinimas | Medicininių intervencijų klasifikacijos skyriaus pavadinimas (pagal medicinos specialybes) |
| `operacija` | `string` | — | `2` | `open` | — | Operacija | Galimos trys reikšmės: 1) "Taip" - operacinėje atliekama procedūra (operacija) – tai medicininė procedūra, kuri pagal AR-DRG 8.0 versiją laikoma svarbia bet kurioje PDK ir nulemia gydymo atvejo priskyrimą chirurginio pobūdžio DRG. 2) "Ne" - ne operacinėje atliekama procedūra |
| `didzioji_operacija` | `string` | — | `4` | `open` | — | Didžioji operacija | Nurodoma ar ACHI kodas priklauso didžiųjų operacijų sąrašui patvirtintam Sveikatos apsaugos ministro 2012 m. vasario 27 d. įsakymu Nr. V-145 "Dėl Didžiųjų operacijų sąrašo sudarymo tvarkos aprašo ir didžiųjų operacijų sąrašo patvirtinimo" |
| `nuo` | `date` | `D` | `4` | `open` | — | Galioja nuo | Procedūros (ACHI) galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Galioja iki | Procedūros (ACHI) galiojimo pabaigos data |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `operacija` | `"Ne"` | — | — | Ne | — |
| `operacija` | `"Taip"` | — | — | Taip | — |
| `didzioji_operacija` | `"Ne"` | — | — | — | — |
| `didzioji_operacija` | `"Taip"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bloko_nr` | `create(property: "blokas", type: "ref", ref: "Blokas")` | `type` | `4` | — | — | — | — |
| `bloko_nr` | `update(property: "blokas.nr", type: "")` | `property` | `4` | — | — | — | — |
| `bloko_pavadinimas` | `update(property: "blokas.pavadinimas", type: "")` | — | `4` | — | — | — | — |
| `poskyrio_nr` | `create(property: "poskyris", type: "ref", ref: "Poskyris")` | `type` | `4` | — | — | — | — |
| `poskyrio_nr` | `update(property: "poskyris.nr", type: "")` | — | `4` | — | — | — | — |
| `poskyrio_pavadinimas` | `update(property: "poskyris.pavadinimas", type: "")` | — | `4` | — | — | — | — |
| `skyriaus_nr` | `create(property: "skyrius", type: "ref", ref: "Skyrius")` | `type` | `4` | — | — | — | — |
| `skyriaus_nr` | `update(property: "skyrius.nr", type: "")` | — | `4` | — | — | — | — |
| `bloku_grupe` | `update(property: "blokas.grupe", type: "")` | — | `4` | — | — | — | — |
| `skyriaus_pavadinimas` | `update(property: "skyrius.pavadinimas", type: "")` | — | — | — | — | — | — |
| `operacija` | `update(source: "", prepare: "Nenurodyta")` | — | `4` | — | `spinta: 293,vadovas:dsa/dimensijos.html#klasifikatoriai` | — | — |
| `didzioji_operacija` | `update(source: "", prepare: "Nenurodyta")` | — | `4` | — | `spinta: 293,vadovas:dsa/dimensijos.html#klasifikatoriai` | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/achi.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L8)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/achi (https://data.gov.lt/datasets/1383/)
