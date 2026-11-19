---
type: Table
title: "BarelioMatavimas — Barelių matavimai"
description: "Lentelėje skelbiami barelių matavimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/BarelioMatavimas"
tags: [gov, vmt, bareliomatavimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L12"
    title: "atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv#L12"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2830/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vmt/inventorizacija"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# BarelioMatavimas — Barelių matavimai

Lentelėje skelbiami barelių matavimų duomenys. Viena eilutė - vienas barelio matavimas. Pateikiama barelio lokacija trakte, matavimo data, penkerių metų ciklas, būsena ir konfidencialumo tikslais "triukšmintos" barelių centrų koordinatės.[^manifest]

- **Model:** `datasets/gov/vmt/inventorizacija/BarelioMatavimas`[^manifest]
- **Dataset:** [Nacionalinės miškų inventorizacijos matavimų duomenys](../inventorizacija.md) (`datasets/gov/vmt/inventorizacija`)[^manifest]
- **Manifest CSV:** [datasets/gov/vmt/inventorizacija.csv#L12](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L12)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmt/inventorizacija/BarelioMatavimas` (`deployed`)[^manifest]
- **Provider:** `vmt` — Valstybinė Miškų Tarnyba *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `trakto_id` | `string` | — | `4` | `open` | — | Trakto identifikacinis numeris | — |
| `barelio_id` | `string` | — | `4` | `open` | — | Barelio identifikacinis numeris | — |
| `bar_tipas` | `string` | — | `4` | `open` | — | Barelio tipas | — |
| `bar_padetis` | `string` | — | `4` | `open` | — | Barelio padėtis trakte | — |
| `matavimo_data` | `date` | `D` | `4` | `open` | — | Barelio matavimo data | — |
| `penkmetis` | `string` | — | `4` | `open` | — | Barelio matavimo penkmetis | — |
| `geometrija` | `geometry(point, 3346)` | — | `4` | `open` | — | Barelių centrų taškų LKS94 koordinatės. Dėl konfidencialumo pateiktos koordinatės yra "triukšmintos" ir neatspindi tikslių barelių centrų taškų. | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bar_tipas` | `"Pastovus 1 kartą"` | — | — | — | — |
| `bar_tipas` | `"Pastovus 2 kartą"` | — | — | — | — |
| `bar_tipas` | `"Pastovus 3 kartą"` | — | — | — | — |
| `bar_tipas` | `"Pastovus 4 kartą"` | — | — | — | — |
| `bar_tipas` | `"Pastovus 5 kartą"` | — | — | — | — |
| `bar_tipas` | `"Laikinas 1 kartą"` | — | — | — | — |
| `bar_padetis` | `"Barelis yra šiaurinėje trakto kraštinėje"` | — | — | — | — |
| `bar_padetis` | `"Barelis yra vakarinėje trakto kraštinėje"` | — | — | — | — |
| `bar_padetis` | `"Barelis yra rytinėje trakto kraštinėje"` | — | — | — | — |
| `bar_padetis` | `"Barelis yra pietinėje trakto kraštinėje"` | — | — | — | — |
| `penkmetis` | `"1998_02t"` | — | — | — | — |
| `penkmetis` | `"2003_07t"` | — | — | — | — |
| `penkmetis` | `"2008_12"` | — | — | — | — |
| `penkmetis` | `"2013_17"` | — | — | — | — |
| `penkmetis` | `"2018-2022"` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vmt/inventorizacija.csv#L12 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmt/inventorizacija.csv#L12)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vmt/inventorizacija (https://data.gov.lt/datasets/2830/)
