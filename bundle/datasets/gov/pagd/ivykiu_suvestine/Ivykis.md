---
type: Table
title: "Ivykis — Priešgaisrinės apsaugos ir gelbėjimo departamento įvykių ir išvykčių suvestinė"
description: "Gaisrų, gelbėjimo darbų ir priešgaisrinių gelbėjimo pajėgų išvykčių suvestinė"
resource: "https://get.data.gov.lt/datasets/gov/pagd/ivykiu_suvestine/Ivykis"
tags: [gov, pagd, ivykis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/ivykiu_suvestine.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/pagd/ivykiu_suvestine.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2793/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pagd/ivykiu_suvestine"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Ivykis — Priešgaisrinės apsaugos ir gelbėjimo departamento įvykių ir išvykčių suvestinė

Gaisrų, gelbėjimo darbų ir priešgaisrinių gelbėjimo pajėgų išvykčių suvestinė[^manifest]

- **Model:** `datasets/gov/pagd/ivykiu_suvestine/Ivykis`[^manifest]
- **Dataset:** [Priešgaisrinės apsaugos ir gelbėjimo departamento įvykių ir išvykčių suvestinė](../ivykiu_suvestine.md) (`datasets/gov/pagd/ivykiu_suvestine`)[^manifest]
- **Manifest CSV:** [datasets/gov/pagd/ivykiu_suvestine.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/ivykiu_suvestine.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pagd/ivykiu_suvestine/Ivykis` (`deployed`)[^manifest]
- **Provider:** `pagd` — Priešgaisrinės apsaugos ir gelbėjimo departamentas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `korteles_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/pagd/ivykiu_suvestine.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pagd/ivykiu_suvestine.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pagd/ivykiu_suvestine (https://data.gov.lt/datasets/2793/)
