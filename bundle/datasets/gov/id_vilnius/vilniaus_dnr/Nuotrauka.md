---
type: Table
title: "Nuotrauka — Vilniaus miesto nuotraukos"
description: "Duomenys iš „ID Vilnius“ apie istorines Vilniaus miesto fotografijas ir atvirutes."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/Nuotrauka"
tags: [gov, id_vilnius, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L120"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nuotrauka — Vilniaus miesto nuotraukos

Duomenys iš „ID Vilnius“ apie istorines Vilniaus miesto fotografijas ir atvirutes. Viena eilutė yra viena unikali nuotrauka ar atvirutė. Eilutės informaciją sudaro nuotraukos identifikacinis numeris, pavadinimas, tipas, autorius, nuotraukos aprašymas, laikotarpis, šaltinis, šaltinio nuoroda, nuotraukos nuoroda ir preliminari nuotraukos atlikimo vieta koordinačių sistemoje.

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/Nuotrauka`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L120](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L120)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/Nuotrauka`
- **Primary Key (`ref`):** `nuotraukos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nuotraukos_id` | `string` | — | `4` | `open` | — | Nuotraukos identifikacinis numeris (pirminis raktas) | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Nufotografuto objekto pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Nufotografuoto objekto tipas | — |
| `autorius` | `string` | — | `4` | `open` | — | Nuotraukos autorius | — |
| `aprasymas` | `string` | — | `4` | `open` | — | Nuotraukos aprašymas | — |
| `laikotarpis` | `string` | — | `4` | `open` | — | Laikotarpis | Laikotarpis, kada buvo atlikta nuotrauka |
| `laikotarpio_pradzia` | `date` | `Y` | `4` | `open` | — | Laikotarpio pradžia | Laiko intervalo pradžia, kada nuotrauka galėjo būti atlikta |
| `laikotarpio_pabaiga` | `date` | `Y` | `4` | `open` | — | Laikotarpio pabaiga | Laiko intervalo pabaiga, kada nuotrauka galėjo būti atlikta |
| `saltinis` | `string` | — | `4` | `open` | — | Nuotraukos šaltinio pavadinimas | — |
| `saltinio_nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į šaltinį | — |
| `nuotraukos_nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į nuotrauką | — |
| `geometrija` | `geometry(4326)` | — | `4` | `open` | — | Geometrija | WGS-84 koordinatės taškas, kuriame galėjo būti atlikta nuotrauka |

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv
