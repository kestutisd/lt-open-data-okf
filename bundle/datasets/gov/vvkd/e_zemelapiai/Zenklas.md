---
type: Table
title: "Zenklas — Vandens kelių ženklų informaciniai duomenys"
description: "Šiame sluoksnyje pateikiami vidaus vandenų kelių ženklų geoerdviniai duomenys, pavadinimai, tipai ir pan. Sluoksnyje pateikiami ženklai išsidėstę Nemunu nuo Kauno iki žiočių, Minijoje iki Klaipėdos kanalo, Klaipėdos kanale, Kuršių..."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/Zenklas"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L157"
    last_modified: "2026-11-11T14:39:20Z"
---

# Zenklas — Vandens kelių ženklų informaciniai duomenys

Šiame sluoksnyje pateikiami vidaus vandenų kelių ženklų geoerdviniai duomenys, pavadinimai, tipai ir pan. Sluoksnyje pateikiami ženklai išsidėstę Nemunu nuo Kauno iki žiočių, Minijoje iki Klaipėdos kanalo, Klaipėdos kanale, Kuršių mariose ir Nevėžyje nuo Vareikonių iki žiočių.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/Zenklas`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L157](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L157)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/Zenklas`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
