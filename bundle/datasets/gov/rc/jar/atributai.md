---
type: Dataset
title: "Juridinių asmenų registro atributų klasifikatoriai"
description: "Lietuvos Respublikos juridinių asmenų registro atributų klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.) (JAR atributų klasifikatorius; JAR kokybinių atributų klasifikatorius; JAR leistinų atributų klasifikatorius; JAR tekstinių..."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/atributai"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Juridinių asmenų registro atributų klasifikatoriai

Lietuvos Respublikos juridinių asmenų registro atributų klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.) (JAR atributų klasifikatorius; JAR kokybinių atributų klasifikatorius; JAR leistinų atributų klasifikatorius; JAR tekstinių atributų klasifikatorius).

- **Namespace:** `datasets/gov/rc/jar/atributai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/jar/atributai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/atributai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/atributai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Atributas](atributai/Atributas.md) | Juridinių asmenų registro atributų klasifikatorius | `4` | `kodas` | — | 6 | — |
| [LeistinasAtributas](atributai/LeistinasAtributas.md) | Juridinių asmenų registro leistinų atributų klasifikatorius pagal teisines formas | `4` | `forma,atributas` | — | 2 | — |
| [TekstinisAtributas](atributai/TekstinisAtributas.md) | Juridinių asmenų registro tekstinių atributų klasifikatorius | `4` | `kodas` | — | 3 | — |
| [AtributoTipas](atributai/AtributoTipas.md) | Juridinių asmenų registro atributų tipų klasifikatorius | `4` | `kodas` | — | 3 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/atributai.csv
