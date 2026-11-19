---
type: Dataset
title: "Suvartojimas"
description: "Deklaruotas vandens ir šilumos suvartojimas"
resource: "https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/suvartojimas"
tags: [gov, koris_grandis, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# Suvartojimas

Deklaruotas vandens ir šilumos suvartojimas[^manifest]

- **Namespace:** `datasets/gov/koris_grandis/skaitikliai/suvartojimas`[^manifest]
- **Manifest CSV:** [datasets/gov/koris_grandis/skaitikliai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/koris_grandis/skaitikliai/suvartojimas` (`deployed`)[^manifest]
- **Provider:** `koris_grandis` — Komunaliniai suvartojimo įrašai sistemoje „GRANDIS“ *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [VilkaviskioFiziniuKarstasVanduo](suvartojimas/VilkaviskioFiziniuKarstasVanduo.md) | UAB „Vilkaviškio šilumos tinklų“ karšto vandens suvartojimas, už kurį moka fiziniai asmenys | `4` | `vda_id` | — | `12` | — |
| [VilkaviskioJuridiniuKarstasVanduo](suvartojimas/VilkaviskioJuridiniuKarstasVanduo.md) | UAB „Vilkaviškio šilumos tinklų“ karšto vandens suvartojimas, už kurį moka juridiniai asmenys | `4` | `vda_id` | — | `17` | — |
| [VilkaviskioJuridiniuSiluma](suvartojimas/VilkaviskioJuridiniuSiluma.md) | UAB „Vilkaviškio šilumos tinklų“ šilumos suvartojimas, už kurį moka juridiniai asmenys | `4` | `vda_id` | — | `16` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/koris_grandis/skaitikliai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/koris_grandis/skaitikliai.csv#L4)
