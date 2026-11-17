---
type: Table
title: "AsmenybeGatve — Gatvės pavadintos asmenybių vardais"
description: "Duomenys iš „ID Vilnius“ apie gatves, kurioms suteikti asmenybių vardų pavadinimai."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeGatve"
tags: [gov, id_vilnius, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L48"
    last_modified: "2026-11-11T14:39:20Z"
---

# AsmenybeGatve — Gatvės pavadintos asmenybių vardais

Duomenys iš „ID Vilnius“ apie gatves, kurioms suteikti asmenybių vardų pavadinimai. Viena lentelės eilutė atitinka vieną gatvę su jai priskirta asmenybe. Eilutės informaciją sudaro unikalios eilutės ir asmenybės identifikaciniai numeriai, gatvės pavadinimas ir geometrinis gatvės liniją atvaizduojantis stulpelis.

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeGatve`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L48)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeGatve`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | — |
| `asmenybes_id` | `string` | — | `4` | `open` | — | Asmens susijusio su gatve identifikacinis numeris | — |
| `pav` | `string` | — | `4` | `open` | — | Gatvės pavadinimas | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Gatvės koordinatės WGS-84 koordinačių sistemoje | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv
