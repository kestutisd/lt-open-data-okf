---
type: Table
title: "AtminimoObjektas — Skulptūros ir atminimo lentos"
description: "\"Duomenys iš „ID Vilnius“ apie Vilniaus mieste esančias atminimo lentas, skulptūras, kitus meninius ar mažosios architektūros objektus bei programos „Kuriu Vilnių“ metu įgyvendintus meno projektus."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/AtminimoObjektas"
tags: [gov, id_vilnius, atminimoobjektas, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L61"
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L61"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# AtminimoObjektas — Skulptūros ir atminimo lentos

"Duomenys iš „ID Vilnius“ apie Vilniaus mieste esančias atminimo lentas, skulptūras, kitus meninius ar mažosios architektūros objektus bei programos „Kuriu Vilnių“ metu įgyvendintus meno projektus. Viena lentelės eilutė yra vienas unikalus objektas. Eilutės informaciją sudaro objekto identifikacinis numeris, pavadinimas, ant objekto esantis tekstas, objekto aprašymas, seniūnija, adresas ir geolokacija, kur objektas yra pastatytas, objekto įrengimo data, užsakovas, autorius, architektas, skulptorius, informacija apie objekto konstrukciją. Paskutiniai du stulpeliai nurodo, ar objektas yra pašalintas ir kada pašalintas."[^manifest]

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/AtminimoObjektas`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)[^manifest]
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L61](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L61)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/AtminimoObjektas` (`deployed`)[^manifest]
- **Provider:** `id_vilnius`[^manifest]
- **Primary Key (`ref`):** `objekto_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `objekto_id` | `string` | — | `4` | `open` | — | Skulptūros arba atminimo objekto identifikacinis numeris (pirminis raktas) | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Skulptūros arba atminimo objekto pavadinimas | — |
| `tekstas` | `string` | — | `4` | `open` | — | Tekstas esantis ant skulptūros arba atminimo objekto | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Skulptūros arba atminimo objekto aprašymas | — |
| `seniunija` | `string` | — | `4` | `open` | — | Seniūnija | "Seniūnijos pavadinimas, kuriame stovi skulptūra arba atminimo objektas" |
| `lokacija` | `string` | — | `4` | `open` | — | Skulptūros arba atminimo objekto adresas | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Geometrija | Skulptūros arba atminimo objekto koordinatės WGS-84 koordinačių sistemoje |
| `irengtas` | `date` | `D` | `4` | `open` | — | Skulptūros arba atminimo objekto įrengimo data | — |
| `uzsakovas` | `string` | — | `3` | `open` | — | Skulptūros arba atminimo objekto užsakovas | — |
| `autorius` | `string` | — | `4` | `open` | — | Skulptūros arba atminimo objekto sumanymo autorius | — |
| `architektas` | `string` | — | `4` | `open` | — | Skulptūros arba atminimo objekto architektas | — |
| `skulptorius` | `string` | — | `4` | `open` | — | Skulptūros arba atminimo objekto skulptorius | — |
| `konstrukc` | `string` | — | `3` | `open` | — | Konstrukcija iš kurios sudaryta skulptūra arba atminimo objektas | — |
| `obj_pasal` | `boolean` | — | `4` | `open` | — | Objektas pašalintas | "Požymis, nurodantis, ar skulptūra arba atminimo objektas yra pašalintas" |
| `obj_pasal_data` | `date` | `Y` | `4` | `open` | — | Skulptūros arba atminimo objekto pašalinimo data | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L61 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L61)
