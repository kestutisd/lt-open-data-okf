---
type: Table
title: "PVPBuklesKaita — PVP būklės kaita"
description: "Iš šios lentelės skaičiuojama, ar PVP autoriai buvo parengę projektų per pastaruosius 1 ir 3 metus"
resource: "https://get.data.gov.lt/datasets/gov/miskai/vmp/PVPBuklesKaita"
tags: [gov, miskai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/miskai/vmp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# PVPBuklesKaita — PVP būklės kaita

Iš šios lentelės skaičiuojama, ar PVP autoriai buvo parengę projektų per pastaruosius 1 ir 3 metus

- **Model:** `datasets/gov/miskai/vmp/PVPBuklesKaita`[^manifest]
- **Dataset:** [datasets/gov/miskai/vmp](../vmp.md) (`datasets/gov/miskai/vmp`)
- **Manifest CSV:** [datasets/gov/miskai/vmp.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/vmp/PVPBuklesKaita`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bukle` | `ref` | [PVPBukle](PVPBukle.md) | `4` | `open` | — | Būklė | — |
| `bukles_data` | `datetime` | — | `4` | `open` | — | Patvirtinto projekto data | Požymis, ar PVP autorius per pastaruosius 1 ir 3 metus buvo parengęs PVP projektų |
| `pvp` | `ref` | [PrivacValduProjektas](PrivacValduProjektas.md) | `4` | `open` | — | Privatus vidinės miškotvarkos projektas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/vmp.csv
