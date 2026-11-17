---
type: Table
title: "Diagnoze — Mokinių sveikatos patikrinimų metu nustatytos diagnozės. Lentelės objektas - mokinio sveikatos tikrinimo metu išrašyta diagnozė."
description: "Spinta table datasets/gov/lsd/sveikata/mokiniu_sveikata/Diagnoze (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata/Diagnoze"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19"
    last_modified: "2026-11-11T14:39:20Z"
---

# Diagnoze — Mokinių sveikatos patikrinimų metu nustatytos diagnozės. Lentelės objektas - mokinio sveikatos tikrinimo metu išrašyta diagnozė.

- **Model:** `datasets/gov/lsd/sveikata/mokiniu_sveikata/Diagnoze`[^manifest]
- **Dataset:** [Kasmetinės vaikų sveikatos patikros duomenys](../mokiniu_sveikata.md) (`datasets/gov/lsd/sveikata/mokiniu_sveikata`)
- **Manifest CSV:** [datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/mokiniu_sveikata.csv#L19)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/mokiniu_sveikata/Diagnoze`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `tikrinimo_id` | `string` | — | `4` | `open` | — | Sveikatos tikrinimo vizito identifikatorius | Visos patikrinimo metu surašytos diagnozės susietos pagal tikrinimo_id stulpelį. |
| `diagnoze` | `string` | — | `4` | `open` | — | Diagnozės pavadinimas | — |
| `tlk_kodas` | `string` | — | `4` | `open` | — | Tarptautinės ligų klasifikacijos (TLK) kodas | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/mokiniu_sveikata.csv
