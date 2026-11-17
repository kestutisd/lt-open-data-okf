---
type: Dataset
title: "Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenys"
description: "Spinta dataset datasets/gov/nvsc/uzkreciamos_ligos/atvejai (4 tables)."
resource: "https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai"
tags: [gov, nvsc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nacionalinio visuomenės sveikatos centro užkrečiamų ligų duomenys

- **Namespace:** `datasets/gov/nvsc/uzkreciamos_ligos/atvejai`[^manifest]
- **Manifest CSV:** [datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nvsc/uzkreciamos_ligos/atvejai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Bendrieji](atvejai/Bendrieji.md) | Užkrečiamųjų ligų atvejai bendrieji | `4` | `vda_id` | — | 17 | — |
| [GyvenamojiVieta](atvejai/GyvenamojiVieta.md) | Užkrečiamųjų ligų atvejai pagal gyvenamąją vietą | `4` | `vda_id` | — | 16 | — |
| [SocialineGrupe](atvejai/SocialineGrupe.md) | Užkrečiamųjų ligų atvejai pagal socialines grupes | `4` | `vda_id` | — | 17 | — |
| [Tyrimas](atvejai/Tyrimas.md) | Užkrečiamųjų ligų tyrimai | `4` | `vda_id` | — | 8 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nvsc/uzkreciamos_ligos/atvejai.csv
