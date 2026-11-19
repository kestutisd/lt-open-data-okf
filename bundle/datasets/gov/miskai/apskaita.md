---
type: Dataset
title: "datasets/gov/miskai/apskaita"
description: "Lithuanian open data dataset datasets/gov/miskai/apskaita (4 lentelės)."
resource: "https://get.data.gov.lt/datasets/gov/miskai/apskaita"
tags: [gov, miskai, deployed]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/miskai/apskaita

- **Namespace:** `datasets/gov/miskai/apskaita`[^manifest]
- **Manifest CSV:** [datasets/gov/miskai/apskaita.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/miskai/apskaita` (`deployed`)[^manifest]
- **Provider:** `miskai` — Valstybinė miškų tarnyba *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `4` (4 lentelės)[^manifest]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BendroPlotoPaskirst](apskaita/BendroPlotoPaskirst.md) | Bendro žemės ploto pasiskirstymas pagal žemės naudmenas (ha) | `3` | `zemes_misku_gr` | — | `17` | — |
| [MiskoZemesPaskirst](apskaita/MiskoZemesPaskirst.md) | Miško žemės pasiskirstymas pagal žemės naudmenas (ha) | `3` | `misku_gr_kateg` | — | `10` | — |
| [MiskuPlotuPaskirst](apskaita/MiskuPlotuPaskirst.md) | Visų miškų plotų pasiskirstymas pagal žemės naudmenas (ha) | `3` | — | — | `3` | — |
| [TaksacRodiklis](apskaita/TaksacRodiklis.md) | Visų miškų medynų taksaciniai rodikliai | `2` | — | — | `14` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(model)` | `create(type: "param", ref: "dist", source: "/datasets/gov/ivpk/adp/catalog/DatasetDistribution")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/miskai/apskaita.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/miskai/apskaita.csv#L2)
