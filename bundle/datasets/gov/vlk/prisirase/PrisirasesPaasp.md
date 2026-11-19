---
type: Table
title: "PrisirasesPaasp — Prisirašiusių prie PAASP asmenų skaičius"
description: "Informacija apie prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičių"
resource: "https://get.data.gov.lt/datasets/gov/vlk/prisirase/PrisirasesPaasp"
tags: [gov, vlk, prisirasespaasp, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vlk/prisirase.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1586/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/prisirase"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PrisirasesPaasp — Prisirašiusių prie PAASP asmenų skaičius

Informacija apie prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių įstaigų asmenų skaičių[^manifest]

- **Model:** `datasets/gov/vlk/prisirase/PrisirasesPaasp`[^manifest]
- **Dataset:** [Prisirašiusių prie pirminės ambulatorinės asmens sveikatos priežiūros paslaugas teikiančių...](../prisirase.md) (`datasets/gov/vlk/prisirase`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/prisirase.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/prisirase/PrisirasesPaasp` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | Ataskaitinio laikotarpio metai |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | Ataskaitinio laikotarpio mėnuo |
| `istaiga` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID` via `Istaiga[kodas]`: `istaiga._id`) | `4` | `open` | — | Įstaigos ID | Įstaigos, prie kurios prisirašę asmenys, ID |
| `apylinke` | `string` | — | `4` | `open` | — | Apylinkė | Specialistas, prie kurio asmuo prirašytas (šeimos gydytojas, pediatras, terapeutas) |
| `draustumas` | `integer` | — | `3` | `open` | — | Draustumas | Požymis, parodantis, ar asmenys buvo apdrausti PSD nurodytu laikotarpiu |
| `tlk` | `string` | — | — | `open` | — | Teritorinė ligonių kasa | — |
| `savivaldybe` | `integer` | — | `2` | `open` | — | Savivaldybės kodas | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Amžiaus grupė | — |
| `amzius` | `integer` | — | `3` | `open` | — | Amžius metais | — |
| `asmenys` | `number` | `U` | `4` | `open` | — | Prisirašiusių asmenų skaičius | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/prisirase.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/prisirase (https://data.gov.lt/datasets/1586/)
