---
type: Table
title: "KaunasViesasisTransportas — Kauno viešojo transporto GPS padėties duomenys"
description: "Spinta table datasets/gov/viesasis_transport/gps_duomenys/KaunasViesasisTransportas (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys/KaunasViesasisTransportas"
tags: [gov, viesasis_transport, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/viesasis_transport/gps_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# KaunasViesasisTransportas — Kauno viešojo transporto GPS padėties duomenys

- **Model:** `datasets/gov/viesasis_transport/gps_duomenys/KaunasViesasisTransportas`[^manifest]
- **Dataset:** [Viešojo transporto GPS padėties duomenys](../gps_duomenys.md) (`datasets/gov/viesasis_transport/gps_duomenys`)
- **Manifest CSV:** [datasets/gov/viesasis_transport/gps_duomenys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys/KaunasViesasisTransportas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

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

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `transportas` | `"Autobusai"` | — | `open` | Autobusas | — |
| `transportas` | `"Troleibusai"` | — | `open` | Troleibusas | — |
| `masinos_tipas` | `"Mažos talpos VT priemonė"` | — | `open` | Mažesnė nei 12m ilgio viešojo transporto priemonė | — |
| `masinos_tipas` | `"Standartinės talpos VT priemonė"` | — | `open` | Standartinė 12m ilgio viešojo transporto priemonė | — |
| `masinos_tipas` | `"Padidintos talpos VT priemonė"` | — | `open` | Padidintos talpos 18m ilgio viešojo transporto priemonė | — |
| `masinos_tipas` | `"Ypač didelės talpos VT priemonė"` | — | `open` | Padidintos talpos 25m ilgio viešojo transporto priemonė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/viesasis_transport/gps_duomenys.csv
