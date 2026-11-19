---
type: Table
title: "Gatve — Vilniaus gatvės ir istoriniai jų pavadinimai"
description: "\"Duomenys iš „ID Vilnius“ apie Vilniaus miesto gatves ir kai kurių gatvių istorinius pavadinimus."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/Gatve"
tags: [gov, id_vilnius, gatve, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L78"
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L78"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gatve — Vilniaus gatvės ir istoriniai jų pavadinimai

"Duomenys iš „ID Vilnius“ apie Vilniaus miesto gatves ir kai kurių gatvių istorinius pavadinimus. Viena lentelės eilutė yra dabartinė gatvė ir jos istorinis pavadinimas. Jei gatvė neturi informacijos apie istorinį pavadinimą, tuomet nurodomas tik dabartinis gatvės pavadinimas su jos koordinatėmis. Eilutės informaciją sudaro dabartinės gatvės identifikacinis numeris, klasė, poklasis, pavadinimas, pavadinimo reikšmė ir gatvės koordinačių linija, taip pat istorinės gatvės identifikacinis numeris, pavadinimas, žemėlapio, kuriame gatvė nustatyta,sudarymo metai ir istorinės gatvės lokacija koordinačių sistemoje."[^manifest]

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/Gatve`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)[^manifest]
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L78](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L78)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/Gatve` (`deployed`)[^manifest]
- **Provider:** `id_vilnius`[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | "Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius (pirminis raktas) sudarytas iš stulpelių dabartine_gatve_id ir istorine_gatve_id" |
| `dabartine_gatve_id` | `string` | — | `4` | `open` | — | Dabar egzistuojančios gatvės identifikacinis numeris | — |
| `klase` | `string` | — | `4` | `open` | — | Dabar egzistuojančios gatvės klasė | — |
| `poklasis` | `string` | — | `4` | `open` | — | Dabar egzistuojančios gatvės poklasis | — |
| `dabartine_gatve` | `string` | — | `4` | `open` | — | Dabartinės gatvės pavadinimas | — |
| `gatves_paaiskinimas` | `string` | — | `4` | `open` | — | Dabartinės gatvės pavadinimo paaiškinimas | — |
| `dabartine_geometrija` | `geometry(4326)` | — | `4` | `open` | — | Dabartinės gatvės linijinės koordinatės WGS-84 formatu | — |
| `istorine_gatve_id` | `string` | — | `4` | `open` | — | Istorinės gatvės identifikacinis numeris | — |
| `istorine_gatve` | `string` | — | `4` | `open` | — | Istorinės gatvės pavadinimas | — |
| `zemelapio_metai` | `date` | `Y` | `4` | `open` | — | Žemėlapio metai | "Žemėlapio sudarymo metai, kuriame yra istorinė gatvė" |
| `istorine_geometrija` | `geometry(4326)` | — | `4` | `open` | — | Istorinės gatvės koordinatės WGS-84 formatu | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L78 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L78)
