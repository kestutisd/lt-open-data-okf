---
type: Table
title: "PajamuEilute — Valstybės pajamų duomenys"
description: "Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui numatyti automatiškai apdorojami viešųjų finansų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/finmin/afis/PajamuEilute"
tags: [gov, finmin, pajamueilute, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/finmin/afis.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2771/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/afis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PajamuEilute — Valstybės pajamų duomenys

Lietuvos Respublikos finansų ministerijos Atvirų finansų informacinėje sistemoje (AFIS) nuo 2015 m. kaupiami, kas 3 mėnesius atnaujinami ir atvėrimui numatyti automatiškai apdorojami viešųjų finansų duomenys. Duomenų rinkinį sudaro: pajamų kodai ir 2–4 lygio straipsniai, pradinis pajamų planas, patikslintas pajamų planas ir tikrasis pajamų kiekis pagal ataskaitinio ketvirčio paskutinės dienos informaciją.[^manifest]

- **Model:** `datasets/gov/finmin/afis/PajamuEilute`[^manifest]
- **Dataset:** [Valstybės pajamų ir išlaidų duomenys](../afis.md) (`datasets/gov/finmin/afis`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/afis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/afis/PajamuEilute` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/afis.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/afis.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/afis (https://data.gov.lt/datasets/2771/)
