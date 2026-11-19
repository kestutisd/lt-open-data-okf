---
type: Table
title: "DarboVertinimas — Universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys"
description: "Lentelėje - universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys iš Lietuvos mokslo tarybos Mokslo (meno) veiklos rezultatų vertinimo sistemos „Vieversys“."
resource: "https://get.data.gov.lt/datasets/gov/lmt/top_darbu_vertinimas/DarboVertinimas"
tags: [gov, lmt, darbovertinimas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmt/top_darbu_vertinimas.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/lmt/top_darbu_vertinimas.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3804/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lmt/top_darbu_vertinimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# DarboVertinimas — Universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys

Lentelėje - universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo duomenys iš Lietuvos mokslo tarybos Mokslo (meno) veiklos rezultatų vertinimo sistemos „Vieversys“. Duomenys lentelėje pateikiami nuo 2017 metų ir atnaujinami, papildomi kas metus. Svarbu atkreipti dėmesį, kad laikui bėgant gali atsirasti pasikeitimų mokslo srityse (pvz.: mokslo sritis „Biomedicinos mokslai“ nuo 2018 metų pervadinta į „Medicinos ir sveikatos mokslai“) ir vertinimo tvarkose (daugiau skaityti čia: https://lmt.lrv.lt/lt/veiklos-sritys/mokslo-kokybe/mokslo-meno-vertinimas/universitetai-ir-moksliniu-tyrimu-institutai/kasmetinis-mokslo-meno-veiklos-vertinimas/). Dėl techninių klausimų ar klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/lmt/top_darbu_vertinimas/DarboVertinimas`[^manifest]
- **Dataset:** [Universitetų ir mokslinių tyrimų institutų mokslo, meno darbų formaliojo (kasmetinio) vertinimo...](../top_darbu_vertinimas.md) (`datasets/gov/lmt/top_darbu_vertinimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/lmt/top_darbu_vertinimas.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmt/top_darbu_vertinimas.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lmt/top_darbu_vertinimas/DarboVertinimas` (`deployed`)[^manifest]
- **Provider:** `lmt` — Lietuvos mokslo taryba *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lmt/top_darbu_vertinimas.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lmt/top_darbu_vertinimas.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lmt/top_darbu_vertinimas (https://data.gov.lt/datasets/3804/)
