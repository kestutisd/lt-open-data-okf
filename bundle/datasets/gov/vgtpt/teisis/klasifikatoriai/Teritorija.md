---
type: Table
title: "Teritorija — Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius"
description: "Spinta table datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija"
tags: [gov, vgtpt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vgtpt/teisis/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# Teritorija — Teisinės pagalbos paslaugų informacinės sistemos teritorijos klasifikatorius

- **Model:** `datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija`[^manifest]
- **Dataset:** [Teisinės pagalbos paslaugų informacinės sistemos (TEISIS) klasifikatoriai](../klasifikatoriai.md) (`datasets/gov/vgtpt/teisis/klasifikatoriai`)
- **Manifest CSV:** [datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vgtpt/teisis/klasifikatoriai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vgtpt/teisis/klasifikatoriai/Teritorija`
- **Primary Key (`ref`):** `nr`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `nr` | `integer` | — | `4` | `open` | — | Eilės numeris šiame duomenų rinkinyje | — |
| `teritorijos_kodas` | `string` | — | `4` | `open` | — | Pagalbą gaunančio asmens gyvenamosios vietos teritorijos kodas | — |
| `teritorijos_pavadinimas` | `string` | — | `3` | `open` | — | Pagalbą gaunančio asmens gyvenamosios vietos teritorijos pavadinimas | Iš Adresų registro |
| `sav_kodas` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../../rc/ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės kodas | Iš Adresų registro |

[^manifest]: atviriduomenys/manifest — datasets/gov/vgtpt/teisis/klasifikatoriai.csv
