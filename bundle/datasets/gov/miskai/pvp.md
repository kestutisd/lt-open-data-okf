---
type: Dataset
title: "datasets/gov/miskai/pvp"
description: "Spinta dataset datasets/gov/miskai/pvp (9 tables)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/pvp"
tags: [gov, miskai, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/pvp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/miskai/pvp

- **Namespace:** `datasets/gov/miskai/pvp`[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/pvp.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/pvp.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/pvp`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PVPBukle](pvp/PVPBukle.md) | Projekto būklė | `4` | — | — | 1 | — |
| [PrivacValduProjektas](pvp/PrivacValduProjektas.md) | Privačių miškų vidinės miškotvarkos projektas | `4` | — | — | 9 | — |
| [PVPAutorius](pvp/PVPAutorius.md) | Projekto autorius | `4` | — | — | 1 | — |
| [Rajonas](pvp/Rajonas.md) | Savivaldybė | `4` | — | — | 1 | — |
| [PVPBuklesKaita](pvp/PVPBuklesKaita.md) | Projekto būklės data | `4` | — | — | 3 | — |
| [Vietove](pvp/Vietove.md) | Vietovė | `4` | — | — | 2 | Vietovė / Blokas : Sklypas = kadastro numeris |
| [BlokuSklypas](pvp/BlokuSklypas.md) | Sklypas | `4` | — | — | 3 | Vietovė / Blokas : Sklypas = kadastro numeris |
| [PVPKadSklypas](pvp/PVPKadSklypas.md) | PVP sklypai | `4` | — | — | 2 | — |
| [VietovesBlokas](pvp/VietovesBlokas.md) | Blokas | `4` | — | — | 3 | Vietovė / Blokas : Sklypas = kadastro numeris |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/pvp.csv
