---
type: Table
title: "DarboVertinimas — Universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys"
description: "Lentelėje - universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys iš Lietuvos mokslo tarybos Mokslo (meno) veiklos rezultatų vertinimo sistemos „Vieversys“."
resource: "https://get.data.gov.lt/datasets/gov/lmt/top_darbu_vertinimas/DarboVertinimas"
tags: [gov, lmt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lmt/top_darbu_vertinimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmt/top_darbu_vertinimas.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# DarboVertinimas — Universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys

Lentelėje - universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys iš Lietuvos mokslo tarybos Mokslo (meno) veiklos rezultatų vertinimo sistemos „Vieversys“. Duomenys lentelėje pateikiami nuo 2017 metų ir atnaujinami, papildomi kas metus. Svarbu atkreipti dėmesį, kad laikui bėgant gali atsirasti pasikeitimų mokslo srityse (pvz.: mokslo sritis „Biomedicinos mokslai“ nuo 2018 metų pervadinta į „Medicinos ir sveikatos mokslai“) ir vertinimo tvarkose (daugiau skaityti čia: https://lmt.lrv.lt/lt/veiklos-sritys/mokslo-kokybe/mokslo-meno-vertinimas/universitetai-ir-moksliniu-tyrimu-institutai/kasmetinis-mokslo-meno-veiklos-vertinimas/).

- **Model:** `datasets/gov/lmt/top_darbu_vertinimas/DarboVertinimas`[^manifest]
- **Dataset:** [Universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys](../top_darbu_vertinimas.md) (`datasets/gov/lmt/top_darbu_vertinimas`)
- **Manifest CSV:** [datasets/gov/lmt/top_darbu_vertinimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmt/top_darbu_vertinimas.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmt/top_darbu_vertinimas/DarboVertinimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `ataskaitiniai_vertinimo_metai` | `string` | — | `4` | `open` | — | Ataskaitiniai vertinimo metai | — |
| `komisija` | `string` | — | `4` | `open` | — | Vertinimo komisija | — |
| `taskai_po_vertinimo` | `number` | — | `4` | `open` | — | Taškai po vertinimo | — |
| `inst_pavadinimas` | `string` | — | `4` | `open` | — | Institucijos pavadinimas | — |
| `inst_tipas` | `string` | — | `4` | `open` | — | Institucijos tipas | — |
| `darbo_priskyrimas_krypciai` | `number` | `%` | `4` | `open` | — | Darbo priskyrimas konkrečiai mokslo krypčiai (proc.) | — |
| `mokslo_kryptis` | `string` | — | `4` | `open` | — | Mokslo kryptis | — |
| `mokslo_sritis` | `string` | — | `4` | `open` | — | Mokslo sritis | — |
| `wos_straipsnio_id` | `string` | — | `4` | `open` | — | WOS ("Web of Science") darbo (straipsnio) identifikatorius | — |
| `top_straipsnio_id` | `string` | — | `4` | `open` | — | Top darbo (straipsnio) unikalus Nr. Vieversyje | — |
| `straipsnio_pavadinimas` | `string` | — | `4` | `open` | — | Darbo (straipsnio) pavadinimas | — |
| `straipsnio_autoriai` | `string` | — | `4` | `open` | — | Darbo (straipsnio) autoriai | — |
| `autoriu_sk` | `integer` | `U` | `4` | `open` | — | Darbo (straipsnio) autorių skaičius | — |
| `inst_sk` | `integer` | `U` | `4` | `open` | — | Darbo (straipsnio) įstaigų skaičius | — |
| `leidinio_pavadinimas` | `string` | — | `4` | `open` | — | Darbo (straipsnio) mokslo leidinio pavadinimas | — |
| `straipsnio_publikavimo_metai` | `string` | — | `4` | `open` | — | Darbo (straipsnio) publikavimo metai | — |
| `leidinio_tomas` | `string` | — | `4` | `open` | — | Mokslo leidinio tomas | — |
| `leidinio_numeris` | `string` | — | `4` | `open` | — | Mokslo leidinio numeris | — |
| `straipsnio_puslapiai` | `string` | — | `4` | `open` | — | Darbo (straipsnio) puslapiai | — |
| `elektronine_prieiga` | `string` | — | `4` | `open` | — | Darbo (straipsnio) elektroninė prieiga (nuoroda) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lmt/top_darbu_vertinimas.csv
