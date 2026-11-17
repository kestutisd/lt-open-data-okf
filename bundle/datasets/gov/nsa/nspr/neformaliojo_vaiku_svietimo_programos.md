---
type: Dataset
title: "Neformaliojo vaikų švietimo programos"
description: "Spinta dataset datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos"
tags: [gov, nsa, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Neformaliojo vaikų švietimo programos

- **Namespace:** `datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Programa](neformaliojo_vaiku_svietimo_programos/Programa.md) | Neformaliojo vaikų švietimo programos | `4` | `vda_prime_key` | — | 25 | Viena eilutė atitinka vieną neformaliojo vaikų švietimo programą |
| [Lankymas](neformaliojo_vaiku_svietimo_programos/Lankymas.md) | Neformaliojo vaikų švietimo programų lankymas | `4` | `vda_prime_key` | — | 4 | Viena eilutė atitinka vieną neformaliojo vaikų švietimo programą lankiusių mokinių skaičių atitinkamais mokslo metais |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/nspr/neformaliojo_vaiku_svietimo_programos.csv
