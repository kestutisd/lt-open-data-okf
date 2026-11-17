---
type: Dataset
title: "Diagnozių dažnis"
description: "Spinta dataset datasets/gov/lsd/sveikata/diagnozes (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Diagnozių dažnis

- **Namespace:** `datasets/gov/lsd/sveikata/diagnozes`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/diagnozes`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [EspbiDiagnoze025](diagnozes/EspbiDiagnoze025.md) | Diagnozių dažnis pagal E025 formos duomenis | `4` | `vda_id` | — | 7 | "Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS E025 dokumente (“Ambulatorinio apsilankymo aprašymas”), dažnis pagal apsilankymo metus, lytį ir savivaldybę... |
| [EspbiDiagnoze003](diagnozes/EspbiDiagnoze003.md) | Diagnozių dažnis pagal E003 formos duomenis | `4` | `vda_id` | — | 7 | "Diagnozių TLK-10-AM kodų, nurodytų ESPBI IS E003 dokumente (“Stacionaro epikrizė”), dažnis pagal apsilankymo metus, lytį ir savivaldybę sveikatos... |
| [Persalimas](diagnozes/Persalimas.md) | Kvėpavimo takų infekcijų dažnis dienos tikslumu | `4` | `vda_id` | — | 6 | "Kvėpavimo takų infekcijų diagnozių dinamika: TLK-10-AM kodų, nurodytų ESPBI IS E025 dokumente (“Ambulatorinio apsilankymo aprašymas”), dažnis pagal... |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/diagnozes/diagnozes.csv
