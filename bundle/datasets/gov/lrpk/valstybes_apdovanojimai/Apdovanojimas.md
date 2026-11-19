---
type: Table
title: "Apdovanojimas — Valstybės apdovanojimai"
description: "Valstybės apdovanojimas – aukščiausio valstybės pareigūno ar kito turinčio teisę apdovanoti pareigūno skiriamas ordinas, medalis ir kitoks pasižymėjimo ženklas, skiriamas valstybei nusipelniusiam asmeniui."
resource: "https://get.data.gov.lt/datasets/gov/lrpk/valstybes_apdovanojimai/Apdovanojimas"
tags: [gov, lrpk, apdovanojimas, deployed, level-4, cadence-weekly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2757/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lrpk/valstybes_apdovanojimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Apdovanojimas — Valstybės apdovanojimai

Valstybės apdovanojimas – aukščiausio valstybės pareigūno ar kito turinčio teisę apdovanoti pareigūno skiriamas ordinas, medalis ir kitoks pasižymėjimo ženklas, skiriamas valstybei nusipelniusiam asmeniui.[^manifest]

- **Model:** `datasets/gov/lrpk/valstybes_apdovanojimai/Apdovanojimas`[^manifest]
- **Dataset:** [Valstybės apdovanojimai](../valstybes_apdovanojimai.md) (`datasets/gov/lrpk/valstybes_apdovanojimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrpk/valstybes_apdovanojimai/Apdovanojimas` (`deployed`)[^manifest]
- **Provider:** `lrpk` — Lietuvos Respublikos Prezidento kanceliarija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `WEEKLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrpk/valstybes_apdovanojimai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lrpk/valstybes_apdovanojimai (https://data.gov.lt/datasets/2757/)
