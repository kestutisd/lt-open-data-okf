---
type: Table
title: "LovuProfilis — Aktualūs asmens sveikatos priežiūros įstaigų lovų skaičiai"
description: "UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigų (ASPĮ), naudojančių ESIS, turimų lovų duomenis."
resource: "https://get.data.gov.lt/datasets/gov/esis/lovu_skaiciai/LovuProfilis"
tags: [gov, esis, lovuprofilis, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/lovu_skaiciai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/esis/lovu_skaiciai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2707/"
    title: "data.gov.lt DCAT-AP — datasets/gov/esis/lovu_skaiciai"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# LovuProfilis — Aktualūs asmens sveikatos priežiūros įstaigų lovų skaičiai

UAB „Varutis“ vystoma ir administruojama Elektroninė sveikatos istorijos sistema (ESIS) kaupia asmens sveikatos priežiūros įstaigų (ASPĮ), naudojančių ESIS, turimų lovų duomenis. Priklausomai nuo ASPĮ, duomenų laiko aprėptis gali skirtis, tačiau duomenys yra atnaujinami kasdien. Duomenų rinkinį sudaro: ASPĮ JAR kodas, pavadinimas ir savivaldybė, lovos profilio pavadinimas, bendras visų atitinkamo profilio lovų skaičius ir laikinai nepildomas, einamąją dieną užimtų lovų skaičius.[^manifest]

- **Model:** `datasets/gov/esis/lovu_skaiciai/LovuProfilis`[^manifest]
- **Dataset:** [Aktualūs asmens sveikatos priežiūros įstaigų lovų skaičiai](../lovu_skaiciai.md) (`datasets/gov/esis/lovu_skaiciai`)[^manifest]
- **Manifest CSV:** [datasets/gov/esis/lovu_skaiciai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/lovu_skaiciai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/esis/lovu_skaiciai/LovuProfilis` (`deployed`)[^manifest]
- **Provider:** `esis`[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `aspi_jar_kodas` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos JAR kodas | — |
| `aspi_pavadinimas` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos pavadinimas | — |
| `aspi_savivaldybe` | `string` | — | `4` | `open` | — | Asmens sveikatos priežiūros įstaigos savivaldybė | — |
| `lovos_profilis` | `string` | — | `4` | `open` | — | Lovų profilio pavadinimas | — |
| `is_viso_lovu_sk` | `integer` | `U` | `4` | `open` | — | Bendras lovų skaičius | — |
| `uzimtu_lovu_sk` | `integer` | `U` | `4` | `open` | — | Faktinis užimtų lovų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/esis/lovu_skaiciai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/esis/lovu_skaiciai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/esis/lovu_skaiciai (https://data.gov.lt/datasets/2707/)
