---
type: Table
title: "PrisirasesPaasp — Prisirašiusių prie PAASP asmenų skaičius"
description: "Informacija apie prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičių"
resource: "https://get.data.gov.lt/datasets/gov/vlk/prisirase/PrisirasesPaasp"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/prisirase.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrisirasesPaasp — Prisirašiusių prie PAASP asmenų skaičius

Informacija apie prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičių

- **Model:** `datasets/gov/vlk/prisirase/PrisirasesPaasp`[^manifest]
- **Dataset:** [datasets/gov/vlk/prisirase](../prisirase.md) (`datasets/gov/vlk/prisirase`)
- **Manifest CSV:** [datasets/gov/vlk/prisirase.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/prisirase/PrisirasesPaasp`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | Ataskaitinio laikotarpio metai |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | Ataskaitinio laikotarpio mėnuo |
| `istaiga` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga[kodas]](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | Įstaigos, prie kurios prisirašę asmenys, ID |
| `apylinke` | `string` | — | `4` | `open` | — | Apylinkė | Specialistas, prie kurio asmuo prirašytas (šeimos gydytojas, pediatras, terapeutas) |
| `draustumas` | `integer` | — | `3` | `open` | — | Draustumas | Požymis, parodantis, ar asmenys buvo apdrausti PSD nurodytu laikotarpiu |
| `tlk` | `string` | — | — | `open` | — | Teritorinė ligonių kasa | — |
| `savivaldybe` | `integer` | — | `2` | `open` | — | Savivaldybės kodas | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Amžiaus grupė | — |
| `amzius` | `integer` | — | `3` | `open` | — | Amžius metais | — |
| `asmenys` | `number` | `U` | `4` | `open` | — | Prisirašiusių asmenų skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `apylinke` | `"Šeimos gydytojo"` | — | — | — | — |
| `apylinke` | `"Terapeuto"` | — | — | — | — |
| `apylinke` | `"Pediatro"` | — | — | — | — |
| `tlk` | `"Vilniaus TLK"` | — | — | — | — |
| `tlk` | `"Kauno TLK"` | — | — | — | — |
| `tlk` | `"Klaipėdos TLK"` | — | — | — | — |
| `tlk` | `"Šiaulių TLK"` | — | — | — | — |
| `tlk` | `"Panevėžio TLK"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `update(type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe[pavadinimas]")` | `type` | `2` | — | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `property` | `2` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/prisirase.csv
