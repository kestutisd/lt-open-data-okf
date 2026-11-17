---
type: Table
title: "JuridinisAsmuoKapitalas"
description: "Spinta table datasets/gov/rc/jar/ja_kapitalas/JuridinisAsmuoKapitalas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/jar/ja_kapitalas/JuridinisAsmuoKapitalas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/jar/ja_kapitalas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/ja_kapitalas.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# JuridinisAsmuoKapitalas

- **Model:** `datasets/gov/rc/jar/ja_kapitalas/JuridinisAsmuoKapitalas`[^manifest]
- **Dataset:** [Juridinių asmenų įstatinio kapitalo duomenys](../ja_kapitalas.md) (`datasets/gov/rc/jar/ja_kapitalas`)
- **Manifest CSV:** [datasets/gov/rc/jar/ja_kapitalas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/jar/ja_kapitalas.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/jar/ja_kapitalas/JuridinisAsmuoKapitalas`
- **Primary Key (`ref`):** `juridinis_asmuo`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `juridinis_asmuo` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo](../iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Juridinio asmens pavadinimas juridinių asmenų registre | — |
| `forma` | `ref` | [/datasets/gov/rc/jar/formos_statusai/Forma](../formos_statusai/Forma.md) | `4` | `open` | — | Juridinio asmens formos pavadinimas | — |
| `data_nuo` | `date` | `D` | `4` | `open` | — | Įstatinio kapitalo įregistravimo data | — |
| `reiksme` | `number` | — | `3` | `open` | — | Įstatinio kapitalo dydis skaičiais | — |
| `valiuta` | `string` | — | `3` | `open` | — | Valiutos kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/jar/ja_kapitalas.csv
