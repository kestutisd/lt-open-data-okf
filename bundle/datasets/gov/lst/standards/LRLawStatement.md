---
type: Table
title: "LRLawStatement"
description: "Nacionalinių teisės aktų, kuriais į nacionalinę teisę perkelta Europos Sąjungos direktyva arba standartas turi nuokrypą arba standartas turi išskirtinę nuorodą, duomenys (pavadinimas, numeris, priėmimo data, įsigaliojimo data, panaikinimo data, Valstybės žinių numeris..."
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/LRLawStatement"
tags: [gov, lst, lrlawstatement, deployed, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L165"
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv#L165"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1636/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lst/standards"
    author: "team:vda"
    last_modified: "2026-10-02T00:00:00Z"
---

# LRLawStatement

Nacionalinių teisės aktų, kuriais į nacionalinę teisę perkelta Europos Sąjungos direktyva arba standartas turi nuokrypą arba standartas turi išskirtinę nuorodą, duomenys (pavadinimas, numeris, priėmimo data, įsigaliojimo data, panaikinimo data, Valstybės žinių numeris, Valstybės žinių data)[^manifest]

- **Model:** `datasets/gov/lst/standards/LRLawStatement`[^manifest]
- **Dataset:** [Lietuvos standartų ir standartizacijos leidinių bibliografinių duomenų bazė](../standards.md) (`datasets/gov/lst/standards`)[^manifest]
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L165](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L165)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/LRLawStatement` (`deployed`)[^manifest]
- **Provider:** `lst` — Lietuvos standartizacijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-10-02`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | — | — | `open` | — | — | — |
| `type` | `ref` | [LRLawStatementType](LRLawStatementType.md) | — | `open` | — | — | — |
| `number` | `string` | — | — | `open` | — | — | — |
| `valid_from` | `datetime` | — | — | `open` | — | — | — |
| `link` | `string` | — | — | `open` | — | — | — |
| `state_news_nr` | `string` | — | — | `open` | — | — | — |
| `state_news_date` | `datetime` | — | — | `open` | — | — | — |
| `remarks` | `string` | — | — | `open` | — | — | — |
| `implementation_date` | `datetime` | — | — | `open` | — | — | — |
| `withdrawal_date` | `datetime` | — | — | `open` | — | — | — |
| `register_nr` | `string` | — | — | `open` | — | — | — |
| `register_date` | `datetime` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv#L165 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L165)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lst/standards (https://data.gov.lt/datasets/1636/)
