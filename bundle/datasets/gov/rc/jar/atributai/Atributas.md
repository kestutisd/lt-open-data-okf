---
type: Table
title: "Atributas — Juridinių asmenų registro atributų klasifikatorius"
description: "Spinta table datasets/gov/rc/jar/atributai/Atributas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/atributai/Atributas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atributas — Juridinių asmenų registro atributų klasifikatorius

- **Model:** `datasets/gov/rc/jar/atributai/Atributas`[^manifest]
- **Dataset:** [Juridinių asmenų registro atributų klasifikatoriai](../atributai.md) (`datasets/gov/rc/jar/atributai`)
- **Manifest CSV:** [datasets/gov/rc/jar/atributai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/atributai/Atributas`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Juridinių asmenų registro atributo kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinių asmenų registro atributo pavadinimas | — |
| `name` | `string` | — | `3` | `open` | — | Juridinių asmenų registro atributo pavadinimas anglų kalba | — |
| `tipas` | `ref` | [AtributoTipas](AtributoTipas.md) | `4` | `open` | — | Juridinių asmenų registro atributo tipo kodas | — |
| `pozymis` | `string` | — | `4` | `open` | — | Juridinių asmenų registro atributo požymis | — |
| `pozymis_en` | `string` | — | `4` | `open` | — | Juridinių asmenų registro atributo požymis anglų kalba | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `pozymis` | `"Būtinas"` | — | — | Būtinas | — |
| `pozymis` | `"Nebūtinas"` | — | — | Nebūtinas | — |
| `pozymis_en` | `"Required"` | — | — | Required | — |
| `pozymis_en` | `"Not required"` | — | — | Not required | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv
