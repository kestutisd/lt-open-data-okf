---
type: Dataset
title: "Sistema skirta AB Šiaulių energija klientų duomenų valdymui, karšto vandens bei šildymo tiekimo paslaugų apskaičiavimui, sąskaitų leidimui ir skolų valdymui."
description: "Spinta dataset datasets/gov/se/billingas (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/se/billingas"
tags: [gov, se, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/se/registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sistema skirta AB Šiaulių energija klientų duomenų valdymui, karšto vandens bei šildymo tiekimo paslaugų apskaičiavimui, sąskaitų leidimui ir skolų valdymui.

- **Namespace:** `datasets/gov/se/billingas`[^manifest]
- **Manifest CSV:** [datasets/gov/se/registras.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/se/registras.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/se/billingas`
- **Parent Namespace (`ns`):** AB Šiaulių energija (`datasets/gov/se`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Registras](billingas/Registras.md) | Tiekiamų paslaugų registras | `4` | `id` | — | 9 | Šiaulių energijos teikiamų paslaugų ir suvartotų kiekių registras. |
| [Patalpa](billingas/Patalpa.md) | Patalpos | `4` | `patalpos_id` | — | 10 | Patalpos ir pastato, kuriame yra patalpa informacija, kur teikiamos Šiaulių energijos paslaugos. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/se/registras.csv
