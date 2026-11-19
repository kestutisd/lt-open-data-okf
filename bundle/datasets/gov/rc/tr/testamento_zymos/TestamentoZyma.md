---
type: Table
title: "TestamentoZyma"
description: "Spinta table datasets/gov/rc/tr/testamento_zymos/TestamentoZyma (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/tr/testamento_zymos/TestamentoZyma"
tags: [gov, rc, testamentozyma, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamento_zymos.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/rc/tr/testamento_zymos.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2144/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/tr/testamento_zymos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# TestamentoZyma

- **Model:** `datasets/gov/rc/tr/testamento_zymos/TestamentoZyma`[^manifest]
- **Dataset:** [Testamentų registro (TR) duomenys apie testamentų žymas](../testamento_zymos.md) (`datasets/gov/rc/tr/testamento_zymos`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/tr/testamento_zymos.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamento_zymos.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/tr/testamento_zymos/TestamentoZyma` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Objekto identifikavimo kodas šiame duomenų rinkinyje | — |
| `obj_tipas` | `integer` | — | `4` | `open` | — | Registro objekto tipas | — |
| `obj_pavadinimas` | `string` | — | `3` | `open` | — | Registro objekto pavadinimas | — |
| `zyma_id` | `integer` | — | `4` | `open` | — | Žymos identifikavimo kodas šiame duomenų rinkinyje | — |
| `zyma_tipas` | `ref` | [TrZyma](../tr_klasifikatoriai/TrZyma.md) (`level=4 UUID`: `zyma_tipas._id`) | `4` | `open` | — | Žymos tipas | — |
| `zyma_data` | `string` | — | `3` | `open` | — | Žymos įregistravimo laikotarpis (metai-ketvirtis) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/tr/testamento_zymos.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/tr/testamento_zymos.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/tr/testamento_zymos (https://data.gov.lt/datasets/2144/)
