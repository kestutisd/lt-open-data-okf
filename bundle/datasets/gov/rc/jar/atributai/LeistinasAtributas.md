---
type: Table
title: "LeistinasAtributas — Juridinių asmenų registro leistinų atributų klasifikatorius pagal teisines formas"
description: "Spinta table datasets/gov/rc/jar/atributai/LeistinasAtributas (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/atributai/LeistinasAtributas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L16"
    last_modified: "2026-11-11T14:39:20Z"
---

# LeistinasAtributas — Juridinių asmenų registro leistinų atributų klasifikatorius pagal teisines formas

- **Model:** `datasets/gov/rc/jar/atributai/LeistinasAtributas`[^manifest]
- **Dataset:** [Juridinių asmenų registro atributų klasifikatoriai](../atributai.md) (`datasets/gov/rc/jar/atributai`)
- **Manifest CSV:** [datasets/gov/rc/jar/atributai.csv#L16](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L16)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/atributai/LeistinasAtributas`
- **Primary Key (`ref`):** `forma,atributas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | Juridinių asmenų registro leistina forma | — |
| `atributas` | `ref` | [Atributas](Atributas.md) | `4` | `open` | — | Juridinių asmenų registro leistino atributo kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv
