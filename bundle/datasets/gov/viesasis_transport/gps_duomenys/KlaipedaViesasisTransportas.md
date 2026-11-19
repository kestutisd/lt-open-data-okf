---
type: Table
title: "KlaipedaViesasisTransportas — Klaipėdos viešojo transporto GPS padėties duomenys"
description: "Rinkiniuose pateikiama viešojo transporto GPS informacija."
resource: "https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys/KlaipedaViesasisTransportas"
tags: [gov, viesasis_transport, klaipedaviesasistransportas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L51"
    title: "atviriduomenys/manifest — datasets/gov/viesasis_transport/gps_duomenys.csv#L51"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3856/"
    title: "data.gov.lt DCAT-AP — datasets/gov/viesasis_transport/gps_duomenys"
    author: "team:vda"
    last_modified: "2026-01-15T00:00:00Z"
---

# KlaipedaViesasisTransportas — Klaipėdos viešojo transporto GPS padėties duomenys

**Dataset Context:** Rinkiniuose pateikiama viešojo transporto GPS informacija. Viešojo transporto padėties informacija matuojama kas 5-20 sekundžių. Duomenys atnaujinami kartą per dieną. Pateikiama informacija apie transporto rūšį, maršrutą, reiso identifikatorių, mašinos numerį, mašinos koordinates matavimo metu WGS-84 ir LKS-94 koordinačių sistemose, greitį, azimutą, reiso pradžią, nuokrypį nuo grafiko sekundėmis, mašinos tipą, matavimo datą ir laiką. Rinkinių objektas – vienos transporto priemonės GPS koordinatės laike. Duomenys nuo 2025-07-01. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/viesasis_transport/gps_duomenys/KlaipedaViesasisTransportas`[^manifest]
- **Dataset:** [Viešojo transporto GPS padėties duomenys](../gps_duomenys.md) (`datasets/gov/viesasis_transport/gps_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/viesasis_transport/gps_duomenys.csv#L51](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L51)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys/KlaipedaViesasisTransportas` (`deployed`)[^manifest]
- **Provider:** `viesasis_transport` — Viešojo transporto duomenys *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-01-15`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `transportas` | `string` | — | `4` | `open` | — | Transporto tipas | — |
| `marsrutas` | `string` | — | `4` | `open` | — | Maršrutas | — |
| `reiso_id` | `string` | — | `4` | `open` | — | Reiso identifikatorius | — |
| `masinos_numeris` | `string` | — | `4` | `open` | — | Garažinis mašinos numeris | — |
| `ilguma_wgs` | `number` | — | `4` | `open` | — | Transporto priemonės ilgumos koordinatė WGS-84 formatu laike (matavimo_data, matavimo_laikas) | — |
| `platuma_wgs` | `number` | — | `4` | `open` | — | Transporto priemonės platumos koordinatė WGS-84 formatu laike (matavimo_data, matavimo_laikas) | — |
| `x_koord_lks` | `number` | — | `4` | `open` | — | Transporto priemonės X koordinatė LKS-94 koordinačių sistemoje laike (matavimo_data, matavimo_laikas) | — |
| `y_koord_lks` | `number` | — | `4` | `open` | — | Transporto priemonės Y koordinatė LKS-94 koordinačių sistemoje laike (matavimo_data, matavimo_laikas) | — |
| `greitis_kmh` | `integer` | `km/h` | `4` | `open` | — | Transporto priemonės greitis, km/h | — |
| `azimutas` | `integer` | `°` | `4` | `open` | — | Transporto priemonės azimutas | — |
| `reiso_pradzia` | `time` | — | `3` | `open` | — | Reiso pradžia formatu HH:mm:ss | — |
| `nuokrypis_sekundemis` | `integer` | `S` | `4` | `open` | — | Nuokrypis nuo grafiko sekundėmis | — |
| `matavimo_data` | `date` | `D` | `4` | `open` | — | Matavimo data formatu YYYY-MM-DD | — |
| `matavimo_laikas` | `time` | — | `3` | `open` | — | Matavimo laikas formatu HH:mm:ss | — |
| `masinos_tipas` | `string` | — | `4` | `open` | — | Mašinos tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/viesasis_transport/gps_duomenys.csv#L51 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L51)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/viesasis_transport/gps_duomenys (https://data.gov.lt/datasets/3856/)
