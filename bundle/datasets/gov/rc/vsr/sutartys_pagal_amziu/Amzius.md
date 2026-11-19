---
type: Table
title: "Amzius — Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis pagal pasirašančių šalių amžių"
description: "Spinta table datasets/gov/rc/vsr/sutartys_pagal_amziu/Amzius (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/vsr/sutartys_pagal_amziu/Amzius"
tags: [gov, rc, amzius, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutartys_pagal_amziu.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/vsr/sutartys_pagal_amziu.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2155/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/vsr/sutartys_pagal_amziu"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Amzius — Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis pagal pasirašančių šalių amžių

- **Model:** `datasets/gov/rc/vsr/sutartys_pagal_amziu/Amzius`[^manifest]
- **Dataset:** [Vedybų sutarčių registro (VSR) duomenys apie vedybų sutartis pagal pasirašančių šalių amžių](../sutartys_pagal_amziu.md) (`datasets/gov/rc/vsr/sutartys_pagal_amziu`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/vsr/sutartys_pagal_amziu.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutartys_pagal_amziu.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/vsr/sutartys_pagal_amziu/Amzius` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `dok_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dok_id` | `integer` | — | `4` | `open` | — | Dokumento identifikavimo kodas šiame rinkinyje | — |
| `porusis` | `ref` | [Porusis](../klasifikatoriai/Porusis.md) (`level=4 UUID`: `porusis._id`) | `4` | `open` | — | Sutarties porūšis iš VRS sutarčių porūšių klasifikatoriaus | — |
| `lytis` | `string` | — | `4` | `open` | — | Asmens lytis | — |
| `amzius` | `integer` | — | `3` | `open` | — | Asmens amžius (sutarties sudarymo metu) | — |
| `reg_metai` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (metai) | — |
| `reg_ketvirtis` | `integer` | — | `2` | `open` | — | Dokumento įregistravimo data (ketvirtis) | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"V"` | — | — | Vyras | — |
| `lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/vsr/sutartys_pagal_amziu.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/vsr/sutartys_pagal_amziu.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/vsr/sutartys_pagal_amziu (https://data.gov.lt/datasets/2155/)
