---
type: Table
title: "AsmenybeRysys — Vilniuje įamžintų asmenybių tarpusavio ryšiai"
description: "\"Duomenys iš „ID Vilnius“ apie Vilniuje įamžintų asmenybių tarpusavio ryšius."
resource: "https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeRysys"
tags: [gov, id_vilnius, asmenyberysys, deployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L54"
    title: "atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L54"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# AsmenybeRysys — Vilniuje įamžintų asmenybių tarpusavio ryšiai

"Duomenys iš „ID Vilnius“ apie Vilniuje įamžintų asmenybių tarpusavio ryšius. Vienoje lentelės eilutėje nurodomas vienas ryšys tarp dviejų Vilniuje įamžintų asmenybių. Eilutės informaciją sudaro ryšio, asmenybės ir susijusios asmenybės identifikaciniai numeriai iri ryšio tipas. Jei nėra nurodytas susijusios asmenybės identifikacinis numeris, tuomet paskutiniame stulpelyje įrašomas susijusios asmenybės vardas ir pavardė."[^manifest]

- **Model:** `datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeRysys`[^manifest]
- **Dataset:** [Vilniaus miesto istoriniai duomenys - Vilniaus DNR](../vilniaus_dnr.md) (`datasets/gov/id_vilnius/vilniaus_dnr`)[^manifest]
- **Manifest CSV:** [datasets/gov/id_vilnius/vilniaus_dnr.csv#L54](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L54)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/id_vilnius/vilniaus_dnr/AsmenybeRysys` (`deployed`)[^manifest]
- **Provider:** `id_vilnius`[^manifest]
- **Primary Key (`ref`):** `rysio_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `rysio_id` | `string` | — | `4` | `open` | — | Asmenybių ryšio identifikacinis numeris (pirminis raktas) | — |
| `asmenybes_id` | `string` | — | `4` | `open` | — | Asmenybės identifikacinis numeris | — |
| `susijusios_asmenybes_id` | `string` | — | `4` | `open` | — | Susijusios asmenybės identifikacinis numeris | — |
| `rysio_tipas` | `string` | — | `4` | `open` | — | Asmenybių ryšio tipas | — |
| `susijes_asmuo_text` | `string` | — | `4` | `open` | — | Susijusi asmenybė | "Susijusios asmenybės vardas ir pavardė, kuomet nėra susijusios asmenybės identifikacinio numerio" |

[^manifest]: atviriduomenys/manifest — datasets/gov/id_vilnius/vilniaus_dnr.csv#L54 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/id_vilnius/vilniaus_dnr.csv#L54)
