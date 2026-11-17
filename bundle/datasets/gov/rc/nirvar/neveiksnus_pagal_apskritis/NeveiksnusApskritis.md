---
type: Table
title: "NeveiksnusApskritis — NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal apskritis ir registracijos metus"
description: "Spinta table datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis/NeveiksnusApskritis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis/NeveiksnusApskritis"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# NeveiksnusApskritis — NIRVAR statistika apie teismo tvarka neveiksniais pripažintus asmenis pagal apskritis ir registracijos metus

- **Model:** `datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis/NeveiksnusApskritis`[^manifest]
- **Dataset:** [Neveiksnių ir ribotai veiksnių asmenų registras](../neveiksnus_pagal_apskritis.md) (`datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis`)
- **Manifest CSV:** [datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis/NeveiksnusApskritis`
- **Primary Key (`ref`):** `apskritis, reg_metai`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../ar/apskritis/Apskritis.md) | `4` | `open` | — | Apskrities pavadinimas iš Adresų registro | — |
| `reg_metai` | `integer` | — | `2` | `open` | — | Registravimo metai | — |
| `neveiksniu_asm_skaicius` | `string` | — | `3` | `open` | — | Neveiksnių asmenų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_metai` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/nirvar/neveiksnus_pagal_apskritis.csv
