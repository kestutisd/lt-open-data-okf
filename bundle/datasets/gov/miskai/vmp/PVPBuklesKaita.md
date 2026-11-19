---
type: Table
title: "PVPBuklesKaita — PVP būklės kaita"
description: "Iš šios lentelės skaičiuojama, ar PVP autoriai buvo parengę projektų per pastaruosius 1 ir 3 metus"
resource: "https://get.data.gov.lt/datasets/gov/miskai/vmp/PVPBuklesKaita"
tags: [gov, miskai, pvpbukleskaita, deployed, level-4, cadence-irreg]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L20"
    title: "atviriduomenys/manifest — datasets/gov/miskai/vmp.csv#L20"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/916/"
    title: "data.gov.lt DCAT-AP — datasets/gov/miskai/vmp"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# PVPBuklesKaita — PVP būklės kaita

Iš šios lentelės skaičiuojama, ar PVP autoriai buvo parengę projektų per pastaruosius 1 ir 3 metus[^manifest]

- **Model:** `datasets/gov/miskai/vmp/PVPBuklesKaita`[^manifest]
- **Dataset:** [Privačių vidinės miškotvarkos projektų rengėjų sąrašas](../vmp.md) (`datasets/gov/miskai/vmp`)[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/vmp.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L20)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/vmp/PVPBuklesKaita` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `IRREG`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `bukle` | `ref` | [PVPBukle](PVPBukle.md) (`level=4 UUID`: `bukle._id`) | `4` | `open` | — | Būklė | — |
| `bukles_data` | `datetime` | — | `4` | `open` | — | Patvirtinto projekto data | Požymis, ar PVP autorius per pastaruosius 1 ir 3 metus buvo parengęs PVP projektų |
| `pvp` | `ref` | [PrivacValduProjektas](PrivacValduProjektas.md) (`level=4 UUID`: `pvp._id`) | `4` | `open` | — | Privatus vidinės miškotvarkos projektas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/vmp.csv#L20 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/vmp.csv#L20)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/miskai/vmp (https://data.gov.lt/datasets/916/)
