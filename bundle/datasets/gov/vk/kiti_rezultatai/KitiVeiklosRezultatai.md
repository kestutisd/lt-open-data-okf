---
type: Table
title: "KitiVeiklosRezultatai — Valstybės kontrolės vertinimų rezultatai"
description: "Valstybės kontrolės vertinimų (ne auditų) rezultatai"
resource: "https://get.data.gov.lt/datasets/gov/vk/kiti_rezultatai/KitiVeiklosRezultatai"
tags: [gov, vk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vk/kitirezultatai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/kitirezultatai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# KitiVeiklosRezultatai — Valstybės kontrolės vertinimų rezultatai

Valstybės kontrolės vertinimų (ne auditų) rezultatai

- **Model:** `datasets/gov/vk/kiti_rezultatai/KitiVeiklosRezultatai`[^manifest]
- **Dataset:** [datasets/gov/vk/kiti_rezultatai](../kiti_rezultatai.md) (`datasets/gov/vk/kiti_rezultatai`)
- **Manifest CSV:** [datasets/gov/vk/kitirezultatai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vk/kitirezultatai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vk/kiti_rezultatai/KitiVeiklosRezultatai`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `audit_cardid` | `integer` | — | `3` | `open` | — | Produkto ID | Vertinimo (ne audito) identifikacijos numeris |
| `vertinimo_pavadinimas` | `string` | — | `3` | `open` | — | Produkto pavadinimas | Vertinimo (ne audito) pavadinimas |
| `registravimo_data` | `date` | `D` | `4` | `open` | — | Registracijos data | Dokumento registracijos dokumentų valdymo posistemyje data |
| `failo_url` | `url` | — | `4` | `open` | — | Nuoroda į produkto dokumentą | Vertinimo (ne audito) dokumentas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vk/kitirezultatai.csv
