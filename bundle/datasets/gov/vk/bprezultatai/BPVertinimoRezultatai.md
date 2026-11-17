---
type: Table
title: "BPVertinimoRezultatai — Biudžeto politikos stebėsenos vertinimų rezultatai"
description: "Valstybės kontrolės biudžeto politikos stebėsenos vertinimų rezultatai"
resource: "https://get.data.gov.lt/datasets/gov/vk/bprezultatai/BPVertinimoRezultatai"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/bprezultatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/bprezultatai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# BPVertinimoRezultatai — Biudžeto politikos stebėsenos vertinimų rezultatai

Valstybės kontrolės biudžeto politikos stebėsenos vertinimų rezultatai

- **Model:** `datasets/gov/vk/bprezultatai/BPVertinimoRezultatai`[^manifest]
- **Dataset:** [datasets/gov/vk/bprezultatai](../bprezultatai.md) (`datasets/gov/vk/bprezultatai`)
- **Manifest CSV:** [datasets/gov/vk/bprezultatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/bprezultatai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/bprezultatai/BPVertinimoRezultatai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_cardid` | `integer` | — | `3` | `open` | — | Produkto ID | Vertinimo, išvados, ataskaitos, projekcijos identifikacijos numeris |
| `vertinimo_pavadinimas` | `string` | — | `3` | `open` | — | Produkto pavadinimas | Vertinimo, išvados, ataskaitos, projekcijos pavadinimas |
| `registravimo_data` | `date` | `D` | `4` | `open` | — | Registracijos data | Dokumento registracijos dokumentų valdymo posistemyje data |
| `fail_url` | `url` | — | `4` | `open` | — | Nuoroda į produkto dokumentą | Vertinimo, išvados, ataskaitos, projekcijos dokumentas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/bprezultatai.csv
