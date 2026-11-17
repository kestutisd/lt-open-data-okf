---
type: Table
title: "TestamentoZyma"
description: "Spinta table datasets/gov/rc/tr/testamento_zymos/TestamentoZyma (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/testamento_zymos/TestamentoZyma"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/testamento_zymos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamento_zymos.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# TestamentoZyma

- **Model:** `datasets/gov/rc/tr/testamento_zymos/TestamentoZyma`[^manifest]
- **Dataset:** [Testamentų registro (TR) duomenys apie testamentų žymas](../testamento_zymos.md) (`datasets/gov/rc/tr/testamento_zymos`)
- **Manifest CSV:** [datasets/gov/rc/tr/testamento_zymos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamento_zymos.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/testamento_zymos/TestamentoZyma`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Objekto identifikavimo kodas šiame duomenų rinkinyje | — |
| `obj_tipas` | `integer` | — | `4` | `open` | — | Registro objekto tipas | — |
| `obj_pavadinimas` | `string` | — | `3` | `open` | — | Registro objekto pavadinimas | — |
| `zyma_id` | `integer` | — | `4` | `open` | — | Žymos identifikavimo kodas šiame duomenų rinkinyje | — |
| `zyma_tipas` | `ref` | [/datasets/gov/rc/tr/tr_klasifikatoriai/TrZyma](../tr_klasifikatoriai/TrZyma.md) | `4` | `open` | — | Žymos tipas | — |
| `zyma_data` | `string` | — | `3` | `open` | — | Žymos įregistravimo laikotarpis (metai-ketvirtis) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/testamento_zymos.csv
