---
type: Table
title: "Forma — Juridinių asmenų registro teisinių formų klasifikatorius"
description: "Spinta table datasets/gov/rc/jar/formos_statusai/Forma (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/formos_statusai/Forma"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/formos_statusai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/formos_statusai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Forma — Juridinių asmenų registro teisinių formų klasifikatorius

- **Model:** `datasets/gov/rc/jar/formos_statusai/Forma`[^manifest]
- **Dataset:** [Juridinių asmenų registro teisinių formų ir statusų klasifikatoriai](../formos_statusai.md) (`datasets/gov/rc/jar/formos_statusai`)
- **Manifest CSV:** [datasets/gov/rc/jar/formos_statusai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/formos_statusai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/formos_statusai/Forma`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `integer` | — | `4` | `open` | — | Juridinio asmens formos kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinio asmens formos pavadinimas | — |
| `pav_ilgas` | `string` | — | `3` | `open` | — | Juridinio asmens formos ilgasis pavadinimas | — |
| `name` | `string` | — | `3` | `open` | — | Juridinio asmens formos pavadinimas anglų kalba | — |
| `tipas` | `string` | — | `4` | `open` | — | Juridinio asmens formos tipas | — |
| `type` | `string` | — | `4` | `open` | — | Juridinio asmens formos tipas anglų kalba | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"privatus"` | — | — | Privatus | — |
| `tipas` | `"viešasis"` | — | — | Viešasis | — |
| `type` | `"private"` | — | — | Private | — |
| `type` | `"public"` | — | — | Public | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/formos_statusai.csv
