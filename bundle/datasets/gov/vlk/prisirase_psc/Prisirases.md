---
type: Table
title: "Prisirases — Prisirašiusių prie psichikos sveikatos centro asmenų skaičius"
description: "Informacija apie prisirašiusių prie psichikos sveikatos centrų asmenų skaičių (paskutinei mėnesio dienai)"
resource: "https://get.data.gov.lt/datasets/gov/vlk/prisirase_psc/Prisirases"
tags: [gov, vlk, prisirases, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_pcs.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/vlk/prisirase_pcs.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2324/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/prisirase_psc"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Prisirases — Prisirašiusių prie psichikos sveikatos centro asmenų skaičius

Informacija apie prisirašiusių prie psichikos sveikatos centrų asmenų skaičių (paskutinei mėnesio dienai)[^manifest]

- **Model:** `datasets/gov/vlk/prisirase_psc/Prisirases`[^manifest]
- **Dataset:** [Prisirašiusių prie psichikos sveikatos centrų asmenų skaičius](../prisirase_psc.md) (`datasets/gov/vlk/prisirase_psc`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/prisirase_pcs.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_pcs.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/prisirase_psc/Prisirases` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `data` | `date` | `M` | `4` | `open` | — | Data | Ataskaitinio laikotarpio data mėnesio tikslumu |
| `istaiga` | `ref` | [Istaiga](../istaigos/Istaiga.md) (`level=4 UUID` via `Istaiga[kodas]`: `istaiga._id`) | `4` | `open` | — | Įstaigos ID | Įstaigos, prie kurios prisirašę asmenys, ID |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `draustumas` | `integer` | — | `3` | `open` | — | Draustumas | Požymis, parodantis, ar asmenys buvo apdrausti PSD nurodytu laikotarpiu |
| `tlk` | `string` | — | `4` | `open` | — | Teritorinė ligonių kasa | — |
| `amziaus_grupe` | `string` | — | `4` | `open` | — | Amžiaus grupė | — |
| `asmenys` | `number` | `U` | `4` | `open` | — | Asmenų skaičius | Prisirašiusių prie pirminės psichikos centro asmenų skaičius (paskutinei mėnesio dienai) |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | — | — |
| `lytis` | `"Vyras"` | — | — | — | — |
| `tlk` | `"Vilniaus TLK"` | — | — | — | — |
| `tlk` | `"Kauno TLK"` | — | — | — | — |
| `tlk` | `"Klaipėdos TLK"` | — | — | — | — |
| `tlk` | `"Šiaulių TLK"` | — | — | — | — |
| `tlk` | `"Panevėžio TLK"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/prisirase_pcs.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/prisirase_pcs.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/prisirase_psc (https://data.gov.lt/datasets/2324/)
