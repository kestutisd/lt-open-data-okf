---
type: Table
title: "DokumentoPotipis — Juridinių asmenų registro dokumentų potipių klasifikatorius"
description: "Spinta table datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoPotipis (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoPotipis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# DokumentoPotipis — Juridinių asmenų registro dokumentų potipių klasifikatorius

- **Model:** `datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoPotipis`[^manifest]
- **Dataset:** [Juridinių asmenų registro dokumentų klasifikatoriai](../dokumentu_tipai_potipiai.md) (`datasets/gov/rc/jar/dokumentu_tipai_potipiai`)
- **Manifest CSV:** [datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/dokumentu_tipai_potipiai/DokumentoPotipis`
- **Primary Key (`ref`):** `kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dokumento_tipas` | `ref` | [DokumentoTipas](DokumentoTipas.md) | `4` | `open` | — | Juridinių asmenų registro dokumento tipo kodas | — |
| `kodas` | `integer` | — | `4` | `open` | — | Juridinių asmenų registro dokumento potipio kodas | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Juridinių asmenų registro dokumento potipio pavadinimas | — |
| `name` | `string` | — | `3` | `open` | — | Juridinių asmenų registro dokumento potipio pavadinimas anglų kalba | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/dokumentu_tipai_potipiai.csv
