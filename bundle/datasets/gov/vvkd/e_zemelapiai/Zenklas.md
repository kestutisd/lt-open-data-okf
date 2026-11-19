---
type: Table
title: "Zenklas — Vandens kelių ženklų informaciniai duomenys"
description: "Šiame sluoksnyje pateikiami vidaus vandenų kelių ženklų geoerdviniai duomenys, pavadinimai, tipai ir pan."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/Zenklas"
tags: [gov, vvkd, zenklas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L157"
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv#L157"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1983/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkd/e_zemelapiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Zenklas — Vandens kelių ženklų informaciniai duomenys

Šiame sluoksnyje pateikiami vidaus vandenų kelių ženklų geoerdviniai duomenys, pavadinimai, tipai ir pan. Sluoksnyje pateikiami ženklai išsidėstę Nemunu nuo Kauno iki žiočių, Minijoje iki Klaipėdos kanalo, Klaipėdos kanale, Kuršių mariose ir Nevėžyje nuo Vareikonių iki žiočių.[^manifest]

- **Model:** `datasets/gov/vvkd/e_zemelapiai/Zenklas`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L157](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L157)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/Zenklas` (`deployed`)[^manifest]
- **Provider:** `vvkd` — AB Vidaus vandens kelių direkcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `fid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `pav` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Tipas | — |
| `kodas` | `string` | — | `4` | `open` | — | Kodas | — |
| `info_lt` | `string` | — | `4` | `open` | — | Informacija | — |
| `signalas` | `string` | — | `4` | `open` | — | Bujaus šviesos signalo kodas | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `info_lt` | `update(property: "info_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv#L157 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L157)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkd/e_zemelapiai (https://data.gov.lt/datasets/1983/)
