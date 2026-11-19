---
type: Table
title: "Subjektas — Pateikiama informacija apie dauginamąją medžiagą tiekiančius ūkio subjektus (vardas, pavardė/ pavadinimas, tiekiamos augalų grupės, veiklos rūšys, dauginamosios medžiagos pažymėjimo numeris, įsakymo data)"
description: "Spinta table datasets/gov/vat/atestuota_dm/Subjektas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/atestuota_dm/Subjektas"
tags: [gov, vat, subjektas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r23_atestuota_dm.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/r23_atestuota_dm.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2574/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/atestuota_dm"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Subjektas — Pateikiama informacija apie dauginamąją medžiagą tiekiančius ūkio subjektus (vardas, pavardė/ pavadinimas, tiekiamos augalų...

- **Model:** `datasets/gov/vat/atestuota_dm/Subjektas`[^manifest]
- **Dataset:** [Atestuotų dauginamosios medžiagos tiekėjų sąrašas](../atestuota_dm.md) (`datasets/gov/vat/atestuota_dm`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/r23_atestuota_dm.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r23_atestuota_dm.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/atestuota_dm/Subjektas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `eil_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eil_nr` | `string` | — | `4` | `open` | — | Eilės numeris | — |
| `tiekejas` | `string` | — | `4` | `open` | — | Tiekėjo vardas, pavardė / pavadinimas | — |
| `veikla` | `string` | — | `4` | `open` | — | Veiklos sritis (-ys) | — |
| `augalu_grupe` | `string` | — | `4` | `open` | — | Augalų grupė (-ės) | — |
| `pazymejimas` | `string` | — | `4` | `open` | — | Pažymėjimo Nr. | — |
| `isakymas` | `string` | — | `4` | `open` | — | Įsakymo data ir Nr. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/r23_atestuota_dm.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/r23_atestuota_dm.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/atestuota_dm (https://data.gov.lt/datasets/2574/)
