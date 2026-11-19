---
type: Table
title: "FinansinisDuomuo — \"Lentelėje pateikti valstybės strategijų, programų finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). \""
description: "Spinta table datasets/gov/finmin/sis/FinansinisDuomuo (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sis/FinansinisDuomuo"
tags: [gov, finmin, finansinisduomuo, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L48"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv#L48"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2862/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# FinansinisDuomuo — "Lentelėje pateikti valstybės strategijų, programų finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos...

- **Model:** `datasets/gov/finmin/sis/FinansinisDuomuo`[^manifest]
- **Dataset:** [Stebėsenos informacinė sistemos dokumentai, elementų hierarchija, finansiniai ir rodiklių duomenys](../sis.md) (`datasets/gov/finmin/sis`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sis/finmin.csv#L48](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L48)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sis/FinansinisDuomuo` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `fnv_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fnv_id` | `string` | — | `4` | `open` | — | "Įrašo identifikacinis numeris. Generuojamas seka FNV_SEQ." | — |
| `doc_id` | `string` | — | `4` | `open` | — | "Dokumento kodas, atvaizduojamas ataskaitose." | — |
| `obj_id` | `string` | — | `4` | `open` | — | "Žemesnio lygmens objektas (objektas-vaikas). Nuoroda į OBJECTS.OBJ_ID." | — |
| `pradz_data` | `date` | `D` | `4` | `open` | — | "Finansavimo pradžios data" | — |
| `pabaig_data` | `date` | `D` | `4` | `open` | — | "Finansavimo pabaigos data" | — |
| `verte_eur` | `number` | — | `4` | `open` | — | "Planinė arba faktinė objekto finansinio rodiklio reikšmė (EUR)." | — |
| `pozymis_1` | `string` | — | `4` | `open` | — | "Požymis, ar planas, faktas, poreikis." | — |
| `islaidu_tipas` | `string` | — | `4` | `open` | — | "Išlaidų tipas." | — |
| `finansavimo_saltinis` | `string` | — | `4` | `open` | — | "Finansavimo šaltinio pavadinimas." | — |
| `pozymis_2` | `string` | — | `4` | `open` | — | "Lėšų tipas." | — |
| `valst_funkcijos_pav` | `string` | — | `4` | `open` | — | "Valstybės funkcijos pavadinimas." | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv#L48 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L48)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sis (https://data.gov.lt/datasets/2862/)
