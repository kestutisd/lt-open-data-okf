---
type: Table
title: "GylisKaunasKursiuMarios — Gylių duomenys"
description: "Šiame sluoksnyje pateikiami gylių duomenys Nemune nuo Birštono iki Kauno, Nemune nuo Kauno iki Kuršių marių, Kuršių mariose, Klaipėdos kanale, Minijoje nuo Atmatos iki Klaipėdos kanalo."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisKaunasKursiuMarios"
tags: [gov, vvkd, gyliskaunaskursiumarios, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L32"
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv#L32"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1983/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkd/e_zemelapiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# GylisKaunasKursiuMarios — Gylių duomenys

Šiame sluoksnyje pateikiami gylių duomenys Nemune nuo Birštono iki Kauno, Nemune nuo Kauno iki Kuršių marių, Kuršių mariose, Klaipėdos kanale, Minijoje nuo Atmatos iki Klaipėdos kanalo.[^manifest]

- **Model:** `datasets/gov/vvkd/e_zemelapiai/GylisKaunasKursiuMarios`[^manifest]
- **Dataset:** [Vidaus vandenų e-navigacinių žemėlapių informacija](../e_zemelapiai.md) (`datasets/gov/vvkd/e_zemelapiai`)[^manifest]
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L32)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai/GylisKaunasKursiuMarios` (`deployed`)[^manifest]
- **Provider:** `vvkd` — AB Vidaus vandens kelių direkcija *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `fid`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv#L32 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L32)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkd/e_zemelapiai (https://data.gov.lt/datasets/1983/)
