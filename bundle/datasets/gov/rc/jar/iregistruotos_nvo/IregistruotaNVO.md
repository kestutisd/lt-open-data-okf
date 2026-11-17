---
type: Table
title: "IregistruotaNVO — Juridinių asmenų registre įregistruotos NVO"
description: "Spinta table datasets/gov/rc/jar/iregistruotos_nvo/IregistruotaNVO (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/iregistruotos_nvo/IregistruotaNVO"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/iregistruotos_nvo.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruotos_nvo.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# IregistruotaNVO — Juridinių asmenų registre įregistruotos NVO

- **Model:** `datasets/gov/rc/jar/iregistruotos_nvo/IregistruotaNVO`[^manifest]
- **Dataset:** [Juridinių asmenų registre įregistruotos nevyriausybinės organizacijos (pagal žymą „NEVYRIAUSYBINĖS ORGANIZACIJOS“)](../iregistruotos_nvo.md) (`datasets/gov/rc/jar/iregistruotos_nvo`)
- **Manifest CSV:** [datasets/gov/rc/jar/iregistruotos_nvo.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/iregistruotos_nvo.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/iregistruotos_nvo/IregistruotaNVO`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmens pavadinimas Juridinių asmenų registre | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens teisinės formos pavadinimas | — |
| `nvc_nuo` | `date` | `D` | `4` | `open` | — | Žymos „Nevyriausybinė organizacija“ įregistravimo juridiniam asmeniui data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/iregistruotos_nvo.csv
