---
type: Table
title: "Rodiklis — \"Lentelėje pateikti valstybės strategijų, programų rodiklių duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). \""
description: "Spinta table datasets/gov/finmin/sis/Rodiklis (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sis/Rodiklis"
tags: [gov, finmin, rodiklis, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L36"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv#L36"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2862/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Rodiklis — "Lentelėje pateikti valstybės strategijų, programų rodiklių duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos...

- **Model:** `datasets/gov/finmin/sis/Rodiklis`[^manifest]
- **Dataset:** [Stebėsenos informacinė sistemos dokumentai, elementų hierarchija, finansiniai ir rodiklių duomenys](../sis.md) (`datasets/gov/finmin/sis`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sis/finmin.csv#L36](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L36)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sis/Rodiklis` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id_planas`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id_planas` | `string` | — | `4` | `open` | — | "Unikalus identifikatorius" | — |
| `id_faktas` | `string` | — | `4` | `open` | — | "Fakto unikalus identifikatorius" | — |
| `doc_id` | `string` | — | `4` | `open` | — | "Dokumento kodas, atvaizduojamas ataskaitose." | — |
| `obj_id` | `string` | — | `4` | `open` | — | "Žemesnio lygmens objektas (objektas-vaikas). Nuoroda į OBJECTS.OBJ_ID." | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | "Laikotarpio pradžios diena." | — |
| `data_iki` | `date` | `D` | `4` | `open` | — | "Laikotarpio pabaigos diena." | — |
| `plano_reiksme_kiekybine` | `number` | — | `4` | `open` | — | "Rodiklio plano kiekybinė reikšmė" | — |
| `plano_reiksme_kokybine` | `string` | — | `4` | `open` | — | "Rodiklio plano kokybinė reikšmė" | — |
| `fakto_reiksme_kiekybine` | `number` | — | `4` | `open` | — | "Faktinė rodiklio reikšmė." | — |
| `fakto_reiksme_kokybine` | `string` | — | `4` | `open` | — | "Faktinė rodiklio reikšmė (simbolinio tipo)." | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv#L36 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L36)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sis (https://data.gov.lt/datasets/2862/)
