---
type: Table
title: "Operacija — Centralizuotai perkamų endoprotezų panaudojimas"
description: "Informacija apie PSDF biudžeto lėšomis atliktų centralizuotai perkamų sąnarių endoprotezavimo operacijų skaičių"
resource: "https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai/Operacija"
tags: [gov, vlk, operacija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1798/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/cp_endoprotezai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Operacija — Centralizuotai perkamų endoprotezų panaudojimas

Informacija apie PSDF biudžeto lėšomis atliktų centralizuotai perkamų sąnarių endoprotezavimo operacijų skaičių[^manifest]

- **Model:** `datasets/gov/vlk/cp_endoprotezai/Operacija`[^manifest]
- **Dataset:** [Centralizuotai apmokamų endoprotezų panaudojimas](../cp_endoprotezai.md) (`datasets/gov/vlk/cp_endoprotezai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/cp_endoprotezai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai/Operacija` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `istg_id` | `ref` | [Istaiga](Istaiga.md) (`level=4 UUID`: `istg_id._id`) | `4` | `open` | — | Nuoroda į Istaiga | Gydymo įstaigos unikalus numeris |
| `lokalizacijos_id` | `ref` | [Lokalizacija](Lokalizacija.md) (`level=4 UUID`: `lokalizacijos_id._id`) | `4` | `open` | — | Nuoroda į Lokalizacija | Endoprotezo lokalizacijos unikalus numeris |
| `prasymo_id` | `ref` | [Prasymas](Prasymas.md) (`level=4 UUID`: `prasymo_id._id`) | `4` | `open` | — | Nuoroda į Prasymas | Prašymo unikalus numeris |
| `data` | `date` | `M` | `4` | `open` | — | Operacijos data | Operacijos atlikimo data mėnesio tikslumu |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/cp_endoprotezai (https://data.gov.lt/datasets/1798/)
