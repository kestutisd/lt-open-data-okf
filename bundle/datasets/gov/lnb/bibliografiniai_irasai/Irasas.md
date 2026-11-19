---
type: Table
title: "Irasas — Bibliografiniai įrašai"
description: "Martyno Mažvydo bibliotekos LIBIS IS bibliografinių įrašų sąrašas"
resource: "https://get.data.gov.lt/datasets/gov/lnb/bibliografiniai_irasai/Irasas"
tags: [gov, lnb, irasas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/bibliografiniai_irasai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lnb/bibliografiniai_irasai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2625/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/bibliografiniai_irasai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Irasas — Bibliografiniai įrašai

Martyno Mažvydo bibliotekos LIBIS IS bibliografinių įrašų sąrašas[^manifest]

- **Model:** `datasets/gov/lnb/bibliografiniai_irasai/Irasas`[^manifest]
- **Dataset:** [Bibliografiniai įrašai](../bibliografiniai_irasai.md) (`datasets/gov/lnb/bibliografiniai_irasai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/bibliografiniai_irasai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/bibliografiniai_irasai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/bibliografiniai_irasai/Irasas` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `iraso_kodas` | `string` | — | `4` | `open` | — | Įrašo kodas | — |
| `iraso_pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas sąrašui | — |
| `leidinio_tipas` | `string` | — | `4` | `open` | — | Bibliografinio įrašo tipas | — |
| `leidinio_forma` | `string` | — | `4` | `open` | — | Bibliografinio įrašo forma | — |
| `leidinio_pavadinimas` | `string` | — | `4` | `open` | — | Bibliografinio įrašo pavadinimas | — |
| `leidinio_autorius` | `string` | — | `4` | `open` | — | Bibliografinio įrašo autorius | — |
| `publikavimo_duomenys` | `string` | — | `4` | `open` | — | Bibliografinio įrašo publikavimo duomenys | — |
| `publikavimo_metai` | `string` | — | `4` | `open` | — | Bibliografinio įrašo publikavimo metai | — |
| `fiziniai_duomenys` | `string` | — | `4` | `open` | — | Bibliografinio įrašo fiziniai duomenys | — |
| `leidinio_kalba` | `string` | — | `4` | `open` | — | Bibliografinio įrašo kalba(kodas) | — |
| `leidinio_kalba_pavadinimas` | `string` | — | `4` | `open` | — | Bibliografinio įrašo kalba(pavadinimas) | — |
| `leidinio_auditorija` | `string` | — | `4` | `open` | — | Bibliografinio įrašo auditorija | — |
| `leidinio_isbn` | `string` | — | `4` | `open` | — | Bibliografinio įrašo ISBN | — |
| `leidinio_udk` | `string` | — | `4` | `open` | — | Bibliografinio įrašo UDK | — |
| `leidinio_dalykas` | `string` | — | `4` | `open` | — | Bibliografinio įrašo dalykas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/bibliografiniai_irasai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/bibliografiniai_irasai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/bibliografiniai_irasai (https://data.gov.lt/datasets/2625/)
