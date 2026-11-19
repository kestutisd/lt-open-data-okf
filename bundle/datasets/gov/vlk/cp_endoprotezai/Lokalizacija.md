---
type: Table
title: "Lokalizacija — Protezų lokalizacijų klasifikatorius"
description: "Protezų lokalizacijų klasifikatorius"
resource: "https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai/Lokalizacija"
tags: [gov, vlk, lokalizacija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1798/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/cp_endoprotezai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Lokalizacija — Protezų lokalizacijų klasifikatorius

Protezų lokalizacijų klasifikatorius[^manifest]

- **Model:** `datasets/gov/vlk/cp_endoprotezai/Lokalizacija`[^manifest]
- **Dataset:** [Centralizuotai apmokamų endoprotezų panaudojimas](../cp_endoprotezai.md) (`datasets/gov/vlk/cp_endoprotezai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/cp_endoprotezai.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/cp_endoprotezai/Lokalizacija` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Protezo lokalizacijos kodas | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Protezo lokalizacijos aprašymas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Protezo lokalizacijos pavadinimas | Endoprotezo lokalizacija: klubo, kelio ir kt. |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/cp_endoprotezai.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/cp_endoprotezai.csv#L18)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/cp_endoprotezai (https://data.gov.lt/datasets/1798/)
