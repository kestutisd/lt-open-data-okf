---
type: Table
title: "Darbuotojas — Aktualūs asmens sveikatos priežiūros įstaigų personalo duomenys"
description: "UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigose (ASPĮ), naudojančiose ESIS, dirbančio personalo tarnybinius duomenis."
resource: "https://get.data.gov.lt/datasets/gov/esis/med_personalas/Darbuotojas"
tags: [gov, esis, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/esis/med_personalas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/med_personalas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Darbuotojas — Aktualūs asmens sveikatos priežiūros įstaigų personalo duomenys

UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigose (ASPĮ), naudojančiose ESIS, dirbančio personalo tarnybinius duomenis. Priklausomai nuo ASPĮ, duomenų laiko aprėptis gali skirtis, tačiau duomenys yra atnaujinami kasdien. Duomenų rinkinį sudaro: ASPĮ JAR kodas, pavadinimas ir savivaldybė, darbuotojo pseudonimizuotas asmens kodas, darbuotojui priskirtas padalinys, einamos pareigos ir ataskaitinė data, nurodanti esamo duomenų įrašo aktualumą.

- **Model:** `datasets/gov/esis/med_personalas/Darbuotojas`[^manifest]
- **Dataset:** [Aktualūs asmens sveikatos priežiūros įstaigų personalo duomenys](../med_personalas.md) (`datasets/gov/esis/med_personalas`)
- **Manifest CSV:** [datasets/gov/esis/med_personalas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/med_personalas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/esis/med_personalas/Darbuotojas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `aspi_jar_kodas` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos JAR kodas | — |
| `aspi_pavadinimas` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos pavadinimas | — |
| `aspi_savivaldybe` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos savivaldybė | — |
| `aspi_padalinys` | `string` | — | `4` | `open` | — | Darbuotojui priskirtas padalinys | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Darbuotojo pseudonomizuotas asmens kodas | — |
| `pareigos` | `string` | — | `4` | `open` | — | Darbuotojo einamos pareigos | — |
| `ataskaitine_data` | `datetime` | `S` | `4` | `open` | — | Data, nuo kada aktualūs duomenys esamame įraše | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/esis/med_personalas.csv
