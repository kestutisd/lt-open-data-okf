---
type: Table
title: "Ivykis — Priešgaisrinės apsaugos ir gelbėjimo departamento įvykių ir išvykčių suvestinė"
description: "Gaisrų, gelbėjimo darbų ir priešgaisrinių gelbėjimo pajėgų išvykčių suvestinė"
resource: "https://get.data.gov.lt/datasets/gov/pagd/ivykiu_suvestine/Ivykis"
tags: [gov, pagd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pagd/ivykiu_suvestine.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/ivykiu_suvestine.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Ivykis — Priešgaisrinės apsaugos ir gelbėjimo departamento įvykių ir išvykčių suvestinė

Gaisrų, gelbėjimo darbų ir priešgaisrinių gelbėjimo pajėgų išvykčių suvestinė

- **Model:** `datasets/gov/pagd/ivykiu_suvestine/Ivykis`[^manifest]
- **Dataset:** [Priešgaisrinės apsaugos ir gelbėjimo departamento įvykių ir išvykčių suvestinė](../ivykiu_suvestine.md) (`datasets/gov/pagd/ivykiu_suvestine`)
- **Manifest CSV:** [datasets/gov/pagd/ivykiu_suvestine.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/ivykiu_suvestine.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/ivykiu_suvestine/Ivykis`
- **Primary Key (`ref`):** `korteles_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `korteles_id` | `string` | — | `4` | `open` | — | Kortelės identifikatorius | — |
| `susieta_su_kortele` | `string` | — | `4` | `open` | — | Sąsaja su kitu įvykiu | — |
| `korteles_data` | `date` | `D` | `4` | `open` | — | Kortelės pildymo data | — |
| `ivykio_aprasymas_lt` | `string` | — | `4` | `open` | — | Įvykio aprašymas | — |
| `administracinis_vienetas` | `string` | — | `4` | `open` | — | Teritorija kur įvyko įvykis | — |
| `pagd_padalinys` | `string` | — | `4` | `open` | — | Priešgaisrinės apsaugos gelbėjimo departamento padalinys | — |
| `vietoves_tipas` | `string` | — | `4` | `open` | — | Vietovės tipas | — |
| `darbu_atlikimo_rajonas` | `string` | — | `4` | `open` | — | Darbų atlikimo rajonas | — |
| `ivykio_vieta` | `string` | — | `4` | `open` | — | Įvykio vieta objekte | — |
| `ivykio_vietos_aukstas` | `integer` | — | `4` | `open` | — | Įvykio aukštas objekte | — |
| `iskvietimo_laikas` | `datetime` | — | `4` | `open` | — | Iškvietimo į įvykį laikas | — |
| `likvidavimo_laikas` | `datetime` | — | `4` | `open` | — | Įvykio likvidavimo laikas | — |
| `ivykio_medziaga` | `string` | — | `4` | `open` | — | Medžiaga sukėlusi įvykį | — |
| `ivykio_priezastis` | `string` | — | `4` | `open` | — | Įvykio priežastis | — |
| `isgelbeta_zmoniu` | `integer` | — | `4` | `open` | — | Išgelbėta žmonių | — |
| `zuvo_zmoniu` | `integer` | — | `4` | `open` | — | Žuvo žmonių | — |
| `zuvo_nepilnameciu` | `integer` | — | `4` | `open` | — | Žuvo nepilnamečių | — |
| `traumuota_zmoniu` | `integer` | — | `4` | `open` | — | Traumuota žmonių | — |
| `sunaikinta_statiniu` | `integer` | — | `4` | `open` | — | Sunaikinta statinių | — |
| `ivykio_svarba` | `integer` | — | `4` | `open` | — | Ivykio svarba | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `vietoves_tipas` | `"Miestas"` | — | — | — | — |
| `vietoves_tipas` | `"Kaimas"` | — | — | — | — |
| `vietoves_tipas` | `"Miestelis"` | — | — | — | — |
| `vietoves_tipas` | `"Kita vietovė"` | — | — | — | — |
| `darbu_atlikimo_rajonas` | `"Operacijų rajone"` | — | — | — | — |
| `darbu_atlikimo_rajonas` | `"Kaimyniniame rajone"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ivykio_aprasymas_lt` | `update(property: "ivykio_aprasymas_lt@lt", type: "text")` | `type` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/ivykiu_suvestine.csv
