---
type: Table
title: "Suma — Privalomojo sveikatos draudimo fondo biudžeto įplaukų plano vykdymo ataskaita"
description: "Informacija apie Privalomojo sveikatos draudimo fondo biudžeto įplaukas"
resource: "https://get.data.gov.lt/datasets/gov/vlk/iplaukos/Suma"
tags: [gov, vlk, suma, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/iplaukos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vlk/iplaukos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2329/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/iplaukos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Suma — Privalomojo sveikatos draudimo fondo biudžeto įplaukų plano vykdymo ataskaita

Informacija apie Privalomojo sveikatos draudimo fondo biudžeto įplaukas[^manifest]

- **Model:** `datasets/gov/vlk/iplaukos/Suma`[^manifest]
- **Dataset:** [PSDF biudžeto įplaukų plano vykdymo ataskaita](../iplaukos.md) (`datasets/gov/vlk/iplaukos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/iplaukos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/iplaukos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/iplaukos/Suma` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `str_kodas` | `string` | — | `3` | `open` | — | Įplaukų straipsnio kodas | — |
| `str_pavadinimas` | `string` | — | `3` | `open` | — | Įplaukų straipsnio pavadinimas | — |
| `tikslinimas` | `string` | — | `3` | `open` | — | Patikslinimas | — |
| `gautinos_sumos_pradzioje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pradžioje - gautinos sumos | — |
| `moketinos_sumos_pradzioje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pradžioje - mokėtinos sumos | — |
| `planuotos_sumos` | `number` | — | `2` | `open` | — | Ataskaitinį laikotarpį - planuotos sumos | — |
| `gautinos_sumos` | `number` | — | `2` | `open` | — | Ataskaitinį laikotarpį - gautinos sumos | — |
| `gautos_sumos` | `number` | — | `2` | `open` | — | Ataskaitinį laikotarpį - gautos sumos | — |
| `gautinos_sumos_pabaigoje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pabaigoje - gautinos sumos | — |
| `moketinos_sumos_pabaigoje` | `number` | — | `2` | `open` | — | Ataskaitinio laikotarpio pabaigoje - mokėtinos sumos | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |
| `gautinos_sumos_pradzioje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `moketinos_sumos_pradzioje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `planuotos_sumos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `gautinos_sumos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `gautos_sumos` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `gautinos_sumos_pabaigoje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |
| `moketinos_sumos_pabaigoje` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/iplaukos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/iplaukos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/iplaukos (https://data.gov.lt/datasets/2329/)
