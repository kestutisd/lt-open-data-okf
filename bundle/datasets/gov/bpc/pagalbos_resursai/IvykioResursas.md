---
type: Table
title: "IvykioResursas — Pagalbos resursų iškvietimų duomenys"
description: "Lentelėje pateikta informacija iš Bendrojo pagalbos centro (BPC) apie resursų (greitosios medicinos pagalbos ir priešgaisrinės gelbėjimo tarnybos) iškvietimus."
resource: "https://get.data.gov.lt/datasets/gov/bpc/pagalbos_resursai/IvykioResursas"
tags: [gov, bpc, ivykioresursas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_resursai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/bpc/pagalbos_resursai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# IvykioResursas — Pagalbos resursų iškvietimų duomenys

Lentelėje pateikta informacija iš Bendrojo pagalbos centro (BPC) apie resursų (greitosios medicinos pagalbos ir priešgaisrinės gelbėjimo tarnybos) iškvietimus. Duomenys atnaujinami kas mėnesį.[^manifest]

- **Model:** `datasets/gov/bpc/pagalbos_resursai/IvykioResursas`[^manifest]
- **Dataset:** [datasets/gov/bpc/pagalbos_resursai](../pagalbos_resursai.md) (`datasets/gov/bpc/pagalbos_resursai`)[^manifest]
- **Manifest CSV:** [datasets/gov/bpc/pagalbos_resursai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_resursai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/bpc/pagalbos_resursai/IvykioResursas` (`deployed`)[^manifest]
- **Provider:** `bpc` — Bendrasis pagalbos centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `ivykio_id` | `string` | — | `4` | `open` | — | Įvykio identifikatorius | — |
| `resurso_id` | `string` | — | `4` | `open` | — | Resurso identifikatorius | — |
| `isvykimo_id` | `string` | — | `4` | `open` | — | Resurso išvykimo identifikatorius | — |
| `aukstesnis_ivykio_tipas` | `string` | — | `4` | `open` | — | Aukštesnis įvykio tipas | — |
| `zemesnis_ivykio_tipas` | `string` | — | `4` | `open` | — | Žemesnis įvykio tipas | — |
| `resurso_tipas_iskvietimo_metu` | `string` | — | `4` | `open` | — | Resurso tipas pagalbos iškvietimo metu | — |
| `resurso_grupe` | `string` | — | `4` | `open` | — | Resurso grupė | — |
| `baze_iskvietimo_metu` | `string` | — | `4` | `open` | — | Resurso bazė iškvietimo metu | — |
| `iskvietimo_pradzia` | `datetime` | `S` | `4` | `open` | — | Iškvietimo pradžia | — |
| `rezervacijos_laikas` | `datetime` | `S` | `4` | `open` | — | Resurso rezervacijos laikas | — |
| `isvykimo_laikas` | `datetime` | `S` | `4` | `open` | — | Pagalbos ekipažo (resurso) išvykimo laikas | — |
| `atvykimo_laikas` | `datetime` | `S` | `4` | `open` | — | Pagalbos ekipažo (resurso) atvykimo į įvykio vietą laikas | — |
| `uzbaigimo_laikas` | `datetime` | `S` | `4` | `open` | — | Pagalbos teikimo užbaigimo laikas | — |
| `uzbaigimo_laikas_radiju` | `datetime` | `S` | `4` | `open` | — | Pagalbos teikimo užbaigimo radiju laikas | — |
| `miestas` | `string` | — | `4` | `open` | — | Įvykio miestas | — |
| `vietove` | `string` | — | `4` | `open` | — | Įvykio vietovė | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Įvykio savivaldybė | — |
| `gatve` | `string` | — | `4` | `open` | — | Įvykio gatvė | — |
| `x_koord_lks` | `integer` | — | `4` | `open` | — | Įvykio X koordinatė (pagal LKS-94 sistemą) | — |
| `y_koord_lks` | `integer` | — | `4` | `open` | — | Įvykio Y koordinatė (pagal LKS-94 sistemą) | — |
| `atsaukimo_priezastis` | `string` | — | `4` | `open` | — | Resurso iškvietimo atšaukimo priežastis | — |
| `statusas` | `string` | — | `4` | `open` | — | Pagalbos suteikimo statusas | — |
| `statuso_laikas` | `datetime` | `S` | `4` | `open` | — | Pagalbos suteikimo laikas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/bpc/pagalbos_resursai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/bpc/pagalbos_resursai.csv#L6)
