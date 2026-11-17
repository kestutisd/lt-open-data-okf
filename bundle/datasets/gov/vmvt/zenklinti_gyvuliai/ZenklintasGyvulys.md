---
type: Table
title: "ZenklintasGyvulys — Ženklinti gyvuliai"
description: "Lentelėje pateikiami Valstybinės maisto ir veterinarijos tarnybos duomenys apie ženklintus gyvulius."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/zenklinti_gyvuliai/ZenklintasGyvulys"
tags: [gov, vmvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/zenklinti_gyvuliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/zenklinti_gyvuliai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# ZenklintasGyvulys — Ženklinti gyvuliai

Lentelėje pateikiami Valstybinės maisto ir veterinarijos tarnybos duomenys apie ženklintus gyvulius. Viena eilutė atitinka vieną ženklintą gyvulį. Pateikiama informacija apie gyvulio kodus, gyvulio tėvų kodus, gimimo datas ir kt. Duomenys nuo 1988 metų (ženklinimo data).

- **Model:** `datasets/gov/vmvt/zenklinti_gyvuliai/ZenklintasGyvulys`[^manifest]
- **Dataset:** [Ženklinti gyvuliai](../zenklinti_gyvuliai.md) (`datasets/gov/vmvt/zenklinti_gyvuliai`)
- **Manifest CSV:** [datasets/gov/vmvt/zenklinti_gyvuliai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/zenklinti_gyvuliai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/zenklinti_gyvuliai/ZenklintasGyvulys`
- **Primary Key (`ref`):** `gvs_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gvs_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikacinis kodas | — |
| `gyvulio_kodas_senas` | `string` | — | `4` | `open` | — | Gyvulio senasis ženklinimo kodas | — |
| `gyvulio_kodas` | `string` | — | `4` | `open` | — | Gyvulio naujasis ženklinimo kodas | — |
| `gyvulio_veisle` | `string` | — | `4` | `open` | — | Gyvulio veislė | — |
| `gimimo_data` | `date` | `D` | `4` | `open` | — | Gyvulio gimimo data | — |
| `isregistravimo_data` | `date` | `D` | `4` | `open` | — | Gyvulio išregistravimo data | — |
| `isregistravimo_priezastis` | `string` | — | `4` | `open` | — | Gyvulio išregistravimo priežastis | — |
| `importo_data` | `date` | `D` | `4` | `open` | — | Gyvulio importavimo data | — |
| `motinos_kodas` | `string` | — | `4` | `open` | — | Gyvulio motinos ženklinimo kodas | — |
| `tevo_kodas` | `string` | — | `4` | `open` | — | Gyvulio tėvo ženklinimo kodas | — |
| `gyvulio_vardas` | `string` | — | `4` | `open` | — | Gyvulio vardas | — |
| `zenklinimo_data` | `date` | `D` | `4` | `open` | — | Gyvulio ženklinimo data | — |
| `vet_darb_ak` | `string` | — | `4` | `open` | — | Veterinarijos darbuotojo asmens kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/zenklinti_gyvuliai.csv
