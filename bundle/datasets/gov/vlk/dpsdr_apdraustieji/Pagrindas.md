---
type: Table
title: "Pagrindas — Draudžiamųjų grupės"
description: "Spinta table datasets/gov/vlk/dpsdr_apdraustieji/Pagrindas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji/Pagrindas"
tags: [gov, vlk, pagrindas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L13"
    title: "atviriduomenys/manifest — datasets/gov/vlk/dpsdr_apdraustieji.csv#L13"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1591/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/dpsdr_apdraustieji"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Pagrindas — Draudžiamųjų grupės

- **Model:** `datasets/gov/vlk/dpsdr_apdraustieji/Pagrindas`[^manifest]
- **Dataset:** [Apdraustųjų skaičius, pagal DPSDR nustatytas draudimo grupes](../dpsdr_apdraustieji.md) (`datasets/gov/vlk/dpsdr_apdraustieji`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/dpsdr_apdraustieji.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L13)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/dpsdr_apdraustieji/Pagrindas` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `kodas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Kodas | Draudžiamųjų grupės kodas |
| `pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas | Draudžiamųjų grupės pavadinimas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/dpsdr_apdraustieji.csv#L13 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/dpsdr_apdraustieji.csv#L13)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/dpsdr_apdraustieji (https://data.gov.lt/datasets/1591/)
