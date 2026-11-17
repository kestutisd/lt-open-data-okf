---
type: Dataset
title: "Viešojo transporto GPS padėties duomenys"
description: "Rinkiniuose pateikiama viešojo transporto GPS informacija."
resource: "https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys"
tags: [gov, viesasis_transport, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/viesasis_transport/gps_duomenys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Viešojo transporto GPS padėties duomenys

Rinkiniuose pateikiama viešojo transporto GPS informacija. Viešojo transporto padėties informacija matuojama kas 5-20 sekundžių. Duomenys atnaujinami kartą per dieną. Pateikiama informacija apie transporto rūšį, maršrutą, reiso identifikatorių, mašinos numerį, mašinos koordinates matavimo metu WGS-84 ir LKS-94 koordinačių sistemose, greitį, azimutą, reiso pradžią, nuokrypį nuo grafiko sekundėmis, mašinos tipą, matavimo datą ir laiką. Rinkinių objektas – vienos transporto priemonės GPS koordinatės laike. Duomenys nuo 2025-07-01.

- **Namespace:** `datasets/gov/viesasis_transport/gps_duomenys`[^manifest]
- **Manifest CSV:** [datasets/gov/viesasis_transport/gps_duomenys.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/viesasis_transport/gps_duomenys.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/viesasis_transport/gps_duomenys`
- **Parent Namespace (`ns`):** Viešojo transporto duomenys (`datasets/gov/viesasis_transport`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KaunasViesasisTransportas](gps_duomenys/KaunasViesasisTransportas.md) | Kauno viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | 16 | — |
| [VilniusViesasisTransportas](gps_duomenys/VilniusViesasisTransportas.md) | Vilniaus viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | 16 | — |
| [KlaipedaViesasisTransportas](gps_duomenys/KlaipedaViesasisTransportas.md) | Klaipėdos viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | 16 | — |
| [TaurageViesasisTransportas](gps_duomenys/TaurageViesasisTransportas.md) | Tauragės viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | 16 | — |
| [AlytusViesasisTransportas](gps_duomenys/AlytusViesasisTransportas.md) | Alytaus viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | 16 | — |
| [PanevezysViesasisTransportas](gps_duomenys/PanevezysViesasisTransportas.md) | Panevėžio viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | 16 | — |
| [DruskininkaiViesasisTransportas](gps_duomenys/DruskininkaiViesasisTransportas.md) | Druskininkų viešojo transporto GPS padėties duomenys | `4` | `vda_prime_key` | — | 16 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/viesasis_transport/gps_duomenys.csv
