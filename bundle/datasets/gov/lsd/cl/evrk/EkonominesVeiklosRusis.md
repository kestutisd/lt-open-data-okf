---
type: Table
title: "EkonominesVeiklosRusis — Ekonominės veikos rūšis (EVRK)"
description: "Spinta table datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/cl/evrk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# EkonominesVeiklosRusis — Ekonominės veikos rūšis (EVRK)

- **Model:** `datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis`[^manifest]
- **Dataset:** [Ekonominės veiklos klasifikatorius](../evrk.md) (`datasets/gov/lsd/cl/evrk`)
- **Manifest CSV:** [datasets/gov/lsd/cl/evrk.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/cl/evrk.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/cl/evrk/EkonominesVeiklosRusis`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `string` | — | `4` | `open` | — | Lygmens kodas | — |
| `pavadinimas_lt` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `pavadinimas_en` | `string` | — | `2` | `open` | — | Pavadinimas | — |
| `pastabos_lt` | `string` | — | `2` | `open` | — | Aiškinamosios pastabos | — |
| `pastabos_en` | `string` | — | `2` | `open` | — | Aiškinamosios pastabos | — |
| `lygmuo` | `ref` | [Lygmuo](Lygmuo.md) | `4` | `open` | — | Lygmuo | — |
| `bendresne_veiklos_rusis` | `ref` | [EkonominesVeiklosRusis](EkonominesVeiklosRusis.md) | `5` | `open` | `skos:broader` | Bendresnė ekonominės veiklos rūšis | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/cl/evrk.csv
