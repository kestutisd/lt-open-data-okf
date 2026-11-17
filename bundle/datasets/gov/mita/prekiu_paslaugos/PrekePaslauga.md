---
type: Table
title: "PrekePaslauga"
description: "Spinta table datasets/gov/mita/prekiu_paslaugos/PrekePaslauga (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/mita/prekiu_paslaugos/PrekePaslauga"
tags: [gov, mita, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/mita/prekes_paslaugos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/prekes_paslaugos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# PrekePaslauga

- **Model:** `datasets/gov/mita/prekiu_paslaugos/PrekePaslauga`[^manifest]
- **Dataset:** [Mokslo, inovacijų ir technologijų agentūros duomenų bazėse registruotų žinioms imlių produktų duomenys.](../prekiu_paslaugos.md) (`datasets/gov/mita/prekiu_paslaugos`)
- **Manifest CSV:** [datasets/gov/mita/prekes_paslaugos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/mita/prekes_paslaugos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/mita/prekiu_paslaugos/PrekePaslauga`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `produktas` | `string` | — | `3` | `open` | — | Produkto pavadinimas | — |
| `savininkas` | `string` | — | `2` | `open` | — | Juridinio asmens pavadinimas | — |
| `jar_kodas` | `string` | — | `2` | `open` | — | Juridinio asmens kodas | — |
| `aprasymas` | `string` | — | `2` | `open` | — | Produkto aprašymas | — |
| `nuoroda` | `url` | — | `4` | `open` | — | URL nuoroda į detalų produkto aprašymą | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savininkas` | `create(property: "savininkas", type: "ref", ref: "/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | — | — | — | — |
| `savininkas` | `update(property: "savininkas.ja_pavadinimas", type: "")` | `property` | `2` | — | — | — | — |
| `jar_kodas` | `update(property: "savininkas.ja_kodas", type: "")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/mita/prekes_paslaugos.csv
