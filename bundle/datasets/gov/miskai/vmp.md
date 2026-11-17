---
type: Dataset
title: "datasets/gov/miskai/vmp"
description: "Spinta dataset datasets/gov/miskai/vmp (4 tables)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/vmp"
tags: [gov, miskai, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/vmp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/miskai/vmp

- **Namespace:** `datasets/gov/miskai/vmp`[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/vmp.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/vmp`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PVPBukle](vmp/PVPBukle.md) | PVP būklė | `4` | — | — | 1 | Reikalinga požymiui, ar PVP autorius per pastaruosius 1 ar 3 metus buvo parengęs patvirtintų projektų |
| [PrivacValduProjektas](vmp/PrivacValduProjektas.md) | Privačių valdų projektas | `4` | — | — | 7 | Informacija apie projektą, kurį parengė PVP autorius |
| [PVPAutorius](vmp/PVPAutorius.md) | PVP autorius | `4` | — | — | 2 | Informacija apie privačių miškų vidinės miškotvarkos projektų autorius |
| [PVPBuklesKaita](vmp/PVPBuklesKaita.md) | PVP būklės kaita | `4` | — | — | 3 | Iš šios lentelės skaičiuojama, ar PVP autoriai buvo parengę projektų per pastaruosius 1 ir 3 metus |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/vmp.csv
