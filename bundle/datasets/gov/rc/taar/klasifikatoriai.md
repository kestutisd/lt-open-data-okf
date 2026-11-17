---
type: Dataset
title: "TAAR klasifikatoriai"
description: "Turto arešto aktų registro klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.): TAAR turto tipų klasifikatorius; TAAR tipų potipių klasifikatorius; TAAR dokumentų statusų klasifikatorius; TAAR areštuojančių institucijų klasifikatorius."
resource: "https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/taar/klasifikatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# TAAR klasifikatoriai

Turto arešto aktų registro klasifikatoriai (duomenų rinkinių grupė, viso 4 vnt.): TAAR turto tipų klasifikatorius; TAAR tipų potipių klasifikatorius; TAAR dokumentų statusų klasifikatorius; TAAR areštuojančių institucijų klasifikatorius.

- **Namespace:** `datasets/gov/rc/taar/klasifikatoriai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/taar/klasifikatoriai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/taar/klasifikatoriai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/taar/klasifikatoriai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [TurtoTipas](klasifikatoriai/TurtoTipas.md) | Turto arešto aktų registro turto tipų klasifikatorius | `4` | `kodas` | — | 2 | — |
| [TurtoPotipis](klasifikatoriai/TurtoPotipis.md) | — | `4` | `kodas` | — | 2 | — |
| [DokumentoStatusas](klasifikatoriai/DokumentoStatusas.md) | Turto arešto aktų registro dokumentų statusų klasifikatorius | `4` | `kodas` | — | 2 | — |
| [AI](klasifikatoriai/AI.md) | Turto arešto aktų registro areštuojančių institucijų tipų klasifikatorius | `4` | `tipas` | — | 2 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/taar/klasifikatoriai.csv
