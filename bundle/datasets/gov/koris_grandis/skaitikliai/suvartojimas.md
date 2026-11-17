---
type: Dataset
title: "Suvartojimas"
description: "Deklaruotas vandens ir šilumos suvartojimas"
resource: "https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/suvartojimas"
tags: [gov, koris_grandis, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Suvartojimas

Deklaruotas vandens ir šilumos suvartojimas

- **Namespace:** `datasets/gov/koris_grandis/skaitikliai/suvartojimas`[^manifest]
- **Manifest CSV:** [datasets/gov/koris_grandis/skaitikliai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/suvartojimas`
- **Parent Namespace (`ns`):** UAB „KORIS“ sistema „GRANDIS“ (`datasets/gov/koris_grandis`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VilkaviskioFiziniuKarstasVanduo](suvartojimas/VilkaviskioFiziniuKarstasVanduo.md) | UAB „Vilkaviškio šilumos tinklų“ karšto vandens suvartojimas, už kurį moka fiziniai asmenys | `4` | `vda_id` | — | 12 | — |
| [VilkaviskioJuridiniuKarstasVanduo](suvartojimas/VilkaviskioJuridiniuKarstasVanduo.md) | UAB „Vilkaviškio šilumos tinklų“ karšto vandens suvartojimas, už kurį moka juridiniai asmenys | `4` | `vda_id` | — | 17 | — |
| [VilkaviskioJuridiniuSiluma](suvartojimas/VilkaviskioJuridiniuSiluma.md) | UAB „Vilkaviškio šilumos tinklų“ šilumos suvartojimas, už kurį moka juridiniai asmenys | `4` | `vda_id` | — | 16 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv
