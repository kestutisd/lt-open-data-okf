---
type: Table
title: "GylisKaunasKursiuMarios — Gylių duomenys"
description: "Šiame sluoksnyje pateikiami gylių duomenys Nemune nuo Birštono iki Kauno, Nemune nuo Kauno iki Kuršių marių, Kuršių mariose, Klaipėdos kanale, Minijoje nuo Atmatos iki Klaipėdos kanalo."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisKaunasKursiuMarios"
tags: [gov, vvkd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L32"
    last_modified: "2026-11-11T14:39:20Z"
---

# GylisKaunasKursiuMarios — Gylių duomenys

Šiame sluoksnyje pateikiami gylių duomenys Nemune nuo Birštono iki Kauno, Nemune nuo Kauno iki Kuršių marių, Kuršių mariose, Klaipėdos kanale, Minijoje nuo Atmatos iki Klaipėdos kanalo.

- **Model:** `datasets/gov/vvkd/e_zemelapiai/GylisKaunasKursiuMarios`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L32)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisKaunasKursiuMarios`
- **Primary Key (`ref`):** `fid`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fid` | `string` | — | `4` | `open` | — | Identifikavimo kodas | — |
| `atkarpa` | `string` | — | `3` | `open` | — | Upės ruožo atkarpos pavadinimas | — |
| `eil_nr` | `string` | — | `4` | `open` | — | Taško eilės numeracija | — |
| `gylis_cm` | `number` | `cm` | `4` | `open` | — | Gylis centimetrais | — |
| `data` | `datetime` | `L` | `4` | `open` | — | Data | — |
| `skales_tip` | `string` | — | `4` | `open` | — | Sutartinio ženklo klasifikatoriaus kodas | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto plotas | — |
| `geometry` | `geometry(3857)` | — | `4` | `open` | — | Geometrijos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv
