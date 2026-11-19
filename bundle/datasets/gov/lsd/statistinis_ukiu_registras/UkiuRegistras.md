---
type: Table
title: "UkiuRegistras — Statistinis ūkių registras"
description: "Statistinio ūkių registro atviri duomenys"
resource: "https://get.data.gov.lt/datasets/gov/lsd/statistinis_ukiu_registras/UkiuRegistras"
tags: [gov, lsd, ukiuregistras, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistinis_ukiu_registras.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lsd/statistinis_ukiu_registras.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/5962/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/statistinis_ukiu_registras"
    author: "team:vda"
    last_modified: "2026-09-07T00:00:00Z"
---

# UkiuRegistras — Statistinis ūkių registras

Statistinio ūkių registro atviri duomenys[^manifest]

- **Model:** `datasets/gov/lsd/statistinis_ukiu_registras/UkiuRegistras`[^manifest]
- **Dataset:** [Statistinis ūkių registras](../statistinis_ukiu_registras.md) (`datasets/gov/lsd/statistinis_ukiu_registras`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/statistinis_ukiu_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistinis_ukiu_registras.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/statistinis_ukiu_registras/UkiuRegistras` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `u_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-09-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `u_id` | `string` | — | `4` | `open` | — | Unikalus ūkio identifikacinis kodas | — |
| `metai` | `string` | — | `4` | `open` | — | Metai, už kuriuos atveriamas registras | — |
| `lytis` | `string` | — | `4` | `open` | — | Ūkio valdytojo (ūkininkaujančio asmens) lytis | — |
| `amzius` | `string` | — | `4` | `open` | — | Ūkio valdytojo (ūkininkaujančio asmens) amžius | — |
| `naudmenos` | `string` | — | `4` | `open` | — | Ūkio deklaruotas žemės ūkio naudmenų plotas (ha) | — |
| `salyginiu_gyv_sk` | `number` | — | `4` | `open` | — | Ūkyje laikomų gyvūnų skaičius, išreikštas sutartiniais vienetais | — |
| `standartine_produkcija` | `string` | — | `4` | `open` | — | Ūkio standartinės produkcijos dydis | — |
| `bendras_uk_tipas` | `string` | — | `4` | `open` | — | Ūkio bendrasis ūkininkavimo tipas | — |
| `pagrindinis_uk_tipas` | `string` | — | `4` | `open` | — | Ūkio pagrindinis ūkininkavimo tipas | — |
| `konkretus_uk_tipas` | `string` | — | `4` | `open` | — | Ūkio ypatingasis ūkininkavimo specializacijos tipas | — |
| `evd_klase` | `string` | — | `4` | `open` | — | Ūkio ekonominio valdos dydžio klasė | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | `V` | — | Vyras | — |
| `lytis` | `"Moteris"` | `M` | — | Moteris | — |
| `lytis` | `"Nezinoma"` | `N` | — | Lytis nežinoma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `standartine_produkcija` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/statistinis_ukiu_registras.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/statistinis_ukiu_registras.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/statistinis_ukiu_registras (https://data.gov.lt/datasets/5962/)
