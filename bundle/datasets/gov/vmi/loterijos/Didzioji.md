---
type: Table
title: "Didzioji — Didžiųjų verslo loterijų ir lošimų mokesčio deklaracijų duomenys"
description: "Loterija, kurios bilietai platinami visoje Lietuvos Respublikos teritorijoje ir nominalioji numatomų išplatinti bilietų vertė neribojama."
resource: "https://get.data.gov.lt/datasets/gov/vmi/loterijos/Didzioji"
tags: [gov, vmi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/loterijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Didzioji — Didžiųjų verslo loterijų ir lošimų mokesčio deklaracijų duomenys

Loterija, kurios bilietai platinami visoje Lietuvos Respublikos teritorijoje ir nominalioji numatomų išplatinti bilietų vertė neribojama.

- **Model:** `datasets/gov/vmi/loterijos/Didzioji`[^manifest]
- **Dataset:** [Loterijų verslo loterijų ir lošimų mokesčio deklaracijų (forma FR0583) duomenys](../loterijos.md) (`datasets/gov/vmi/loterijos`)
- **Manifest CSV:** [datasets/gov/vmi/loterijos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/loterijos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/loterijos/Didzioji`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ketvirtis` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, ketvirtis | — |
| `metai` | `integer` | — | `2` | `open` | — | Mokestinio laikotarpio, už kurį teikiama deklaracija, metai | — |
| `mokescio_suma` | `number` | — | `2` | `open` | — | Mokesčio suma | — |
| `moketoju_sk` | `integer` | `U` | `4` | `open` | — | Mokesčių mokėtojų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `mokescio_suma` | `update(type: "money", ref: "EUR")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/loterijos.csv
