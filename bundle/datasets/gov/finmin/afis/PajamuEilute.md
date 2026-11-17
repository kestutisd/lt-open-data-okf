---
type: Table
title: "PajamuEilute — Valstybės pajamų duomenys"
description: "Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui numatyti automatiškai apdorojami viešųjų finansų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/finmin/afis/PajamuEilute"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/afis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PajamuEilute — Valstybės pajamų duomenys

Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui numatyti automatiškai apdorojami viešųjų finansų duomenys. Duomenų rinkinį sudaro: pajamų kodai ir 2–4 lygio straipsniai, pradinis pajamų planas, patikslintas pajamų planas ir tikrasis pajamų kiekis pagal ataskaitinio ketvirčio paskutinės dienos informaciją.

- **Model:** `datasets/gov/finmin/afis/PajamuEilute`[^manifest]
- **Dataset:** [Valstybės pajamų ir išlaidų duomenys](../afis.md) (`datasets/gov/finmin/afis`)
- **Manifest CSV:** [datasets/gov/finmin/afis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/afis/PajamuEilute`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `ataskaitinis_periodas` | `date` | `D` | `4` | `open` | — | Paskutinė metų ketvirčio diena | — |
| `pajamu_kodo_lygis_2` | `string` | — | `4` | `open` | — | 2-o lygio pajamų grupės kodas | — |
| `pajamu_straipsnio_lygis_2` | `string` | — | `4` | `open` | — | 2-o lygio pajamų grupės pavadinimas | — |
| `pajamu_kodo_lygis_3` | `string` | — | `4` | `open` | — | 3-io lygio pajamų grupės kodas | — |
| `pajamu_straipsnio_lygis_3` | `string` | — | `4` | `open` | — | 3-io lygio pajamų grupės pavadinimas | — |
| `pajamu_kodo_lygis_4` | `string` | — | `4` | `open` | — | 4-o lygio pajamų grupės kodas | — |
| `pajamu_straipsnio_lygis_4` | `string` | — | `4` | `open` | — | 4-o lygio pajamų straipsnis | — |
| `planas` | `number` | — | `4` | `open` | — | Pradinis pajamų planas | — |
| `patikslintas_planas` | `number` | — | `4` | `open` | — | Patikslintas pajamų planas | — |
| `vykdymas` | `number` | — | `4` | `open` | — | Pajamų kiekis vykdant planą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/afis.csv
