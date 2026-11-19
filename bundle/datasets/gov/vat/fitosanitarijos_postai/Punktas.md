---
type: Table
title: "Punktas — Pasienio kontrolės punktų fitosanitarijos postų (skyrių) duomenys"
description: "Spinta table datasets/gov/vat/fitosanitarijos_postai/Punktas (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_postai/Punktas"
tags: [gov, vat, punktas, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_postai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/vat/fitosanitarijos_postai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1891/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarijos_postai"
    author: "team:vda"
    last_modified: "2026-10-19T00:00:00Z"
---

# Punktas — Pasienio kontrolės punktų fitosanitarijos postų (skyrių) duomenys

- **Model:** `datasets/gov/vat/fitosanitarijos_postai/Punktas`[^manifest]
- **Dataset:** [Pasienio kontrolės punktų fitosanitarijos postai (skyriai)](../fitosanitarijos_postai.md) (`datasets/gov/vat/fitosanitarijos_postai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vat/fitosanitarijos_postai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_postai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/fitosanitarijos_postai/Punktas` (`deployed`)[^manifest]
- **Provider:** `vat` — Valstybinė augalininkystės tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2026-10-19`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikacinis numeris | — |
| `padalinys` | `string` | — | `4` | `open` | — | Padalinio pavadinimas | — |
| `adresas` | `string` | — | `2` | `open` | — | Padalinio adresas | — |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Padalinio vietos koordinatės (LKS - 3346) | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `padalinys` | `"Klaipėdos jūrų uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Medininkų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Šalčininkų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Kybartų pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |
| `padalinys` | `"Kauno oro uosto pasienio kontrolės punkto fitosanitarijos postas (skyrius)"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/fitosanitarijos_postai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/fitosanitarijos_postai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vat/fitosanitarijos_postai (https://data.gov.lt/datasets/1891/)
