---
type: Table
title: "AsmenybeGatve — Gatvės pavadintos asmenybių vardais"
description: "\"Duomenys iš „ID Vilnius“ apie gatves, kurioms suteikti asmenybių vardų pavadinimai."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeGatve"
tags: [gov, id_vilnius, asmenybegatve, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L48"
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L48"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# AsmenybeGatve — Gatvės pavadintos asmenybių vardais

"Duomenys iš „ID Vilnius“ apie gatves, kurioms suteikti asmenybių vardų pavadinimai. Viena lentelės eilutė atitinka vieną gatvę su jai priskirta asmenybe. Eilutės informaciją sudaro unikalios eilutės ir asmenybės identifikaciniai numeriai, gatvės pavadinimas ir geometrinis gatvės liniją atvaizduojantis stulpelis."[^manifest]

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeGatve`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)[^manifest]
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L48)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeGatve` (`deployed`)[^manifest]
- **Provider:** `id_vilnius`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `asmenybes_id` | `string` | — | `4` | `open` | — | Asmens susijusio su gatve identifikacinis numeris | — |
| `pav` | `string` | — | `4` | `open` | — | Gatvės pavadinimas | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Gatvės koordinatės WGS-84 koordinačių sistemoje | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L48 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L48)
