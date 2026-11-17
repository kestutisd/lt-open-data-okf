---
type: Table
title: "FaktoPotipis — Juridinių asmenų registro faktų potipių klasifikatorius"
description: "Spinta table datasets/gov/rc/jar/faktu_tipai_potipiai/FaktoPotipis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/faktu_tipai_potipiai/FaktoPotipis"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/faktu_tipai_potipiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# FaktoPotipis — Juridinių asmenų registro faktų potipių klasifikatorius

- **Model:** `datasets/gov/rc/jar/faktu_tipai_potipiai/FaktoPotipis`[^manifest]
- **Dataset:** [Juridinių asmenų registro faktų tipų ir potipių klasifikatoriai](../faktu_tipai_potipiai.md) (`datasets/gov/rc/jar/faktu_tipai_potipiai`)
- **Manifest CSV:** [datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/faktu_tipai_potipiai.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/faktu_tipai_potipiai/FaktoPotipis`
- **Primary Key (`ref`):** `kodas`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `fakto_tipas` | `ref` | [FaktoTipas](FaktoTipas.md) | `4` | `open` | — | Juridinių asmenų registro fakto tipo kodas | — |
| `kodas` | `integer` | — | `4` | `open` | — | Juridinių asmenų registro fakto potipio kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinių asmenų registro fakto potipio pavadinimas | — |
| `name` | `string` | — | `3` | `open` | — | Juridinių asmenų registro fakto potipio pavadinimas anglų kalba | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/faktu_tipai_potipiai.csv
