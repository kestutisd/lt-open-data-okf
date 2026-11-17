---
type: Table
title: "RibotaiVeiksnusApskritis — NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos metus"
description: "Spinta table datasets/gov/rc/nirvar/veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# RibotaiVeiksnusApskritis — NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos metus

- **Model:** `datasets/gov/rc/nirvar/veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis`[^manifest]
- **Dataset:** [NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos metus](../veiksnus_pagal_apskritis.md) (`datasets/gov/rc/nirvar/veiksnus_pagal_apskritis`)
- **Manifest CSV:** [datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis`
- **Primary Key (`ref`):** `apskritis, reg_met`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../../ar/apskritis/Apskritis.md) | `4` | `open` | — | Apskrities pavadinimas iš Adresų registro | — |
| `reg_met` | `integer` | — | `2` | `open` | — | Registravimo metai | — |
| `ribotai_veiksniu_asm_skaicius` | `string` | — | `3` | `open` | — | Ribotai veiksnių asmenų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_met` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv
