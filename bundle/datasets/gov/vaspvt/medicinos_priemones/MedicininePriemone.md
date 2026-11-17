---
type: Table
title: "MedicininePriemone — Sveikatos priežiūros įstaigų įsigytos medicininės priemonės"
description: "Spinta table datasets/gov/vaspvt/medicinos_priemones/MedicininePriemone (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/medicinos_priemones/MedicininePriemone"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_priemones.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_priemones.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# MedicininePriemone — Sveikatos priežiūros įstaigų įsigytos medicininės priemonės

- **Model:** `datasets/gov/vaspvt/medicinos_priemones/MedicininePriemone`[^manifest]
- **Dataset:** [Sveikatos priežiūros įstaigų įsigytos medicininės priemonės](../medicinos_priemones.md) (`datasets/gov/vaspvt/medicinos_priemones`)
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_priemones.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_priemones.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/medicinos_priemones/MedicininePriemone`
- **Primary Key (`ref`):** `pri_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pri_id` | `string` | — | `4` | `open` | — | Prietaiso ID | Medicinos priemonės unikalus identifikacinis numeris |
| `pavadinimas` | `string` | — | `4` | `open` | — | Pavadinimas | Bendrinis medicinos priemonės pavadinimas |
| `modelis` | `string` | — | `4` | `open` | — | Modelis | Medicinos priemonės modelis |
| `ce_zyma` | `boolean` | — | `4` | `open` | — | CE žyma | Indikatorius, ar medicinos prietaisas turi CE ženklinimą (Conformite Europeene), reiškiantį atitiktį ES saugos reikalavimams |
| `ce_nr` | `string` | — | `4` | `open` | — | CE numeris | Notifikuotosios įstaigos identifikacinis numeris |
| `savininko_kodas` | `string` | — | `4` | `open` | — | Savininko kodas | Sveikatos priežiūros įstaigos, kuriai priklauso priemonė, JAR kodas |
| `savininko_pav` | `string` | — | `4` | `open` | — | Savininko pavadinimas | Sveikatos priežiūros įstaigos, kuriai priklauso priemonė, pavadinimas |
| `pagaminta` | `date` | `Y` | `4` | `open` | — | Pagaminimo data | Medicinos priemonės pagaminimo data |
| `isigyta` | `date` | `Y` | `4` | `open` | — | Įsigijimo data | Medicinos priemonės įsigijimo data |
| `pradetas_naudoti` | `date` | `Y` | `4` | `open` | — | Pradėjimo naudoti data | Medicinos priemonės naudojimo pradžios data |
| `naudojimas_nutrauktas` | `date` | `D` | `4` | `open` | — | Naudojimas nutrauktas | Data, kada medicinos priemonės naudojimas buvo galutinai nutrauktas |
| `nutraukimo_priezastis_lt` | `string` | — | `4` | `open` | — | Nutraukimo priežastis | Priežastis, kodėl medicinos priemonė nebenaudojama |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nutraukimo_priezastis_lt` | `update(property: "nutraukimo_priezastis_lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_priemones.csv
