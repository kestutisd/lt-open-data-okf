---
type: Table
title: "Siunta — Pateikiami duomenys apie dokumento pavadinimą, datą, Nr., augalo rūšį / sėklos mišinio pavadinimą, veislę, siuntos Nr., panaikinimo / paskelbimo datą"
description: "Informacija apie uždraustas tiekti rinkai dauginamosios medžiagos siuntas"
resource: "https://get.data.gov.lt/datasets/gov/vat/uzdraustos_medziagos/Siunta"
tags: [gov, vat, siunta, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1881/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/uzdraustos_medziagos"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Siunta — Pateikiami duomenys apie dokumento pavadinimą, datą, Nr., augalo rūšį / sėklos mišinio pavadinimą, veislę, siuntos Nr....

**Dataset Context:** Informacija apie uždraustas tiekti rinkai dauginamosios medžiagos siuntas[^manifest]

- **Model:** `datasets/gov/vat/uzdraustos_medziagos/Siunta`[^manifest]
- **Dataset:** [Informacija apie uždraustas tiekti rinkai dauginamosios medžiagos siuntas](../uzdraustos_medziagos.md) (`datasets/gov/vat/uzdraustos_medziagos`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/uzdraustos_medziagos/Siunta` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eiles_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eiles_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `dokumentas` | `string` | — | `3` | `open` | — | Dokumento tipas | — |
| `data` | `string` | — | `1` | `open` | — | Dokumento data ir Nr. | — |
| `rusis` | `string` | — | `3` | `open` | — | Augalo rūšis/ sėklos mišinio pavadinimas | — |
| `veisle` | `string` | — | `4` | `open` | — | Veislė | — |
| `siuntos_nr` | `string` | — | `1` | `open` | — | Siuntos numeris | — |
| `pastaba` | `string` | — | `2` | `open` | — | Pastaba | — |
| `paskelbimas` | `date` | `D` | `4` | `open` | — | Panaikinimo paskelbimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r25_uzdraustos_medziagos.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/uzdraustos_medziagos (https://data.gov.lt/datasets/1881/)
