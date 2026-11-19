---
type: Table
title: "RibotaiVeiksnusApskritis — NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos metus"
description: "Spinta table datasets/gov/rc/nirvar/veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis (3 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis"
tags: [gov, rc, ribotaiveiksnusapskritis, deployed, level-3, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2149/"
    title: "data.gov.lt DCAT-AP — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# RibotaiVeiksnusApskritis — NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir registracijos...

- **Model:** `datasets/gov/rc/nirvar/veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis`[^manifest]
- **Dataset:** [NIRVAR statistika apie teismo tvarka ribotai veiksniais pripažintus asmenis pagal apskritis ir...](../veiksnus_pagal_apskritis.md) (`datasets/gov/rc/nirvar/veiksnus_pagal_apskritis`)[^manifest]
- **Manifest CSV:** [datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis/RibotaiVeiksnusApskritis` (`deployed`)[^manifest]
- **Provider:** `rc` — VĮ Registrų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `apskritis, reg_met`[^manifest]
- **Level:** `3`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `ref` | [Apskritis](../../ar/apskritis/Apskritis.md) (`level=4 UUID`: `apskritis._id`) | `4` | `open` | — | Apskrities pavadinimas iš Adresų registro | — |
| `reg_met` | `integer` | — | `2` | `open` | — | Registravimo metai | — |
| `ribotai_veiksniu_asm_skaicius` | `string` | — | `3` | `open` | — | Ribotai veiksnių asmenų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reg_met` | `update(type: "date", ref: "Y")` | `type` | `4` | — | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/nirvar/veiksnus_pagal_apskritis.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/rc/nirvar/veiksnus_pagal_apskritis (https://data.gov.lt/datasets/2149/)
