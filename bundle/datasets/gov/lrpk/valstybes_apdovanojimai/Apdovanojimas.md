---
type: Table
title: "Apdovanojimas — Valstybės apdovanojimai"
description: "Valstybės apdovanojimas – aukščiausio valstybės pareigūno ar kito turinčio teisę apdovanoti pareigūno skiriamas ordinas, medalis ir kitoks pasižymėjimo ženklas, skiriamas valstybei nusipelniusiam asmeniui."
resource: "https://get.data.gov.lt/datasets/gov/lrpk/valstybes_apdovanojimai/Apdovanojimas"
tags: [gov, lrpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrpk/valstybes_apdovanojimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apdovanojimas — Valstybės apdovanojimai

Valstybės apdovanojimas – aukščiausio valstybės pareigūno ar kito turinčio teisę apdovanoti pareigūno skiriamas ordinas, medalis ir kitoks pasižymėjimo ženklas, skiriamas valstybei nusipelniusiam asmeniui.

- **Model:** `datasets/gov/lrpk/valstybes_apdovanojimai/Apdovanojimas`[^manifest]
- **Dataset:** [Valstybės apdovanojimai](../valstybes_apdovanojimai.md) (`datasets/gov/lrpk/valstybes_apdovanojimai`)
- **Manifest CSV:** [datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrpk/valstybes_apdovanojimai/Apdovanojimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `asmuo` | `string` | — | `4` | `open` | — | Apdovanojimo gavėjo vardas, pavardė | — |
| `pilietybe` | `string` | — | `4` | `open` | — | Apdovanotojo pilietybė | — |
| `apdovanojimas` | `string` | — | `4` | `open` | — | Apdovanojimo pavadinimas | — |
| `laipsnis` | `string` | — | `4` | `open` | — | Apdovanojimo laipsnis | — |
| `dekreto_numeris` | `string` | — | `4` | `open` | — | Dekreto numeris | — |
| `dekreto_data` | `date` | `D` | `4` | `open` | — | Dekreto data | — |
| `apdovanojimo_numeris` | `string` | — | `4` | `open` | — | Apdovanojimo numeris | — |
| `po_mirties` | `boolean` | — | `4` | `open` | — | Požymis, ar apdovanojimas gautas po mirties | — |
| `pastabos` | `string` | — | `4` | `open` | — | Pastabos, jei apdovanojimas atimtas: atėmimo dekreto numeris ir data | — |
| `prezidentas` | `string` | — | `4` | `open` | — | Prezidentas dekreto datai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrpk/valstybes_apdovanojimai.csv
