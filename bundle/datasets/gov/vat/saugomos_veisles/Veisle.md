---
type: Table
title: "Veisle — Pateikiama informacija apie į Nacionalinį sąrašą įrašytas veisles, išbrauktas veisles, veislių palaikytojų ir selekcininkų įgaliotųjų atstovų sąrašus."
description: "Spinta table datasets/gov/vat/saugomos_veisles/Veisle (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles/Veisle"
tags: [gov, vat, veisle, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1868/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/saugomos_veisles"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Veisle — Pateikiama informacija apie į Nacionalinį sąrašą įrašytas veisles, išbrauktas veisles, veislių palaikytojų ir selekcininkų...

- **Model:** `datasets/gov/vat/saugomos_veisles/Veisle`[^manifest]
- **Dataset:** [Nacionalinis saugomų augalų veislių sąrašas, Lietuvos Respublikoje saugomų augalų veislių...](../saugomos_veisles.md) (`datasets/gov/vat/saugomos_veisles`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/saugomos_veisles.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles/Veisle` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `grupe` | `string` | — | `4` | `open` | — | Augalų grupė | — |
| `gentis` | `string` | — | `4` | `open` | — | Augalų genčių ir rūšių grupė | — |
| `veisle` | `string` | — | `4` | `open` | — | Augalo veislės pavadinimas | — |
| `rusis` | `string` | — | `2` | `open` | — | Augalo rūšis | — |
| `atnaujinimo_metai` | `integer` | — | `2` | `open` | — | Įrašymo atnaujinimo metai | — |
| `galioja_iki` | `integer` | — | `2` | `open` | — | Metai, iki kurių gruodžio 31 d. galioja įrašymas | — |
| `atstovas` | `string` | — | `1` | `open` | — | Atstovo pavadinimas | — |
| `atstovo_adresas` | `string` | — | `2` | `open` | — | Atstovo adresas | — |
| `metai` | `integer` | — | `2` | `open` | — | Įrašymo metai | — |
| `palaikytojas` | `string` | — | `1` | `open` | — | Veislės palaikytojas | — |
| `pastabos` | `string` | — | `2` | `open` | — | Pastabos | — |
| `buveine` | `string` | — | `1` | `open` | — | Palaikytojo adresas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Palaikytojo adreso koordinatės (LKS) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `grupe` | `"ŽEMĖS ŪKIO AUGALAI"` | — | — | — | — |
| `grupe` | `"DARŽOVĖS"` | — | — | — | — |
| `grupe` | `"Sodo augalai"` | — | — | — | — |
| `grupe` | `"Dekoratyviniai augalai"` | — | — | — | — |
| `gentis` | `"Javai"` | — | — | — | — |
| `gentis` | `"Aliejiniai ir pluoštiniai augalai"` | — | — | — | — |
| `gentis` | `"Runkeliai"` | — | — | — | — |
| `gentis` | `"Pašariniai pupiniai augalai"` | — | — | — | — |
| `gentis` | `"Pašariniai migliniai augalai"` | — | — | — | — |
| `gentis` | `"Daržovės"` | — | — | — | — |
| `gentis` | `"Bulvės"` | — | — | — | — |
| `gentis` | `"Serbentai"` | — | — | — | — |
| `gentis` | `"Trešnės, Vyšnios"` | — | — | — | — |
| `gentis` | `"Braškės, žemuogės"` | — | — | — | — |
| `gentis` | `"Obelys"` | — | — | — | — |
| `gentis` | `"Pašariniai kitų rūšių augalai"` | — | — | — | — |
| `gentis` | `"Kriaušės"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `atnaujinimo_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `galioja_iki` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/saugomos_veisles (https://data.gov.lt/datasets/1868/)
