---
type: Table
title: "RibotaiVeiksnusSavivaldybe — NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal savivaldybes"
description: "Spinta table datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes/RibotaiVeiksnusSavivaldybe (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes/RibotaiVeiksnusSavivaldybe"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# RibotaiVeiksnusSavivaldybe — NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal savivaldybes

- **Model:** `datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes/RibotaiVeiksnusSavivaldybe`[^manifest]
- **Dataset:** [NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal savivaldybes](../veiksnus_pagal_savivaldybes.md) (`datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes`)
- **Manifest CSV:** [datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes/RibotaiVeiksnusSavivaldybe`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės pavadinimas iš Adresų registro | — |
| `ribotai_veiksniu_asm_skaicius` | `string` | — | `3` | `open` | — | Ribotai veiksnių asmenų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv
