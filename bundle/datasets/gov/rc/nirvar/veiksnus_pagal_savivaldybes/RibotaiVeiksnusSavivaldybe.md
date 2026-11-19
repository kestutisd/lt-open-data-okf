---
type: Table
title: "RibotaiVeiksnusSavivaldybe — NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal savivaldybes"
description: "Spinta table datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes/RibotaiVeiksnusSavivaldybe (2 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes/RibotaiVeiksnusSavivaldybe"
tags: [gov, rc, ribotaiveiksnussavivaldybe, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2150/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# RibotaiVeiksnusSavivaldybe — NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal savivaldybes

- **Model:** `datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes/RibotaiVeiksnusSavivaldybe`[^manifest]
- **Dataset:** [NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal savivaldybes](../veiksnus_pagal_savivaldybes.md) (`datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes/RibotaiVeiksnusSavivaldybe` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `ref` | [Savivaldybe](../../ar/savivaldybe/Savivaldybe.md) (`level=4 UUID`: `savivaldybe._id`) | `4` | `open` | — | Savivaldybės pavadinimas iš Adresų registro | — |
| `ribotai_veiksniu_asm_skaicius` | `string` | — | `3` | `open` | — | Ribotai veiksnių asmenų skaičius | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/nirvar/veiksnus_pagal_savivaldybes (https://data.gov.lt/datasets/2150/)
