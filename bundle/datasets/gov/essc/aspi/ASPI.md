---
type: Table
title: "ASPI — ASPĮ aprūpinimas AAP"
description: "Ekstremalių sveikatai situacijų centras (ESSC) kaupia sveikatos priežiūros įstaigų aprūpinimo asmens apsaugos priemonėmis bei jų sunaudojimo ir atstatymo duomenis, gaunamus iš Sveikatos apsaugos ministerijos."
resource: "https://get.data.gov.lt/datasets/gov/essc/aspi/ASPI"
tags: [gov, essc, aspi, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/aspi.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/essc/aspi.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2619/"
    title: "data.gov.lt DCAT-AP — datasets/gov/essc/aspi"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ASPI — ASPĮ aprūpinimas AAP

Ekstremalių sveikatai situacijų centras (ESSC) kaupia sveikatos priežiūros įstaigų aprūpinimo asmens apsaugos priemonėmis bei jų sunaudojimo ir atstatymo duomenis, gaunamus iš Sveikatos apsaugos ministerijos. Duomenys kaupiami nuo 2023 m. ir atnaujinami balandžio bei spalio mėnesiais. Duomenys apima datą, nuo kada aktualūs turimi duomenys, įstaigos ir priemonės pavadinimus, priemonės paskirtį, išduotą, panaudotą, turimą ir atstatytą priemonės kiekius bei atstatymo datą.[^manifest]

- **Model:** `datasets/gov/essc/aspi/ASPI`[^manifest]
- **Dataset:** [ASPĮ aprūpinimas AAP](../aspi.md) (`datasets/gov/essc/aspi`)[^manifest]
- **Manifest CSV:** [datasets/gov/essc/aspi.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/aspi.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/essc/aspi/ASPI` (`deployed`)[^manifest]
- **Provider:** `essc` — Ekstremalių sveikatai situacijų centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `duomenu_aktualumo_data` | `date` | `M` | `4` | `open` | — | Nuo kada aktualūs turimi duomenys | — |
| `aspi_pavadinimas` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos pavadinimas | — |
| `priemones_pavadinimas` | `string` | — | `4` | `open` | — | Priemonės pavadinimas | — |
| `isduotas_kiekis` | `integer` | — | `4` | `open` | — | Išduotas priemonės kiekis | — |
| `panaudotas_kiekis` | `integer` | — | `4` | `open` | — | Panaudotas priemonės kiekis | — |
| `panaudojimo_tikslas` | `string` | — | `4` | `open` | — | Priemonės paskirtis | — |
| `atstatytas_kiekis` | `integer` | — | `4` | `open` | — | Atkurtas priemonės kiekis | — |
| `planuojama_atstatymo_data` | `date` | `D` | `4` | `open` | — | Kada planuojama atkurti pradinį priemonės kiekį | — |
| `turimas_kiekis` | `integer` | — | `4` | `open` | — | Aktualiu metu turimas priemonės kiekis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/essc/aspi.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/essc/aspi.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/essc/aspi (https://data.gov.lt/datasets/2619/)
