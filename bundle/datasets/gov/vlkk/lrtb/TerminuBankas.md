---
type: Table
title: "TerminuBankas — VLKK terminų banko terminų duomenys"
description: "Valstybinės lietuvių kalbos komisijos Lietuvos Respublikos terminų banke kaupiami įvairių sričių terminai lietuvių bei kitomis Europos kalbomis, kaip vokiečių, prancūzų, lenkų."
resource: "https://get.data.gov.lt/datasets/gov/vlkk/lrtb/TerminuBankas"
tags: [gov, vlkk, terminubankas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/lrtb.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vlkk/lrtb.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlkk/lrtb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# TerminuBankas — VLKK terminų banko terminų duomenys

Valstybinės lietuvių kalbos komisijos Lietuvos Respublikos terminų banke kaupiami įvairių sričių terminai lietuvių bei kitomis Europos kalbomis, kaip vokiečių, prancūzų, lenkų. Duomenys kaupiami nuo 2005 m. ir atnaujinami kas mėnesį. Apimami duomenys yra patys terminai, jų sritys, kalba, statusas: teiktinas, neteiktinas arba aprobuotas, įvedimo data bei organizacija, pateikusi patį terminą. Tarp tokių organizacijų patenka VLKK, Užsienio reikalų ministerija, Policijos departamentas.[^manifest]

- **Model:** `datasets/gov/vlkk/lrtb/TerminuBankas`[^manifest]
- **Dataset:** [VLKK terminų banko terminų duomenys](../lrtb.md) (`datasets/gov/vlkk/lrtb`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlkk/lrtb.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/lrtb.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlkk/lrtb/TerminuBankas` (`deployed`)[^manifest]
- **Provider:** `vlkk` — Valstybinė lietuvių kalbos komisija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `termino_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `termino_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `terminas` | `string` | — | `4` | `open` | — | Terminas | — |
| `sritis` | `string` | — | `4` | `open` | — | Termino sritis | — |
| `kalba` | `string` | — | `4` | `open` | — | Termino kalba | — |
| `statusas` | `string` | — | `4` | `open` | — | Termino statusas, anot VLKK | — |
| `pateikusi_org` | `string` | — | `4` | `open` | — | Terminą pateikusi organizacija | — |
| `ivedimo_data` | `datetime` | `S` | `4` | `open` | — | Termino įvedimo data ir laikas sekundžių tikslumu | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | — | `Teiktinas` | — | Teiktinas terminas | — |
| `statusas` | — | `Neteiktinas` | — | Neteiktinas terminas | — |
| `statusas` | — | `Aprobuotas` | — | Aprobuotas terminas | — |

# Related References

- [ISO 639 Language Codes Reference](../../../../references/iso-639-kalbu-kodai.md) — ISO 639-1 / 639-2 / EU NAL codes and special markers `zxx`, `und`, `mul`, `mis`.

[^manifest]: atviriduomenys/manifest — datasets/gov/vlkk/lrtb.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/lrtb.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlkk/lrtb (https://data.gov.lt/datasets/2636/)
